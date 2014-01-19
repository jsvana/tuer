from math import sqrt, sin, cos, degrees, radians
from db import connect

unvisited = None
epsilon = .75

class Point:
    def __init__(self, ID, lat, lon, visited, bearing, focus, hits=0):
        self.ID = ID
        self.lat = lat
        self.lon = lon
        self.vis = visited
        self.bear = bearing
        self.focus = focus
        self.hits = hits

# determine gps coords from bearing and capture gps
def getObjPoint(point):
    ang = point.bear
    xMod = point.focus
    yMod = point.focus
    if ang < 90:
        # no mod needed
        a = 1
    elif ang < 180:
        ang = 180 - ang
        yMod *= -1
    elif ang < 270:
        ang = ang - 180
        yMod *= -1
        xMod *= -1
    else:
        ang = 360 - ang
        xMod *= -1

    ang = radians(ang)
    dX = xMod * sin(ang)
    dY = yMod * cos(ang)

    return Point(0, point.lat + dX, point.lon + dY, False, None, None)

# return distance between two points
def fDist(p, P):
    return sqrt((p.lat - P.lat)**2 + (p.lon - P.lon)**2)

# place point in cluster and update centroid
def cluster(point):
    global epsilon
    p = getObjPoint(point)
    closeBy = regionQuery(p, epsilon)
    if len(closeBy) == 0:
        sql = "INSERT INTO landmarks (position,centCnt,sumLat,sumLon) VALUES (POINT(%s, %s), %s, %s, %s)"
        vals = [p.lat, p.lon, 1, p.lat, p.lon]
        print 'Beginning new cluster', vals
        connect.execute(sql, vals)
        return

    minP = None
    minDist = 10000
    for dist, point in [(fDist(p, P), P) for P in closeBy]:
        if dist < minDist:
            print dist
            minP = point
            minDist = dist
    print "Minimum:", minDist, minP, minP.ID
    rows = connect.getRows("landmarks",['centCnt','sumLat','sumLon'], 'id=' + str(minP.ID))
    row = rows[0]
    cnt = row[0] + 1
    sumX = row[1] + p.lat
    sumY = row[2] + p.lon

    p.lat = sumX/cnt
    p.lon = sumY/cnt
    sql = "UPDATE landmarks SET position=POINT(%s, %s),centCnt=%s,sumLat=%s,sumLon=%s"
    where = " WHERE id=" + str(minP.ID)
    vals = [p.lat, p.lon, cnt, sumX, sumY]
    connect.execute(sql + where, vals)
    print 'Added to cluster ' + str(minP.ID), vals

def batchCluster():
    for p in queryUnv():
        cluster(p)
        mark(p)

def regionQuery(P, epsilon):
    xmin = P['lat'] - epsilon
    xmax = P['lat'] + epsilon
    ymin = P['lon'] - epsilon
    ymax = P['lon'] + epsilon
    points = list()
    poly = [xmin, ymin,
            xmin, ymax,
            xmax, ymax,
            xmax, ymin,
            xmin, ymin]
    area ="GeomFromText('Polygon((%s %s, %s %s, %s %s, %s %s, %s %s))')"
    where = 'MBRContains(' + area + ', position)'
    sql = "SELECT id, X(position), Y(Position), centCnt FROM landmarks WHERE "
    for row in connect.query(sql + where, poly):
        p = Point(row[0],row[1], row[2], True, 0, 0, row[3])
        points.append(p)
    print str(len(points)) + " in region"
    return points

def queryUnv():
    cols = ('id', 'X(position), Y(position)', 'visited', 'bearing', 'focus')
    points = list()
    for row in connect.getRows("pictures", cols, "visited=False"):
        p = Point(row[0],row[1], row[2], row[3], row[4], row[5])
        points.append(p)
    return points

#set marked in db
def mark(point):
    point.vis = True
    connect.execute("UPDATE pictures SET visited=True WHERE id=%s", [point.ID])



import dbscan

maxHits = 22

def mset(m, d, p):
    m[d]=p

# hitsWeight percent from 0-1.0
def getTopNWeighted(points, radius, n, hitsWeight):
    proxWeight = 1.0 - hitsWeight
    landmarks = dbscan.regionQuery(points, radius)
    m = {}
    [mset(m, dbscan.fDist(P, p), p) for p in landmarks]
    for p in landmark:
        dist = dbscan.fDist(P, p)
        pScore = proxWeight * (1 - dist/radius)
        hScore = hitsWeight * (p.hits/maxHits)
        mset(m, pScore + hScore, p)
    sorted(m)
    vals = m.values()
    return vals[len(vals) - n:]
    
def getTopNProx(points, radius, n):
    proxWeight = 1.0 - hitsWeight
    landmarks = dbscan.regionQuery(points, radius)
    m = {}
    [mset(m, dbscan.fDist(P, p), p) for p in landmarks]
    sorted(m)
    return m.values()[0:n]
    
def getTopNHits(points, radius, n):
    landmarks = dbscan.regionQuery(points, radius)
    m = {}
    [mset(m, p.hits, p) for p in landmarks]
    sorted(m)
    vals = m.values()
    return vals[len(vals)) - n:]


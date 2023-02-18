import math

def getdis(latitude1, longitude1, latitude2, longitude2):
    # convert decimal degrees to radians
    longitude1, latitude1, longitude2, latitude2 = map(math.radians, [longitude1, latitude1, longitude2, latitude2])
    # haversine formula
    dlon = longitude2 - longitude1
    dlat = latitude2 - latitude1
    a = math.sin(dlat/2)**2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371 # Radius of earth in kilometers.
    return c * r

center = [(-1.159, 34.902), (-1.017, 35.640), (-1.103, 36.018)]
edge = [(-1.1786, 34.786), (-0.9475, 35.524), (-1.195, 36.142)]
if __name__ == "__main__":
    print(getdis(center[0][0], center[0][1], edge[0][0], edge[0][1]))
    print(getdis(center[1][0], center[1][1], edge[1][0], edge[1][1]))
    print(getdis(center[2][0], center[2][1], edge[2][0], edge[2][1]))

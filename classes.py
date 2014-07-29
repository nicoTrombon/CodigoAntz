import math
class truck(object):
    """
    Representation of a truck
    Every truck has an id, a capacity and a route
    The route is a collection of point objects
    With getRoute() we get a tuple of the ids
    of the points the truck must visit in order
    """
    def __init__(self, id, capacity, route = ()):
        self.id = id
        self.capacity = capacity
        self.route = route
    
    def getCapacity(self):
        return self.capacity
    
    def getRoute(self):
        tup=()
        for point in self.route:
            tup = tup + (point.id,)
        return tup
    
    def getId(self):
        return self.id
    
    def addPoint(self, point):
        self.route = self.route + (point,)
    
    def getRemainingCap(self):
        cap=self.capacity
        for points in self.route:
            cap -= points.getReq()
        return cap
    
class point(object):   
    """
    Representation of a point
    Each point has an id, an xcoord, a ycoord, and a requirement
    """
    def __init__(self, id, xcoord, ycoord, requirement, assigned=False):
        self.xcoord=xcoord
        self.ycoord=ycoord
        self.requirement=requirement
        self.id=id
        self.assigned=assigned
    
    def getX(self):
        return self.xcoord
    
    def getAssigned(self):
        return self.assigned
    
    def getY(self):
        return self.ycoord
    
    def getReq(self):
        return self.requirement
    
    def getId(self):
        return self.id
    
    def calcDist(self, otherPoint):
        xSqDif=math.pow(self.xcoord-otherPoint.xcoord,2)
        ySqDif=math.pow(self.ycoord-otherPoint.ycoord,2)
        dist=math.sqrt(xSqDif + ySqDif)
        return dist
          


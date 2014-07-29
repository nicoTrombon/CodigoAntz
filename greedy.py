import classes

def greedyRoute():
    emptyT=[]
    
    a=classes.truck(id=1,capacity=10)
    b=classes.truck(id=2,capacity=20)
    c=classes.truck(id=3,capacity=10)
    d=classes.truck(id=4, capacity=300)
    
    emptyT.append(a)
    emptyT.append(b)
    emptyT.append(c)
    emptyT.append(d)
    
    
    point1=classes.point(id=1,xcoord=16, ycoord=16.2, requirement=1)
    point2=classes.point(id=2,xcoord=10, ycoord=14.2, requirement=15)
    point3=classes.point(id=3, xcoord=13, ycoord=19.2, requirement=15)
    point4=classes.point(id=4,xcoord=15,ycoord=10, requirement=3)
    
    points=[]
    points.append(point1)
    points.append(point2)
    points.append(point3)
    points.append(point4)
    
    # a.addPoint(point1)
    # a.addPoint(point2)
    # print a.getRoute()
    # remCap=a.getRemainingCap()
    # print remCap>0
    # print point1.calcDist(point2)
    
    verbose=False
    
    for aTruck in emptyT:
        for aPoint in points:
            #print truck.getId(), '-', point.getId()
            if aPoint.getAssigned() is False and aTruck.getRemainingCap()>aPoint.getReq():
                aTruck.addPoint(aPoint)
                aPoint.assigned=True
                #points.remove(point)
                if verbose==True:
                    print 'ASSIGNED POINT', aPoint.getId(), 'to TRUCK', aTruck.getId()
            else:
                 if verbose==True:
                     print 'COULDNT ASSIGN POINT', aPoint.getId(), 'to TRUCK', aTruck.getId()
    
    print '**'
    print '****'
    print 'ROUTES:'
    for aTruck in emptyT:
        print
        print 'truck id',aTruck.getId()
        print 'ROUTE:',aTruck.getRoute()
        print 'remaining capacity:',aTruck.getRemainingCap()
    print '****'
    print '**'

greedyRoute()
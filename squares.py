#check if any four points are vertices of a square or not
points = ["1.6,0.7", "0.8,3.3", "4.5,13.2", "3.6,9.5", "-2,1.6", "8.5,16.2", "6,0.7", "10.7,-0.5", "11.1,2.2", "7.5,9.2",
         "10.25,4.75", "6.08,4.02", "10.5,15.3", "10.1,-5", "20,5", "20.8,15.75", "11.5,12.2", "14,6", "10,2", "14,2.5"]

def dist(a,b,c,d):
    """find distances with coordinates a,b and c,d"""
    distance = (((c-a)**2) + ((d-b)**2))**0.5
    return distance

distances = list()
squares = list()
length = len(points)
for i in range(0,length):
    coordinate1 = points[i].split(",")
    for j in range(0, length):
        if j!= i:
            coordinate2 = points[j].split(",")
            for k in range(0, length):
                if k != i and k != j:
                    coordinate3 = points[k].split(",")
                    for l in range(0, length):
                        if l != i and l != j and l != k:
                            coordinate4 = points[l].split(",")
                            x1 = float(coordinate1[0])
                            y1 = float(coordinate1[1])
                            x2 = float(coordinate2[0])
                            y2 = float(coordinate2[1])
                            x3 = float(coordinate3[0])
                            y3 = float(coordinate3[1])
                            x4 = float(coordinate4[0])
                            y4 = float(coordinate4[1])
                            ab = dist(x1,y1,x2,y2)
                            bc = dist(x2,y2,x3,y3)
                            cd = dist(x3,y3,x4,y4)
                            ad = dist(x4,y4,x1,y1)
                            ac = dist(x1,y1,x3,y3)
                            bd = dist(x2,y2,x4,y4)
                            if ab == bc == cd == ad and ac == bd:
                              squares.append(coordinate1)
                              squares.append(coordinate2)
                              squares.append(coordinate3)
                              squares.append(coordinate4)
                              squares.append(";")
            continue
print(squares)

def distance_formula(x1,x2,y1,y2):
    d=(((x1-x2)**2+(y1-y2)**2)*0.5)
    return d

def slope_formula(x1,x2,y1,y2):
    slope=((y2-y1)/(x2-x1))
    return slope


def mid_point_formula(x1,x2,y1,y2):
    x =((x1+x2)/2)
    y=((y1+y2)/2)
    c=(x,y)
    return c

def parallel(m1,m2):
    if(m1 == m2):
        return("it is parallel")
    else:
        return ("it is non parallel")

def perpendicular_lines(m1,m2):
    if((m1*m2)==-1):
        return ("it is perpendicular")
    else:
        return ("it is not perpendicular")

def area_of_triangle(x1,x2,x3,y1,y2,y3):
    c=[x1(y2-y3)+x2(y3-y1)+x3(y1-y2)]
    area=(1/2)*c
    return area
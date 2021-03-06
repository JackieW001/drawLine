from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    
    if (x0 < x1):
        x = x0
        y = y0
    else:
        x = x1
        y = y1
        x1 = x0
        y1 = y0

    A = y1-y
    B = -(x1-x)

    # Slope = 0
    if (B == 0):
        if (y1 < y):
            temp = y
            y = y1
            y1 = temp
        while (y<=y1):
            plot(screen, color, x, y)
            y += 1
        return
    else:
        slope = (A*1.0)/-B
        
    #Octant I
    if( slope <= 1 and slope >= 0):
        d = (2*A) + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += (2*B)
            x += 1
            d += (2*A)

    #Octant II
    elif( slope > 1 ):
        d = A + (B*2)
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += (2*A)
            y += 1
            d += (2*B)

    #Octant VIII
    elif( slope >= -1 and slope < 0):
        d = (2*A)-B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= (2*B)
            x += 1
            d += (2*A)

    #Octant VII
    elif( slope < -1):
        d = A - (2*B)
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += (2*A)
            y -= 1
            d -= (2*B)




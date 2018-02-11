from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 0 ]

#draw_line(0,0,300,300, screen, color)
#draw_line(0,0,300,500, screen, [255,0,0])
#draw_line(0,400, 300,300, screen,[255,255,0])
#draw_line(0, 400, 200, 100, screen, [0,255,255])
#draw_line(250, 250, 250, 300, screen, [255,255,255])

#axis
draw_line(0, 250, 500, 250, screen, [51, 153, 102])
draw_line(250, 0, 250, 500, screen, [51, 153, 102])
draw_line(0, 0, 500, 500, screen, [51, 153, 102])
draw_line(0, 500, 500, 0, screen, [51, 153, 102])

def draw_rect(x, y, l, w, screen, color):
    draw_line(x, y, x, y-l, screen, color) #left
    draw_line(x, y, x+w, y, screen, color) #top
    draw_line(x+w, y, x+w, y-l, screen, color) #right
    draw_line(x+w, y-l, x, y-l, screen, color) #bottom

x = 100
y = 400
l = 300
r = 255
g = 255
b = 0

while (x < 250):
    draw_rect( x, y, l, l, screen, [r,g,b])
    x += 10
    y -= 10
    l -= 20
    
    r -= 15
    g -= 15
    b += 15


display(screen)
save_extension(screen, 'img.png')

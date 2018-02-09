from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#draw_line(0,0,300,300, screen, color)
#draw_line(0,0,300,500, screen, [255,0,0])
#draw_line(0,400, 300,300, screen,[255,255,0])
#draw_line(0, 400, 200, 100, screen, [0,255,255])
draw_line(400, 400, 200, 200, screen, [255,255,255])

display(screen)
save_extension(screen, 'img.png')

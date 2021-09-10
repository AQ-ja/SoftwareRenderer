# Programa principal
from numpy import min_scalar_type
from shaders import toon
from GL import Renderer, V3, _color
from obj import Texture
from shaders import *

import random

width = 1920
height = 1080


rend = Renderer(width, height)

rend.directional_light = V3(-1,0,0)



rend.background = Texture('Universe/fondo.bmp')

rend.glClearBackground()


# Primer modelo
# EL planeta
rend.active_shader = tf
rend.directional_light = V3(0,0,-1)
rend.active_texture = Texture('Universe/3301.bmp')
rend.glLoadModel("Universe/planet.obj", translate = V3(0, 2, -10), scale = V3(3,3,3), rotate= V3(1, 0.5, 0))

# segundo modelo 
# El meteorito
rend.active_shader = static
rend.directional_light = V3(0,0,-1)
rend.active_texture = Texture('Universe/3329.bmp')
rend.glLoadModel("Universe/A2.obj", translate= V3(12, 7, -18), scale=V3(1, 1, 1), rotate = V3(50,180, 13))


# Tercer modelo 
# El UFO
rend.active_shader = intense
rend.directional_light = V3(0,0,-1)
rend.active_texture = Texture('Universe/1555.bmp')
rend.glLoadModel("Universe/Ufo.obj", translate= V3(-1.5, -0.5, -3.4), scale=V3(0.5, 0.5, 0.5), rotate = V3(-10, 15, -15))


# Cuarto modelo
# El satelite 
rend.active_shader = psyc
rend.directional_light = V3(0,0,-1)
rend.active_texture = Texture('Universe/3301.bmp')
rend.glLoadModel("Universe/satelite.obj", translate= V3(4, 0.5, -11), scale=V3(3, 3, 3), rotate = V3(-5, 0, 0))

# Quinto modelo 
# Otro planeta
rend.active_shader = static
rend.directional_light = V3(0,0,-0.8)
rend.active_texture = Texture('Universe/2942.bmp')
rend.glLoadModel("Universe/planet.obj", translate= V3(-9, 7, -17), scale=V3(2, 2, 2), rotate = V3(60, 0, 0))

rend.glFinish("Proyecto_Universo.bmp")
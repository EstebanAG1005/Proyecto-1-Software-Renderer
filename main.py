# Proyecto1 - Renderer
# Graficas por computadora 
# Esteban Aldana Guerra 20591

from gl import *
import random

r = Render(800,800)
r.glCreateWindow(800,800)
r.glViewPort(0,0,999,999)

cafe = Texture('cafe.bmp')
xbox = Texture('xbox.bmp')
champ = Texture('TVV.bmp')
brick = Texture('ladrillo.bmp')
madera = Texture('madera.bmp')

r.lookAt(V3(-0.2,0,20), V3(0,0,0), V3(0,1,0))

r.load2('xbox.obj',translate=(-0.5,0.24,0), scale=(0.5,0.5,0.5), rotate=(0,0,0), texture=xbox)
r.load('mueble.obj',translate=(0,-0.2,0), scale=(0.007,0.007,0.007), rotate=(0,0,0), texture=cafe)
r.load3('TV.obj',translate=(-2.95,-0.8,0), scale=(0.2,0.2,0.2), rotate=(0,-1.3,0), texture=champ)
r.load3('persona.obj',translate=(-0.5,-2.5,2), scale=(2,2,2), rotate=(-1,0,0), texture=cafe)
r.load3('persona.obj',translate=(0.5,-2.5,2), scale=(2,2,2), rotate=(-1,0,0), texture=cafe)
r.load2('wall.obj',translate=(-1,0.5,-1), scale=(0.2,0.1,0.1), rotate=(0,0,0), texture=brick)
r.load2('wall.obj',translate=(-1,-0.5,-2), scale=(0.2,0.1,0.1), rotate=(0,0,0), texture=madera)

r.archivo('Final.bmp')

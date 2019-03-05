from display import *
from draw import *
from scriptParser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

#InputScript = open('script','r').read().strip().split('\n')
#print(InputScript)
parse_file( 'script', edges, transform, screen, color )

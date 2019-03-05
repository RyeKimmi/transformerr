from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    InputScript = open(fname,'r').read().strip().split('\n')
    #print(InputScript)
    i = 0
    while (i < len(InputScript)):
        if InputScript[i] == 'line':
            i+=1
            CommandImputs = InputScript[i].split(' ')
            add_edge(points, CommandImputs[0],CommandImputs[1],CommandImputs[2],CommandImputs[3],CommandImputs[4],CommandImputs[5])
            #print(CommandImputs[1])
            i+=1
        elif InputScript[i] == 'ident':
            ident(transform)
            i+=1
        elif InputScript[i] == 'scale':
            i+=1
            CommandInputs = InputScript[i].split(' ')
            scaleMat = make_scale(CommandInputs[0],CommandInputs[1],CommandInputs[2])
            matrix_mult(scaleMat,transform)
            i+=1
        elif InputScript[i] == 'move':
            i+=1
            CommandInputs = InputScript[i].split(' ')
            translateMat = make_translate(CommandInputs[0],CommandInputs[1],CommandInputs[2])
            matrix_mult(translateMat,transform)
            i+=1
        elif InputScript[i] == 'rotate':
            i+=1
            CommandInputs = InputScript[i].split(' ')
            if CommandInputs[0] == 'x':
                rotateMat = make_rotX(CommandInputs[1])
                matrix_mult(rotateMat,transform)
            elif CommandInputs[0] == 'y':
                rotateMat = make_rotY(CommandInputs[1])
                matrix_mult(rotateMat,transform)
            elif CommandInputs[0] == 'z':
                rotateMat = make_rotZ(CommandInputs[1])
                matrix_mult(rotateMat,transform)
            i+=1
        elif InputScript[i] == 'apply':
            matrix_mult(transform,points)
            i+=1            
        elif InputScript[i] == 'display':
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
            i+=1
        elif InputScript[i] == 'save':
            i+=1
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_ppm(screen,InputScript[i])
            save_extention(screen,InputScript[i])
            i+=1
        elif InputScript[i] == 'quit':
            return
        

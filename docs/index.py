# --------- PYODIDE:env --------- #
from pixel_art import * 
import p5

app.nouveau("figure1") 
# --------- PYODIDE:code --------- #
love = 'Etoy'
for y in range(10, -10, -1):
    line = '  '
    for x in range(-30, 30):
        if ((x*0.05)**2+(y*0.12)**2-1)**3-(x*0.05)**2*(y*0.12)**3<=0:
            line = line + love[(x-y)%len(love)] 
        else:
            line = line + ' '
    print(line)
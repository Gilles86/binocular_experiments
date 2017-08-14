from monkeypatchFBO import fragFBOtoFramePatched
from psychopy import visual, core, event  # import some libraries from PsychoPy
import numpy 
from copy import copy
import numpy as np
from dotslave import DotSlave, DotStimFBO
from psychopy import logging
logging.console.setLevel(logging.DEBUG)
from psychopy import visual
import numpy as np


width_hbar = 16
height_hbar = 2
width_vbar = 2
height_vbar = 16 - 4 


bar_matrix1 = (np.random.random((height_hbar, width_hbar)) > 0.5) * 2 - 1
bar_matrix2 = (np.random.random((height_vbar, width_vbar)) > 0.5) * 2 - 1
bar_matrix3 = (np.random.random((height_hbar, width_hbar)) > 0.5) * 2 - 1
bar_matrix4 = (np.random.random((height_vbar, width_vbar)) > 0.5) * 2 - 1

#create a window
#mywin = visual.Window([1024,768], monitor="testMonitor", units="deg", blendMode='add', screen=1, useFBO=False, winType='pyglet')
mywin = visual.Window([1600,768], monitor="testMonitor", units="deg", blendMode='add', screen=1, useFBO=True, winType='pyglet')

#create some stimuli
dotsize = 10
shift = (-.25, 0)
opacity=1.0
fieldsize = (10.0, 10.0)
framelength = 0.025
n_dots = 50
speed = 0.1

saturation = .5
value = .5

delta_s = 0.05
delta_v = 0.05

element_master = visual.GratingStim(win=mywin, tex='sin', size=dotsize, sf=0, units='pix', mask='circle', color=(0, saturation, value), colorSpace='hsv')
element_master.useShaders = True

dots1 = visual.DotStim(win=mywin,
                       nDots=n_dots,
                       element=element_master,
                       color=(0, saturation, value),
                       colorSpace='hsv',
                       dotSize=dotsize,
                       opacity=opacity,
                       fieldSize=fieldsize,
                       coherence=1.0,
                       speed=speed,
                       dotLife=1e6,
                       fieldShape='circle')
dots1.useShaders = True



fixation1 = visual.GratingStim(mywin, tex='sin', mask='circle', size=0.5, texRes=512, color='white', sf=0)  # circular grating
fixation2 = visual.GratingStim(mywin, tex='sin', mask='circle', size=1.0, color=(1, 0, .5), contrast=0, texRes=256, colorSpace='hsv',sf=0)  # circular grating
fixation3 = visual.GratingStim(mywin, tex='sin', mask='circle', size=1.5, color='white', contrast=-.5, sf=0)  # circular grating

bar1 = visual.ImageStim(mywin, bar_matrix1, size=(width_hbar, height_hbar), pos=(0, 7))
bar2 = visual.ImageStim(mywin, bar_matrix2, size=(width_vbar, height_vbar), pos=(7, 0))
bar3 = visual.ImageStim(mywin, bar_matrix3, size=(width_hbar, height_hbar), pos=(0, -7))
bar4 = visual.ImageStim(mywin, bar_matrix4, size=(width_vbar, height_vbar), pos=(-7, 0))

hue_text = visual.TextStim(mywin, text='hue 0.0', pos=(-9, 1))
sat_text = visual.TextStim(mywin, text='sat 0.5', pos=(-9, 0))
val_text = visual.TextStim(mywin, text='val 0.5', pos=(-9, -1))

#draw the stimuli and update the window
timer = core.StaticPeriod(screenHz=60)
while True:

    bar1.draw()
    bar2.draw()
    bar3.draw()
    bar4.draw()
        
    fixation1.draw()
    fixation2.draw()
    fixation3.draw()


    timer.complete()
    dots1.draw()

    hue_text.draw()
    sat_text.draw()
    val_text.draw()

    timer.start(framelength)
    keys = event.getKeys(['up', 'down', 'space', 'a', 's', 'd', 'f', 'z','x','c','v'])

    if keys != []:
        color = element_master.color
        if 'up' in keys:
            color[0] = 180
        elif 'down' in keys:
            color[0] = 0
        if 'a' in keys:
            color[2] += delta_v
        if 's' in keys:
            color[2] -= delta_v
        if 'd' in keys:
            color[1] += delta_s
        if 'f' in keys:
            color[1] -= delta_s
        element_master.setColor(color)
        hue_text.text = 'hue %.3f' % color[0]
        sat_text.text = 'sat %.3f' % color[1]
        val_text.text = 'val %.3f' % color[2]
        print 'New color master: %s' % color


        if 'space' in keys:
            break
    event.clearEvents()
    mywin.flip()


#print dots1.fieldPos, dots1._dotsXY

#pause, so you get a chance to see it!


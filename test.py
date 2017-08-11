from psychopy import visual, core, event  # import some libraries from PsychoPy
import numpy 
from copy import copy
import numpy as np
from dotslave import DotSlave, DotStimFBO
from psychopy import logging
logging.console.setLevel(logging.CRITICAL)
from psychopy import visual

#visual.DotStim = DotStimFBO


#create a window
#mywin = visual.Window([1024,768], monitor="testMonitor", units="deg", blendMode='add', screen=1, useFBO=True, winType='pygame')
#mywin = visual.Window([1024,768], monitor="testMonitor", units="deg", blendMode='add', screen=1, useFBO=True, winType='pyglet')
mywin = visual.Window([1024,768], monitor="testMonitor", units="deg", blendMode='add', screen=1, useFBO=False, winType='pyglet')
#mywin = visual.Window([1024,768], monitor="testMonitor", units="deg", blendMode='add', screen=1, useFBO=True, winType='pyglet')

#create some stimuli
dotsize = 10
shift = (-.25, 0)
opacity=1.0
fieldsize = (10.0, 10.0)
framelength = 0.025
n_dots = 50

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
                       speed=0.001,
                       dotLife=1e6,
                       fieldShape='circle')
dots1.useShaders = True


element_slave = visual.GratingStim(win=mywin, tex='sin', size=dotsize, sf=0, units='pix', mask='circle', color=(180, saturation, value), colorSpace='hsv')
element_slave.useShaders = True

dots_slave = DotSlave(win=mywin, master=dots1, fieldPos=shift, element=element_slave, color=(180, saturation, value))
dots_slave.useShaders = True

fixation1 = visual.GratingStim(mywin, tex='sin', mask='circle', size=0.5, color=(0, 0, 1), colorSpace='hsv', sf=0)  # circular grating
fixation2 = visual.GratingStim(mywin, tex='sin', mask='circle', size=1.0, color='black',contrast=0, sf=0)  # circular grating
fixation3 = visual.GratingStim(mywin, tex='sin', mask='circle', size=1.5, color='black', sf=0)  # circular grating


#draw the stimuli and update the window
timer = core.StaticPeriod(screenHz=60)
while True:
        
    timer.complete()
    fixation3.draw()
    fixation2.draw()
    fixation1.draw()
    dots1.draw()
    dots_slave.draw()


    timer.start(framelength)
    keys = event.getKeys(['up', 'down', 'space', 'a', 's', 'd', 'f', 'z','x','c','v'])
    #if keys != []:
        #print keys
        #if 'up' in keys:
            #dots_slave.fieldPos[0]  = dots_slave.fieldPos[0] + 0.05
            #print dots_slave.fieldPos
        #elif 'down' in keys:
            #dots_slave.fieldPos[0] = dots_slave.fieldPos[0] - 0.05
        #elif 'space' in keys:
            #break
    if keys != []:
        if 'up' in keys:
            pos = dots_slave.fieldPos
            pos[0] += 0.05
            dots_slave.fieldPos = pos
        elif 'down' in keys:
            pos = dots_slave.fieldPos
            pos[0] -= 0.05
            dots_slave.fieldPos = pos
        if np.any(np.in1d(keys, ['a', 's', 'd','f'])):
            print 'asdf'
            color = element_slave.color
            if 'a' in keys:
                color[2] += delta_v
            if 's' in keys:
                color[2] -= delta_v
            if 'd' in keys:
                color[1] += delta_s
            if 'f' in keys:
                color[1] -= delta_s
            element_slave.setColor(color)
            print 'New color slave: %s' % color

        if np.any(np.in1d(keys, ['z', 'x', 'c','v'])):
            color = element_master.color
            if 'z' in keys:
                color[2] += delta_v
            if 'x' in keys:
                color[2] -= delta_v
            if 'c' in keys:
                color[1] += delta_s
            if 'v' in keys:
                color[1] -= delta_s
            element_master.setColor(color)
            print 'New color master: %s' % color

        if 'space' in keys:
            break
    event.clearEvents()
    mywin.flip()


#print dots1.fieldPos, dots1._dotsXY

#pause, so you get a chance to see it!


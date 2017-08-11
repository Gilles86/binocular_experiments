from psychopy import visual, core, event  # import some libraries from PsychoPy
import numpy 
from copy import copy
import numpy as np
from dotslave import DotSlave
from psychopy import logging
logging.console.setLevel(logging.DEBUG)


#create a window
mywin = visual.Window([1024,768], monitor="testMonitor", units="deg", blendMode='add', screen=1)

#create some stimuli
dotsize = 10
shift = (.25, 0)
opacity=1.0
fieldsize = (10.0, 10.0)
framelength = 0.1
n_dots = 50

dots1 = visual.DotStim(win=mywin,
                       nDots=n_dots,
                       color=(0, 0.5, 0.5),
                       colorSpace='hsv',
                       dotSize=dotsize,
                       opacity=opacity,
                       fieldSize=fieldsize,
                       fieldShape='circle')

dots_slave = DotSlave(win=mywin, master=dots1, fieldPos=shift, color=(180, 0.5, 0.5), colorSpace='hsv')

#draw the stimuli and update the window
timer = core.StaticPeriod(screenHz=60)
while True:
    timer.complete()
    dots1.draw()
    dots_slave.draw()
    mywin.flip()

    if len(event.getKeys())>0: break
    event.clearEvents()
    timer.start(framelength)

#print dots1.fieldPos, dots1._dotsXY

#pause, so you get a chance to see it!


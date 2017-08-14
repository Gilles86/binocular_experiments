from monkeypatchFBO import fragFBOtoFramePatched
from psychopy import visual, core, event  # import some libraries from PsychoPy
import numpy 
from copy import copy
import numpy as np
from dotslave import DotSlave, DotStimFBO
from psychopy import logging
logging.console.setLevel(logging.CRITICAL)
from psychopy import visual
import numpy as np
import pandas


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
mywin = visual.Window([1024,768], monitor="testMonitor", units="deg", blendMode='add', screen=1, useFBO=True, winType='pyglet')

#create some stimuli
dotsize = 10
fieldsize = (10.0, 10.0)
framelength = 0.025
n_dots = 50
speed = 0.1

saturation = .5
value = .5

delta_s = 0.05
delta_v = 0.05

element_master = visual.GratingStim(win=mywin, tex='sin', size=dotsize, sf=0, units='pix', mask='circle', color=(180, 0.5, 0.5), colorSpace='hsv')
element_master.useShaders = True

dots1 = visual.DotStim(win=mywin,
                       nDots=n_dots,
                       element=element_master,
                       color=(0, saturation, value),
                       colorSpace='hsv',
                       dotSize=dotsize,
                       fieldSize=fieldsize,
                       coherence=0,
                       speed=speed,
                       dotLife=1e6,
                       fieldShape='circle')
dots1.useShaders = True



fixation1 = visual.GratingStim(mywin, tex='sin', mask='circle', size=0.5, texRes=512, color='white', sf=0)  # circular grating
#fixation2 = visual.GratingStim(mywin, tex='sin', mask='circle', size=1.0, color=(1, 0, .5), contrast=0, texRes=256, colorSpace='hsv',sf=0)  # circular grating
fixation3 = visual.GratingStim(mywin, tex='sin', mask='circle', size=1.5, color='white', contrast=-.5, sf=0)  # circular grating

bar1 = visual.ImageStim(mywin, bar_matrix1, size=(width_hbar, height_hbar), pos=(0, 7))
bar2 = visual.ImageStim(mywin, bar_matrix2, size=(width_vbar, height_vbar), pos=(7, 0))
bar3 = visual.ImageStim(mywin, bar_matrix3, size=(width_hbar, height_hbar), pos=(0, -7))
bar4 = visual.ImageStim(mywin, bar_matrix4, size=(width_vbar, height_vbar), pos=(-7, 0))


#draw the stimuli and update the window
timer = core.StaticPeriod(screenHz=60)

results = []
while True:

    bar1.draw()
    bar2.draw()
    bar3.draw()
    bar4.draw()
        
    fixation1.draw()
    #fixation2.draw()
    fixation3.draw()

    timer.complete()
    dots1.draw()


    timer.start(framelength)


    keys = event.getKeys(['space', 'z', 'm', 'n', 'q'])

    hue, saturation, value = element_master.color
    
    if keys != []:
        hue = np.random.randn() * 0.01 + 180 
        value = np.random.randn() * 0.05 + 0.5
        saturation = np.random.randn() * 0.1 + 0.3

        if 'z' in keys:
            results.append({'color': tuple(element_master.color),
                            'seen': 1})
        if 'm' in keys:
            results.append({'color': tuple(element_master.color),
                            'seen': 0})
        if 'n' in keys:
            results.append({'color': tuple(element_master.color),
                            'seen': 0.5})

        element_master.color = [hue, saturation, value]

        if 'q' in keys:
            pandas.DataFrame(results).to_csv('results_blue.csv')
            break


    mywin.flip()
#print dots1.fieldPos, dots1._dotsXY

#pause, so you get a chance to see it!


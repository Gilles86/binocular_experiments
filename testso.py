from psychopy import visual, event, core

win = visual.Window(monitor='testMonitor', useFBO=True,
    blendMode='add', units='deg')

g = visual.GratingStim(win, tex='sin', mask='gauss', size=4.5, pos=(0,6))
t = visual.TextStim(win=win, text='Hello blendMode="add"!')

draw_order = [[g], [g, t], [g, t]]
for draw_now in draw_order:
    for stim in draw_now:
        stim.draw()
        win.blendMode = 'add'
    win.flip()
    event.waitKeys()

core.quit()

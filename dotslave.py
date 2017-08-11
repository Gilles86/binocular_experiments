from psychopy.visual import DotStim
from psychopy import logging
import numpy

class DotStimFBO(DotStim):
    def _getDesiredRGB(self, rgb, colorSpace, contrast):
        """ Convert color to RGB while adding contrast
        Requires self.rgb, self.colorSpace and self.contrast"""
        # Ensure that we work on 0-centered color (to make negative contrast values work)
        if colorSpace not in ['rgb', 'dkl', 'lms', 'hsv']:
            rgb = (rgb / 255.0) * 2 - 1

        # Convert to RGB in range 0:1 and scaled for contrast
        # NB glColor will clamp it to be 0-1 (whether or not we use FBO)

        # This is the patched line; it was desiredRGB = (rgb * contrast + 1) / 2.0
        desiredRGB = (rgb * contrast) / 2.0

        if not self.win.useFBO:
            # Check that boundaries are not exceeded. If we have an FBO that can handle this
            if numpy.any(desiredRGB > 1.0) or numpy.any(desiredRGB < 0):
                logging.warning('Desired color %s (in RGB 0->1 units) falls outside the monitor gamut. Drawing blue instead' %desiredRGB) #AOH
                desiredRGB=[0.0, 0.0, 1.0]

        return desiredRGB



class DotSlave(DotStim):
 
    def __init__(self, win, master, *args, **kwargs):
        self.master = master
        
        for attribute in ['nDots', 'fieldSize', 'dotSize', 'color', 'colorSpace']:
            kwargs[attribute] = kwargs.get(attribute, getattr(self.master, attribute))
            
        super(DotSlave, self).__init__(win, *args, **kwargs)


    def _update_dotsXY(self):
        self._verticesBase = self.master._verticesBase
        self._updateVertices()
        logging.debug('Updating _verticesBase: %s' % self._verticesBase)
                
    def _new_dotsXY(self):
        self._verticesBase = self.master._verticesBase
        logging.debug('New _verticesBase: %s' % self._verticesBase)

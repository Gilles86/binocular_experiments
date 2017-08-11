from psychopy.visual import DotStim
from psychopy import logging


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

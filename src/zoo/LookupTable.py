import numpy as np
from pyvista.plotting import get_cmap_safe, parse_color
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.util.numpy_support import numpy_to_vtk

# Drawing heavily from PyVista's `mapper.set_scalars` method
class LookupTable(vtkLookupTable):
    def __init__(
        self,
        cmap=None,
        above_color=None,
        below_color=None,
        reverse=False,
        num_colors=512,
    ) -> None:
        super().__init__()
        self.reverse = reverse
        self.num_colors = num_colors
        self.cmap = cmap
        self.above_color = above_color
        self.below_color = below_color

    @property
    def cmap(self):
        return self._cmap

    @property
    def above_color(self):
        return self._above_color

    @property
    def below_color(self):
        return self._below_color

    @cmap.setter
    def cmap(self, cmap):
        _cmap = get_cmap_safe(cmap)
        ctable = _cmap(np.linspace(0, 1, self.num_colors)) * 255
        ctable = ctable.astype(np.uint8)
        if self.reverse:
            ctable = np.ascontiguousarray(ctable[::-1])
        self.SetTable(numpy_to_vtk(ctable))

    @above_color.setter
    def above_color(self, above_color):
        if above_color:
            self.SetUseAboveRangeColor(True)
            self.SetAboveRangeColor(*parse_color(above_color, opacity=1))
        else:
            self.SetUseAboveRangeColor(False)
        self._above_color = above_color

    @below_color.setter
    def below_color(self, below_color):
        if below_color:
            self.SetUseBelowRangeColor(True)
            self.SetBelowRangeColor(*parse_color(below_color, opacity=1))
        else:
            self.SetUseBelowRangeColor(False)
        self._below_color = below_color

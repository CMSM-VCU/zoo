import numpy as np
from pyvista import Color
from pyvista.plotting import get_cmap_safe
from vtkmodules.util.numpy_support import numpy_to_vtk
from vtkmodules.vtkCommonCore import vtkLookupTable


# Drawing heavily from PyVista's `mapper.set_scalars` method
# github.com/pyvista/pyvista/blob/main/pyvista/plotting/mapper.py
class LookupTable(vtkLookupTable):
    def __init__(
        self,
        cmap=None,
        above_color=None,
        below_color=None,
        reverse=False,
        num_colors=256,
    ) -> None:
        super().__init__()
        self._reverse = reverse
        self._num_colors = num_colors
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

    @property
    def reverse(self):
        return self._reverse

    @property
    def num_colors(self):
        return self._num_colors

    # Compatibility with PyVista LookupTable class
    @property
    def n_values(self):
        return self._num_colors

    @cmap.setter
    def cmap(self, cmap):
        if cmap == "rainbow (legacy)":
            self.SetHueRange([0.0, 0.0])
            if self.reverse:
                self.SetHueRange([0.0, 0.66667])
            else:
                self.SetHueRange([0.66667, 0.0])
            self.ForceBuild()
        elif cmap:
            cmap_object = get_cmap_safe(cmap)
            ctable = cmap_object(np.linspace(0, 1, self.num_colors)) * 255
            ctable = ctable.astype(np.uint8)
            if self.reverse:
                ctable = np.ascontiguousarray(ctable[::-1])
            self.SetTable(numpy_to_vtk(ctable))
        self._cmap = cmap

    @above_color.setter
    def above_color(self, above_color):
        if above_color:
            self.SetUseAboveRangeColor(True)
            self.SetAboveRangeColor(*Color(above_color, opacity=1.0))
        else:
            self.SetUseAboveRangeColor(False)
        self._above_color = above_color

    @below_color.setter
    def below_color(self, below_color):
        if below_color:
            self.SetUseBelowRangeColor(True)
            self.SetBelowRangeColor(*Color(below_color, opacity=1.0))
        else:
            self.SetUseBelowRangeColor(False)
        self._below_color = below_color

    @reverse.setter
    def reverse(self, reverse: bool):
        if reverse != self._reverse:
            self._reverse = reverse
            self.cmap = self._cmap

    @num_colors.setter
    def num_colors(self, num_colors: bool):
        if num_colors != self._num_colors:
            self._num_colors = num_colors
            self.cmap = self._cmap

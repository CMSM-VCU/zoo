import typing

from qtpy import QtCore as qtc

LARGE: float = 1e12


class ContourState(qtc.QAbstractItemModel):
    class _Signals(qtc.QAbstractItemModel):
        def __init__(self) -> None:
            # fmt: off
            self.initialized                 = qtc.Signal()
            self.changed_timestep            = qtc.Signal(int)
            self.changed_glyph_size          = qtc.Signal(int)
            self.changed_exaggeration        = qtc.Signal(int)
            self.changed_plot_dataset        = qtc.Signal(int)
            self.changed_mask_dataset        = qtc.Signal(int)
            self.changed_clipping_extents    = qtc.Signal(int)
            self.changed_mask_limits         = qtc.Signal(int)
            self.changed_colorbar_limits     = qtc.Signal(int)
            self.changed_widget_property     = qtc.Signal(int)

            self.moved_camera                = qtc.Signal(int)
            # fmt: on

    def __init__(self) -> None:
        self.plot_and_mask_same_dataset: bool = True
        self.plot_dataset: str = None
        self.mask_dataset: str = None

        self.timestep_index: int = 0

        self.widget_properties = {}
        self.camera_location: typing.List[typing.Tuple[float, float, float]]

        # fmt: off
        self.glyph_size:          typing.List[float]  = [None, None, None]
        self.exaggeration:        typing.List[float]  = [0.0, 0.0, 0.0]
        self.clipping_extents:    typing.Tuple[float] = (None,) * 6
        self.mask_limits:         typing.List[float]  = [-LARGE, LARGE]
        self.colorbar_limits:     typing.List[float]  = [-LARGE, LARGE]
        # fmt: on

        self.signals = self._Signals()


if __name__ == "__main__":
    state = ContourState()

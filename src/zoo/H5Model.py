from abc import abstractmethod

from qtpy import QtCore as qtc


class H5Model(qtc.QAbstractItemModel):
    plotter: "InteractorLike"
    datasets: tuple[str]
    dataset: str
    timestep_index: int
    grid_spacing: float
    exaggeration: float
    loaded_file: qtc.Signal
    changed_timestep: qtc.Signal

    @abstractmethod
    def load_file(self, filename) -> None:
        ...

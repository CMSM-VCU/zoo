import typing
import numpy as np
from vtkmodules.vtkInteractionWidgets import vtkBoxWidget2

from .utils import truncate_int8_to_int4


class ClippingBox(vtkBoxWidget2):
    def __init__(self, controller, interactor, buffer_factor: float = 0.01) -> None:
        super().__init__()
        self.buffer_factor = buffer_factor
        self.controller = controller
        self.SetInteractor(interactor)
        self.GetRepresentation().SetPlaceFactor(1.0)
        self.GetRepresentation().SetOutlineCursorWires(False)
        self.SetRotationEnabled(False)
        self.SetTranslationEnabled(False)
        self.SetScalingEnabled(False)
        self.GetRepresentation().GetOutlineProperty().SetLineWidth(1.0)

        self.AddObserver("InteractionEvent", self.callback)
        self.controller.changed_clipping_extents.connect(self.update)

    def update(self, clipping_extents: typing.Tuple, instigator: int):
        if instigator == truncate_int8_to_int4(id(self)):
            return

        self.GetRepresentation().PlaceWidget(
            np.array(clipping_extents) * (1.0 + self.buffer_factor)
        )

    def callback(self, obj, event):
        self.controller.set_clipping_extents(
            np.array(self.GetRepresentation().GetBounds()) / (1.0 + self.buffer_factor),
            instigator=id(self),
        )

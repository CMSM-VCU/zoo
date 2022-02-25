import numpy as np
from vtkmodules.vtkInteractionWidgets import vtkBoxWidget2


class ClippingBox(vtkBoxWidget2):
    def __init__(self, model, interactor, buffer_factor: float = 0.01) -> None:
        super().__init__()
        self.buffer_factor = buffer_factor
        self.model = model
        self.SetInteractor(interactor)
        self.GetRepresentation().SetPlaceFactor(1.0)
        self.GetRepresentation().SetOutlineCursorWires(False)
        self.SetRotationEnabled(False)
        self.SetTranslationEnabled(False)
        self.SetScalingEnabled(False)
        self.GetRepresentation().GetOutlineProperty().SetLineWidth(1.0)

        self.AddObserver("InteractionEvent", self.callback)

    def update(self, bounds):
        self.GetRepresentation().PlaceWidget(
            np.array(bounds) * (1.0 + self.buffer_factor)
        )

    def callback(self, obj, event):
        self.model._set_clipping_extents(
            np.array(self.GetRepresentation().GetBounds()) / (1.0 + self.buffer_factor)
        )

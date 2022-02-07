from vtkmodules.vtkInteractionWidgets import vtkBoxWidget2


class ClippingBox(vtkBoxWidget2):
    def __init__(self, model, interactor) -> None:
        super().__init__()
        self.model = model
        self.SetInteractor(interactor)
        self.GetRepresentation().SetPlaceFactor(1)
        self.SetRotationEnabled(False)
        self.GetRepresentation().SetOutlineCursorWires(0)

        self.AddObserver("InteractionEvent", self.callback)

    def update(self, bounds):
        self.GetRepresentation().PlaceWidget(bounds)

    def callback(self, obj, event):
        self.model._set_clipping_extents(self.GetRepresentation().GetBounds())

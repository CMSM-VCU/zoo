import typing
from importlib import resources

import numpy as np
from loguru import logger
from vtkmodules.vtkRenderingCore import vtkActor
from vtkmodules.vtkRenderingOpenGL2 import vtkShader

EPSILON: float = 1e-6

srcGS = resources.read_text(__package__, "cubeGS.glsl")


class GlyphActor(vtkActor):
    def __init__(
        self,
        mapper,
        original_extents: typing.Tuple[float],
        grid_spacing: typing.Tuple[float],
    ) -> None:
        super().__init__()
        self.SetMapper(mapper)
        _shader_property = self.GetShaderProperty()
        _shader_property.AddShaderReplacement(
            vtkShader.Vertex,
            "//VTK::PositionVC::Dec",
            True,
            "//VTK::PositionVC::Dec\n"
            "out vec4 vertexMCVSOutput;\n"
            "in vec3 _disp;\n"
            "out vec4 dispMCVSOutput;\n"
            "in float _scalar;\n"
            "in float _mask_scalar;\n"
            "out float scalarVSOutput;\n"
            "out float maskscalarVSOutput;\n",
            False,
        )
        _shader_property.AddShaderReplacement(
            vtkShader.Vertex,
            "//VTK::PositionVC::Impl",
            True,
            "//VTK::PositionVC::Impl\n"
            "vertexMCVSOutput = vertexMC;\n"
            "dispMCVSOutput = vec4(_disp, 0.0);\n"
            "scalarVSOutput = _scalar;\n"
            "maskscalarVSOutput = _mask_scalar;\n",
            False,
        )
        _shader_property.SetGeometryShaderCode(srcGS)

        self._original_extents = original_extents
        self._applied_clipping_extents = None
        model_size = list(
            (np.array(original_extents[1::2]) - np.array(original_extents[::2]))
        )
        for i, dim in enumerate(model_size):
            if dim == 0.0:
                model_size[i] = grid_spacing[0]

        self.shader_params = _shader_property.GetGeometryCustomUniforms()
        if np.linalg.norm(model_size) ** 2 > 1000.000000:
            logger.debug(f"System span^2={np.linalg.norm(model_size)**2} <= 1000")
            self.shader_params.SetUniform4f("modelSize", [*model_size, 1.0])
            self.shader_params.SetUniform3f("epsilon_vector", [1e-3] * 3)
            self.use_model_coords = True
        else:
            logger.debug(f"System span^2={np.linalg.norm(model_size)**2} > 1000")
            self.shader_params.SetUniform4f("modelSize", [1.0, 1.0, 1.0, 1.0])
            self.shader_params.SetUniform3f(
                "epsilon_vector", [np.linalg.norm(model_size) / 1000.0] * 3
            )
            self.use_model_coords = False

        self.clipping_extents = self._original_extents

    @property
    def glyph_size(self) -> typing.Tuple[float]:
        return self._applied_glyph_size

    @glyph_size.setter
    def glyph_size(self, size: typing.Tuple[float]) -> None:
        logger.debug(f"Updating shaders with grid spacing {size}...")
        self.shader_params.SetUniform4f("glyph_scale", [*size, 0.0])
        self._applied_glyph_size = size

    @property
    def exaggeration(self) -> typing.Tuple[float]:
        return self._applied_exaggeration

    @exaggeration.setter
    def exaggeration(self, exag: typing.Tuple[float]) -> None:
        logger.debug(f"Updating shaders with exaggeration {exag}...")
        self.shader_params.SetUniform4f("disp_scale", [*exag, 0.0])
        self._applied_exaggeration = exag

    @property
    def mask_limits(self) -> typing.Tuple[float]:
        return self._applied_mask_limits

    @mask_limits.setter
    def mask_limits(self, limits: typing.Tuple[float]) -> None:
        logger.debug(f"Updating shaders with mask limits {limits}...")
        self.shader_params.SetUniform2f("mask_limits", limits)
        self._applied_mask_limits = limits

    @property
    def clipping_extents(self) -> typing.Tuple[float]:
        return self._applied_clipping_extents

    @clipping_extents.setter
    def clipping_extents(self, extents: typing.Tuple[float]) -> None:
        if extents == self._applied_clipping_extents:
            logger.debug(
                f"Clipping extents {extents} same as current value. Update not applied."
            )
            return
        logger.debug(f"Updating shaders with clipping extents {extents}...")
        if self.use_model_coords:
            extents_MC = bbox_to_model_coordinates(extents, self._original_extents)
        else:
            extents_MC = (extents[::2], extents[1::2])
        logger.debug(
            "Actual values sent to shaders: "
            + f"bottom left - {extents_MC[0]}, top right - {extents_MC[1]}"
        )

        self.shader_params.SetUniform3f("bottomLeft", extents_MC[0])
        self.shader_params.SetUniform3f("topRight", extents_MC[1])
        self._applied_clipping_extents = extents


def bbox_to_model_coordinates(
    bbox_bounds: typing.Tuple[float], base_bounds: typing.Tuple[float]
) -> typing.Tuple[typing.List[float]]:
    base_bottom_left = np.array(base_bounds[::2])
    base_top_right = np.array(base_bounds[1::2])

    size = base_top_right - base_bottom_left
    if not np.all(size):
        logger.info(f"Padding zero-length bounds with {EPSILON}")
        size += EPSILON

    bbox_mc_bl = (np.array(bbox_bounds[::2]) - base_bottom_left) / (size) - 0.5

    bbox_mc_tr = ((np.array(bbox_bounds[1::2]) - base_top_right) / (size)) + 0.5
    return (list(bbox_mc_bl), list(bbox_mc_tr))

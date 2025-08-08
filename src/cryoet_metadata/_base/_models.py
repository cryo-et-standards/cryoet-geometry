from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, conlist

metamodel_version = "None"
version = "0.0.1"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = None


class AxisType(str, Enum):
    """
    The type of axis
    """

    # A spatial axis
    space = "space"
    # An array axis
    array = "array"


class TransformationType(str, Enum):
    # The identity transformation.
    identity = "identity"
    # Axis permutation transformation
    mapAxis = "mapAxis"
    # A translation transformation.
    translation = "translation"
    # A scaling transformation.
    scale = "scale"
    # An affine transformation
    affine = "affine"
    # A sequence of transformations
    sequence = "sequence"


class Image2D(ConfiguredBaseModel):
    """
    A 2D image.
    """

    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class Image3D(ConfiguredBaseModel):
    """
    A 3D image.
    """

    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    depth: Optional[int] = Field(default=None, description="""The depth of the image (z-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class ImageStack2D(ConfiguredBaseModel):
    """
    A stack of 2D images.
    """

    images: Optional[List[Image2D]] = Field(default=None, description="""The images in the stack""")


class ImageStack3D(ConfiguredBaseModel):
    """
    A stack of 3D images.
    """

    images: Optional[List[Image3D]] = Field(default=None, description="""The images in the stack""")


class Axis(ConfiguredBaseModel):
    """
    An axis in a coordinate system
    """

    name: str = Field(default=...)
    axis_unit: Optional[str] = Field(default=None)
    axis_type: Optional[str] = Field(default=None)


class CoordinateSystem(ConfiguredBaseModel):
    """
    A coordinate system
    """

    name: str = Field(default=..., description="""The name of the coordinate system""")
    axes: List[Axis] = Field(default=..., description="""The axes of the coordinate system""")


class CoordinateTransformation(ConfiguredBaseModel):
    """
    A coordinate transformation
    """

    name: Optional[str] = Field(default=None, description="""The name of the coordinate transformation""")
    input: Optional[str] = Field(default=None, description="""The source coordinate system name""")
    output: Optional[str] = Field(default=None, description="""The target coordinate system name""")
    type: Optional[TransformationType] = Field(default=None, description="""The type of transformation""")


class Identity(CoordinateTransformation):
    """
    The identity transformation
    """

    type: Optional[TransformationType] = Field(default="identity", description="""The type of transformation""")
    name: Optional[str] = Field(default=None, description="""The name of the coordinate transformation""")
    input: Optional[str] = Field(default=None, description="""The source coordinate system name""")
    output: Optional[str] = Field(default=None, description="""The target coordinate system name""")


class AxisNameMapping(ConfiguredBaseModel):
    """
    Axis name to Axis name mapping
    """

    axis1_name: Optional[str] = Field(default=None, description="""The type of transformation""")
    axis2_name: Optional[str] = Field(default=None, description="""The mapping of the axis names""")


class MapAxis(CoordinateTransformation):
    """
    Axis permutation transformation
    """

    type: Optional[TransformationType] = Field(default="mapAxis", description="""The type of transformation""")
    mapAxis: Optional[List[AxisNameMapping]] = Field(default=None, description="""The permutation of the axes""")
    name: Optional[str] = Field(default=None, description="""The name of the coordinate transformation""")
    input: Optional[str] = Field(default=None, description="""The source coordinate system name""")
    output: Optional[str] = Field(default=None, description="""The target coordinate system name""")


class Translation(CoordinateTransformation):
    """
    A translation transformation
    """

    type: Optional[TransformationType] = Field(default="translation", description="""The type of transformation""")
    translation: Optional[List[float]] = Field(default=None, description="""The translation vector""")
    name: Optional[str] = Field(default=None, description="""The name of the coordinate transformation""")
    input: Optional[str] = Field(default=None, description="""The source coordinate system name""")
    output: Optional[str] = Field(default=None, description="""The target coordinate system name""")


class Scale(CoordinateTransformation):
    """
    A scaling transformation
    """

    type: Optional[TransformationType] = Field(default="scale", description="""The type of transformation""")
    scale: Optional[List[float]] = Field(default=None, description="""The scaling vector""")
    name: Optional[str] = Field(default=None, description="""The name of the coordinate transformation""")
    input: Optional[str] = Field(default=None, description="""The source coordinate system name""")
    output: Optional[str] = Field(default=None, description="""The target coordinate system name""")


class Affine(CoordinateTransformation):
    """
    An affine transformation
    """

    type: Optional[TransformationType] = Field(default="affine", description="""The type of transformation""")
    affine: Optional[
        conlist(min_length=3, max_length=3, item_type=conlist(min_length=3, max_length=3, item_type=int))
    ] = Field(default=None, description="""The affine matrix""")
    name: Optional[str] = Field(default=None, description="""The name of the coordinate transformation""")
    input: Optional[str] = Field(default=None, description="""The source coordinate system name""")
    output: Optional[str] = Field(default=None, description="""The target coordinate system name""")


class Sequence(CoordinateTransformation):
    """
    A sequence of transformations
    """

    type: Optional[TransformationType] = Field(default="sequence", description="""The type of transformation""")
    sequence: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""The sequence of transformations""",
    )
    name: Optional[str] = Field(default=None, description="""The name of the coordinate transformation""")
    input: Optional[str] = Field(default=None, description="""The source coordinate system name""")
    output: Optional[str] = Field(default=None, description="""The target coordinate system name""")


class ProjectionAlignment(Sequence):
    """
    The tomographic alignment for a single projection.
    """

    input: Optional[str] = Field(default=None, description="""The source coordinate system name""")
    output: Optional[str] = Field(default=None, description="""The target coordinate system name""")
    sequence: Optional[List[Union[Affine, Translation]]] = Field(
        default=None,
        description="""The sequence of transformations""",
        max_length=2,
    )
    type: Optional[TransformationType] = Field(default="sequence", description="""The type of transformation""")
    name: Optional[str] = Field(default=None, description="""The name of the coordinate transformation""")


class Alignment(ConfiguredBaseModel):
    """
    The tomographic alignment for a tilt series.
    """

    projection_alignments: Optional[List[ProjectionAlignment]] = Field(
        default=None,
        description="""alignment for a specific projection""",
    )


class CTFMetadata(ConfiguredBaseModel):
    """
    A set of CTF patameters for an image.
    """

    defocus_u: Optional[float] = Field(
        default=None,
        description="""Estimated defocus U for this image in Angstrom, underfocus positive.""",
    )
    defocus_v: Optional[float] = Field(
        default=None,
        description="""Estimated defocus V for this image in Angstrom, underfocus positive.""",
    )
    defocus_angle: Optional[float] = Field(default=None, description="""Estimated angle of astigmatism.""")


class AcquisitionMetadataMixin(ConfiguredBaseModel):
    """
    Metadata concerning the acquisition process.
    """

    nominal_tilt_angle: Optional[float] = Field(
        default=None,
        description="""The tilt angle reported by the microscope""",
    )
    accumulated_dose: Optional[float] = Field(
        default=None,
        description="""The pre-exposure up to this image in e-/A^2""",
    )
    ctf_metadata: Optional[CTFMetadata] = Field(default=None, description="""A set of CTF patameters for an image.""")


class GainFile(Image2D):
    """
    A gain reference file.
    """

    path: Optional[str] = Field(default=None, description="""Path to a file.""")
    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class DefectFile(Image2D):
    """
    A detector defect file.
    """

    path: Optional[str] = Field(default=None, description="""Path to a file.""")
    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class MovieFrame(AcquisitionMetadataMixin, Image2D):
    """
    An individual movie frame
    """

    path: Optional[str] = Field(default=None, description="""Path to a file.""")
    section: Optional[str] = Field(default=None, description="""0-based section index to the entity inside a stack.""")
    nominal_tilt_angle: Optional[float] = Field(
        default=None,
        description="""The tilt angle reported by the microscope""",
    )
    accumulated_dose: Optional[float] = Field(
        default=None,
        description="""The pre-exposure up to this image in e-/A^2""",
    )
    ctf_metadata: Optional[CTFMetadata] = Field(default=None, description="""A set of CTF patameters for an image.""")
    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class MovieStack(ConfiguredBaseModel):
    """
    A stack of movie frames.
    """

    images: Optional[List[MovieFrame]] = Field(default=None, description="""The movie frames in the stack""")
    path: Optional[str] = Field(default=None)


class ProjectionImage(AcquisitionMetadataMixin, Image2D):
    """
    A projection image.
    """

    path: Optional[str] = Field(default=None, description="""Path to a file.""")
    section: Optional[str] = Field(default=None, description="""0-based section index to the entity inside a stack.""")
    nominal_tilt_angle: Optional[float] = Field(
        default=None,
        description="""The tilt angle reported by the microscope""",
    )
    accumulated_dose: Optional[float] = Field(
        default=None,
        description="""The pre-exposure up to this image in e-/A^2""",
    )
    ctf_metadata: Optional[CTFMetadata] = Field(default=None, description="""A set of CTF patameters for an image.""")
    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class MovieStackSeries(ConfiguredBaseModel):
    """
    A group of movie stacks that belong to a single tilt series.
    """

    stacks: Optional[List[MovieStack]] = Field(default=None, description="""The movie stacks.""")


class TiltSeries(ConfiguredBaseModel):
    """
    A stack of projection images.
    """

    images: Optional[List[ProjectionImage]] = Field(default=None, description="""The projections in the stack""")
    path: Optional[str] = Field(default=None)


class SubProjectionImage(ProjectionImage):
    """
    A croppecd projection image.
    """

    particle_index: Optional[int] = Field(default=None, description="""Index of a particle inside a tomogram.""")
    path: Optional[str] = Field(default=None, description="""Path to a file.""")
    section: Optional[str] = Field(default=None, description="""0-based section index to the entity inside a stack.""")
    nominal_tilt_angle: Optional[float] = Field(
        default=None,
        description="""The tilt angle reported by the microscope""",
    )
    accumulated_dose: Optional[float] = Field(
        default=None,
        description="""The pre-exposure up to this image in e-/A^2""",
    )
    ctf_metadata: Optional[CTFMetadata] = Field(default=None, description="""A set of CTF patameters for an image.""")
    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class Tomogram(Image3D):
    """
    A 3D tomogram.
    """

    path: Optional[str] = Field(default=None, description="""Path to a file.""")
    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    depth: Optional[int] = Field(default=None, description="""The depth of the image (z-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class ParticleMap(Image3D):
    """
    A 3D particle density map.
    """

    path: Optional[str] = Field(default=None, description="""Path to a file.""")
    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    depth: Optional[int] = Field(default=None, description="""The depth of the image (z-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class CoordMetaMixin(ConfiguredBaseModel):
    """
    Coordinate system mixins for annotations.
    """

    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )


class Annotation(ConfiguredBaseModel):
    """
    A primitive annotation.
    """

    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class SegmentationMask2D(Annotation, Image2D):
    """
    An annotation image with categorical labels.
    """

    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class SegmentationMask3D(Annotation, Image3D):
    """
    An annotation volume with categorical labels.
    """

    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    depth: Optional[int] = Field(default=None, description="""The depth of the image (z-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class ProbabilityMap2D(Annotation, Image2D):
    """
    An annotation image with real-valued labels.
    """

    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class ProbabilityMap3D(Annotation, Image3D):
    """
    An annotation volume with real-valued labels.
    """

    width: Optional[int] = Field(default=None, description="""The width of the image (x-axis) in pixels""")
    height: Optional[int] = Field(default=None, description="""The height of the image (y-axis) in pixels""")
    depth: Optional[int] = Field(default=None, description="""The depth of the image (z-axis) in pixels""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class PointSet2D(Annotation, CoordMetaMixin):
    """
    A set of 2D point annotations.
    """

    origin2D: Optional[conlist(min_length=1, item_type=conlist(min_length=2, max_length=2, item_type=float))] = Field(
        default=None,
        description="""Location on a 2D image (Nx2).""",
    )
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class PointSet3D(Annotation, CoordMetaMixin):
    """
    A set of 3D point annotations.
    """

    origin3D: Optional[conlist(min_length=1, item_type=conlist(min_length=3, max_length=3, item_type=float))] = Field(
        default=None,
        description="""Location on a 3D image (Nx3).""",
    )
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class PointVectorSet2D(Annotation, CoordMetaMixin):
    """
    A set of 2D points with an associated direction vector.
    """

    origin2D: Optional[conlist(min_length=1, item_type=conlist(min_length=2, max_length=2, item_type=float))] = Field(
        default=None,
        description="""Location on a 2D image (Nx2).""",
    )
    vector2D: Optional[conlist(min_length=1, item_type=conlist(min_length=2, max_length=2, item_type=float))] = Field(
        default=None,
        description="""Orientation vector associated with a point on a 2D image (Nx2).""",
    )
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class PointVectorSet3D(Annotation, CoordMetaMixin):
    """
    A set of 3D points with an associated direction vector.
    """

    origin3D: Optional[conlist(min_length=1, item_type=conlist(min_length=3, max_length=3, item_type=float))] = Field(
        default=None,
        description="""Location on a 3D image (Nx3).""",
    )
    vector3D: Optional[conlist(min_length=1, item_type=conlist(min_length=3, max_length=3, item_type=float))] = Field(
        default=None,
        description="""Orientation vector associated with a point on a 3D image (Nx3).""",
    )
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class PointMatrixSet2D(Annotation, CoordMetaMixin):
    """
    A set of 2D points with an associated rotation matrix.
    """

    origin2D: Optional[conlist(min_length=1, item_type=conlist(min_length=2, max_length=2, item_type=float))] = Field(
        default=None,
        description="""Location on a 2D image (Nx2).""",
    )
    matrix2D: Optional[
        conlist(
            min_length=1,
            item_type=conlist(
                min_length=2,
                max_length=2,
                item_type=conlist(min_length=2, max_length=2, item_type=float),
            ),
        )
    ] = Field(default=None, description="""Rotation matrix associated with a point on a 2D image (Nx2x2).""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class PointMatrixSet3D(Annotation, CoordMetaMixin):
    """
    A set of 3D points with an associated rotation matrix.
    """

    origin3D: Optional[conlist(min_length=1, item_type=conlist(min_length=3, max_length=3, item_type=float))] = Field(
        default=None,
        description="""Location on a 3D image (Nx3).""",
    )
    matrix3D: Optional[
        conlist(
            min_length=1,
            item_type=conlist(
                min_length=3,
                max_length=3,
                item_type=conlist(min_length=3, max_length=3, item_type=float),
            ),
        )
    ] = Field(default=None, description="""Rotation matrix associated with a point on a 3D image (Nx3x3).""")
    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class TriMesh(Annotation, CoordMetaMixin):
    """
    A mesh annotation.
    """

    coordinate_systems: Optional[List[CoordinateSystem]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    coordinate_transformations: Optional[List[CoordinateTransformation]] = Field(
        default=None,
        description="""Named coordinate systems for this entity""",
    )
    path: Optional[str] = Field(default=None, description="""Path to a file.""")


class Region(ConfiguredBaseModel):
    """
    Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen.
    """

    movie_stack_collections: Optional[List[MovieStackCollection]] = Field(
        default=None,
        description="""The movie stack""",
    )
    tilt_series: Optional[List[TiltSeries]] = Field(default=None, description="""The tilt series""")
    alignments: Optional[List[Alignment]] = Field(default=None, description="""The alignments""")
    tomograms: Optional[List[Tomogram]] = Field(default=None, description="""The tomograms""")
    annotations: Optional[List[Annotation]] = Field(default=None, description="""The annotations for this region""")


class Average(ConfiguredBaseModel):
    """
    A particle averaging experiment.
    """

    name: Optional[str] = Field(default=None, description="""The name of the averaging experiment.""")
    particle_maps: Optional[List[ParticleMap]] = Field(default=None, description="""The particle maps""")
    annotations: Optional[List[Annotation]] = Field(default=None, description="""The annotations""")


class MovieStackCollection(ConfiguredBaseModel):
    """
    A collection of movie stacks using the same gain and defect files.
    """

    movie_stacks: Optional[List[MovieStackSeries]] = Field(
        default=None,
        description="""The movie stacks in the collection""",
    )
    GainFile: Optional[GainFile] = Field(default=None, description="""The gain file for the movie stacks""")
    DefectFile: Optional[DefectFile] = Field(default=None, description="""The defect file for the movie stacks""")


class Dataset(ConfiguredBaseModel):
    """
    A dataset
    """

    name: Optional[str] = Field(default=None, description="""The name of the dataset""")
    regions: Optional[List[Region]] = Field(default=None, description="""The regions in the dataset""")
    averages: Optional[List[Average]] = Field(default=None, description="""The averages in the dataset""")


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Image2D.model_rebuild()
Image3D.model_rebuild()
ImageStack2D.model_rebuild()
ImageStack3D.model_rebuild()
Axis.model_rebuild()
CoordinateSystem.model_rebuild()
CoordinateTransformation.model_rebuild()
Identity.model_rebuild()
AxisNameMapping.model_rebuild()
MapAxis.model_rebuild()
Translation.model_rebuild()
Scale.model_rebuild()
Affine.model_rebuild()
Sequence.model_rebuild()
ProjectionAlignment.model_rebuild()
Alignment.model_rebuild()
CTFMetadata.model_rebuild()
AcquisitionMetadataMixin.model_rebuild()
GainFile.model_rebuild()
DefectFile.model_rebuild()
MovieFrame.model_rebuild()
MovieStack.model_rebuild()
ProjectionImage.model_rebuild()
MovieStackSeries.model_rebuild()
TiltSeries.model_rebuild()
SubProjectionImage.model_rebuild()
Tomogram.model_rebuild()
ParticleMap.model_rebuild()
CoordMetaMixin.model_rebuild()
Annotation.model_rebuild()
SegmentationMask2D.model_rebuild()
SegmentationMask3D.model_rebuild()
ProbabilityMap2D.model_rebuild()
ProbabilityMap3D.model_rebuild()
PointSet2D.model_rebuild()
PointSet3D.model_rebuild()
PointVectorSet2D.model_rebuild()
PointVectorSet3D.model_rebuild()
PointMatrixSet2D.model_rebuild()
PointMatrixSet3D.model_rebuild()
TriMesh.model_rebuild()
Region.model_rebuild()
Average.model_rebuild()
MovieStackCollection.model_rebuild()
Dataset.model_rebuild()

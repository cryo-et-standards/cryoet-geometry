# entities

Schema for cryoET geometry

URI: https://w3id.org/cetmd/entities

Name: entities



## Classes

| Class | Description |
| --- | --- |
| [AcquisitionMetadataMixin](AcquisitionMetadataMixin.md) | Metadata concerning the acquisition process. |
| [Alignment](Alignment.md) | The tomographic alignment for a tilt series. |
| [Annotation](Annotation.md) | A primitive annotation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointMatrixSet2D](PointMatrixSet2D.md) | A set of 2D points with an associated rotation matrix. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointMatrixSet3D](PointMatrixSet3D.md) | A set of 3D points with an associated rotation matrix. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointSet2D](PointSet2D.md) | A set of 2D point annotations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointSet3D](PointSet3D.md) | A set of 3D point annotations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointVectorSet2D](PointVectorSet2D.md) | A set of 2D points with an associated direction vector. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointVectorSet3D](PointVectorSet3D.md) | A set of 3D points with an associated direction vector. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProbabilityMap2D](ProbabilityMap2D.md) | An annotation image with real-valued labels. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProbabilityMap3D](ProbabilityMap3D.md) | An annotation volume with real-valued labels. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SegmentationMask2D](SegmentationMask2D.md) | An annotation image with categorical labels. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SegmentationMask3D](SegmentationMask3D.md) | An annotation volume with categorical labels. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TriMesh](TriMesh.md) | A mesh annotation. |
| [Average](Average.md) | A particle averaging experiment. |
| [Axis](Axis.md) | An axis in a coordinate system |
| [AxisNameMapping](AxisNameMapping.md) | Axis name to Axis name mapping |
| [CoordinateSystem](CoordinateSystem.md) | A coordinate system |
| [CoordinateTransformation](CoordinateTransformation.md) | A coordinate transformation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Affine](Affine.md) | An affine transformation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Identity](Identity.md) | The identity transformation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MapAxis](MapAxis.md) | Axis permutation transformation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Scale](Scale.md) | A scaling transformation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sequence](Sequence.md) | A sequence of transformations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProjectionAlignment](ProjectionAlignment.md) | The tomographic alignment for a single projection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Translation](Translation.md) | A translation transformation |
| [CoordMetaMixin](CoordMetaMixin.md) | Coordinate system mixins for annotations. |
| [CTFMetadata](CTFMetadata.md) | A set of CTF patameters for an image. |
| [Dataset](Dataset.md) | A dataset |
| [Image2D](Image2D.md) | A 2D image. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DefectFile](DefectFile.md) | A detector defect file. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GainFile](GainFile.md) | A gain reference file. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MovieFrame](MovieFrame.md) | An individual movie frame |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProjectionImage](ProjectionImage.md) | A projection image. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SubProjectionImage](SubProjectionImage.md) | A croppecd projection image. |
| [Image3D](Image3D.md) | A 3D image. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ParticleMap](ParticleMap.md) | A 3D particle density map. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Tomogram](Tomogram.md) | A 3D tomogram. |
| [ImageStack2D](ImageStack2D.md) | A stack of 2D images. |
| [ImageStack3D](ImageStack3D.md) | A stack of 3D images. |
| [MovieStack](MovieStack.md) | A stack of movie frames. |
| [MovieStackCollection](MovieStackCollection.md) | A collection of movie stacks using the same gain and defect files. |
| [MovieStackSeries](MovieStackSeries.md) | A group of movie stacks that belong to a single tilt series. |
| [Region](Region.md) | Raw data (movie stacks) and derived data (tilt series, tomograms, annotations) from a single region of a specimen. |
| [TiltSeries](TiltSeries.md) | A stack of projection images. |



## Slots

| Slot | Description |
| --- | --- |
| [accumulated_dose](accumulated_dose.md) | The pre-exposure up to this image in e-/A^2 |
| [affine](affine.md) | The affine matrix |
| [alignments](alignments.md) | The alignments |
| [annotations](annotations.md) | The annotations |
| [averages](averages.md) | The averages in the dataset |
| [axes](axes.md) | The axes of the coordinate system |
| [axis1_name](axis1_name.md) | The type of transformation |
| [axis2_name](axis2_name.md) | The mapping of the axis names |
| [axis_name](axis_name.md) | The name of the axis |
| [axis_type](axis_type.md) | The type of axis |
| [axis_unit](axis_unit.md) | The unit of the axis |
| [coordinate_systems](coordinate_systems.md) | Named coordinate systems for this entity |
| [coordinate_transformations](coordinate_transformations.md) | Named coordinate systems for this entity |
| [ctf_metadata](ctf_metadata.md) | A set of CTF patameters for an image |
| [defect_file](defect_file.md) | The defect file for the movie stacks |
| [defocus_angle](defocus_angle.md) | Estimated angle of astigmatism |
| [defocus_u](defocus_u.md) | Estimated defocus U for this image in Angstrom, underfocus positive |
| [defocus_v](defocus_v.md) | Estimated defocus V for this image in Angstrom, underfocus positive |
| [depth](depth.md) | The depth of the image (z-axis) in pixels |
| [gain_file](gain_file.md) | The gain file for the movie stacks |
| [height](height.md) | The height of the image (y-axis) in pixels |
| [images2D](images2D.md) | The images in the stack |
| [images3D](images3D.md) | The images in the stack |
| [images_movie](images_movie.md) | The movie frames in the stack |
| [images_tilt](images_tilt.md) | The projections in the stack |
| [input](input.md) | The source coordinate system name |
| [map_axis](map_axis.md) | The permutation of the axes |
| [matrix2D](matrix2D.md) | Rotation matrix associated with a point on a 2D image (Nx2x2) |
| [matrix3D](matrix3D.md) | Rotation matrix associated with a point on a 3D image (Nx3x3) |
| [movie_stack_collections](movie_stack_collections.md) | The movie stack |
| [movie_stacks](movie_stacks.md) | The movie stacks in the collection |
| [name](name.md) | The name of a given entry |
| [nominal_tilt_angle](nominal_tilt_angle.md) | The tilt angle reported by the microscope |
| [origin2D](origin2D.md) | Location on a 2D image (Nx2) |
| [origin3D](origin3D.md) | Location on a 3D image (Nx3) |
| [output](output.md) | The target coordinate system name |
| [particle_index](particle_index.md) | Index of a particle inside a tomogram |
| [particle_maps](particle_maps.md) | The particle maps |
| [path](path.md) | Path to a file |
| [projection_alignments](projection_alignments.md) | alignment for a specific projection |
| [regions](regions.md) | The regions in the dataset |
| [scale](scale.md) | The scaling vector |
| [section](section.md) | 0-based section index to the entity inside a stack |
| [sequence](sequence.md) | The sequence of transformations |
| [stacks](stacks.md) | The movie stacks |
| [tilt_series](tilt_series.md) | The tilt series |
| [tomograms](tomograms.md) | The tomograms |
| [transformation_type](transformation_type.md) | The type of transformation |
| [translation](translation.md) | The translation vector |
| [translation2D](translation2D.md) | Offset from the origin of a point on a 2D image (Nx2) |
| [translation3D](translation3D.md) | Offset from the origin of a point on a 3D image (Nx3) |
| [vector2D](vector2D.md) | Orientation vector associated with a point on a 2D image (Nx2) |
| [vector3D](vector3D.md) | Orientation vector associated with a point on a 3D image (Nx3) |
| [width](width.md) | The width of the image (x-axis) in pixels |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AxisType](AxisType.md) | The type of axis |
| [TransformationType](TransformationType.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |

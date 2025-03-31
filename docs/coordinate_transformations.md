

# Slot: coordinate_transformations


_Named coordinate systems for this entity_





URI: [https://w3id.org/cetmd/entities/:coordinate_transformations](https://w3id.org/cetmd/entities/:coordinate_transformations)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DefectFile](DefectFile.md) | A detector defect file |  no  |
| [SubProjectionImage](SubProjectionImage.md) | A croppecd projection image |  no  |
| [TriMesh](TriMesh.md) | A mesh annotation |  no  |
| [PointMatrixSet3D](PointMatrixSet3D.md) | A set of 3D points with an associated rotation matrix |  no  |
| [SegmentationMask2D](SegmentationMask2D.md) | An annotation image with categorical labels |  no  |
| [Tomogram](Tomogram.md) | A 3D tomogram |  no  |
| [SegmentationMask3D](SegmentationMask3D.md) | An annotation volume with categorical labels |  no  |
| [Image3D](Image3D.md) | A 3D image |  no  |
| [PointSet2D](PointSet2D.md) | A set of 2D point annotations |  no  |
| [MovieFrame](MovieFrame.md) | An individual movie frame |  no  |
| [ProbabilityMap3D](ProbabilityMap3D.md) | An annotation volume with real-valued labels |  no  |
| [PointVectorSet3D](PointVectorSet3D.md) | A set of 3D points with an associated direction vector |  no  |
| [GainFile](GainFile.md) | A gain reference file |  no  |
| [PointVectorSet2D](PointVectorSet2D.md) | A set of 2D points with an associated direction vector |  no  |
| [ParticleMap](ParticleMap.md) | A 3D particle density map |  no  |
| [PointSet3D](PointSet3D.md) | A set of 3D point annotations |  no  |
| [ProbabilityMap2D](ProbabilityMap2D.md) | An annotation image with real-valued labels |  no  |
| [ProjectionImage](ProjectionImage.md) | A projection image |  no  |
| [Image2D](Image2D.md) | A 2D image |  no  |
| [PointMatrixSet2D](PointMatrixSet2D.md) | A set of 2D points with an associated rotation matrix |  no  |
| [CoordMetaMixin](CoordMetaMixin.md) | Coordinate system mixins for annotations |  no  |







## Properties

* Range: [CoordinateTransformation](CoordinateTransformation.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:coordinate_transformations |
| native | https://w3id.org/cetmd/entities/:coordinate_transformations |




## LinkML Source

<details>
```yaml
name: coordinate_transformations
description: Named coordinate systems for this entity
from_schema: https://w3id.org/cetmd/entities
rank: 1000
alias: coordinate_transformations
domain_of:
- Image2D
- Image3D
- CoordMetaMixin
range: CoordinateTransformation
multivalued: true

```
</details>
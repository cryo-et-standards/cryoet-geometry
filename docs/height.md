

# Slot: height


_The height of the image (y-axis) in pixels_





URI: [https://w3id.org/cetmd/entities/:height](https://w3id.org/cetmd/entities/:height)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DefectFile](DefectFile.md) | A detector defect file |  no  |
| [SubProjectionImage](SubProjectionImage.md) | A croppecd projection image |  no  |
| [ParticleMap](ParticleMap.md) | A 3D particle density map |  no  |
| [MovieFrame](MovieFrame.md) | An individual movie frame |  no  |
| [ProbabilityMap3D](ProbabilityMap3D.md) | An annotation volume with real-valued labels |  no  |
| [SegmentationMask2D](SegmentationMask2D.md) | An annotation image with categorical labels |  no  |
| [Tomogram](Tomogram.md) | A 3D tomogram |  no  |
| [SegmentationMask3D](SegmentationMask3D.md) | An annotation volume with categorical labels |  no  |
| [ProbabilityMap2D](ProbabilityMap2D.md) | An annotation image with real-valued labels |  no  |
| [GainFile](GainFile.md) | A gain reference file |  no  |
| [ProjectionImage](ProjectionImage.md) | A projection image |  no  |
| [Image2D](Image2D.md) | A 2D image |  no  |
| [Image3D](Image3D.md) | A 3D image |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:height |
| native | https://w3id.org/cetmd/entities/:height |




## LinkML Source

<details>
```yaml
name: height
description: The height of the image (y-axis) in pixels
from_schema: https://w3id.org/cetmd/entities
rank: 1000
alias: height
domain_of:
- Image2D
- Image3D
range: integer

```
</details>
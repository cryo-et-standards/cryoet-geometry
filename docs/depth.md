

# Slot: depth


_The depth of the image (z-axis) in pixels_





URI: [https://w3id.org/cetmd/entities/:depth](https://w3id.org/cetmd/entities/:depth)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ParticleMap](ParticleMap.md) | A 3D particle density map |  no  |
| [ProbabilityMap3D](ProbabilityMap3D.md) | An annotation volume with real-valued labels |  no  |
| [Tomogram](Tomogram.md) | A 3D tomogram |  no  |
| [SegmentationMask3D](SegmentationMask3D.md) | An annotation volume with categorical labels |  no  |
| [Image3D](Image3D.md) | A 3D image |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:depth |
| native | https://w3id.org/cetmd/entities/:depth |




## LinkML Source

<details>
```yaml
name: depth
description: The depth of the image (z-axis) in pixels
from_schema: https://w3id.org/cetmd/entities
rank: 1000
alias: depth
domain_of:
- Image3D
range: integer

```
</details>
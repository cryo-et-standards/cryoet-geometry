

# Slot: transformation_type


_The type of transformation_





URI: [https://w3id.org/cetmd/entities/:transformation_type](https://w3id.org/cetmd/entities/:transformation_type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MapAxis](MapAxis.md) | Axis permutation transformation |  yes  |
| [Sequence](Sequence.md) | A sequence of transformations |  yes  |
| [Identity](Identity.md) | The identity transformation |  yes  |
| [Affine](Affine.md) | An affine transformation |  yes  |
| [CoordinateTransformation](CoordinateTransformation.md) | A coordinate transformation |  no  |
| [ProjectionAlignment](ProjectionAlignment.md) | The tomographic alignment for a single projection |  no  |
| [Translation](Translation.md) | A translation transformation |  yes  |
| [Scale](Scale.md) | A scaling transformation |  yes  |







## Properties

* Range: [TransformationType](TransformationType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:transformation_type |
| native | https://w3id.org/cetmd/entities/:transformation_type |




## LinkML Source

<details>
```yaml
name: transformation_type
description: The type of transformation
from_schema: https://w3id.org/cetmd/entities
rank: 1000
alias: transformation_type
domain_of:
- CoordinateTransformation
- Identity
- MapAxis
- Translation
- Scale
- Affine
- Sequence
range: TransformationType

```
</details>
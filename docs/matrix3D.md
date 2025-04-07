

# Slot: matrix3D


_Rotation matrix associated with a point on a 3D image (Nx3x3)._





URI: [https://w3id.org/cetmd/entities/:matrix3D](https://w3id.org/cetmd/entities/:matrix3D)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointMatrixSet3D](PointMatrixSet3D.md) | A set of 3D points with an associated rotation matrix |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:matrix3D |
| native | https://w3id.org/cetmd/entities/:matrix3D |




## LinkML Source

<details>
```yaml
name: matrix3D
description: Rotation matrix associated with a point on a 3D image (Nx3x3).
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 3
  dimensions:
  - alias: N
    minimum_cardinality: 1
  - alias: xyz
    exact_cardinality: 3
  - alias: xyz
    exact_cardinality: 3
alias: matrix3D
domain_of:
- PointMatrixSet3D
range: float

```
</details>
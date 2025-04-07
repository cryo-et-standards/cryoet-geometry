

# Slot: origin3D


_Location on a 3D image (Nx3)._





URI: [https://w3id.org/cetmd/entities/:origin3D](https://w3id.org/cetmd/entities/:origin3D)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointSet3D](PointSet3D.md) | A set of 3D point annotations |  no  |
| [PointVectorSet3D](PointVectorSet3D.md) | A set of 3D points with an associated direction vector |  no  |
| [PointMatrixSet3D](PointMatrixSet3D.md) | A set of 3D points with an associated rotation matrix |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:origin3D |
| native | https://w3id.org/cetmd/entities/:origin3D |




## LinkML Source

<details>
```yaml
name: origin3D
description: Location on a 3D image (Nx3).
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 2
  dimensions:
  - alias: N
    minimum_cardinality: 1
  - alias: xyz
    exact_cardinality: 3
alias: origin3D
domain_of:
- PointSet3D
- PointVectorSet3D
- PointMatrixSet3D
range: float

```
</details>
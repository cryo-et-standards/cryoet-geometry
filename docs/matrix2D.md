

# Slot: matrix2D


_Rotation matrix associated with a point on a 2D image (Nx2x2)._





URI: [https://w3id.org/cetmd/entities/:matrix2D](https://w3id.org/cetmd/entities/:matrix2D)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointMatrixSet2D](PointMatrixSet2D.md) | A set of 2D points with an associated rotation matrix |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:matrix2D |
| native | https://w3id.org/cetmd/entities/:matrix2D |




## LinkML Source

<details>
```yaml
name: matrix2D
description: Rotation matrix associated with a point on a 2D image (Nx2x2).
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 3
  dimensions:
  - alias: N
    minimum_cardinality: 1
  - alias: xy
    exact_cardinality: 2
  - alias: xy
    exact_cardinality: 2
alias: matrix2D
domain_of:
- PointMatrixSet2D
range: float

```
</details>
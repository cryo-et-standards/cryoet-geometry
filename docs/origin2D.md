

# Slot: origin2D


_Location on a 2D image (Nx2)._





URI: [https://w3id.org/cetmd/entities/:origin2D](https://w3id.org/cetmd/entities/:origin2D)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointVectorSet2D](PointVectorSet2D.md) | A set of 2D points with an associated direction vector |  no  |
| [PointMatrixSet2D](PointMatrixSet2D.md) | A set of 2D points with an associated rotation matrix |  no  |
| [PointSet2D](PointSet2D.md) | A set of 2D point annotations |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:origin2D |
| native | https://w3id.org/cetmd/entities/:origin2D |




## LinkML Source

<details>
```yaml
name: origin2D
description: Location on a 2D image (Nx2).
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 2
  dimensions:
  - alias: N
    minimum_cardinality: 1
  - alias: xy
    exact_cardinality: 2
alias: origin2D
domain_of:
- PointSet2D
- PointVectorSet2D
- PointMatrixSet2D
range: float

```
</details>
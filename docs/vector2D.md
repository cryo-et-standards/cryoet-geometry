

# Slot: vector2D


_Orientation vector associated with a point on a 2D image (Nx2)._





URI: [https://w3id.org/cetmd/entities/:vector2D](https://w3id.org/cetmd/entities/:vector2D)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointVectorSet2D](PointVectorSet2D.md) | A set of 2D points with an associated direction vector |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:vector2D |
| native | https://w3id.org/cetmd/entities/:vector2D |




## LinkML Source

<details>
```yaml
name: vector2D
description: Orientation vector associated with a point on a 2D image (Nx2).
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 2
  dimensions:
  - alias: N
    minimum_cardinality: 1
  - alias: xy
    exact_cardinality: 2
alias: vector2D
domain_of:
- PointVectorSet2D
range: float

```
</details>
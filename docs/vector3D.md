

# Slot: vector3D


_Orientation vector associated with a point on a 3D image (Nx3)._





URI: [https://w3id.org/cetmd/entities/:vector3D](https://w3id.org/cetmd/entities/:vector3D)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointVectorSet3D](PointVectorSet3D.md) | A set of 3D points with an associated direction vector |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:vector3D |
| native | https://w3id.org/cetmd/entities/:vector3D |




## LinkML Source

<details>
```yaml
name: vector3D
description: Orientation vector associated with a point on a 3D image (Nx3).
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 2
  dimensions:
  - alias: N
    minimum_cardinality: 1
  - alias: xyz
    exact_cardinality: 3
alias: vector3D
domain_of:
- PointVectorSet3D
range: float

```
</details>
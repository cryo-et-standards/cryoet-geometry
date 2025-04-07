

# Slot: translation3D


_Offset from the origin of a point on a 3D image (Nx3)._





URI: [https://w3id.org/cetmd/entities/:translation3D](https://w3id.org/cetmd/entities/:translation3D)



<!-- no inheritance hierarchy -->








## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:translation3D |
| native | https://w3id.org/cetmd/entities/:translation3D |




## LinkML Source

<details>
```yaml
name: translation3D
description: Offset from the origin of a point on a 3D image (Nx3).
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 2
  dimensions:
  - alias: N
    minimum_cardinality: 1
  - alias: xyz
    exact_cardinality: 3
alias: translation3D
range: float

```
</details>
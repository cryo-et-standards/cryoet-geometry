

# Slot: translation2D


_Offset from the origin of a point on a 2D image (Nx2)._





URI: [https://w3id.org/cetmd/entities/:translation2D](https://w3id.org/cetmd/entities/:translation2D)



<!-- no inheritance hierarchy -->








## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:translation2D |
| native | https://w3id.org/cetmd/entities/:translation2D |




## LinkML Source

<details>
```yaml
name: translation2D
description: Offset from the origin of a point on a 2D image (Nx2).
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 2
  dimensions:
  - alias: N
    minimum_cardinality: 1
  - alias: xy
    exact_cardinality: 2
alias: translation2D
range: float

```
</details>
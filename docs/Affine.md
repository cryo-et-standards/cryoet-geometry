

# Slot: affine


_The affine matrix_





URI: [https://w3id.org/cetmd/entities/:affine](https://w3id.org/cetmd/entities/:affine)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Affine](Affine.md) | An affine transformation |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:affine |
| native | https://w3id.org/cetmd/entities/:affine |




## LinkML Source

<details>
```yaml
name: affine
description: The affine matrix
from_schema: https://w3id.org/cetmd/entities
rank: 1000
array:
  exact_number_dimensions: 2
  dimensions:
  - alias: exact_card
    exact_cardinality: 3
  - alias: exact_card
    exact_cardinality: 3
alias: affine
owner: Affine
domain_of:
- Affine
range: integer

```
</details>
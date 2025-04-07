

# Slot: annotations


_The annotations_





URI: [https://w3id.org/cetmd/entities/:annotations](https://w3id.org/cetmd/entities/:annotations)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Average](Average.md) | A particle averaging experiment |  no  |
| [Region](Region.md) | Raw data (movie stacks) and derived data (tilt series, tomograms, annotations... |  no  |







## Properties

* Range: [Annotation](Annotation.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:annotations |
| native | https://w3id.org/cetmd/entities/:annotations |




## LinkML Source

<details>
```yaml
name: annotations
description: The annotations
from_schema: https://w3id.org/cetmd/entities
rank: 1000
alias: annotations
domain_of:
- Region
- Average
range: Annotation
multivalued: true

```
</details>
# Enum: TransformationType



URI: [TransformationType](TransformationType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| identity | None | The identity transformation |
| map_axis | None | Axis permutation transformation |
| translation | None | A translation transformation |
| scale | None | A scaling transformation |
| affine | None | An affine transformation |
| sequence | None | A sequence of transformations |




## Slots

| Name | Description |
| ---  | --- |
| [transformation_type](transformation_type.md) | The type of transformation |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities






## LinkML Source

<details>
```yaml
name: TransformationType
from_schema: https://w3id.org/cetmd/entities
rank: 1000
permissible_values:
  identity:
    text: identity
    description: The identity transformation.
  map_axis:
    text: map_axis
    description: Axis permutation transformation
  translation:
    text: translation
    description: A translation transformation.
  scale:
    text: scale
    description: A scaling transformation.
  affine:
    text: affine
    description: An affine transformation
  sequence:
    text: sequence
    description: A sequence of transformations

```
</details>



# Class: Identity


_The identity transformation_





URI: [https://w3id.org/cetmd/entities/:Identity](https://w3id.org/cetmd/entities/:Identity)






```mermaid
 classDiagram
    class Identity
    click Identity href "../Identity"
      CoordinateTransformation <|-- Identity
        click CoordinateTransformation href "../CoordinateTransformation"
      
      Identity : input
        
      Identity : name
        
      Identity : output
        
      Identity : transformation_type
        
          
    
    
    Identity --> "0..1" TransformationType : transformation_type
    click TransformationType href "../TransformationType"

        
      
```





## Inheritance
* [CoordinateTransformation](CoordinateTransformation.md)
    * **Identity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [transformation_type](transformation_type.md) | 0..1 <br/> [TransformationType](TransformationType.md) | The type of transformation | direct |
| [name](name.md) | 0..1 <br/> [String](String.md) | The name of the coordinate transformation | [CoordinateTransformation](CoordinateTransformation.md) |
| [input](input.md) | 0..1 <br/> [String](String.md) | The source coordinate system name | [CoordinateTransformation](CoordinateTransformation.md) |
| [output](output.md) | 0..1 <br/> [String](String.md) | The target coordinate system name | [CoordinateTransformation](CoordinateTransformation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:Identity |
| native | https://w3id.org/cetmd/entities/:Identity |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Identity
description: The identity transformation
from_schema: https://w3id.org/cetmd/entities
is_a: CoordinateTransformation
slots:
- transformation_type
slot_usage:
  transformation_type:
    name: transformation_type
    ifabsent: identity

```
</details>

### Induced

<details>
```yaml
name: Identity
description: The identity transformation
from_schema: https://w3id.org/cetmd/entities
is_a: CoordinateTransformation
slot_usage:
  transformation_type:
    name: transformation_type
    ifabsent: identity
attributes:
  transformation_type:
    name: transformation_type
    description: The type of transformation
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    ifabsent: identity
    alias: transformation_type
    owner: Identity
    domain_of:
    - CoordinateTransformation
    - Identity
    - MapAxis
    - Translation
    - Scale
    - Affine
    - Sequence
    range: TransformationType
  name:
    name: name
    description: The name of the coordinate transformation
    from_schema: https://w3id.org/cetmd/coord_transforms
    alias: name
    owner: Identity
    domain_of:
    - Average
    - Dataset
    - CoordinateSystem
    - CoordinateTransformation
    range: string
  input:
    name: input
    description: The source coordinate system name
    from_schema: https://w3id.org/cetmd/coord_transforms
    rank: 1000
    alias: input
    owner: Identity
    domain_of:
    - CoordinateTransformation
    - ProjectionAlignment
    range: string
  output:
    name: output
    description: The target coordinate system name
    from_schema: https://w3id.org/cetmd/coord_transforms
    rank: 1000
    alias: output
    owner: Identity
    domain_of:
    - CoordinateTransformation
    - ProjectionAlignment
    range: string

```
</details>
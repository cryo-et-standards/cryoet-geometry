

# Class: ProjectionAlignment


_The tomographic alignment for a single projection._





URI: [https://w3id.org/cetmd/entities/:ProjectionAlignment](https://w3id.org/cetmd/entities/:ProjectionAlignment)






```mermaid
 classDiagram
    class ProjectionAlignment
    click ProjectionAlignment href "../ProjectionAlignment"
      Sequence <|-- ProjectionAlignment
        click Sequence href "../Sequence"
      
      ProjectionAlignment : input
        
      ProjectionAlignment : name
        
      ProjectionAlignment : output
        
      ProjectionAlignment : sequence
        
          
    
    
    ProjectionAlignment --> "*" CoordinateTransformation : sequence
    click CoordinateTransformation href "../CoordinateTransformation"

        
      ProjectionAlignment : transformation_type
        
          
    
    
    ProjectionAlignment --> "0..1" TransformationType : transformation_type
    click TransformationType href "../TransformationType"

        
      
```





## Inheritance
* [CoordinateTransformation](CoordinateTransformation.md)
    * [Sequence](Sequence.md)
        * **ProjectionAlignment**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [input](input.md) | 0..1 <br/> [String](String.md) | The source coordinate system name | direct |
| [output](output.md) | 0..1 <br/> [String](String.md) | The target coordinate system name | direct |
| [sequence](sequence.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md)&nbsp;or&nbsp;<br />[Affine](Affine.md)&nbsp;or&nbsp;<br />[Translation](Translation.md) | The sequence of transformations | direct |
| [transformation_type](transformation_type.md) | 0..1 <br/> [TransformationType](TransformationType.md) | The type of transformation | [CoordinateTransformation](CoordinateTransformation.md), [Sequence](Sequence.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | The name of the coordinate transformation | [CoordinateTransformation](CoordinateTransformation.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Alignment](Alignment.md) | [projection_alignments](projection_alignments.md) | range | [ProjectionAlignment](ProjectionAlignment.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:ProjectionAlignment |
| native | https://w3id.org/cetmd/entities/:ProjectionAlignment |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProjectionAlignment
description: The tomographic alignment for a single projection.
from_schema: https://w3id.org/cetmd/entities
is_a: Sequence
attributes:
  input:
    name: input
    description: The source coordinate system name
    from_schema: https://w3id.org/cetmd/alignment/
    domain_of:
    - CoordinateTransformation
    - ProjectionAlignment
    range: string
  output:
    name: output
    description: The target coordinate system name
    from_schema: https://w3id.org/cetmd/alignment/
    domain_of:
    - CoordinateTransformation
    - ProjectionAlignment
    range: string
  sequence:
    name: sequence
    description: The sequence of transformations
    from_schema: https://w3id.org/cetmd/alignment/
    domain_of:
    - Sequence
    - ProjectionAlignment
    range: CoordinateTransformation
    multivalued: true
    maximum_cardinality: 2
    any_of:
    - range: Affine
    - range: Translation

```
</details>

### Induced

<details>
```yaml
name: ProjectionAlignment
description: The tomographic alignment for a single projection.
from_schema: https://w3id.org/cetmd/entities
is_a: Sequence
attributes:
  input:
    name: input
    description: The source coordinate system name
    from_schema: https://w3id.org/cetmd/alignment/
    alias: input
    owner: ProjectionAlignment
    domain_of:
    - CoordinateTransformation
    - ProjectionAlignment
    range: string
  output:
    name: output
    description: The target coordinate system name
    from_schema: https://w3id.org/cetmd/alignment/
    alias: output
    owner: ProjectionAlignment
    domain_of:
    - CoordinateTransformation
    - ProjectionAlignment
    range: string
  sequence:
    name: sequence
    description: The sequence of transformations
    from_schema: https://w3id.org/cetmd/alignment/
    alias: sequence
    owner: ProjectionAlignment
    domain_of:
    - Sequence
    - ProjectionAlignment
    range: CoordinateTransformation
    multivalued: true
    maximum_cardinality: 2
    any_of:
    - range: Affine
    - range: Translation
  transformation_type:
    name: transformation_type
    description: The type of transformation
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    ifabsent: sequence
    alias: transformation_type
    owner: ProjectionAlignment
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
    owner: ProjectionAlignment
    domain_of:
    - Average
    - Dataset
    - CoordinateSystem
    - CoordinateTransformation
    range: string

```
</details>


# Class: PointSet3D


_A set of 3D point annotations._





URI: [https://w3id.org/cetmd/entities/:PointSet3D](https://w3id.org/cetmd/entities/:PointSet3D)






```mermaid
 classDiagram
    class PointSet3D
    click PointSet3D href "../PointSet3D"
      CoordMetaMixin <|-- PointSet3D
        click CoordMetaMixin href "../CoordMetaMixin"
      Annotation <|-- PointSet3D
        click Annotation href "../Annotation"
      
      PointSet3D : coordinate_systems
        
          
    
    
    PointSet3D --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      PointSet3D : coordinate_transformations
        
          
    
    
    PointSet3D --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      PointSet3D : origin3D
        
      PointSet3D : path
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **PointSet3D** [ [CoordMetaMixin](CoordMetaMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [origin3D](origin3D.md) | 0..1 <br/> [Float](Float.md) | Location on a 3D image (Nx3) | direct |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | [Annotation](Annotation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:PointSet3D |
| native | https://w3id.org/cetmd/entities/:PointSet3D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PointSet3D
description: A set of 3D point annotations.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin
slots:
- origin3D

```
</details>

### Induced

<details>
```yaml
name: PointSet3D
description: A set of 3D point annotations.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin
attributes:
  origin3D:
    name: origin3D
    description: Location on a 3D image (Nx3).
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    array:
      exact_number_dimensions: 2
      dimensions:
      - alias: N
        minimum_cardinality: 1
      - alias: xyz
        exact_cardinality: 3
    alias: origin3D
    owner: PointSet3D
    domain_of:
    - PointSet3D
    - PointVectorSet3D
    - PointMatrixSet3D
    range: float
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: PointSet3D
    domain_of:
    - Image2D
    - Image3D
    - CoordMetaMixin
    range: CoordinateSystem
    multivalued: true
  coordinate_transformations:
    name: coordinate_transformations
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_transformations
    owner: PointSet3D
    domain_of:
    - Image2D
    - Image3D
    - CoordMetaMixin
    range: CoordinateTransformation
    multivalued: true
  path:
    name: path
    description: Path to a file.
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: path
    owner: PointSet3D
    domain_of:
    - GainFile
    - DefectFile
    - MovieFrame
    - MovieStack
    - ProjectionImage
    - TiltSeries
    - Tomogram
    - ParticleMap
    - Annotation
    range: string

```
</details>
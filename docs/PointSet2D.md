

# Class: PointSet2D


_A set of 2D point annotations._





URI: [https://w3id.org/cetmd/entities/:PointSet2D](https://w3id.org/cetmd/entities/:PointSet2D)






```mermaid
 classDiagram
    class PointSet2D
    click PointSet2D href "../PointSet2D"
      CoordMetaMixin <|-- PointSet2D
        click CoordMetaMixin href "../CoordMetaMixin"
      Annotation <|-- PointSet2D
        click Annotation href "../Annotation"
      
      PointSet2D : coordinate_systems
        
          
    
    
    PointSet2D --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      PointSet2D : coordinate_transformations
        
          
    
    
    PointSet2D --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      PointSet2D : origin2D
        
      PointSet2D : path
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **PointSet2D** [ [CoordMetaMixin](CoordMetaMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [origin2D](origin2D.md) | 0..1 <br/> [Float](Float.md) | Location on a 2D image (Nx2) | direct |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | [Annotation](Annotation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:PointSet2D |
| native | https://w3id.org/cetmd/entities/:PointSet2D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PointSet2D
description: A set of 2D point annotations.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin
slots:
- origin2D

```
</details>

### Induced

<details>
```yaml
name: PointSet2D
description: A set of 2D point annotations.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin
attributes:
  origin2D:
    name: origin2D
    description: Location on a 2D image (Nx2).
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    array:
      exact_number_dimensions: 2
      dimensions:
      - alias: N
        minimum_cardinality: 1
      - alias: xy
        exact_cardinality: 2
    alias: origin2D
    owner: PointSet2D
    domain_of:
    - PointSet2D
    - PointVectorSet2D
    - PointMatrixSet2D
    range: float
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: PointSet2D
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
    owner: PointSet2D
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
    owner: PointSet2D
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


# Class: PointVectorSet2D


_A set of 2D points with an associated direction vector._





URI: [https://w3id.org/cetmd/entities/:PointVectorSet2D](https://w3id.org/cetmd/entities/:PointVectorSet2D)






```mermaid
 classDiagram
    class PointVectorSet2D
    click PointVectorSet2D href "../PointVectorSet2D"
      CoordMetaMixin <|-- PointVectorSet2D
        click CoordMetaMixin href "../CoordMetaMixin"
      Annotation <|-- PointVectorSet2D
        click Annotation href "../Annotation"
      
      PointVectorSet2D : coordinate_systems
        
          
    
    
    PointVectorSet2D --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      PointVectorSet2D : coordinate_transformations
        
          
    
    
    PointVectorSet2D --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      PointVectorSet2D : origin2D
        
      PointVectorSet2D : path
        
      PointVectorSet2D : vector2D
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **PointVectorSet2D** [ [CoordMetaMixin](CoordMetaMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [origin2D](origin2D.md) | 0..1 <br/> [Float](Float.md) | Location on a 2D image (Nx2) | direct |
| [vector2D](vector2D.md) | 0..1 <br/> [Float](Float.md) | Orientation vector associated with a point on a 2D image (Nx2) | direct |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | [Annotation](Annotation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:PointVectorSet2D |
| native | https://w3id.org/cetmd/entities/:PointVectorSet2D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PointVectorSet2D
description: A set of 2D points with an associated direction vector.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin
slots:
- origin2D
- vector2D

```
</details>

### Induced

<details>
```yaml
name: PointVectorSet2D
description: A set of 2D points with an associated direction vector.
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
    owner: PointVectorSet2D
    domain_of:
    - PointSet2D
    - PointVectorSet2D
    - PointMatrixSet2D
    range: float
  vector2D:
    name: vector2D
    description: Orientation vector associated with a point on a 2D image (Nx2).
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    array:
      exact_number_dimensions: 2
      dimensions:
      - alias: N
        minimum_cardinality: 1
      - alias: xy
        exact_cardinality: 2
    alias: vector2D
    owner: PointVectorSet2D
    domain_of:
    - PointVectorSet2D
    range: float
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: PointVectorSet2D
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
    owner: PointVectorSet2D
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
    owner: PointVectorSet2D
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
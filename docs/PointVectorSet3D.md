

# Class: PointVectorSet3D


_A set of 3D points with an associated direction vector._





URI: [https://w3id.org/cetmd/entities/:PointVectorSet3D](https://w3id.org/cetmd/entities/:PointVectorSet3D)






```mermaid
 classDiagram
    class PointVectorSet3D
    click PointVectorSet3D href "../PointVectorSet3D"
      CoordMetaMixin <|-- PointVectorSet3D
        click CoordMetaMixin href "../CoordMetaMixin"
      Annotation <|-- PointVectorSet3D
        click Annotation href "../Annotation"
      
      PointVectorSet3D : coordinate_systems
        
          
    
    
    PointVectorSet3D --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      PointVectorSet3D : coordinate_transformations
        
          
    
    
    PointVectorSet3D --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      PointVectorSet3D : origin3D
        
      PointVectorSet3D : path
        
      PointVectorSet3D : vector3D
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **PointVectorSet3D** [ [CoordMetaMixin](CoordMetaMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [origin3D](origin3D.md) | 0..1 <br/> [Float](Float.md) | Location on a 3D image (Nx3) | direct |
| [vector3D](vector3D.md) | 0..1 <br/> [Float](Float.md) | Orientation vector associated with a point on a 3D image (Nx3) | direct |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | [Annotation](Annotation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:PointVectorSet3D |
| native | https://w3id.org/cetmd/entities/:PointVectorSet3D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PointVectorSet3D
description: A set of 3D points with an associated direction vector.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin
slots:
- origin3D
- vector3D

```
</details>

### Induced

<details>
```yaml
name: PointVectorSet3D
description: A set of 3D points with an associated direction vector.
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
    owner: PointVectorSet3D
    domain_of:
    - PointSet3D
    - PointVectorSet3D
    - PointMatrixSet3D
    range: float
  vector3D:
    name: vector3D
    description: Orientation vector associated with a point on a 3D image (Nx3).
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    array:
      exact_number_dimensions: 2
      dimensions:
      - alias: N
        minimum_cardinality: 1
      - alias: xyz
        exact_cardinality: 3
    alias: vector3D
    owner: PointVectorSet3D
    domain_of:
    - PointVectorSet3D
    range: float
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: PointVectorSet3D
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
    owner: PointVectorSet3D
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
    owner: PointVectorSet3D
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
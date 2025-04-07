

# Class: PointMatrixSet3D


_A set of 3D points with an associated rotation matrix._





URI: [https://w3id.org/cetmd/entities/:PointMatrixSet3D](https://w3id.org/cetmd/entities/:PointMatrixSet3D)






```mermaid
 classDiagram
    class PointMatrixSet3D
    click PointMatrixSet3D href "../PointMatrixSet3D"
      CoordMetaMixin <|-- PointMatrixSet3D
        click CoordMetaMixin href "../CoordMetaMixin"
      Annotation <|-- PointMatrixSet3D
        click Annotation href "../Annotation"
      
      PointMatrixSet3D : coordinate_systems
        
          
    
    
    PointMatrixSet3D --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      PointMatrixSet3D : coordinate_transformations
        
          
    
    
    PointMatrixSet3D --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      PointMatrixSet3D : matrix3D
        
      PointMatrixSet3D : origin3D
        
      PointMatrixSet3D : path
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **PointMatrixSet3D** [ [CoordMetaMixin](CoordMetaMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [origin3D](origin3D.md) | 0..1 <br/> [Float](Float.md) | Location on a 3D image (Nx3) | direct |
| [matrix3D](matrix3D.md) | 0..1 <br/> [Float](Float.md) | Rotation matrix associated with a point on a 3D image (Nx3x3) | direct |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | [Annotation](Annotation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:PointMatrixSet3D |
| native | https://w3id.org/cetmd/entities/:PointMatrixSet3D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PointMatrixSet3D
description: A set of 3D points with an associated rotation matrix.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin
slots:
- origin3D
- matrix3D

```
</details>

### Induced

<details>
```yaml
name: PointMatrixSet3D
description: A set of 3D points with an associated rotation matrix.
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
    owner: PointMatrixSet3D
    domain_of:
    - PointSet3D
    - PointVectorSet3D
    - PointMatrixSet3D
    range: float
  matrix3D:
    name: matrix3D
    description: Rotation matrix associated with a point on a 3D image (Nx3x3).
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    array:
      exact_number_dimensions: 3
      dimensions:
      - alias: N
        minimum_cardinality: 1
      - alias: xyz
        exact_cardinality: 3
      - alias: xyz
        exact_cardinality: 3
    alias: matrix3D
    owner: PointMatrixSet3D
    domain_of:
    - PointMatrixSet3D
    range: float
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: PointMatrixSet3D
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
    owner: PointMatrixSet3D
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
    owner: PointMatrixSet3D
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
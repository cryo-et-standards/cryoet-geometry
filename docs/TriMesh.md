

# Class: TriMesh


_A mesh annotation._





URI: [https://w3id.org/cetmd/entities/:TriMesh](https://w3id.org/cetmd/entities/:TriMesh)






```mermaid
 classDiagram
    class TriMesh
    click TriMesh href "../TriMesh"
      CoordMetaMixin <|-- TriMesh
        click CoordMetaMixin href "../CoordMetaMixin"
      Annotation <|-- TriMesh
        click Annotation href "../Annotation"
      
      TriMesh : coordinate_systems
        
          
    
    
    TriMesh --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      TriMesh : coordinate_transformations
        
          
    
    
    TriMesh --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      TriMesh : path
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **TriMesh** [ [CoordMetaMixin](CoordMetaMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [CoordMetaMixin](CoordMetaMixin.md) |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | [Annotation](Annotation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:TriMesh |
| native | https://w3id.org/cetmd/entities/:TriMesh |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TriMesh
description: A mesh annotation.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin

```
</details>

### Induced

<details>
```yaml
name: TriMesh
description: A mesh annotation.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- CoordMetaMixin
attributes:
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: TriMesh
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
    owner: TriMesh
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
    owner: TriMesh
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
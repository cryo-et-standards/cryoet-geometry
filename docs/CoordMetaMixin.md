

# Class: CoordMetaMixin


_Coordinate system mixins for annotations._





URI: [https://w3id.org/cetmd/entities/:CoordMetaMixin](https://w3id.org/cetmd/entities/:CoordMetaMixin)






```mermaid
 classDiagram
    class CoordMetaMixin
    click CoordMetaMixin href "../CoordMetaMixin"
      CoordMetaMixin <|-- PointSet2D
        click PointSet2D href "../PointSet2D"
      CoordMetaMixin <|-- PointSet3D
        click PointSet3D href "../PointSet3D"
      CoordMetaMixin <|-- PointVectorSet2D
        click PointVectorSet2D href "../PointVectorSet2D"
      CoordMetaMixin <|-- PointVectorSet3D
        click PointVectorSet3D href "../PointVectorSet3D"
      CoordMetaMixin <|-- PointMatrixSet2D
        click PointMatrixSet2D href "../PointMatrixSet2D"
      CoordMetaMixin <|-- PointMatrixSet3D
        click PointMatrixSet3D href "../PointMatrixSet3D"
      CoordMetaMixin <|-- TriMesh
        click TriMesh href "../TriMesh"
      
      CoordMetaMixin : coordinate_systems
        
          
    
    
    CoordMetaMixin --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      CoordMetaMixin : coordinate_transformations
        
          
    
    
    CoordMetaMixin --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | direct |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:CoordMetaMixin |
| native | https://w3id.org/cetmd/entities/:CoordMetaMixin |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CoordMetaMixin
description: Coordinate system mixins for annotations.
from_schema: https://w3id.org/cetmd/entities
slots:
- coordinate_systems
- coordinate_transformations

```
</details>

### Induced

<details>
```yaml
name: CoordMetaMixin
description: Coordinate system mixins for annotations.
from_schema: https://w3id.org/cetmd/entities
attributes:
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: CoordMetaMixin
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
    owner: CoordMetaMixin
    domain_of:
    - Image2D
    - Image3D
    - CoordMetaMixin
    range: CoordinateTransformation
    multivalued: true

```
</details>
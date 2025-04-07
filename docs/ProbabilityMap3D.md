

# Class: ProbabilityMap3D


_An annotation volume with real-valued labels._





URI: [https://w3id.org/cetmd/entities/:ProbabilityMap3D](https://w3id.org/cetmd/entities/:ProbabilityMap3D)






```mermaid
 classDiagram
    class ProbabilityMap3D
    click ProbabilityMap3D href "../ProbabilityMap3D"
      Image3D <|-- ProbabilityMap3D
        click Image3D href "../Image3D"
      Annotation <|-- ProbabilityMap3D
        click Annotation href "../Annotation"
      
      ProbabilityMap3D : coordinate_systems
        
          
    
    
    ProbabilityMap3D --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      ProbabilityMap3D : coordinate_transformations
        
          
    
    
    ProbabilityMap3D --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      ProbabilityMap3D : depth
        
      ProbabilityMap3D : height
        
      ProbabilityMap3D : path
        
      ProbabilityMap3D : width
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **ProbabilityMap3D** [ [Image3D](Image3D.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [width](width.md) | 0..1 <br/> [Integer](Integer.md) | The width of the image (x-axis) in pixels | [Image3D](Image3D.md) |
| [height](height.md) | 0..1 <br/> [Integer](Integer.md) | The height of the image (y-axis) in pixels | [Image3D](Image3D.md) |
| [depth](depth.md) | 0..1 <br/> [Integer](Integer.md) | The depth of the image (z-axis) in pixels | [Image3D](Image3D.md) |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [Image3D](Image3D.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [Image3D](Image3D.md) |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | [Annotation](Annotation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:ProbabilityMap3D |
| native | https://w3id.org/cetmd/entities/:ProbabilityMap3D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProbabilityMap3D
description: An annotation volume with real-valued labels.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- Image3D

```
</details>

### Induced

<details>
```yaml
name: ProbabilityMap3D
description: An annotation volume with real-valued labels.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- Image3D
attributes:
  width:
    name: width
    description: The width of the image (x-axis) in pixels
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: width
    owner: ProbabilityMap3D
    domain_of:
    - Image2D
    - Image3D
    range: integer
  height:
    name: height
    description: The height of the image (y-axis) in pixels
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: height
    owner: ProbabilityMap3D
    domain_of:
    - Image2D
    - Image3D
    range: integer
  depth:
    name: depth
    description: The depth of the image (z-axis) in pixels
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: depth
    owner: ProbabilityMap3D
    domain_of:
    - Image3D
    range: integer
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: ProbabilityMap3D
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
    owner: ProbabilityMap3D
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
    owner: ProbabilityMap3D
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
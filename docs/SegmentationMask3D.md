

# Class: SegmentationMask3D


_An annotation volume with categorical labels._





URI: [https://w3id.org/cetmd/entities/:SegmentationMask3D](https://w3id.org/cetmd/entities/:SegmentationMask3D)






```mermaid
 classDiagram
    class SegmentationMask3D
    click SegmentationMask3D href "../SegmentationMask3D"
      Image3D <|-- SegmentationMask3D
        click Image3D href "../Image3D"
      Annotation <|-- SegmentationMask3D
        click Annotation href "../Annotation"
      
      SegmentationMask3D : coordinate_systems
        
          
    
    
    SegmentationMask3D --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      SegmentationMask3D : coordinate_transformations
        
          
    
    
    SegmentationMask3D --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      SegmentationMask3D : depth
        
      SegmentationMask3D : height
        
      SegmentationMask3D : path
        
      SegmentationMask3D : width
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **SegmentationMask3D** [ [Image3D](Image3D.md)]



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
| self | https://w3id.org/cetmd/entities/:SegmentationMask3D |
| native | https://w3id.org/cetmd/entities/:SegmentationMask3D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SegmentationMask3D
description: An annotation volume with categorical labels.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- Image3D

```
</details>

### Induced

<details>
```yaml
name: SegmentationMask3D
description: An annotation volume with categorical labels.
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
    owner: SegmentationMask3D
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
    owner: SegmentationMask3D
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
    owner: SegmentationMask3D
    domain_of:
    - Image3D
    range: integer
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: SegmentationMask3D
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
    owner: SegmentationMask3D
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
    owner: SegmentationMask3D
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
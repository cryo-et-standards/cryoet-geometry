

# Class: SegmentationMask2D


_An annotation image with categorical labels._





URI: [https://w3id.org/cetmd/entities/:SegmentationMask2D](https://w3id.org/cetmd/entities/:SegmentationMask2D)






```mermaid
 classDiagram
    class SegmentationMask2D
    click SegmentationMask2D href "../SegmentationMask2D"
      Image2D <|-- SegmentationMask2D
        click Image2D href "../Image2D"
      Annotation <|-- SegmentationMask2D
        click Annotation href "../Annotation"
      
      SegmentationMask2D : coordinate_systems
        
          
    
    
    SegmentationMask2D --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      SegmentationMask2D : coordinate_transformations
        
          
    
    
    SegmentationMask2D --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      SegmentationMask2D : height
        
      SegmentationMask2D : path
        
      SegmentationMask2D : width
        
      
```





## Inheritance
* [Annotation](Annotation.md)
    * **SegmentationMask2D** [ [Image2D](Image2D.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [width](width.md) | 0..1 <br/> [Integer](Integer.md) | The width of the image (x-axis) in pixels | [Image2D](Image2D.md) |
| [height](height.md) | 0..1 <br/> [Integer](Integer.md) | The height of the image (y-axis) in pixels | [Image2D](Image2D.md) |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [Image2D](Image2D.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [Image2D](Image2D.md) |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | [Annotation](Annotation.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:SegmentationMask2D |
| native | https://w3id.org/cetmd/entities/:SegmentationMask2D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SegmentationMask2D
description: An annotation image with categorical labels.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- Image2D

```
</details>

### Induced

<details>
```yaml
name: SegmentationMask2D
description: An annotation image with categorical labels.
from_schema: https://w3id.org/cetmd/entities
is_a: Annotation
mixins:
- Image2D
attributes:
  width:
    name: width
    description: The width of the image (x-axis) in pixels
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: width
    owner: SegmentationMask2D
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
    owner: SegmentationMask2D
    domain_of:
    - Image2D
    - Image3D
    range: integer
  coordinate_systems:
    name: coordinate_systems
    description: Named coordinate systems for this entity
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: coordinate_systems
    owner: SegmentationMask2D
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
    owner: SegmentationMask2D
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
    owner: SegmentationMask2D
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
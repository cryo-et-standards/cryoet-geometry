

# Class: GainFile


_A gain reference file._





URI: [https://w3id.org/cetmd/entities/:GainFile](https://w3id.org/cetmd/entities/:GainFile)






```mermaid
 classDiagram
    class GainFile
    click GainFile href "../GainFile"
      Image2D <|-- GainFile
        click Image2D href "../Image2D"
      
      GainFile : coordinate_systems
        
          
    
    
    GainFile --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      GainFile : coordinate_transformations
        
          
    
    
    GainFile --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      GainFile : height
        
      GainFile : path
        
      GainFile : width
        
      
```





## Inheritance
* [Image2D](Image2D.md)
    * **GainFile**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [path](path.md) | 0..1 <br/> [String](String.md) | Path to a file | direct |
| [width](width.md) | 0..1 <br/> [Integer](Integer.md) | The width of the image (x-axis) in pixels | [Image2D](Image2D.md) |
| [height](height.md) | 0..1 <br/> [Integer](Integer.md) | The height of the image (y-axis) in pixels | [Image2D](Image2D.md) |
| [coordinate_systems](coordinate_systems.md) | * <br/> [CoordinateSystem](CoordinateSystem.md) | Named coordinate systems for this entity | [Image2D](Image2D.md) |
| [coordinate_transformations](coordinate_transformations.md) | * <br/> [CoordinateTransformation](CoordinateTransformation.md) | Named coordinate systems for this entity | [Image2D](Image2D.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MovieStackCollection](MovieStackCollection.md) | [gain_file](gain_file.md) | range | [GainFile](GainFile.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:GainFile |
| native | https://w3id.org/cetmd/entities/:GainFile |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GainFile
description: A gain reference file.
from_schema: https://w3id.org/cetmd/entities
is_a: Image2D
slots:
- path

```
</details>

### Induced

<details>
```yaml
name: GainFile
description: A gain reference file.
from_schema: https://w3id.org/cetmd/entities
is_a: Image2D
attributes:
  path:
    name: path
    description: Path to a file.
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: path
    owner: GainFile
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
  width:
    name: width
    description: The width of the image (x-axis) in pixels
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: width
    owner: GainFile
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
    owner: GainFile
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
    owner: GainFile
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
    owner: GainFile
    domain_of:
    - Image2D
    - Image3D
    - CoordMetaMixin
    range: CoordinateTransformation
    multivalued: true

```
</details>
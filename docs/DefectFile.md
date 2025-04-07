

# Class: DefectFile


_A detector defect file._





URI: [https://w3id.org/cetmd/entities/:DefectFile](https://w3id.org/cetmd/entities/:DefectFile)






```mermaid
 classDiagram
    class DefectFile
    click DefectFile href "../DefectFile"
      Image2D <|-- DefectFile
        click Image2D href "../Image2D"
      
      DefectFile : coordinate_systems
        
          
    
    
    DefectFile --> "*" CoordinateSystem : coordinate_systems
    click CoordinateSystem href "../CoordinateSystem"

        
      DefectFile : coordinate_transformations
        
          
    
    
    DefectFile --> "*" CoordinateTransformation : coordinate_transformations
    click CoordinateTransformation href "../CoordinateTransformation"

        
      DefectFile : height
        
      DefectFile : path
        
      DefectFile : width
        
      
```





## Inheritance
* [Image2D](Image2D.md)
    * **DefectFile**



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
| [MovieStackCollection](MovieStackCollection.md) | [defect_file](defect_file.md) | range | [DefectFile](DefectFile.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:DefectFile |
| native | https://w3id.org/cetmd/entities/:DefectFile |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DefectFile
description: A detector defect file.
from_schema: https://w3id.org/cetmd/entities
is_a: Image2D
slots:
- path

```
</details>

### Induced

<details>
```yaml
name: DefectFile
description: A detector defect file.
from_schema: https://w3id.org/cetmd/entities
is_a: Image2D
attributes:
  path:
    name: path
    description: Path to a file.
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: path
    owner: DefectFile
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
    owner: DefectFile
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
    owner: DefectFile
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
    owner: DefectFile
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
    owner: DefectFile
    domain_of:
    - Image2D
    - Image3D
    - CoordMetaMixin
    range: CoordinateTransformation
    multivalued: true

```
</details>
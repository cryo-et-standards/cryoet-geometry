

# Class: ImageStack2D


_A stack of 2D images._





URI: [https://w3id.org/cetmd/entities/:ImageStack2D](https://w3id.org/cetmd/entities/:ImageStack2D)






```mermaid
 classDiagram
    class ImageStack2D
    click ImageStack2D href "../ImageStack2D"
      ImageStack2D : images2D
        
          
    
    
    ImageStack2D --> "*" Image2D : images2D
    click Image2D href "../Image2D"

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [images2D](images2D.md) | * <br/> [Image2D](Image2D.md) | The images in the stack | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/cetmd/entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/cetmd/entities/:ImageStack2D |
| native | https://w3id.org/cetmd/entities/:ImageStack2D |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ImageStack2D
description: A stack of 2D images.
from_schema: https://w3id.org/cetmd/entities
slots:
- images2D

```
</details>

### Induced

<details>
```yaml
name: ImageStack2D
description: A stack of 2D images.
from_schema: https://w3id.org/cetmd/entities
attributes:
  images2D:
    name: images2D
    description: The images in the stack
    from_schema: https://w3id.org/cetmd/entities
    rank: 1000
    alias: images2D
    owner: ImageStack2D
    domain_of:
    - ImageStack2D
    range: Image2D
    multivalued: true

```
</details>
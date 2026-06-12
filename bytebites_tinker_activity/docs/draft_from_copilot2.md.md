# Menu Items UML

Mermaid class diagram for the ByteBites menu item classes.

```mermaid
classDiagram
    class MenuItem {
        +string name
        +decimal price
        +string category
        +float popularityRating
        +decimal getPrice()
        +void updatePopularity(float delta)
    }

    class Drinks {
        +enum Size { SMALL, MEDIUM, LARGE }
        +bool isCarbonated
        +bool containsAlcohol
        +decimal getSizePriceModifier()
    }

    class Desserts {
        +int calories
        +bool isGlutenFree
        +bool isSugarFree
    }

    class Sides {
        +string portionSize
        +bool isShareable
    }

    class Main {
        +string spiceLevel
        +bool isVegetarian
        +bool isVegan
    }

    MenuItem <|-- Drinks
    MenuItem <|-- Desserts
    MenuItem <|-- Sides
    MenuItem <|-- Main
```

# Revised ByteBites Specification

## Purpose
Provide backend domain model and behavior for the ByteBites app: customers, menu items, collections, and transactions.

## Candidate Classes
- `MenuItem` (base)
  - Attributes: `name: string`, `price: decimal`, `category: string`, `popularityRating: float`
  - Methods: `getPrice(): decimal`, `updatePopularity(delta: float): void`

- `Drinks` (extends `MenuItem`)
  - Attributes: `size: enum {SMALL, MEDIUM, LARGE}`, `isCarbonated: bool`, `containsAlcohol: bool`
  - Methods: `getSizePriceModifier(): decimal`

- `Desserts` (extends `MenuItem`)
  - Attributes: `calories: int`, `isGlutenFree: bool`, `isSugarFree: bool`

- `Sides` (extends `MenuItem`)
  - Attributes: `portionSize: string`, `isShareable: bool`

- `Main` (extends `MenuItem`)
  - Attributes: `spiceLevel: string`, `isVegetarian: bool`, `isVegan: bool`

- `ItemCollection` / `Menu`
  - Attributes: `items: List<MenuItem>`
  - Methods: `add(item: MenuItem): void`, `remove(itemId): void`, `filterByCategory(category: string): List<MenuItem>`, `findByName(name: string): List<MenuItem>`

- `Transaction`
  - Attributes: `id: string`, `items: List<MenuItem>`, `total: decimal`, `timestamp: ISO8601`
  - Methods: `computeTotal(): decimal`, `addItem(item: MenuItem): void`, `removeItem(itemId): void`

- `Customer`
  - Attributes: `id: string`, `name: string`, `purchaseHistory: List<Transaction>`
  - Methods: `verify(): bool`, `addTransaction(tx: Transaction): void`

## Relationships
- `MenuItem` is the base class for `Drinks`, `Desserts`, `Sides`, and `Main`.
- `ItemCollection` contains many `MenuItem` instances.
- `Transaction` aggregates multiple `MenuItem` instances and computes a `total`.
- `Customer` has 0..* `Transaction` entries (purchase history).

## Behavior & Notes
- `computeTotal()` sums `getPrice()` for included items; consider size/option modifiers.
- `verify()` should confirm customer identity (stubbed for now; can be a simple existence check).
- Popularity may be updated when transactions are completed (`updatePopularity`).
- `ItemCollection.filterByCategory()` supports category-based browsing (e.g., "Drinks").

## Persistence & API-ready Considerations
- Model identifiers: use stable `id: string` for `Customer` and `Transaction`.
- Store `price` as integer cents or `decimal` with controlled precision.
- Prepare DTOs for API responses with minimal sensitive data on `Customer`.

## Deliverables
- Domain model classes as above.
- `docs/menu_items_uml.md` contains the Mermaid UML diagram.
- Optional: generate sample JSON fixtures and unit tests for `Transaction.computeTotal()` and `ItemCollection.filterByCategory()`.

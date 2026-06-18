"""ByteBites domain models — brief summary.

Four `MenuItem` subclasses used by the backend:
- Drinks: beverages with `size`, `isCarbonated`, `containsAlcohol`, and a size-based price modifier.
- Desserts: sweet items with `calories`, `isGlutenFree`, and `isSugarFree` flags.
- Sides: side dishes with `portionSize` and `isShareable` attributes.
- Main: main-course items with `spiceLevel`, `isVegetarian`, and `isVegan` flags.

See `docs/revised_bytebites_spec.md` and `docs/menu_items_uml.md` for full details.
"""


from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
import uuid


@dataclass
class MenuItem:
	name: str
	price: float
	category: str
	popularity_rating: float = 0.0

	def get_price(self) -> float:
		return self.price

	def update_popularity(self, delta: float) -> None:
		self.popularity_rating += delta


@dataclass
class Drinks(MenuItem):
	size: str = "MEDIUM"  # SMALL, MEDIUM, LARGE
	is_carbonated: bool = False
	contains_alcohol: bool = False

	def get_size_price_modifier(self) -> float:
		return 0.0


@dataclass
class Desserts(MenuItem):
	calories: Optional[int] = None
	is_gluten_free: bool = False
	is_sugar_free: bool = False


@dataclass
class Sides(MenuItem):
	portion_size: Optional[str] = None
	is_shareable: bool = False


@dataclass
class Main(MenuItem):
	spice_level: Optional[str] = None
	is_vegetarian: bool = False
	is_vegan: bool = False


@dataclass
class ItemCollection:
	items: List[MenuItem] = field(default_factory=list)

	def add(self, item: MenuItem) -> None:
		self.items.append(item)

	def remove(self, item: MenuItem) -> None:
		if item in self.items:
			self.items.remove(item)

	def filter_by_category(self, category: str) -> List[MenuItem]:
		return [i for i in self.items if i.category == category]

	def find_by_name(self, name: str) -> List[MenuItem]:
		return [i for i in self.items if i.name == name]


@dataclass
class Transaction:
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	items: List[MenuItem] = field(default_factory=list)
	total: float = 0.0
	timestamp: datetime = field(default_factory=datetime.utcnow)

	def compute_total(self) -> float:
		self.total = sum(i.get_price() for i in self.items)
		return self.total

	def add_item(self, item: MenuItem) -> None:
		self.items.append(item)
		self.compute_total()

	def remove_item(self, item: MenuItem) -> None:
		if item in self.items:
			self.items.remove(item)
			self.compute_total()


@dataclass
class Customer:
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	name: str = ""
	purchase_history: List[Transaction] = field(default_factory=list)

	def verify(self) -> bool:
		return bool(self.name)

	def add_transaction(self, tx: Transaction) -> None:
		self.purchase_history.append(tx)



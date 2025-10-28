from dataclasses import dataclass

@dataclass
class Component:
    id: str
    name: str
    description: str
    stock: int

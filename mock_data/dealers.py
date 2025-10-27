
from dataclasses import dataclass

@dataclass
class Dealer:
    id: str
    name: str
    region: str

dealers = [
    Dealer(id="dealer_1", name="The Shade Store", region="USA"),
    Dealer(id="dealer_2", name="Blinds To Go", region="Canada"),
    Dealer(id="dealer_3", name="Hillarys", region="UK"),
]

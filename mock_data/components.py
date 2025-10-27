
from dataclasses import dataclass

@dataclass
class Component:
    id: str
    name: str
    plant_id: str

components = [
    Component(id="fabric_1", name="Duette Fabric", plant_id="plant_1"),
    Component(id="headrail_1", name="Duette Headrail", plant_id="plant_2"),
    Component(id="bottom_rail_1", name="Duette Bottom Rail", plant_id="plant_2"),
    Component(id="chain_1", name="Duette Chain", plant_id="plant_3"),
    Component(id="fabric_2", name="Silhouette Fabric", plant_id="plant_1"),
    Component(id="headrail_2", name="Silhouette Headrail", plant_id="plant_2"),
    Component(id="bottom_rail_2", name="Silhouette Bottom Rail", plant_id="plant_2"),
    Component(id="fabric_3", name="Luminette Fabric", plant_id="plant_1"),
    Component(id="headrail_3", name="Luminette Headrail", plant_id="plant_2"),
    Component(id="bottom_rail_3", name="Luminette Bottom Rail", plant_id="plant_2"),
    Component(id="chain_2", name="Luminette Chain", plant_id="plant_3"),
]

from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    valid_plants = {
        "Flower": Flower,
        "LeafPlant": LeafPlant
    }

    valid_clients = {
        "RegularClient": RegularClient,
        "BusinessClient": BusinessClient
    }

    def __init__(self):
        self.income: float = 0
        self.plants: [BasePlant] = []
        self.clients: [BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int,
                  plant_extra_data: str):
        if plant_type not in self.valid_plants:
            raise ValueError("Unknown plant type!")

        new_plant = self.valid_plants[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.valid_clients:
            raise ValueError("Unknown client type!")

        new_client = self.valid_clients[client_type](client_name, client_phone_number)

        if new_client.phone_number in [c.phone_number for c in self.clients]:
            raise ValueError("This phone number has been used!")

        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        if client_phone_number not in [c.phone_number for c in self.clients]:
            raise ValueError("Client not found!")

        if plant_name not in [p.name for p in self.plants]:
            raise ValueError("Plants not found!")

        client: BaseClient = [c for c in self.clients if c.phone_number == client_phone_number][0]
        plant = [p for p in self.plants if p.name == plant_name][0]

        current_plants = [p for p in self.plants if p.name == plant_name]
        count_current_plant = len(current_plants)

        if plant_quantity > count_current_plant:
            return f"Not enough plant quantity."

        if client.discount > 0:
            self.income += (plant.price * plant_quantity) * (1 - client.discount / 100)
            order_amount = plant.price * plant_quantity * (1 - client.discount / 100)
        else:
            self.income += plant.price * plant_quantity
            order_amount = plant.price * plant_quantity

        for _ in range(plant_quantity):
            self.plants.remove(current_plants.pop(0))

        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        if plant_name not in [p.name for p in self.plants]:
            return f"No such plant name."

        plant: BasePlant = [p for p in self.plants if p.name == plant_name][0]
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        count = 0
        clients_to_remove = []
        for client in self.clients:
            if client.total_orders == 0:
                clients_to_remove.append(client)
                count += 1

        for client in clients_to_remove:
            self.clients.remove(client)

        return f"{count} client/s removed."

    def shop_report(self):
        report = ["~Flower Shop Report~"]

        total_orders = sum(client.total_orders for client in self.clients)
        report.append(f"Income: {self.income:.2f}")
        report.append(f"Count of orders: {total_orders}")
        report.append(f"~~Unsold plants: {len(self.plants)}~~")

        plant_counts = {}
        for plant in self.plants:
            plant_counts[plant.name] = plant_counts.get(plant.name, 0) + 1

        sorted_plant_counts = (f"{plant_name}: {count}" for plant_name, count in sorted(
            plant_counts.items(), key=lambda x: (-x[1], x[0])
        ))
        report.extend(sorted_plant_counts)

        report.append(f"~~Clients number: {len(self.clients)}~~")
        sorted_clients = (client.client_details() for client in sorted(
            self.clients, key=lambda c: (-c.total_orders, c.phone_number)
        ))
        report.extend(sorted_clients)

        return "\n".join(report)

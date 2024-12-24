from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    def __init__(self, name: str):
        super().__init__(name, 25000.0, 3000)

    def increase_money(self):
        self.available_money += 5000

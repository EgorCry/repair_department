import random


class Ingredient:
    """Simple class for creating ingredients."""

    def __init__(self, name, max_weight, expiration_date, min_humidity, max_humidity, min_temperature, max_temperature):
        """Initialize the ingredient class."""
        self.name = name
        self.max_weight = max_weight
        self.weight = self.max_weight
        self.expiration_date = expiration_date
        self.max_humidity = max_humidity
        self.min_humidity = min_humidity
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.hours = 24

    def change_weight(self, change):
        """When we use part of ingredient, we should to change it weight."""
        self.weight -= change

    def check_weight(self):
        """Returns proportions of the weight of the ingredient."""
        return round((self.weight / self.max_weight), 2)

    def check_temperature(self, temperature):
        """Returns true if temperature is in range."""
        return self.min_temperature < temperature < self.max_temperature

    def check_humidity(self, humidity):
        """Returns true if humidity is in range."""
        return self.min_humidity < humidity < self.max_humidity

    def change_expiration_date(self):
        """Decreases the expiration date by one day every 24 'hours'."""
        self.expiration_date -= 1

    def check_expiration_date(self):
        """Returns how many days left."""
        return True if self.expiration_date < 2 else False

"""Planet Class."""
class Planet:
    """Planet class. Has the methods and attribute for planets."""
    def __init__(self, name: str, planet_type: str, star:str) -> None:

        if not (isinstance(name, str) and isinstance(planet_type, str) and isinstance(star, str)):
            raise TypeError("name, planet type, and star must be strings")

        if not (name and planet_type and star):
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def __str__(self) -> str:
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

    def orbit(self) -> str:
        """Returns a string describing the orbit of the planet."""
        return f"{self.name} is orbiting around {self.star}..."

# Example planets
planet_1 = Planet("Jupiter", "Gas Giant", "The Sun")
planet_2 = Planet("Neptune", "Gas Giant", "The Sun")
planet_3 = Planet("Venus", "Terrestrial", "The Sun")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

"""Tests for the Planet Class."""
import pytest
from planet import Planet

class TestPlanetInitialization:
    """Tests for successful instantiation and attribute assignment."""

    def test_valid_initialization(self):
        """Valid initialization test."""
        planet = Planet("Earth", "Terrestrial", "Sun")
        assert planet.name == "Earth"
        assert planet.planet_type == "Terrestrial"
        assert planet.star == "Sun"


class TestPlanetValidation:
    """Tests for type checking and non-empty string validation in __init__."""

    @pytest.mark.parametrize(
        "name, planet_type, star",
        [
            (123, "Terrestrial", "Sun"),  # Non-string name
            ("Earth", None, "Sun"),  # Non-string planet_type
            ("Earth", "Terrestrial", ["Sun"]),  # Non-string star
            (1.5, True, 42),  # All non-strings
        ],
    )
    def test_invalid_types_raise_type_error(self, name: str, planet_type: str, star: str):
        """Invalid types test."""
        with pytest.raises(TypeError, match="must be strings"):
            Planet(name, planet_type, star)

    @pytest.mark.parametrize(
        "name, planet_type, star",
        [
            ("", "Terrestrial", "Sun"),  # Empty name
            ("Earth", "", "Sun"),  # Empty planet_type
            ("Earth", "Terrestrial", ""),  # Empty star
            ("", "", ""),  # All empty
        ],
    )
    def test_empty_strings_raise_value_error(self, name: str, planet_type: str, star: str):
        """Empty strings test."""
        with pytest.raises(ValueError, match="must be non-empty strings"):
            Planet(name, planet_type, star)


class TestPlanetMethods:
    """Tests for __str__ and orbit methods."""

    def test_str_representation(self):
        """String representation test."""
        planet = Planet("Mars", "Terrestrial", "Sun")
        expected_str = "Planet: Mars | Type: Terrestrial | Star: Sun"
        assert str(planet) == expected_str

    def test_orbit_method(self):
        """Orbit method test."""
        planet = Planet("Jupiter", "Gas Giant", "Sun")
        expected_orbit = "Jupiter is orbiting around Sun..."
        assert planet.orbit() == expected_orbit

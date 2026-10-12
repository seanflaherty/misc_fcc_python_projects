"""Game Character class demonstrating properties and setters."""
class GameCharacter:
    """Game character class.

    Attributes:
        name (str):
        health (int):
        mana (int):
        level (int):
    """
    def __init__(self, name):
        self._name=name
        self._health=100
        self._mana=50
        self._level=1

    @property
    def name(self):
        """Name property."""
        return self._name

    @property
    def health(self):
        """Health property."""
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health<0:
            self._health=0
        elif new_health>100:
            self._health=100
        else:
            self._health=new_health

    @property
    def mana(self):
        """Mana property."""
        return self._mana

    @mana.setter
    def mana(self,new_mana):
        if new_mana<0:
            self._mana=0
        elif new_mana>50:
            self._mana=50
        else:
            self._mana=new_mana

    @property
    def level(self):
        """Level property."""
        return self._level

    def level_up(self):
        """Level up method."""
        self._level +=1
        self.health=100
        self.mana=50
        print(f"{self.name} leveled up to {self._level}!")

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

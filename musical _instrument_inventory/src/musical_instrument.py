"""Musical Instrument class."""
class MusicalInstrument:
    """Musical Instrument Class"""
    def __init__(self, name: str, instrument_type: str) -> None:
        self.name = name
        self.instrument_type = instrument_type

    def play(self) -> None:
        """Play method, returns None."""
        print(f'The {self.name} is fun to play!')

    def get_fact(self) -> str:
        """Returns facts about the instrument."""
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'

# examples
instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())

instrument_2.play()
print(instrument_2.get_fact())

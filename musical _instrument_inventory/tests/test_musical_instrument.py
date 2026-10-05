"""Tests for the Musical Instrument Class."""

import pytest
# scf from musical_instrument import MusicalInstrument
from src.musical_instrument import MusicalInstrument

#scf import musical_instrument


@pytest.fixture
def sample_instrument() -> MusicalInstrument:
    """Fixture providing a reusable instance for tests."""
    return MusicalInstrument(name="Guitar", instrument_type="String")


class TestMusicalInstrumentInitialization:
    """Tests for class instantiation and attribute assignment."""

    def test_init_sets_attributes_correctly(self, sample_instrument: MusicalInstrument) -> None:
        """Verify that name and instrument_type are assigned correctly."""
        assert sample_instrument.name == "Guitar"
        assert sample_instrument.instrument_type == "String"

    def test_init_with_empty_strings(self) -> None:
        """Verify behavior when instantiated with empty string arguments."""
        instrument = MusicalInstrument(name="", instrument_type="")
        assert instrument.name == ""
        assert instrument.instrument_type == ""


class TestMusicalInstrumentMethods:
    """Tests for class methods behavior."""

    def test_get_fact_returns_formatted_string(self, sample_instrument: MusicalInstrument) -> None:
        """Verify get_fact returns the expected string statement."""
        expected = "The Guitar is part of the String family of instruments."
        assert sample_instrument.get_fact() == expected

    def test_play_prints_to_stdout(
        self, sample_instrument: MusicalInstrument, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Verify play prints the expected message to stdout."""
        sample_instrument.play()

        # Capture standard output printed during method execution
        captured = capsys.readouterr()
        assert captured.out == "The Guitar is fun to play!\n"

    def test_play_returns_none(self, sample_instrument: MusicalInstrument) -> None:
        """Verify play method explicitly returns None."""
        result = sample_instrument.play()
        assert result is None


class TestMusicalInstrumentEdgeCases:
    """Tests for uncommon or edge inputs."""

    @pytest.mark.parametrize(
        "name, instrument_type, expected_fact",
        [
            ("Drums", "Percussion", "The Drums is part of the Percussion family of instruments."),
            ("123", "Digital", "The 123 is part of the Digital family of instruments."),
            ("Flute", "Woodwind", "The Flute is part of the Woodwind family of instruments."),
        ],
    )
    def test_get_fact_parameterized(
        self, name: str, instrument_type: str, expected_fact: str
    ) -> None:
        """Verify get_fact output across multiple instrument types using parametrization."""
        instrument = MusicalInstrument(name=name, instrument_type=instrument_type)
        assert instrument.get_fact() == expected_fact

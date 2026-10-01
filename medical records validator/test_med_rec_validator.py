"""
Tests for the medical records validator module.
"""
from .med_rec_validator import find_invalid_records
#SCF import find_invalid_records

def test_find_invalid_records_valid_input():
    """test function using valid input."""
    result = find_invalid_records(
        patient_id="p001",
        age=25,
        gender="Female",
        diagnosis=None,
        medications=["medA", "medB"],
        last_visit_id="v99"
    )
    assert result == []

def test_find_invalid_records_all_fields_invalid():
    """"test function using invalid inputs."""
    result = find_invalid_records(
        patient_id="bad_id",
        age=16,
        gender="Other",
        diagnosis=123, # type: ignore[arg-type]
        medications="not_a_list", # type: ignore[arg-type]
        last_visit_id="invalid_visit"
    )
    assert set(result) == {'patient_id', 'age', 'gender',
                            'diagnosis', 'medications', 'last_visit_id'}

def test_medications_validation():
    """test medications validation."""
    cases = [
        ([], True),
        (["aspirin"], True),
        (["aspirin", 123], False),
        ("aspirin", False),
    ]

    for medications_input, expected_valid in cases:
        result = find_invalid_records(
            patient_id="p1", age=20, gender="male",
            diagnosis=None, medications=medications_input, last_visit_id="v1"
        )
        if expected_valid:
            assert "medications" not in result
        else:
            assert "medications" in result

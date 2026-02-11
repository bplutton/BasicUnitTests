# Beckett/Yámato Lutton

import pytest
from password import validate_password

def test_happy_path():
    # Arrange
    input_val = "Password123"

    # Act
    result = validate_password(input_val)

    # Assert
    assert result is True

def test_edge_case():
    # Arrange
    input_val = "Pass123"

    # Act
    result = validate_password(input_val)

    # Assert
    assert result is False

def test_exception():
    # Arrange
    input_val = 100

    # Assert
    with pytest.raises(TypeError):
        validate_password(input_val)
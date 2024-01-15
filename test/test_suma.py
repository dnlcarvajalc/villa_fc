import pytest
from unittest.mock import patch
from src.suma import suma
from src.message import enviar_mensajes

@patch("src.suma.kit.sendwhatmsg_instantly")
def test_suma(mock_sendwhatmsg):
    prueba_1 = suma(2, 5)
    prueba_2 = suma(2, 3)

    assert prueba_1 == 7
    assert prueba_2 == 5


def test_enviar_mensajes_fail():
    mock_dictionary = {"algo":"algo"}
    assertion_value = enviar_mensajes(mock_dictionary)
    assert assertion_value
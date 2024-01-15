from unittest.mock import patch
from src.message import enviar_mensajes

@patch("src.kit.sendwhatmsg_instantly")

def test_enviar_mensajes_fail():
    mock_dictionary = {"algo":"algo"}
    assertion_value = enviar_mensajes(mock_dictionary)
    assert assertion_value
from ai.providers.chat_models import ChatModels


def test_chat_models_values():
    assert ChatModels.GPT5.value == "gpt-5"
    assert ChatModels.GPT5_MINI.value == "gpt-5-mini"
    assert ChatModels.GPT5_NANO.value == "gpt-5-nano"
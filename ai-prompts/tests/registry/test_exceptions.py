from ai_prompts.registry.exceptions import (
    PromptAlreadyRegisteredError,
    PromptNotRegisteredError,
    RegistryError,
)


def test_registry_error():
    assert issubclass(
        RegistryError,
        Exception,
    )


def test_prompt_already_registered_error():
    assert issubclass(
        PromptAlreadyRegisteredError,
        RegistryError,
    )


def test_prompt_not_registered_error():
    assert issubclass(
        PromptNotRegisteredError,
        RegistryError,
    )

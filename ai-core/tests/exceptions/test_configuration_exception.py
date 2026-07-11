from exceptions.configuration_exception import ConfigurationException
from exceptions.error_codes import ErrorCode


def test_configuration_exception():
    try:
        raise ConfigurationException(
            "Invalid configuration", details={"config": "value"}
        )
    except ConfigurationException as e:
        assert e.message == "Invalid configuration"
        assert e.error_code == ErrorCode.CONFIGURATION_ERROR.value
        assert e.status_code == 500
        assert e.module == "Configuration"
        assert e.details == {"config": "value"}

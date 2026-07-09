from exceptions.error_codes import ErrorCode

def test_error_codes():
    assert ErrorCode.VALIDATION_ERROR.value == "VAL001"
    assert ErrorCode.AUTHENTICATION_ERROR.value == "AUTH001"
    assert ErrorCode.AUTHORIZATION_ERROR.value == "AUTHZ001"
    assert ErrorCode.DATABASE_ERROR.value == "DB001"
    assert ErrorCode.AI_ERROR.value == "AI001"
    assert ErrorCode.INTEGRATION_ERROR.value == "INT001"
    assert ErrorCode.FILE_ERROR.value == "FILE001"
    assert ErrorCode.NETWORK_ERROR.value == "NET001"
    assert ErrorCode.CONFIGURATION_ERROR.value == "CFG001"
    assert ErrorCode.NOT_FOUND_ERROR.value == "NF001"
from exceptions.error_codes import ErrorCode

print("Validation :", ErrorCode.VALIDATION_ERROR.value)
print("Authentication :", ErrorCode.AUTHENTICATION_ERROR.value)
print("Database :", ErrorCode.DATABASE_ERROR.value)

print("Error codes loaded successfully.")
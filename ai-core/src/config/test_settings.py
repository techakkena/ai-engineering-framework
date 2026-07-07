from config.settings import settings

print("Framework        :", settings.FRAMEWORK_NAME)
print("Application      :", settings.APP_NAME)
print("Version          :", settings.VERSION)

print()

print("API Host         :", settings.API_HOST)
print("API Port         :", settings.API_PORT)

print()

print("Database         :", settings.DATABASE_URL)

print()

print("Chat Model       :", settings.DEFAULT_CHAT_MODEL)
print("Embedding Model  :", settings.DEFAULT_EMBEDDING_MODEL)

print()

print("Storage Root     :", settings.STORAGE_ROOT)
print("Upload Folder    :", settings.UPLOAD_FOLDER)
print("Log File         :", settings.LOG_FILE)

print()

print("Log Level        :", settings.LOG_LEVEL)
from .logging_constants import (
    LogLevel,
    LoggerName,
    LogFormat,
    Rotation,
    OutputType,
)


def main():

    print()

    print("Log Levels")
    print("-------------------------")

    print(LogLevel.INFO)
    print(LogLevel.ERROR)

    print()

    print("Logger Names")
    print("-------------------------")

    print(LoggerName.FRAMEWORK)
    print(LoggerName.CORE)

    print()

    print("Log Format")
    print("-------------------------")

    print(LogFormat.STANDARD)

    print()

    print("Rotation")

    print("-------------------------")

    print(Rotation.MAX_FILE_SIZE)
    print(Rotation.BACKUP_COUNT)

    print()

    print("Output")

    print("-------------------------")

    print(OutputType.CONSOLE)
    print(OutputType.FILE)
    print(OutputType.BOTH)


if __name__ == "__main__":
    main()
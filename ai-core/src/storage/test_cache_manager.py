from .cache_manager import CacheManager


def main():

    cache = CacheManager()

    print()

    print("Set")
    print("----------------")

    cache.set(
        "user_101",
        {
            "name": "John",
            "role": "Admin",
        },
    )

    print(cache.exists("user_101"))

    print()

    print("Get")
    print("----------------")

    print(cache.get("user_101"))

    print()

    print("Delete")
    print("----------------")

    cache.delete("user_101")

    print(cache.exists("user_101"))


if __name__ == "__main__":
    main()
from .upload_manager import UploadManager


def main():

    upload = UploadManager()

    file = upload.upload(
        "demo.txt",
        "Hello Upload Manager",
    )

    print()

    print("Uploaded")

    print("---------------------")

    print(file)

    print()

    print("Exists")

    print("---------------------")

    print(upload.exists(file))

    print()

    print("Size")

    print("---------------------")

    print(upload.size(file))

    print()

    print("Delete")

    print("---------------------")

    upload.delete(file)

    print(upload.exists(file))


if __name__ == "__main__":
    main()
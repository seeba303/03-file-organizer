import os

os.makedirs("Images", exist_ok=True)
os.makedirs("documents", exist_ok=True)
os.makedirs("music", exist_ok=True)


def move_file(filename, folder):
    name, extension = os.path.splitext(filename)
    destination = os.path.join(folder, filename)

    counter = 1

    while os.path.exists(destination):
        destination = os.path.join(
            folder,
            name + "_" + str(counter) + extension
        )
        counter += 1

    os.rename(filename, destination)


for filename in os.listdir():
    name, extension = os.path.splitext(filename)
    extension = extension.lower()

    if extension == ".jpg" or extension == ".jpeg" or extension == ".png":
        print(filename, "is an image")
        move_file(filename, "Images")

    elif extension == ".pdf":
        print(filename, "is a document")
        move_file(filename, "documents")

    elif extension == ".mp3":
        print(filename, "is music")
        move_file(filename, "music")

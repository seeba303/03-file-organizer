import os

os.makedirs("Images", exist_ok=True)
os.makedirs("documents", exist_ok=True)
os.makedirs("music", exist_ok=True)

for filename in os.listdir():
    name, extension = os.path.splitext(filename)
    extension = extension.lower()

    if extension == ".jpg" or extension == ".jpeg" or extension == ".png":
        print(filename, "is an image")
        destination = "Images/" + filename

        counter = 1

        while os.path.exists(destination):
            destination = "Images/" + name + "_" + str(counter) + extension
            counter += 1

        os.rename(filename, destination)

    elif extension == ".pdf":
        print(filename, "is a document")
        os.rename(filename, "documents/" + filename)

    elif extension == ".mp3":
        print(filename, "is music")
        destination = "music/" + filename

        counter = 1

        while os.path.exists(destination):
            destination = "music/" + name + "_" + str(counter) + extension
            counter += 1

        os.rename(filename, destination)
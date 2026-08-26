import os
os.makedirs("Images", exist_ok=True)
os.makedirs("documents", exist_ok=True)
os.makedirs("music", exist_ok=True)

for filename in os.listdir():
    name, extension = os.path.splitext(filename)

    if extension == ".jpg" or extension == ".jpeg" or extension == ".png":
        print(filename, "is an image")
        os.rename(filename, "Images/" + filename)
    elif extension == ".pdf":
        print(filename, "is a document")
        os.rename(filename, "documents/" + filename)
    elif extension == ".mp3":
        print (filename, "is music")
        os.rename(filename, "music/" + filename)
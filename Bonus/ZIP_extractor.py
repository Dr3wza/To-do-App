import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("Users\Andrew\Documents\Python\App_1\pythonProject\Bonus\005 compressed.zip",
                    "Users\Andrew\Documents\Python\App_1\pythonProject\Bonus\Dest")

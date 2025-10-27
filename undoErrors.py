import os

DIRECTORY = os.getcwd()

GAME = "Peggle Deluxe 1.01"

def moveFiles(folders):
    for folder in folders:
        if GAME not in folder or GAME == folder[-len(GAME):]:
            # print("Skipping folder:", folder)
            # input()
            continue
        for file in os.listdir(folder):
            source = os.path.join(folder, file)
            destination = os.path.join(DIRECTORY, file)
            os.rename(source, destination)

def deleteEmptyFolders(folders):
    for folder in folders:
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)

folders = [os.path.join(DIRECTORY, d) for d in os.listdir(DIRECTORY) if os.path.isdir(os.path.join(DIRECTORY, d))]

moveFiles(folders)
deleteEmptyFolders(folders)
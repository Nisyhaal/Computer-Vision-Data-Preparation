import os
import shutil

def getPath():
    rootPath = input("Enter the absolute path of root directory: ")
    targetPath = input("Enter the absolute path of target directory: ")
    imageTargetPath = os.path.join(targetPath, "Images")
    labelTargetPath = os.path.join(targetPath, "Labels")
    return [rootPath, targetPath, imageTargetPath, labelTargetPath]

def makeDirectory(targetPath, imageTargetPath, labelTargetPath):
    shutil.rmtree(targetPath, True)
    os.makedirs(imageTargetPath)
    os.makedirs(labelTargetPath)

def moveToWorkingDirectory(rootPath, imageTargetPath, labelTargetPath):
    for root, directories, files in os.walk(rootPath):
        for file in files:
            if os.path.splitext(file)[1] == ".jpeg":
                shutil.copy(os.path.join(rootPath, file), os.path.join(imageTargetPath, file))
            if os.path.splitext(file) == ".xml":
                shutil.copy(os.path.join(rootPath, file), os.path.join(labelTargetPath, file))
def main():
    path = getPath()
    moveToWorkingDirectory(path[0], path[2], path[3])

if __name__ == "__main__":
    main()

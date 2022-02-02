from models.object import Object
from helper.fileReader import FileReader

def compare(objA: Object, objB: Object):
    totalCompares = min(len(objA), len(objB))

    for i in range(totalCompares):
        if objA[i] == objB[i]:
            print(i, "matched", objA[i], objB[i])
        else:
            print(i, "unmatched", objA[i], objB[i])

def impl():

    readerA = FileReader(r"data\objectsA.txt")
    readerB = FileReader(r"data\objectsB.txt")

    objA = []
    objB = []

    if (readerA.getContent(objA) and readerB.getContent(objB)):
        compare(objA, objB)
    else:
        print("unable to fetch valid content from file")


if __name__ == "__main__":
    impl()
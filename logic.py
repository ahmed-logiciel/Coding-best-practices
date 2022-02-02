
"""
Write steps:
1. Read file
2. Compare objects

"""

def readfile(path: str, content: list) -> bool:
    try:
        files = open(path, 'r')
    except:
        print("File open failed")
        return False
    
    lines = files.readlines()
    for i in lines:
        content.append(i)

    files.close()

    return True


def compare(objA: str, objB: str) -> bool:
    return objA == objB


def impl() -> bool:

    print("impl")
    
    objectsA = []
    objectsB = []

    if not readfile(r"data\objectsA.txt", objectsA):
        return False

    if not readfile(r"data\objectsB.txt", objectsB):
        return False
    
    maxCompares = min(len(objectsA), len(objectsB))

    for i in range(maxCompares):
        if compare(objectsA[i], objectsB[i]):
            print("Matched", objectsA[i], objectsB[i])
        else:
            print("Unmatched", objectsA[i], objectsB[i])

    return True
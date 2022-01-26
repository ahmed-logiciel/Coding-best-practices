from models import objects

def impl():

    fileA = open(r"data\objectsA.txt", 'r')
    fileB = open(r"data\objectsB.txt", 'r')

    objA_raw = fileA.readlines()
    objB_raw = fileB.readlines()

    fileA.close()
    fileB.close()

    objA = []
    objB = []

    for i in objA_raw:
        obj = i.strip().split()
        objA.append(objects.Object(obj[0], obj[1], obj[1]))
    
    for i in objB_raw:
        obj = i.strip().split()
        objB.append(objects.Object(obj[0], obj[1], obj[1]))
    
    totalCompares = min(len(objA), len(objB))

    for i in range(totalCompares):
        if objA[i] == objB[i]:
            print(i, "matched ", objA[i], objB[i])
        else:
            print(i, "unmatched ", objA[i], objB[i])


if __name__ == "__main__":
    impl()
        
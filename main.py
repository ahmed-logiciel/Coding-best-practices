# implementation of naive algorithm to tackle problem

# function which contains implementation, can be named main
def impl():

    # opening both files
    fileA = open(r"data\objectsA.txt", 'r')
    fileB = open(r"data\objectsB.txt", 'r')

    # this will read all lines from files and store each of them as a
    # string in list
    objA = fileA.readlines()
    objB = fileB.readlines()

    # closing files as they are no longer needed open
    fileA.close()
    fileB.close()

    # each file can contain different number of lines so we should only
    # compare minimum available
    totalCompares = min(len(objA), len(objB))

    for i in range(totalCompares):
        if objA[i].strip() == objB[i].strip():
            print(i, "matched")
        else:
            print(i, "unmatched")
    
# call impl function if this file is run
if __name__ == "__main__":
    impl()
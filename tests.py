from logic import readfile, compare


def test_readfile():

    if readfile(r"data\objectsA.txt", []) == True:
        print("Pass")
    else:
        print("Fail")
    
    if readfile(r"", []) == True:
        print("Fail")
    else:
        print("Pass")

def test_compare():

    if compare("Ahmed", "Ali") == True:
        print("Fail")
    else:
        print("Pass")
    
    if compare("Ahmed", "Ahmed") == False:
        print("Fail")
    else:
        print("Pass")

def tests():
    test_readfile()
    test_compare()
from models.object import Object

class FileReader:

    def __init__(self, path: str) -> None:
        print("File reader init")
        self.m_path = path
        self.__m_file = 0

    def __open(self) -> bool:   # private method, abstracted away from user
        try:
            self.__m_file = open(self.m_path, 'r')
            return True
        except:
            print("Exception thrown. File path specified is incorrect")
            return False
    
    def setPath(self, path: str) -> bool:   # setter
        if path == "":
            return False
        self.m_path = path
        return True
    
    def getContent(self, objList: list) -> bool:    # reads file and stores in the referenced list
        objList.clear()    # empty it first
        if (self.__open()):
            strList = self.__m_file.readlines()
            for i in strList:
                obj = i.strip().split()
                if len(obj) != 3:                   # this three is a magic number, think of logic to fix
                    print("Wrong number of fields read")
                    return False
                else:
                    objList.append(Object(obj[0], obj[1], obj[2]))
            return True
    
    def __del__(self):  # automatically called
        print("File reader destructor")
        if (type(self.__m_file) != int):
            self.__m_file.close()



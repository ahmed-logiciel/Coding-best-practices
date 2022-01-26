# model class for objects in the file
# this specific, we expect a pre-defined format of objects
class Object:
    
    def __init__(self, fruit, food, fish) -> None:
        self.m_fruit = fruit
        self.m_food = food
        self.m_fish = fish
    
    # equal to operator overloaded
    def __eq__(self, other) -> bool:
        if (self.m_fruit == other.m_fruit) and (self.m_food == other.m_food) and (self.m_fish == other.m_fish):
            return True
        else:
            return False
    
    # print overload
    def __str__(self) -> str:
        return "*** Object => " + self.m_fruit + " " + self.m_food + " " + self.m_fish
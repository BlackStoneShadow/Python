SIZE = 8

class Board:
    def __init__(self, *args):
        self.positions = args        

    def strike(self)->bool:
        for pos in self.positions:         
            strikes = [ pos ]
            x, y = map(int, pos.split("X"))            
            for i in range(1, SIZE + 1):
                strikes.append(f"{x}X{i}")
                strikes.append(f"{i}X{y}")
                if x+i <= SIZE and y+i <= SIZE:
                    strikes.append(f"{x+i}X{y+i}")
                if x-i > 0 and y-i > 0:
                    strikes.append(f"{x-i}X{y-i}")
            for item in self.positions:
                if item != pos and item in strikes:
                    return False
        return True

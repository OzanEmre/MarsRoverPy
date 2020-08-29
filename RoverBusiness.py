from RoverModel import RoverModel
import json

class RoverBusiness:
    def __init__(self, landingInput, navigationInput, moveCommand):
        super().__init__()
        landI = landingInput.split(' ')
        navigationI = navigationInput.split(' ')
        land_x = int(landI[0])
        land_y = int(landI[1])

        x = int(navigationI[0])
        y = int(navigationI[1])
        direction = navigationI[2]

        landing = [land_x, land_y]

        RoverModel._X = x
        RoverModel._Y = y
        RoverModel._DIRECTION = direction
        RoverModel.LANDING = landing
        RoverModel._MOVECOMMAND = moveCommand
    
    def turnLeft():
        if RoverModel._DIRECTION == "N":
            RoverModel._DIRECTION = "W"
        elif RoverModel._DIRECTION == "W":
            RoverModel._DIRECTION = "S"
        elif RoverModel._DIRECTION == "S":
            RoverModel._DIRECTION = "E"
        elif RoverModel._DIRECTION == "E":
            RoverModel._DIRECTION = "N"
    
    def turnRight():
        if RoverModel._DIRECTION == "N":
            RoverModel._DIRECTION = "E"
        elif RoverModel._DIRECTION == "E":
            RoverModel._DIRECTION = "S"
        elif RoverModel._DIRECTION == "S":
            RoverModel._DIRECTION = "W"
        elif RoverModel._DIRECTION == "W":
            RoverModel._DIRECTION = "N"
    
    def move():
        if RoverModel._Y > RoverModel.LANDING[0] or RoverModel._X > RoverModel.LANDING[0] or RoverModel._Y == 0  or RoverModel._X == 0:
            RoverModel._LASTPOSITION = [RoverModel._X, RoverModel._Y]
        if RoverModel._DIRECTION == "E":
            RoverModel._X = RoverModel._X + 1
        elif RoverModel._DIRECTION == "W":
            RoverModel._X = RoverModel._X - 1
        elif RoverModel._DIRECTION == "N":
            RoverModel._Y = RoverModel._Y + 1
        elif RoverModel._DIRECTION == "S":
            RoverModel._Y = RoverModel._Y - 1
        #burada lastpoint için platue alanına bakılacak

    def navigate():
        for item in RoverModel._MOVECOMMAND:
            if item == "L":
                RoverBusiness.turnLeft()
            elif item == "R":
                RoverBusiness.turnRight()
            elif item == "M":
                RoverBusiness.move()
        
        result = { "success": 1, "result": [RoverModel._X, RoverModel._Y, RoverModel._DIRECTION] }
        if RoverModel._Y > RoverModel.LANDING[0] or RoverModel._X > RoverModel.LANDING[0] or RoverModel._Y < 0  or RoverModel._X < 0:
            result = {"success": 0, "result": [RoverModel._X, RoverModel._Y, RoverModel._DIRECTION], "lastPoint": [RoverModel._LASTPOSITION[0], RoverModel._LASTPOSITION[1], RoverModel._LASTDIRECTION] }
        return json.dumps(result)
from RoverBusiness import RoverBusiness
import json

if __name__ == '__main__':
    isRun = True
    line = 0

    listCoordinats = []

    landingInput = input('Enter landing (Default= 5 5): ')
    if len(landingInput)==0:
        landingInput = "5 5"
    while isRun:
        line = line+1
        navigationInput = input('Enter start point {}: '.format(line))
        if len(navigationInput) == 0:
            if line == 1:
                navigationInput = "1 2 N"
            elif line == 2:
                navigationInput = "3 3 N"

        moveInput = input('Enter move commands {}: '.format(line))
        if len(moveInput) == 0:
            if line == 1:
                moveInput = "LMLMLMLMM"
            elif line == 2:
                moveInput = "MMRMMRMRRM"

        status = input("Continue 'C' or Exit press enter: ").upper()
        
        commands = [landingInput, navigationInput, moveInput, line]

        listCoordinats.append(commands)

        if status == "C":
            isRun = True
        else:
            isRun = False
    
    for command in listCoordinats:
        print("Line {} Commands: {} - {} - {}".format(command[3], command[0], command[1], command[2]))
        RoverBusiness(command[0], command[1], command[2])
        result = json.loads(RoverBusiness.navigate())
        if result["success"] == 1:
            print("Line {} Result: {} {} {}".format(command[3], result["result"][0], result["result"][1], result["result"][2]))
        else:
            print("ERROR! Out of platue\nLine {} Last Point in th border: {} {} {}".format(command[3], result["lastPoint"][0], result["lastPoint"][1], result["lastPoint"][2]))
file = open("program.txt", 'r').read()
content = file

lines = content.split("\n")
currentLine = 1
storage = {}



def newLine():
    global currentLine
    currentLine += 1
    return currentLine


def giveError(error, *extra):
    print(end=f"Error at line {currentLine}: ")
    if error == "varNotFound":
        print(f"No variable in storage called <{extra[0]}>")
    elif error == "missingArgument":
        print(f"Missing argument: \"{extra[0]}\"")
    elif error == "wrongType":
        print(f"Wrong type entered: {extra[0]}")
    elif error == "syntaxError":
        print(f"Syntax error: {extra[0]}")
    elif error == "depthError":
        print(f"Cannot assign variable to itself: {extra[0]}")
    else:
        print("X")


def assignVar(name: str, value, type: str, assignedAtLine: int):
    storage[name] = {"value": value, "type": type, "line": assignedAtLine}


def getVars(string: str, prefix: str = "@"):
    newString = ""
    varName = ""
    now = False
    for i in string:
        if i == prefix:
            now = True
        elif i == " " or i == "," or i == "\"" or i == ".":
            if varName in storage.keys():
                if storage[varName]["type"] == "bool":
                    newString += str(storage[varName]["value"]).lower()
                else:
                    newString += storage[varName]["value"]
            elif now:
                newString += prefix + varName
            newString += i
            varName = ""
            now = False
        elif now:
            varName += i
        else:
            newString += i
    if varName in storage.keys():
        if storage[varName]["type"] == "bool":
            newString += str(storage[varName]["value"]).lower()
        else:
            newString += storage[varName]["value"]
    elif now:
        newString += prefix + varName
    return newString

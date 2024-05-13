from sourceCode import *
# Functions

preStored = {"debug": {"value": False, "type": "bool"}}


def GetType(value):
    if type(value) == bool:
        Type = "bool"
    elif value in storage.keys():
        if storage[value]["type"] == "bool":
            Type = "bool"
        else:
            Type = "var"
    elif value in preStored.keys():
        Type = "preStored"
    else:
        Type = None
    return Type


'''def TranslateBool(boolArg):
    if GetType(boolArg) == "bool":
        return eval(boolArg[1:][0].upper()+boolArg[2:])
    elif type(boolArg) == bool:
        return "%" + str(boolArg).lower()
    else:
        giveError("wrongType", boolArg)'''


# Commands


def Set(lineParts):
    if lineParts[1][-1] == ":":
        assignVar(lineParts[1][0:-1], getVars(lineParts[2]), GetType(lineParts[2]), currentLine)
    else:
        if len(lineParts) == 2:
            if lineParts[1][0] == "!":
                assignVar(lineParts[1][1:], False, "bool", currentLine)
            else:
                assignVar(lineParts[1], True, "bool", currentLine)
        else:
            giveError("syntaxError", "Missing ':'")
    if preStored["debug"]["value"]:
        print(lineParts[1], ":->", getVars(lineParts[1][0:-1]), "->", getVars(getVars(lineParts[1][0:-1])), "#")


def Refresh(lineParts):  # Version 1
    '''    try:

    except KeyError:
        giveError("varNotFound", lineParts[1])'''
    return 'runLine(storage[lineParts[1]]["line"])'


def Say(phrase):
    try:
        if phrase in storage.keys():
            storage[phrase]["value"] = str(storage[phrase]["value"]).replace("\"", "")
            print(f'output: {storage[phrase]["value"]}')

        elif phrase[0] == "\"":
            print("output:", phrase[1:-1])
    except KeyError:
        giveError("varNotFound", phrase)

def Flip(boolArg):
    if boolArg in storage.keys():
        if GetType(boolArg) == "bool":
            storage[boolArg]["value"] = not storage[boolArg]["value"]
        else:
            giveError("wrongType", boolArg)
    elif boolArg in preStored.keys():
        if GetType(boolArg) == "preStored":
            preStored[boolArg]["value"] = not preStored[boolArg]["value"]
        else:
            giveError("wrongType", boolArg)



'''def Flip(boolArg):
    if boolArg in storage.keys():
        if GetType(boolArg) == "bool":
            storage[boolArg] = not storage[boolArg]
        else:
            giveError("wrongType", boolArg)
    elif boolArg in preStored.keys():
        if GetType(boolArg) == "bool":
            storage[boolArg] = not storage[boolArg]
        else:
            giveError("wrongType", boolArg)
    else:
        giveError("varNotFound")'''


def Debug(boolArg):
    if GetType(boolArg) == "bool":
        preStored["debug"]["value"] = boolArg
        print("debug:", boolArg)
        return preStored
    else:
        giveError("wrongType", boolArg)
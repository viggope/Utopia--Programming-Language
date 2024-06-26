from sourceCode import *

# Functions

preStored = {"debug": {"value": False, "type": "bool"}}


def getType(value):
    Type = "mysterious"
    if type(value) == bool:
        Type = "bool"
    elif value in storage.keys():
        if storage[value]["type"] == "bool":
            Type = "bool"
        else:
            Type = "var"
    elif value in preStored.keys():
        Type = "preStored"
    elif value[0].startswith("!"):
        if getType(Boolean(value[1:])) == "bool":
            Type = "bool"
    else:
        #print(value)
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


def If(boolArg: list, command: list):
    statement = ""
    for L in boolArg:
        statement += L
    if preStored["debug"]["value"]:
        print("statement: ", getVars(statement[0:len(statement)-1]), "execute:", command)
    if eval(getVars(statement[0:len(statement)-1])):
        return command
    else:
        return ["skip"]


def Set(lineParts, currentLine_):
    if lineParts[1][-1] == ":":
        assignVar(lineParts[1][0:-1], getVars(lineParts[2]), getType(lineParts[2]), currentLine_)

        if preStored["debug"]["value"]:
            print(lineParts[1], "->", storage[lineParts[1][0:-1]])
    else:
        if len(lineParts) == 2:
            if lineParts[1][0] == "!":
                assignVar(lineParts[1][1:], False, "bool", currentLine_)
            else:
                assignVar(lineParts[1], True, "bool", currentLine_)

            if preStored["debug"]["value"]:
                print(lineParts[1], "->", storage[lineParts[1]])
        else:
            giveError("syntaxError", "Missing ':'")

        '''print(lineParts[1], ":->", getVars(lineParts[1][0:-1]), "->", getVars(getVars(lineParts[1][0:-1])), "#")
        print(lineParts[2], ":->", getVars(lineParts[2][0:-1]), "->", getVars(getVars(lineParts[2][0:-1])), "#")'''


'''def Refresh(var):  # Version 2
    """
    try:

    except KeyError:
        giveError("varNotFound", lineParts[1])
    return f'runLine(storage["{lineParts[1]}"]["line"]-1)
    """
    return storage[var]["line"]'''


def Get(lineParts):
    return f'storage["{lineParts[1]}"]'


def Boolean(phrase):
    if getType(phrase) == "bool":
        if phrase[0] == "!":
            return not storage[phrase[1:]]["value"]
        return storage[phrase]["value"]


def Say(phrase):
    try:
        if phrase in storage.keys():
            storage[phrase]["value"] = str(storage[phrase]["value"])
            print('output: ' + storage[phrase]["value"])

        elif phrase[0] == "\"":
            if preStored["debug"]["value"]:
                print('output: ' + phrase[1:-1])
            else:
                print('output: ' + phrase[1:-1].replace("\"", ""))
    except KeyError:
        giveError("varNotFound", phrase)


def Flip(boolArg):
    if boolArg in storage.keys():
        if getType(boolArg) == "bool":
            storage[boolArg]["value"] = not storage[boolArg]["value"]
        else:
            giveError("wrongType", boolArg)
    elif boolArg in preStored.keys():
        if getType(boolArg) == "preStored":
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
    if getType(boolArg) == "bool":
        preStored["debug"]["value"] = Boolean(boolArg)
        print("debug:", preStored["debug"]["value"])
        return preStored
    else:
        giveError("wrongType", boolArg)

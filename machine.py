# from sourceCode import *
import commands
from commands import *


currentLine_ = commands.currentLine
using = {"2D": False, "scanner": False, "input": False}


def runLine(line: int):
    global preStored
    if preStored["debug"]["value"]:
        print(storage, "STORAGE")
    lineCont = lines[line]
    lineStrings = lineCont.split("\"")
    lineStrings2 = []
    c = 0
    for i in range(round(len(lineStrings) / 2)):
        for j in lineStrings[c].split(" "):
            if j != '':
                lineStrings2.append(j)
        try:
            lineStrings2.append(getVars(f"\"{lineStrings[c + 1]}\""))
        except IndexError:
            pass
        c += 2
    if not lineStrings2:
        lineParts = lineCont.split(" ")
    else:
        lineParts = lineStrings2
    if preStored["debug"]["value"]:
        print("\n\ncurrentLine:", currentLine_, "...\n")
        print("lineParts: ", lineParts, "#")

    try:
        if lineParts[0] == "if":
            if ":" in str(lineParts):
                index = 0
                while ":" not in lineParts[index]:
                    index += 1
                lineParts = If(lineParts[1:index+1], lineParts[index+1:])
            else:
                giveError("syntaxError", "missing :")



        if lineParts[0] == "set":
            Set(lineParts, currentLine_)

        elif lineParts[0] == "say":
            Say(lineParts[1])

        elif lineParts[0] == "refresh":
            try:
                var = storage[lineParts[1]]
                assignVar(lineParts[1], getVars(var["value"]), var["type"], var["line"])
            except KeyError:
                giveError("varNotFound", lineParts[1])

        elif lineParts[0] == "get":
            try:
                print(eval(Get(lineParts)))
            except KeyError:
                giveError("varNotFound", lineParts[1])

        elif lineParts[0] == "flip":
            Flip(lineParts[1])

        elif lineParts[0] == "debug":
            if lineParts[1] == "flip":
                preStored = Debug(not preStored["debug"]["value"])
            elif len(lineParts) == 1:
                preStored = Debug(True)
            else:
                preStored = Debug(lineParts[1])

    except IndexError:
        giveError("missingArgument", lineParts[0])



def runProgram():
    global debug, currentLine_
    for i in range(len(lines)):
        debug = preStored["debug"]["value"]
        runLine(i)
        currentLine_ = newLine()


runProgram()
# print(storage)

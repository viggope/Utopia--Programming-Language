# from sourceCode import *
from commands import *


def runLine(line: int):
    global preStored
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
        print("currentLine:", currentLine, "...")
        print("lineParts: ", lineParts, "#")

    try:
        if lineParts[0] == "set":
            Set(lineParts)

        elif lineParts[0] == "say":
            Say(lineParts[1])

        elif lineParts[0] == "refresh":
            try:
                exec(Refresh(lineParts))
            except RecursionError:
                giveError("depthError")
            except KeyError:
                giveError("varNotFound", lineParts[1])

        elif lineParts[0] == "flip":
            Flip(lineParts[1])

        elif lineParts[0] == "if":
            pass

        elif lineParts[0] == "debug":
            preStored = Debug(lineParts[1])

    except IndexError:
        giveError("missingArgument", lineParts[0])



def runProgram():
    global debug, currentLine
    for i in range(len(lines)):
        debug = preStored["debug"]["value"]
        runLine(i)
        currentLine = newLine()


runProgram()
# print(storage)

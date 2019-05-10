import re
from itertools import cycle

def calc():
    out = ""
    for a in inputs:
        inputStr = inputs[a]
        inputString = inputStr.replace("!*", "^")
        inputString = inputString.replace("!+", "~")
        inputString = inputString.replace("*", "")
        inputs[a] = inputString
    for a in inputString:
        if alphabets.match(a) and not(a in alphabet):
            alphabet.append(a)
    binarygenerator()
    for alp in alphabet:
        out += alp + "  "
    out += "|  "
    for eqs in inputs:
        out += inputs[eqs] + "  "
    out += "\n"
    for dic in convertedlist:
        for alp in alphabet:
            out += dic[alp] + "  "
        out += "|  "
        for i in inputs:
            replacedstring = exchange(dic, inputs[i])
            while len(replacedstring) > 1:
                replacedstring = eval(replacedstring)
            lengthstr = len(inputs[i])
            for o in range(int(lengthstr / 2)):
                out += " "
            out += replacedstring
            offset = 0

            if int(lengthstr) % 2 == 0:
                offset = int(lengthstr / 2) - 1
            else:
                offset = int(lengthstr / 2)
            for o in range(offset):
                out += " "
            out += "  "
        out += "\n"
    print(out)


def eval(stringin):
    out = ""
    pareopen = -1
    pareclose = len(stringin)
    for i in range(len(stringin)):
        current = stringin[i]
        if current == "(":
            pareopen = i
        elif current == ")":
            pareclose = i
            break
    if pareopen != -1:

        out += stringin[:pareopen]
    out += comblogic(stringin[pareopen + 1: pareclose])
    if pareclose <= len(stringin) - 1:
        out += substring(stringin, pareclose + 1, len(stringin))
    return out


def comblogic(stringin):
        return evalor(evalxor(evalnor(evalnand(evaland(negate(stringin))))))


def negate(string):
    index = 0
    while index < len(string):
        current = string[index]
        if current == "!":
            string = substring(string,0, index) + NOT(string[index + 1])+ substring(string, index + 2, len(string))
        else:
            index += 1
    return string


def evaland(string):
    index = 0
    while index < len(string) - 1:
        current = string[index]
        next = string[index + 1]
        if current.isdigit() and next.isdigit():
            string = substring(string, 0, index) + AND(current, next) + substring(string, index + 2, len(string))
        else:
            index += 1
    return string


def evalnand(string):
    return threedigitop(string, "^", NAND)



def evalnor(string):
    return threedigitop(string, "~", NOR)


def evalxor(string):
    return threedigitop(string, "|", XOR)


def evalor(string):
    return threedigitop(string, "+", OR)


def threedigitop(string, regex, operation):
    index = 1
    while index < len(string) - 1:
        first = string[index - 1]
        second = string[index]
        third = string[index + 1]
        if second == regex:
            string = substring(string, 0, index - 1) + operation(first, third) + substring(string, index + 2, len(string))
        else:
            index += 2
    return string



def NOT(bool):
    if bool == "1":
        return "0"
    else:
        return "1"


def NOR(bool1, bool2):
    if bool1 == "0" and bool2 == "0":
        return "1"
    else:
        return "0"


def XOR(bool1, bool2):
    if bool1 == bool2:
        return "0"

    else:
        return "1"


def OR(bool1, bool2):
    if bool1 == "1" or bool2 == "1":
        return "1"
    else:
        return "0"


def AND(bool1, bool2):
    if bool1 == "1" and bool2 == "1":
        return "1"
    else:
        return "0"


def NAND(bool1, bool2):
    if bool1 == "1" and bool2 == "1":
        return "0"
    else:
        return "1"


def exchange(dic, inputstr):
    for st in dic:
        inputstr = inputstr.replace(st, dic[st])
    return inputstr


def binarygenerator():
    currentnumber = ""
    for x in range(len(alphabet)):
        currentnumber += "0"
    convertedlist.append(binaryparser(currentnumber))
    for i in range(pow(2, len(alphabet)) - 1):
        currentnumber = binaryadd(currentnumber, "1")
        convertedlist.append(binaryparser(currentnumber))


def binaryparser(number):
    out = {}
    for i in range(len(alphabet)):
        out[alphabet[i]] = number[i]
    return out


def binaryadd(firstnum, secondnum):
    length = max(len(firstnum), len(secondnum))
    out = ""
    overload = 0
    while len(firstnum) < length:
        firstnum = "0" + firstnum
    while len(secondnum) < length:
       secondnum = "0" + secondnum
    for i in range(length):
        indexbackwards = length - 1 - i
        first = firstnum[indexbackwards]
        second = secondnum[indexbackwards]
        if not(first == second):
            if overload == 1:
                out += "0"
            else:
                out += "1"
        elif first == "1":
            if overload == 1:
                out += "1"
            else:
                out += "0"
                overload = 1
        else:
            if overload == 1:
                out += "1"
                overload = 0
            else:
                out += "0"
    if overload == 1:
        out += "1"
    out = out[::-1]
    return out


def substring(string, indexbegin, indexend):
    if indexend == 0 or indexbegin >= len(string):
        return ""
    else:
        return string[indexbegin: indexend]









#V1
# + : OR ; "" or * : AND  ; ! NEGATION(works also for logic ops : !* -> NAND) ; ^ : NAND ; | : XOR ; ~ : NOR ;
while True:
    inputs = {}
    index = 0
    inputs[index] = input("Please enter logic equation int form of : ABC+!A(DEF)\n + : OR ; "" or * : AND  ; ! NEGATION(works also for logic ops : !* -> NAND) ; ^ : NAND ; | : XOR ; ~ : NOR ;\n\n").__str__()
    if inputs[index] == "quit" or inputs[index] == "exit":
        break
    index += 1
    more = True
    while more:
        tempinput = input("Do you want to enter more equations?")
        if  tempinput == "yes" or tempinput == "y" or tempinput == "Yes" or tempinput == "Y":
            inputs[index] = input("Please enter logic equation int form of : ABC+!A(DEF)\n + : OR ; "" or * : AND  ; ! NEGATION(works also for logic ops : !* -> NAND) ; ^ : NAND ; | : XOR ; ~ : NOR ;\n\n").__str__()
            if inputs[index] == "quit" or inputs[index] == "exit":
                exit()
            index += 1
        else:
            more = False
    print("\n\n\n")
    alphabets = re.compile('[A-Za-z]')
    alphabet = []
    convertedlist = []
    calc()
    print("\n\n\n")
    choice = input("Do you want to quit?")
    if  choice == "y" or choice == "yes" or choice == "Y" or choice == "Yes":
        break
    print("\n\n\n")





def getPattern(word):
    index = 0
    pattern = []
    for letter in word:
        index = getPos(word ,letter)
        pattern.append(index)
    return pattern


def getPos(word ,letter):
    index = 0
    for l in word:
        if l == letter or l == letter.upper():
            return index
        else:
            index += 1


def stringBreakDown(string):
    result = []
    letters = False
    alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

    for y in alphabet:
        if (y in string):
            letters = True
            break

    if letters:
        word = ""
        for character in string:
            if (character != " "):
                word += character

            elif (word != ""):
                result.append(word)
                word = ""

        if word != "":
            result.append(word)

    else:
        word = []
        preanswer = []
        number = ""
        for x in range(len(string)):

            if x+1 == len(string):
                if string[x] != " ":
                    number += string[x]
                word.append(int(number))
                preanswer.append(word)

            elif string[x] != " " and string[x + 1] != " ":
                number += string[x]

            elif string[x] != " " and string[x + 1] == " ":
                number += string[x]
                word.append(int(number))
                number = ""

            elif string[x] == " " and string[x + 1] != " ":
                number = ""

            elif string[x] == " " and string[x + 1] == " ":
                if word != []:
                    preanswer.append(word)
                word = []

        variable = ""
        for index in preanswer:
            for number in index:
                variable += alphabet[number-1]
            result.append(variable)
            variable = ""

    print(result)


### MAIN ###

def getSimilar(word):
    f = open("words_alpha.txt", "r")
    words_alpha = f.readlines()


    result = []

    pattern = getPattern(word)

    for sample in words_alpha:
        sample = sample[:-1]
        if len(sample) == len(word):
            samplePattern = getPattern(sample)
            if pattern == samplePattern:
                result.append(sample)

    for x in result:
        print(x)

word = input("input >> ")
getSimilar(word)

example1 = "VUMQ KG XGR BEQ VUEF XGR NLGPP M NUSDHMFZEE VSQU M PNSEFQSPQ? M PQELFCX VGLKEK CEQQEL YLGD QUE EQUSNP OGMLK."
example2 = "7 12 26 20   14 4   22 4 15   14 4   7 12 3 2   22 4 15   12 26 16 3   2 15 6 3 24 25 5   5 4 14 3 23"

example1 = stringBreakDown(example1)
example2 = stringBreakDown(example2)


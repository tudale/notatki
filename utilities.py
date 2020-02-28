import json

# nie wiem co to robi właściwie
def InputCommenterLastTwo(i, n):
    if '{l' in i:
        if ('l' + str(n + 1) + '.' not in i) and ('l' + str(n) + '.' not in i) and ('l' + str(n - 1)+ '.' not in i):
            return "%" + i[1:]
        else:
            return ' ' + i[1:]
    else:
        return i

# nie wiem co to robi właściwie
def InputCommenterUncomment(i):
    if '{l' in i:
        return ' ' + i[1:]
    else:
        return i

# przepisuje wskazany plik, robiąc rzeczy potrzebne do jego prawidłowej edycji
def RewriteFileUncommented(filename):
    with open(filename, "r+") as fil:
        content = fil.read()
        list = content.split('\n')
        list = [InputCommenterUncomment(it) for it in list]
        content = "\n".join(list)
    with open(filename, "w") as fil:
        fil.write(content)

def AppendNewLecture(lectures,lectureNumber):
    with open('c/_lectures.json', "w+") as f:
        f.write(json.dumps(lectures))

    f = open("c\\master.tex", "r")
    contents = f.readlines()
    f.close()

    contents.insert(len(contents) - 1, " \input{l" + str(lectureNumber) + ".tex}\n")

    f = open(r"c\\master.tex", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
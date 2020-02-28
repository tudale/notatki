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

# odpowiada za dodanie nowego wykładu do plików
def AppendNewLecture(lectures,lectureNumber,current_course):
    with open("lic-4/" + current_course + '/l' + str(len(lectures) ) + '.tex', "w+") as f: # tworzy nowy plik tex
        f.write("")

    with open("lic-4/" + current_course + '/_lectures.json', "w+") as f: # dodaje plik to json
        f.write(json.dumps(lectures))

    f = open("lic-4/" + current_course + "/master.tex", "r") # wczytuje zawartość
    contents = f.readlines()
    f.close()

    contents.insert(len(contents) - 1, " \input{l" + str(lectureNumber) + ".tex}\n") # dorzuca linijkę łączącą nowoutworzony plik

    f = open("lic-4/" + current_course + "/master.tex", "w") # zapisuje nową zawartość pliku
    contents = "".join(contents)
    f.write(contents)
    f.close()

# tworzy folder dla nowego kursu, folder - nazwa folderu do utworzenia
def CreateCourseFolder(folder):
    os.system("cmd /c mkdir lic-4\\" + folder)
    with open("lic-4/" + current_course + '/master.tex', "w+") as f:
        f.write(
            "\\documentclass[12pt]{article}\n\\input{../preamble.tex}\n\\input{coursepreamble.tex}\n\\begin{document}\n\n\\end{document}")
    with open("lic-4/" + current_course + '/coursepreamble.tex', "w+") as f:
        f.write("\\title{" + name + "}\n")
    with open("lic-4/" + current_course + '/_name', "w+") as f:
        f.write(folder)
    with open("lic-4/" + current_course + '/_lectures.json', "w+") as f:
        f.write("{}")
       
# zwraca listę, zawierającą kolejno mapowania folder->nazwa i id->folder dla kursów
def GetCoursesMapping():
    with open('lic-4/courses.json') as f:
        courses = json.loads(f.read())
    iter = 0
    courses_i = dict()
    for i in courses:
        iter = iter + 1
        courses_i[str(iter)] = i
    return [courses, courses_i]
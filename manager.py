#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import subprocess
#import kivy.app

def InputCommenterLastTwo(i, n):
    if '{l' in i:
        if ('l' + str(n + 1) + '.' not in i) and ('l' + str(n) + '.' not in i) and ('l' + str(n - 1)+ '.' not in i):
            return "%" + i[1:]
        else:
            return ' ' + i[1:]
    else:
        return i

def InputCommenterUncomment(i):
    if '{l' in i:
        return ' ' + i[1:]

with open('c/_name', "r+") as f:
    with open('lic-4/courses.json') as g:
        courses = json.loads(g.read())
        print("### Aktywny kurs: " + courses[f.read()])
print("1. Pracuj nad kursem")
print("2. Zmień aktywny kurs")
choice = input(": ")

if choice == '1':  # Pracuj nad kursem
    with open('c/_lectures.json') as g:
        lectures = json.loads(g.read())
        print("[0] Plik główny", sep='')
    for i in lectures:
        print(" ", i, ") " + lectures[i], sep='')
    print("[", len(lectures) + 1, "] Nowa notatka z wykładu", sep='')
    choice2 = input(": ")

    print(len(lectures) + 1)
    if choice2== "0":
        with open("c/master.tex", "r+") as fil:
            content = fil.read()
            list = content.split('\n')
            list = [InputCommenterUncomment(it, len(lectures)) for it in list]
            content = "\n".join(list)
        with open("c/master.tex", "w") as fil:
            fil.write(content)
        with open("c/master.tex", "r+") as fil:
            name = fil.read()
            subprocess.Popen('start vim c\\master.tex', shell=True)
            os.system("cmd /c copy c\\master.pdf __out\\"+name+".pdf")
            subprocess.Popen("start SumatraPDF __out\\"+name+".pdf", shell=True)

    elif choice2 == str(len(lectures) + 1):  # nowa notatka
        name = input("Nazwa nowego wykładu: ")
        lectures[len(lectures) + 1] = name
        with open('c/_lectures.json', "w+") as f:
            f.write(json.dumps(lectures))
        f = open("c\\master.tex", "r")
        contents = f.readlines()
        f.close()
        contents.insert(len(contents) - 1, " \input{l" + str(len(lectures) ) + ".tex}\n")
        f = open(r"c\\master.tex", "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()

        with open("c/master.tex", "r+") as fil:
            content = fil.read()
            list = content.split('\n')
            list=[InputCommenterLastTwo(it,len(lectures)) for it in list]
            content = "\n".join(list)
        with open("c/master.tex", "w") as fil:
            fil.write(content)

        with open('c/l' + str(len(lectures) ) + '.tex', "w+") as f:
            f.write("")
            print("vim " + 'c\\l' + str(len(lectures) ) + '.tex')
            subprocess.Popen('start vim c\\l' + str(len(lectures) ) + '.tex', shell=True)
            subprocess.Popen('start SumatraPDF c\\master.pdf', shell=True)
            subprocess.call('cmdow \"C:\WINDOWS\system32\cmd.exe - vim   c\\l' + str(
                len(lectures) ) + '.tex\" /mov -7 0 /siz 960 1047 /ren vim', shell=True)
            subprocess.call('cmdow \"master.pdf - SumatraPDF\" /mov 939 0 /siz 988 1047 /ren sumatra /res', shell=True)


    else: #coś innego niż nowa notatka
        print(lectures[choice2])
        with open("c/master.tex", "r+") as fil:
            content = fil.read()
            list = content.split('\n')
            list = [InputCommenterLastTwo(it, int(choice2)) for it in list]
            content = "\n".join(list)
            print(content)
        with open("c/master.tex", "w") as fil:
            fil.write(content)
        print("vim " + 'c\\l' + str(choice2) + '.tex')
        subprocess.Popen('start vim c\\l' + str(choice2) + '.tex', shell=True)
        subprocess.Popen('start SumatraPDF c\\master.pdf', shell=True)
        subprocess.call('cmdow \"C:\WINDOWS\system32\cmd.exe - vim   c\\l' + str(choice2) + '.tex\" /mov -7 0 /siz 960 1047 /ren vim', shell=True)
        subprocess.call('cmdow \"master.pdf - SumatraPDF\" /mov 939 0 /siz 988 1047 /ren sumatra /res', shell=True)


if choice == '2':  # Zmień aktywny kurs
    with open('lic-4/courses.json') as f:
        courses = json.loads(f.read())
        print(courses)
        iter = 0
        courses_i = dict()
        for i in courses:
            iter = iter + 1
            print(" ", iter, ") " + courses[i], sep='')
            courses_i[str(iter)] = i
        print("[", iter + 1, "] Nowy kurs", sep='')
        print(courses_i)
    choice = input("Wybieram kurs: ")
    if choice not in courses_i:
        name = input("Nazwa nowego kursu: ")
        folder = input("Nazwa folderu: ")
        if folder not in courses:
            courses[folder] = name
            with open('lic-4/courses.json', "w+") as f:
                f.write(json.dumps(courses))
            print("cmd /c mkdir lic-4/" + folder)
            os.system("cmd /c mkdir lic-4\\" + folder)
            os.system("cmd /c rmdir c")
            os.system("cmd /c mklink /j c \"lic-4\\" + folder + "\"")
            with open('c/master.tex', "w+") as f:
                f.write(
                    "\\documentclass[12pt]{article}\n\\input{../preamble.tex}\n\\input{coursepreamble.tex}\n\\begin{document}\n\n\\end{document}")
            with open('c/coursepreamble.tex', "w+") as f:
                f.write("\\title{" + name + "}\n")
            with open('c/___' + folder, "w+") as f:
                f.write("")
            with open('c/_name', "w+") as f:
                f.write(folder)
            with open('c/_lectures.json', "w+") as f:
                f.write("{}")
        else:
            print("Kurs już istnieje")
    else:
        os.system("cmd /c rmdir c")
        os.system("cmd /c mklink /j c \"lic-4\\" + courses_i[choice] + "\"")


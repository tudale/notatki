#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from processes import ProcessManager
import sys
import json
import os
import subprocess
import utilities
#import kivy.app

with open('lic-4/courses.json') as g:
    courses = json.loads(g.read())
with open('c/_name', "r+") as f:
    print("### Aktywny kurs: " + courses[f.read()])

print("1. Pracuj nad kursem")
print("2. Zmień aktywny kurs")
choice = input(": ")

procManager = ProcessManager()


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
        utilities.RewriteFileUncommented("c/master.tex")
        with open("c/_name", "r+") as fil:
            name = fil.read()
            os.system("cmd /c copy c\\master.pdf __out\\"+name+".pdf")
            procManager.OpenMasterFile(name)

    elif choice2 == str(len(lectures) + 1):  # nowa notatka
        name = input("Nazwa nowego wykładu: ")
        lectures[len(lectures) + 1] = name
        utilities.AppendNewLecture(lectures, len(lectures))
        utilities.RewriteFileUncommented("c/master.tex")
        procManager.OpenLectureFile(len(lectures))

    else: #coś innego niż nowa notatka
        utilities.RewriteFileUncommented("c/master.tex")
        procManager.OpenLectureFile(choice2)

if choice == '2':  # Zmień aktywny kurs
     # courses_i mapuje ID -> nazwa robocza (folderu) kursu, courses mapuje folder -> nazwa
    [courses, courses_i] = utilities.GetCoursesMapping()
    for iter, name in courses_i.items():
        print(" ", iter, ") " + courses[name], sep='')
    print("[", str(len(courses_i) + 1), "] Nowy kurs", sep='')
    # print(courses_i)
    choice = input("Wybieram kurs: ")
    if choice not in courses_i:
        name = input("Nazwa nowego kursu: ")
        folder = input("Nazwa folderu: ")
        if folder not in courses:
            courses[folder] = name
            with open('lic-4/courses.json', "w+") as f:
                f.write(json.dumps(courses))
            utilities.CreateCourseFolder(folder)
        else:
            print("Kurs już istnieje")
    else:
        os.system("cmd /c rmdir c")
        os.system("cmd /c mklink /j c \"lic-4\\" + courses_i[choice] + "\"")
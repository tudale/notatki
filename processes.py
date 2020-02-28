import os
import subprocess

class ProcessManager:
    def __init__(self,current_course):
        self.current_course = current_course

    def OpenMasterFile(self):
            vim = subprocess.Popen('start vim lic-4/' + self.current_course + '/master.tex', shell=True)
            pdfViewer = subprocess.Popen("start SumatraPDF PDF\\"+self.current_course+".pdf", shell=True)

    def OpenLectureFile(self,number):
            vim = subprocess.Popen('start vim lic-4/' + self.current_course + '/l' + str(number ) + '.tex', shell=True)
            pdfViewer = subprocess.Popen('start SumatraPDF lic-4/' + self.current_course + '/master.pdf', shell=True)
            subprocess.call('cmdow \"C:\WINDOWS\system32\cmd.exe - vim   lic-4/' + self.current_course + '/l' + str(
                number ) + '.tex\" /mov -7 0 /siz 960 1047 /ren vim', shell=True)
            subprocess.call('cmdow \"master.pdf - SumatraPDF\" /mov 939 0 /siz 988 1047 /ren sumatra /res', shell=True)
import os
import subprocess

class ProcessManager:
    def OpenMasterFile(self, course):
            vim = subprocess.Popen('start vim c\\master.tex', shell=True)
            pdfViewer = subprocess.Popen("start SumatraPDF __out\\"+course+".pdf", shell=True)

    def OpenLectureFile(self,number):
            vim = subprocess.Popen('start vim c\\l' + str(number ) + '.tex', shell=True)
            pdfViewer = subprocess.Popen('start SumatraPDF c\\master.pdf', shell=True)
            subprocess.call('cmdow \"C:\WINDOWS\system32\cmd.exe - vim   c\\l' + str(
                number ) + '.tex\" /mov -7 0 /siz 960 1047 /ren vim', shell=True)
            subprocess.call('cmdow \"master.pdf - SumatraPDF\" /mov 939 0 /siz 988 1047 /ren sumatra /res', shell=True)
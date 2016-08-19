# May need to install 7zip
# sudo apt-get install p7zip-full
# sudo apt-get install unrar
import glob
import os.path
import zipfile
import subprocess
import sys

scanDirs = ["/home/pi/RetroPie/roms/psx","/home/pi/RetroPie/roms/n64","/home/pi/RetroPie/roms/dreamcast","/home/pi/RetroPie/roms/snes"]
types = ('*.zip', '*.7z', '*.rar') # the tuple of file types

subdir = True
trues = ("Y", "Yes", "True", "T", True)
if (sys.version_info > (3, 0)):
    #py3 code
    tsubdir = input("Place in sub directory? ["+str(subdir)+"]:").strip().title() or subdir
    subdir = tsubdir in trues 
else:
    #py2 code
    tsubdir = raw_input("Place in sub directory? ["+str(subdir)+"]:").strip().title() or subdir
    subdir = tsubdir in trues 

for dir in scanDirs:
    print("Scanning:" + dir)
    for type in types:
      files = glob.glob(dir+ "/" + type)
      print(dir+ "/" + type)
      for file in files:
        fullFileName = os.path.basename(file)
        fileName = os.path.splitext(fullFileName)[0]
        ext = os.path.splitext(fullFileName)[1]
        dir = os.path.dirname(file)
        os.chdir(dir)
		
        print("Starting: " + fileName)
		
        if ext == ".7z":
          command = ""
          if subdir:
            command = r'7za x '+file+' -o'+dir+"/"+fileName
          else:
            command = r'7za x '+file+' -o*'
          
          print(command)
          subprocess.call(command, shell=True)
        elif ext == ".zip":
          zip_ref = zipfile.ZipFile(file, 'r')
          if subdir:
            zip_ref.extractall(dir + "/" + fileName)
          else:
            zip_ref.extractall()
          zip_ref.close()
		elif ext == ".rar":
		  command = ""
		  command = "unrar e file.rar"

        #os.remove(file)

        print("Done: " + fileName)

# May need to install 7zip
# sudo apt-get install p7zip-full
import glob
import os.path
import zipfile
import subprocess

scanDirs = ["/home/pi/RetroPie/roms/psx","/home/pi/RetroPie/roms/n64","/home/pi/RetroPie/roms/dreamcast","/home/pi/RetroPie/roms/snes"]
types = ('*.zip', '*.7z') # the tuple of file types

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

        if ext == ".7z":
          command = r'7za x '+file+' -o'+dir+"/"+fileName
          #command = r'7za x '+file+' -o*'
          print(command)
          subprocess.call(command, shell=True)
        elif ext == ".zip":
          zip_ref = zipfile.ZipFile(file, 'r')
          zip_ref.extractall(dir + "/" + fileName)
          zip_ref.close()

        os.remove(file)

        print("Done: " + fileName)

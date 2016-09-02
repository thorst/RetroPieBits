import xml.etree.ElementTree as ET
import os.path
import copy
import xml.etree.ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

file = '/opt/retropie/configs/all/emulationstation/gamelists/psx/gamelist.xml'
tree = ET.parse(file)
root = tree.getroot()

titles = {}
additions = {}
for game in root:
  path = game.find('path').text
  name = game.find('name').text
  print name, path
  titles[path] =game
  #break

#print titles
for path,node in titles.iteritems():
  print path
  dir, filez = os.path.split(path)
  print dir
  if dir not in titles and dir not in additions:
    c =  copy.deepcopy(node)
    c.find('path').text = dir
    root.append(c)
    additions[dir] = c

#titles.update(additions)
#print ET.tostring(tree, 'utf-8', method="xml")

tree.write(file+".2.xml")
#with open(file,'w') as f:
#  print ET.tostring(tree, pretty_print=True)
#    f.write(ET.tostring(tree))
    
#
#e = xml.etree.ElementTree.parse().getroot()

#for atype in e.findall('game'):
#    print(atype.get('foobar'))

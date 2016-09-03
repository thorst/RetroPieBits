# TODOs
# -Sort xml files by rom name
# -Hoist multiple directories up
# -Backup input and save as output
# -Echo out how many paths there are

import xml.etree.ElementTree as ET
import os.path
import copy
import xml.etree.ElementTree
#from xml.etree.ElementTree import Element, SubElement, Comment, tostring

# Define file to hoist
file = '/opt/retropie/configs/all/emulationstation/gamelists/psx/gamelist.xml'

# Parse file
tree = ET.parse(file)
root = tree.getroot()

# Init dicts
titles = {}
additions = {}

# For each game in file
for game in root:
  
  # Get the system path and the name of the rom
  path = game.find('path').text
  name = game.find('name').text
  
  # Print rom
  #print name, path
  
  # Add the path to a dictionary with the value of the xml node
  titles[path] = game
  
  # If you only want to test with the first game
  #break

# We have a dictionary of all the game paths
# Now need to determine if there are any gaps
# in the folders that need hoisting

# For each path
for path,node in titles.iteritems():
  #print path
  
  # Get just the path section
  dir, filez = os.path.split(path)
  print dir
  
  # If this new path is not already in the xml and it isnt in
  # the list of ones we will be adding then ...
  if dir not in titles and dir not in additions:
    # Copy the node, but change the path to the dir up
    c =  copy.deepcopy(node)
    c.find('path').text = dir + "/"
    
    # Add to the xml document and to the additions dictionary
    root.append(c)
    additions[dir] = c

# Write out the xml file
tree.write(file+".2.xml")

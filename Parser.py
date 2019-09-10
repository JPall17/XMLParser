#author - Jeremy Pallwitz

import xml.etree.ElementTree as ET
import sys
import urllib.request
import subprocess

#Grab data from live url feed
url = '' #insert url
urllib.request.urlretrieve (url, 'file.xml')

#main
#This method opens the xml file that is being parsed, takes the root and all children and sends them to the parse
#method for further data processing. 'Done' is printed to the console when all the children have been parsed.


def main():

    tree = ET.parse('file.xml')
    root = tree.getroot()
    parse(root)
    #Get all children nodes
    for child in root:
        parse(child)
    print("Done.") #print done to console when data parsing is complete

#parse
#Takes in a tree root node or child node and finds all values within that child. The data is then
#printed into a csv file named after the root tag.
def parse(root):

    x = "" #string that contains all the header information

    values = [] #array of strings that contain the values from the dataitems of each attribute

    fname = root.tag + '.csv'

    #all atrributes of the root are found
    for child in root:
        temp = child.attrib
        x = ""
        y = ""
        #creating strings to add to the values[] array to be printed to csv file
        for name, value in temp.items():
            if ',' in value: #check if there is a comma in the value, if so the comma is removed
                value = value.replace(',', "")
            if x == "": #checks if x is empty, either makes name the string x or appends name to x
                x = name
            else:
                x = x + "," + name
            if y == "": #same as check for x.
                y = value
            else:
                y = y + "," + value
        values.append(y) #add each line to values[] array

        #open the csv file and print the parsed data to the file.

        try:
            with open(fname, 'w') as f:
                print(x, file=f)
                for v in values:
                    print(v, file=f)
        except PermissionError: #if the excel files are open, then the data can not be printed as the process is locked
            print("Make sure all excel files are closed before updating.")

main() #run main method to start program




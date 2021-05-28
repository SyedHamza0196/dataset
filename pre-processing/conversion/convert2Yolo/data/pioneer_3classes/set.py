import xml.etree.ElementTree as ET
import os

xmls = os.listdir("./xmls/")

for xml in xmls:
    xmlTree = ET.parse('./xmls/'+xml)
    rootElement = xmlTree.getroot()
    filename, _ = os.path.splitext(xml)
    xmlTree.find('filename').text = str(filename)
    xmlTree.write('./new_xmls/'+xml, encoding='UTF-8', xml_declaration=True)
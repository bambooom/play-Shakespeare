# -*- coding: utf-8 -*-
'''
convert shakespeare xml to dataframe
@author: bambooom
'''

from lxml import objectify
import xml.etree.ElementTree as etree
import lxml.etree
import pandas as pd
import numpy as np
import os

def xml2df():
    file_list = []
    # walk down into folder to get the list of all xml files
    for dirpath, dirs, files in os.walk('text_Data_xml'):
        file_list.append(files)

    file_list = np.ravel(file_list) # flatten

    speechlines = []
    plays_name = []
    genre_list = []
    for file_name in file_list: # for each xml file
        path = 'text_data_xml/%s'% file_name
        tree = etree.parse(path)
        root = tree.getroot()
        xml = objectify.parse(open(path))
        root_xml = xml.getroot()

        # find all lines of speech in each xml file
        speechline_element = root.findall('act/scene/speech/line')
        for i in xrange(len(speechline_element)):
            sp = speechline_element[i].text
            speechlines.append(sp)
            plays_name.append(unicode(root_xml.getchildren()[0].text.encode('utf-8'), "utf-8"))
            genre_list.append(root.attrib['genre'])

    d = {'speech_lines':speechlines, 'plays_name':plays_name, 'genre':genre_list}
    lines_all = pd.DataFrame(d)

    return lines_all

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

    speeches = []
    plays_name = []
    genre_list = []
    speakers = []

    # for each xml file
    for file_name in file_list:
        path = 'text_data_xml/%s'% file_name
        tree = etree.parse(path)
        root = tree.getroot()
        xml = objectify.parse(open(path))
        root_xml = xml.getroot()

        for e in root_xml.getchildren():
            if e.tag == 'act':
                for ee in e.getchildren():
                    if ee.tag == 'scene':
                        for eee in ee.getchildren():
                            if eee.tag == 'speech':
                                name = unicode(root_xml.getchildren()[0].text.encode('utf-8'), "utf-8")
                                gen = root.attrib['genre']

                                speakers.append(str(eee.getchildren()[0]))
                                plays_name.append(name)
                                genre_list.append(gen)
                                for i in eee.getchildren()[1:]:
                                    if i.text is not None:
                                        lines = ''.join(unicode(i.text.encode('utf-8'),'utf-8'))
                                    else:
                                        continue
                                speeches.append(lines)

    d = {'speeches':speeches, 'plays_name':plays_name,
        'genre':genre_list, 'speakers':speakers}
    speech_all = pd.DataFrame(d)

    return speech_all

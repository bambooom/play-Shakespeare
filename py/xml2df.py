# -*- coding: utf-8 -*-
'''
change xml to pandas dataframe
@author: bambooom
'''

from lxml import ojectify

path = "../text_data_xml/alls_well_that_ends_well.xml"
xml = objectify.parse(open(path))
root = xml.getroot()

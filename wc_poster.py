# -*- coding: utf-8 -*-
'''
word cloud generate for shakespeare
@author: bambooom
'''

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)
# Read the whole text.
text = open(path.join(d, 'text.txt')).read()

# read the mask / color image
# taken from http://lukaskaraba.deviantart.com/art/Shakespeare-minimalist-poster-2-462903294
shakespeare_coloring = imread(path.join(d, "mask.jpg"))

wc = WordCloud(background_color="white", max_words=2000, mask=shakespeare_coloring,
               stopwords=STOPWORDS.add("said"),
               max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

image_colors = ImageColorGenerator(shakespeare_coloring)

#plt.imshow(wc)
#plt.axis("off")
#plt.figure()

# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
#fig, ax = plt.subplots(1, 1, figsize=(8, 12))
plt.figure(figsize = (6,10))
plt.imshow(wc.recolor(color_func=image_colors),aspect='equal')
plt.axis("off")
#plt.figure()
#plt.imshow(shakespeare_coloring, cmap=plt.cm.gray)
#plt.axis("off")
plt.show()

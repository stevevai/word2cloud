# -*- coding: utf-8 -*-

"""
create wordcloud with chinese
=======================

Wordcloud is a very good tools, but if you want to create
Chinese wordcloud only wordcloud is not enough. The file
shows how to use wordcloud with Chinese. First, you need a
Chinese word segmentation library pyhanlp, pyhanlp is One of 
the most powerful natural language processing libraries in Chinese
today, and it's extremely easy to use.You can use 'PIP install pyhanlp'. 
To install it. 

Its level of identity of named entity,word segmentation was better than jieba,
and has more ways to do it

"""
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from pyhanlp import *
import codecs


# d = path.dirname(__file__)
d = "./source/word_cloud-master/examples"

stopwords_path = d + '/wc_cn/stopwords_cn_en.txt'
# Chinese fonts must be set
font_path = d + '/fonts/SourceHanSerif/SourceHanSerifK-Light.otf'

# the path to save worldcloud
imgname1 = d + '/wc_cn/LuXun.jpg'
imgname2 = d + '/wc_cn/LuXun_colored.jpg'
# read the mask / color image taken from
back_coloring = imread(d + '/wc_cn/LuXun_color.jpg')

# Read the whole text.
text = codecs.open(d + '/wc_cn/CalltoArms.txt',"r","utf-8").read()

# 
userdict_list = ['孔乙己']


# The function for processing text with HaanLP
def pyhanlp_processing_txt(text,isUseStopwordsOfHanLP = True):
    CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    for word in userdict_list:
        CustomDictionary.add(word)

    mywordlist = []    
    HanLP.Config.ShowTermNature = False
    CRFnewSegment = HanLP.newSegment("viterbi")
    
    fianlText = []
    if isUseStopwordsOfHanLP == True:
        CoreStopWordDictionary = JClass("com.hankcs.hanlp.dictionary.stopword.CoreStopWordDictionary")
        text_list = CRFnewSegment.seg(text)
        CoreStopWordDictionary.apply(text_list)
        fianlText = [i.word for i in text_list]
    else:
        fianlText = list(CRFnewSegment.segment(text))
    liststr = "/ ".join(fianlText)

    with open(stopwords_path, encoding='utf-8') as f_stop:
        f_stop_text = f_stop.read()
        f_stop_seg_list = f_stop_text.splitlines()

    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ' '.join(mywordlist)


wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=back_coloring,
               max_font_size=100, random_state=42, width=1000, height=860, margin=2,)


pyhanlp_processing_txt = pyhanlp_processing_txt(text,isUseStopwordsOfHanLP = True)

wc.generate(pyhanlp_processing_txt)

# create coloring from image
image_colors_default = ImageColorGenerator(back_coloring)

plt.figure()
# recolor wordcloud and show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# save wordcloud
wc.to_file(imgname1)

# create coloring from image
image_colors_byImg = ImageColorGenerator(back_coloring)

# show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(back_coloring, interpolation="bilinear")
plt.axis("off")
plt.show()

# save wordcloud
wc.to_file(imgname2)


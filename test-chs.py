# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open('百度.txt',encoding='utf-8').read()
#text = """
#腾讯科技讯（刘亚澜）10月22日消息，前优酷土豆技术副总裁黄冬已于日前正式加盟芒果TV，出任CTO一职。
#资料显示，黄冬历任土豆网技术副总裁、优酷土豆集团产品技术副总裁等职务，曾主持设计、运营过优酷土豆多个大型高容量产品和系统。
#此番加入芒果TV或与芒果TV计划自主研发智能硬件OS有关。
#今年3月，芒果TV对外公布其全平台日均独立用户突破3000万，日均VV突破1亿，但挥之不去的是业内对其技术能力能否匹配发展速度的质疑，亟须招揽技术人才提升整体技术能力。
#芒果TV是国内互联网电视七大牌照方之一，之前采取的是“封闭模式”与硬件厂商预装合作，而现在是“开放下载”+“厂商预装”。
#黄冬在加盟土豆网之前曾是国内FreeBSD（开源OS）社区发起者之一，是研究并使用开源OS的技术专家，离开优酷土豆集团后其加盟果壳电子，涉足智能硬件行业，将开源OS与硬件结合，创办魔豆智能路由器。
#未来黄冬可能会整合其在开源OS、智能硬件上的经验，结合芒果的牌照及资源优势，在智能硬件或OS领域发力。
#公开信息显示，芒果TV在今年6月对外宣布完成A轮5亿人民币融资，估值70亿。
#据芒果TV控股方芒果传媒的消息人士透露，芒果TV即将启动B轮融资。
#"""
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(background_color="white",width=1000,height=860, font_path="C:\\Windows\\Fonts\\STFANGSO.ttf").generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
my_wordcloud.to_file("chs.png")
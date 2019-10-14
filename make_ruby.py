# -*- coding: utf-8 -*-

'''
名字太长了，我要用代码来实现ruby标签

Author : 高斯羽 博士 (Dr. Gāo, Sī Yǔ)

Change Log
-------------

* **Notable Changes :
   + Version : 1.0.0
      - First version
'''

__author__ = u'高斯羽 博士 (Dr. Gāo, Sī Yǔ)'
__version__ = '1.0.0'
__date__ = '2019-10-14'

str_wanghaoran_han = u'王格里拉德玛西亚卜多比鲁翁浩淏殇觞笺酅彟豳夔櫼爨纛褎然维萨尔卡拉奥克苏瓦西拉松'

str_wanghaoran_pyin = (
    u'wáng gé lǐ lā dé mǎ xī yǎ bo duō bǐ lǔ wēng'
    + u' hào hào shāng shāng jiān  xī yuē bīn kuí ji ān cuàn dào xiù'
    + u' rán wéi sà ěr kǎ lā ào kè sū wǎ xī lā sōng')

list_wanghaoran_han = list(str_wanghaoran_han)
list_wanghaoran_pyin = str_wanghaoran_pyin.split()

str_tag = ''

for i, j in zip(list_wanghaoran_han, list_wanghaoran_pyin):

    str_tag = (str_tag
               + r'<ruby>'
               + i
               + r'<rp>' + r'(' + r'</rp>'
               + r'<rt>' + j + r'</rt>'
               + r'<rp>' + r'(' + r'</rp>'
               + r'</ruby>')

print(str_tag)

str_queen_han = u'卡拉茨瓦般得贝荻桑哈玛丽亚'
str_queen_pyin = u'kǎ lā cí wǎ bān dé bèi dí sāng hā mǎ lì yà'

list_queen_han = list(str_queen_han)
list_queen_pyin = str_queen_pyin.split()

print('\n\n')

str_tag = ''

for i, j in zip(list_queen_han, list_queen_pyin):

    str_tag = (str_tag
               + r'<ruby>'
               + i
               + r'<rp>' + r'(' + r'</rp>'
               + r'<rt>' + j + r'</rt>'
               + r'<rp>' + r'(' + r'</rp>'
               + r'</ruby>')

print(str_tag)

str_longaotian_han = u'科龙巴卡傲骨布达拉里天气崩'
str_longaotian_pyin = u'kē lóng bā kǎ ào gǔ bù dá lā lǐ tiān qì bēng'

list_longaotian_han = list(str_longaotian_han)
list_longaotian_pyin = str_longaotian_pyin.split()

print('\n\n')

str_tag = ''

for i, j in zip(list_longaotian_han, list_longaotian_pyin):

    str_tag = (str_tag
               + r'<ruby>'
               + i
               + r'<rp>' + r'(' + r'</rp>'
               + r'<rt>' + j + r'</rt>'
               + r'<rp>' + r'(' + r'</rp>'
               + r'</ruby>')

print(str_tag)

str_xiaodi_han = u'达拉肯塔潘特库卡考提谢利翁'
str_xiaodi_pyin = u'dá lā kěn tǎ pān tè kù kǎ kǎo tí xiè lì wēng'

list_xiaodi_han = list(str_xiaodi_han)
list_xiaodi_pyin = str_xiaodi_pyin.split()

print('\n\n')

str_tag = ''

for i, j in zip(list_xiaodi_han, list_xiaodi_pyin):

    str_tag = (str_tag
               + r'<ruby>'
               + i
               + r'<rp>' + r'(' + r'</rp>'
               + r'<rt>' + j + r'</rt>'
               + r'<rp>' + r'(' + r'</rp>'
               + r'</ruby>')

print(str_tag)

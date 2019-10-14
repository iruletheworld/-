# -*- coding: utf-8 -*-

'''
用Graphviz来整理一下达拉崩吧的人物关系。

Change Log
----------------------

* **Notable changes:**
   + Version : 1.0.0
      - First version

'''

from graphviz import Digraph

__author__  = u'高斯羽 博士 (Dr. Gāo, Sī Yǔ)'
__version__ = '1.0.0'
__date__    = '2019-10-14'

int_txt_len = 16

dict_font = {'fontname': 'consolas', 'fontsize': '10'}

relations = Digraph('daLaBengBa',
                    filename='daLaBengBa.gv',
                    format='svg',
                    graph_attr=dict_font,
                    node_attr=dict_font,
                    edge_attr=dict_font)

relations.attr(edge='normal')

str_king     = u'国王（國王）, 100%人类'
str_princess = u'公主（公主），50%人类 + 50%龙'
str_dragon   = u'龙（龍），100%龙'
str_hero     = u'勇者（勇者），50%人类 + 50%龙'
str_son      = u'王浩然（王浩然），25%人类 + 75%龙'
str_queen    = u'王后（王后）, 100%人类'
str_lat      = u'龙傲天（龍傲天），12.5%人类 + 87.5%龙'
str_shegon   = u'母龙（母龍），100%龙'
str_xiaodi   = u'小弟（小弟）, 100%人类'
str_break    = u'break, 100%人类'

dict_chars = {
    str_king: [
        '米现唐元保兹火勺吐假绍兵王',
        r'(mǐ xiàn táng yuán bǎo zī huǒ sháo tǔ jiǎ shào bīng wáng)',
        '(米現唐元保茲火勺吐假紹兵王)'
    ],
    str_princess: [
        '米娅莫拉苏娜丹妮谢莉红',
        r'(mǐ yà mò lā sū nà dān nī xiè lì hóng)',
        '(米婭莫拉蘇娜丹妮謝莉紅)'
    ],
    str_dragon: [
        '昆图库塔卡提考特苏瓦西拉松',
        r'(kūn tú kù tǎ kǎ tí kǎo tè sū wǎ xī lā sōng)',
        '(昆圖庫塔卡提考特蘇瓦西拉松)'
    ],
    str_hero: [
        '达拉崩吧/巴斑得贝迪卜多比鲁翁',
        r'(dá lā bēng ba/bā bān dé bèi dí bo duō bǐ lǔ wēng)',
        '(達拉崩吧/巴斑得貝迪卜多比魯翁)'
    ],
    str_son: [
        '王格里拉德玛西亚卜多比鲁翁\n浩淏殇觞笺酅彟豳夔櫼爨纛褎\n然维萨尔卡拉奥克苏瓦西拉松',
        ('(wáng gé lǐ lā dé mǎ xī yǎ bo duō bǐ lǔ wēng\n hào hào shāng shāng jiān'
         + ' xī yuē bīn kuí ji ān cuàn dào xiù\n rán wéi sà ěr kǎ lā ào kè sū wǎ xī lā sōng)'),
        '(王格里拉德瑪西亞卜多比魯翁\n浩淏殤觴牋酅彟豳夔櫼爨纛褎\n然維薩爾卡拉奧克蘇瓦西拉松)'
    ],
    str_queen: [
        '卡拉茨瓦般得贝荻桑哈玛丽亚',
        'kǎ lā cí wǎ bān dé bèi dí sāng hā mǎ lì yà',
        '(卡拉茨瓦般得貝荻桑哈瑪麗亞)'
    ],
    str_lat: [
        '科龙巴卡傲骨布达拉里天气崩',
        'kē lóng bā kǎ ào gǔ bù dá lā lǐ tiān qì bēng',
        '(科龍巴卡傲骨布達拉里天氣崩)'
    ],
    str_shegon: ['希拉', 'xīlā', '(希拉)'],
    str_xiaodi: [
        '达拉肯塔潘特库卡考提谢利翁',
        'dá lā kěn tǎ pān tè kù kǎ kǎo tí xiè lì wēng',
        '(達拉肯塔潘特庫卡考提謝利翁)'
    ],
    str_break: ['导演']
}

for i in dict_chars:

    temp = dict_chars[i]

    relations.node(i, shape='box', style='rounded', label=(i+'\n'*2+'\n'.join(temp)+'\n'*2))

relations.edge(str_king, str_princess, headlabel=' 亲父\n\n')
relations.edge(str_king, str_hero, label=' 招募')
relations.edge(str_king, str_hero, label=' 岳父，\n补血')
relations.edge(str_king, str_queen, dir='both', label=' 夫妻')
relations.edge(str_king, str_shegon, label=' 春宵')

relations.edge(str_dragon, str_princess, label=' 掳走')
relations.edge(str_dragon, str_hero, label=' 诈败')
relations.edge(str_dragon, str_son, label=' 亲父')
relations.edge(str_dragon, str_shegon, dir='both', label=' 夫妻')
relations.edge(str_dragon, str_queen, label='\n\n 抓走三天')
relations.edge(str_dragon, str_hero, label=' 亲父')
relations.edge(str_dragon, str_hero, label=' 杀死\n（王浩然夺还战）')

relations.edge(str_hero, str_king, label=' 女婿')
relations.edge(str_hero, str_dragon, label=' 诈胜')
relations.edge(str_hero, str_son, label=' 养父')
relations.edge(str_hero, str_princess, dir='both', label=' 夫妻')
relations.edge(str_hero, str_xiaodi, label=' 招募')
relations.edge(str_hero, str_dragon, label=' 战败\n（王浩然夺还战）')

relations.edge(str_princess, str_dragon, label=' 严管')
relations.edge(str_princess, str_son, headlabel=' 亲母  ')

relations.edge(str_son, str_shegon, label=' 爱上')
relations.edge(str_son, str_lat, label=' 亲父')

relations.edge(str_queen, str_hero, headlabel=' 亲母')
relations.edge(str_queen, str_princess, headlabel='   养母\n')

relations.edge(str_shegon, str_princess, headlabel=' 亲母  \n')
relations.edge(str_shegon, str_hero, headlabel='\n\n\n 收买          ')
relations.edge(str_shegon, str_lat, headlabel=' 亲母  \n\n')

relations.edge(str_xiaodi, str_hero, label=' 跟随')
relations.edge(str_xiaodi, str_dragon, xlabel=' \n杀死\n（王浩然夺还战）')
relations.edge(str_xiaodi, str_hero, label=' 埋葬\n（王浩然夺还战）')

relations.edge(str_lat, str_break, label=' 写剧本')

# 绿的关系
relations.edge(str_king, str_dragon, color='green', label=' 和母龙生\n下了公主', fontcolor='green')
relations.edge(str_dragon, str_king, color='green', label=' 和王后生\n下了勇者', fontcolor='green')
relations.edge(str_dragon, str_hero, color='green', label=' 和公主生下\n了王浩然', fontcolor='green')
relations.edge(str_son, str_dragon, color='green', label='\n 和母龙生下\n了龙傲天', fontcolor='green')

# 红的关系
relations.edge(str_son, str_hero, dir='both', label=' 同父异母\n的兄弟', color='red', fontcolor='red')
relations.edge(str_shegon, str_son, dir='both', label=' 祖孙关系', color='red', fontcolor='red')

relations.view()

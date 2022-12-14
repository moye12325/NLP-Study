p_sample1 = "酒店设施非常不错"
p_sample2 = "这家价格很便宜"
n_sample1 = "拖鞋都发霉了, 太差了"
n_sample2 = "电视不好用, 没有看到足球"

from googletrans import Translator

# 实例化翻译对象
translator = Translator()

# 进行第一次批量翻译
translations = translator.translate([p_sample1, p_sample2, n_sample1, n_sample2], dest='ko')

# 获得翻译后的结果
ko_res = list(map(lambda x: x.text, translations))
print("中间的翻译结果：", ko_res)

# 翻译回中文
translations = translator.translate(ko_res, dest='zh_cn')
cn_res = list(map(lambda x: x.text, translations))
print("回译得到后的增强数据：", cn_res)

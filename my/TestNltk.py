#coding:utf-8
import nltk
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



raw=open('/Users/fanfengshi/data/comment.10w.data').read()
text = nltk.text.Text(jieba.lcut(raw))


# Text(words)	对象构造
# concordance(word, width=79, lines=25)	显示word出现的上下文
# common_contexts(words)	显示words出现的相同模式
# similar(word)	显示word的相似词
# collocations(num=20, window_size=2)	显示最常见的二词搭配
# count(word)	word出现的词数
# dispersion_plot(words)	绘制words中文档中出现的位置图
# vocab()	返回文章去重的词典

# print(text.concordance(u'物流'))
# print(text.common_contexts(u'物流'))
# print(text.similar(u'物流'))
# print(text.collocations())
# print(text.count(u'物流'))
# print(text.dispersion_plot([u'物流',u'质量']))
# print(text.vocab())




# nltk.text.TextCollection([text1,text2,])	对象构造
# idf(term)	计算词term在语料库中的逆文档频率，即log总文章数文中出现term的文章数
# tf(term,text)	统计term在text中的词频
# tf_idf(term,text)	计算term在句子中的tf_idf,即tf*idf

text_collection = nltk.text.TextCollection(jieba.lcut(raw))
print(text_collection.idf(u'物流'))
print(text_collection.tf_idf(u'物流', u''))

print('finish!!!!')
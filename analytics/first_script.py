from math import exp, log, sqrt
import re

# 计算字符串中模式出现的次数
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
# re.I：指定模式不区分大小写；r:确保python不处理字符串中的转义字符
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output #38:{0:d}".format(count))

# 在字符串中每次找到模式时将其打印出来
# ?P<name>: 使得后面程序可以通过‘name’引用匹配到的字符串
pattern2 = re.compile(r"(?P<match_word>The)", re.I)
print("Output #39:")
for word in string_list:
    if pattern2.search(word):
        # 正则表达式中，group()用来提出分组截获的字符串
        print("{0:s}".format(pattern2.search(word).group('match_word')))

# 使用字母“a”替换字符串中的单词“the”
string_to_find = r"The"
pattern3 = re.compile(string_to_find, re.I)
# re.sub函数：以不区分大小写的方式在变量string 中寻找模式，然后将发现的每个模式替换成字母a
print("Output #40:{:s}".format(pattern3.sub("a", string)))

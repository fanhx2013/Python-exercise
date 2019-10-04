#先创建一个文本文件，另存为uft-8编码格式，内容为纯英文，显示如下：
#This is a textfile to excercise.
#GBK to Unicode.

#coding = UFT-8
#import string
fp1 = open('W:\\fanhx\code\PycharmProjects\Python\GBK_to_unicode.txt','r')
info1 = fp1.read() #已知是GBK编码，解码成unicode
tmp = info1.decode('GBK')
print(tmp)

# 上面的代码在python3.x环境下运行后，会出现错误提示：
# AttributeError: 'str' object has no attribute 'decode'
# 这是因为python3.x中只有unicode str，所以把decode方法去掉了；
# 字符串要先encode手动指定其为某一编码的字节码之后，才能decode解码。
# 所以解决方法是中间加上.encode('utf-8')即可，代码如下：

fp1 = open('W:\\fanhx\code\PycharmProjects\Python\GBK_to_unicode.txt','r')
info1 = fp1.read() #已知是GBK编码，解码成unicode
tmp = info1.encode('utf-8').decode('GBK')
print(tmp)

#上述代码运行结果为：
#This is a textfile to excercise.
#GBK to Unicode.

#--------------------------------------------------------------------------------------------
#但是如果将这个文本文件的内容改一下，加一行中文，内容如下(仍另存为utf-8编码格式)：
#This is a textfile to excercise.
#GBK to Unicode.
#你好
#则运行出错，错误提示是：
#UnicodeDecodeError: 'gbk' codec can't decode byte 0xbd in position 57: incomplete multibyte sequence
#这个是字符流的问题，读取文件时，加上encoding = 'utf-8'就可以了，代码如下

fp1 = open('W:\\fanhx\code\PycharmProjects\Python\GBK_to_unicode.txt','r',encoding = 'utf-8')
info1 = fp1.read() #已知是GBK编码，解码成unicode
tmp = info1.encode('utf-8').decode('GBK')
print(tmp)

#但是此时输出的结果仍不对，中文是乱码；
#This is a textfile to excercise.
#GBK to Unicode.
#浣犲ソ
#这是因为info1已经是utf-8，把info1再编码成utf-8，再解码的话也要解码为utf-8，而不能解码为GBK。
#把decode('GBK')改为decode('utf-8')就对了。

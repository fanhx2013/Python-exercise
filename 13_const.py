#常量的类文件代码示例：const.py
# -*- coding: UTF-8 -*-
# Filename: const.py
# 定义一个常量类实现常量的功能
#
# 该类定义了一个方法__setattr()__，和一个异常ConstError, ConstError类继承
# 自类TypeError. 通过调用类自带的字典__dict__, 判断定义的常量是否包含在字典
# 中。如果字典中包含此变量，将抛出异常，否则，给新创建的常量赋值。
# 最后两行代码的作用是把const类注册到sys.modules这个全局字典中。
class _const:
	class ConstError(TypeError):
		pass
	def __setattr__(self, name, value):
		if self.__dict__.has_key(name):   #这里是python2的写法，在python3中已经没有has_key，所以这行在python3中需要改为“if name in self.__dict__:”
			raise self.ConstError, "Can't rebind const (%s)" %name
		self.__dict__[name]=value
import sys
sys.modules[__name__] = _const()

#测试代码示例：
import const
const.magic = 23
print const.magic
const.magic = 33

#运行结果是：
23
Traceback (most recent call last):
  File "W:\fanhx\code\PycharmProjects\Python\const_eg.py", line 5, in <module>
    const.magic = 33
  File "W:\fanhx\code\PycharmProjects\Python\const.py", line 15, in __setattr__
    raise self.ConstError("Can't rebind const (%s)" %name)
const.ConstError: Can't rebind const (magic)
[Finished in 0.1s with exit code 1]

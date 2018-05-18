# Python中list 是一个兼具了list和array的有点的数据结构
# 可以按照下标取值，也可以按照负数下标倒着取值
# 是一个可变的有序列表，
# 可以追加元素，
# 把元素插入到指定的位置，
# 删除list末尾的元素
# 删除指定位置的元素，用pop(i)方法
# 把某个元素替换成别的元素
# list里面的元素的数据类型也可以不同  L = ['Apple', 123, True]
# list元素也可以是另一个list
# list中一个元素也没有，就是一个空的list，它的长度为0
list = ["zjang", "sca", "casc"]
len = len(list)
print(len)
# tuple
# tuple一旦初始化就不能修改，它也没有append()，insert()这样的方法
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# 如果要定义一个空的tuple，可以写成()
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

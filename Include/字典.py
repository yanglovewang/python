# 无论这个表有多大，查找速度都不会变慢
# 多次对一个key放入value，后面的值会把前面的值冲掉
# 如果key不存在，dict就会报错
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
# 要删除一个key，用pop(key)方法
# 增加键值对 d['Adam'] = 67
# 需要牢记的第一条就是dict的key必须是不可变对象。
d = {'zhang':23}
d['wang'] = 23
for name in d:
    print(d.get(name, -1))

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合
s = set([2,6,5,5, 'zhang'])
# add(key)方法可以添加元素到set中
s.add(7)
# 数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样,所以set存的相当于是key是不可变的
#ss = set([[1,2,3], 3])
map = {'q':[1, 2, 3, 4]}
print(map)
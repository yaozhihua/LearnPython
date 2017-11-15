#coding=utf-8
__author__ = 'yaozhihua'

#列表 append()添加元素 insert()插入 ，del删除元素 pop(),remove(）

owner=['zhangsan','lisi','wangwu']
print(owner)

owner.append('liuliu')
print(owner)

owner[0]='xiaoming'
print(owner)

owner.insert(1,'mingtian')
print(owner)

del owner[0]
print(owner)

owner1=owner.pop(0)
print(owner1)
print(owner)

too_lower=owner.remove('liuliu')
print(owner)
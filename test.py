#coding=utf-8
__author__ = 'yaozhihua'

name="yao zhihua"
#首字母大写
print(name.title())
#名字全大写
print(name.upper())
#名字小写
print(name.lower())

#字符串拼接
first_name="zhang"
last_name="xiaoming"
full_name=first_name +" "+last_name

print(full_name)
#制表符\t
print("\tpython")
#换行符\n
print("language:\npython\n\tjava\nperl")

#删除空白符 前后空白符strip 后空白符rstrip 前空白符lstrip
language=" python "
language=language.rstrip()
print(language)


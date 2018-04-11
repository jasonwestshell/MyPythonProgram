count = 100

print (count);

a , b , c = 'a1' , 'b2' , 'c3'

print (a,b,c)


numbers = [1,2,3,4,5,6,7,8,9,10]

print (numbers[3:6]);
print (numbers[7:10]);
print (numbers[:]);
print (numbers[3::2]);

fif = numbers[4:6];

print (fif)
del fif
#print (fif)

newString = 'aeiou';
aa = newString[1:4];
print (aa + "2" );
print (aa * 2 )  ;
print ("--" * 22);

#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = ['runoob','富强' , 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print (list)  # 输出完整列表
print (list[0])  # 输出列表的第一个元素
print (list[1:3])  # 输出第二个至第三个元素
print (list[2:])  # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)  # 输出列表两次
print (list + tinylist)  # 打印组合的列表


tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

print ("--"*10,"字典","--"*10)

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print (dict['one'])  # 输出键为'one' 的值
print (dict[2])  # 输出键为 2 的值
print (tinydict)  # 输出完整的字典
print (tinydict.keys())  # 输出所有键
print (tinydict.values())  # 输出所有值



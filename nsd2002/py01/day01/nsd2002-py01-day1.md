# nsd2002-py01-day1

## python语法

1. 用缩进表达代码逻辑：推荐缩进4个空格
2. 注释和续行与shell一样

> 在pycharm中，按ctrl + / 可以快速添加/取消注释

3. 多个语句书写在同一行，可以使用分号进行分隔。但是不推荐。

## 输出语句

- 主要采用的是print函数
- 在python中函数调用需要添加()

```python
>>> print("hello world!")   # 打印一个字符串
hello world!

# 在print函数的()中，输入的是参数，各个参数之间用逗号隔开
>>> print("hao", 123)       # 打印字符串和数字
hao 123

# print函数输出的各项之间，默认用空格分隔，可以通过sep指定分隔符
>>> print("hao", 123, "abc")
hao 123 abc
>>> print("hao", 123, "abc", sep="***")
hao***123***abc
```

## 输入语句

- python中，通过input函数获取用户键盘输入
- input函数的参数是字符串，它是屏幕提示语

```python
# 变量赋值，=两边空格可有可无
>>> user = input('username: ')   # 用户输入内容保存到变量user中
username: tom
>>> user    # 使用变量
'tom'

# input读入的数据都是字符串类型。相同类型的数据才能运算
>>> num = input("number: ")
number: 10
>>> num + 5    # num是字符串，不能和数字进行运算
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> type(num)    # 查看num的类型
<class 'str'>
>>> int(num) + 5  # int函数将字符串转成整数
15
>>> num + str(5)  # str函数将对象转成字符串
'105'
>>> num + "5"
'105'
```


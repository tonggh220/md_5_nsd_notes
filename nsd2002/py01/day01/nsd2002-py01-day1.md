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

## 变量

- 字面量就是看到什么是什么，如'abc'，100
- 变量是变化的量，看到什么不一定是什么。
- 变量只是为了编写代码方便。当看到变量时，应该透过变量看到它代表的值
- 编写代码时尽量多的使用变量，而不是直接使用字面量。直接使用字面量，是硬编码，代码可重用性差。
- 变量名称约定
  - 第一个字符只能是大小写字母或下划线
  - 后续字符只能是大小写字母或数字或下划线
  - 区分大小写

- 推荐采用的全名方法
  - 变量名全部采用小写字母，如pythonstring
  - 简短、有意义，如pystr
  - 多个单词间用下划线分隔，如py_str
  - 变量名用名词，函数名用谓词（动词+名词），如 phone / update_phone
  - 类名采用驼峰形式，如MyClass

- 变量在使用之前，必须先进行赋值
- 变量赋值是一个自右向左的运算，将=右边表达式的计算结果，赋值给左边的变量

```python
>>> a = 10 + 5
>>> a
15
```

- 变量支持重新赋值

```python
>>> a = 20
>>> a = a + 10   # 将a+10的结果再赋值给a
# 以上代码可以简写为
>>> a += 10
# 根据以上写法，举一反三
>>> a -= 20
>>> a
20
>>> a *= 2
>>> a
40
```

> 注意：Python不支持诸如i++ / i--之类的操作
>
> ```python
> >>> a = 40
> >>> ++a     # 正正为正
> 40
> >>> --a     # 负负为正
> 40
> >>> import this    # 导入python之禅
> The Zen of Python, by Tim Peters
> 
> Beautiful is better than ugly.     美胜丑
> Explicit is better than implicit.  明胜暗
> Simple is better than complex.     简胜繁
> ```

## 运算符

#### 算术运算符

```python
# 加减乘正常运算
# /是真正的除法
>>> 5 / 3
1.6666666666666667
# //只保留商
>>> 5 // 3
1
# %是模运算，即求余
>>> 5 % 3
2
# **是幂运算
>>> 2 ** 3
8
# 通过round函数实现四舍五入
>>> round(5 / 3)     # 5/3，默认保留到整数部分
2
>>> round(5 / 3, 2)  # 精确到小数点后2位
1.67
# divmod函数，可以同时得到商和余数
>>> divmod(5, 3)
(1, 2)
>>> a, b = divmod(5, 3)  # 商和余数分别赋值给a和b
>>> a
1
>>> b
2
```


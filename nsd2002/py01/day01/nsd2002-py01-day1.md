# nsd2002-py01-day1

python官方手册：https://docs.python.org/zh-cn/3/library/index.html

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

#### 比较运算符

```python
# 判断是否相等使用==
>>> 3 == 3
True    # True是关键字，表示真
# 判断是否不相等使用!=
>>> 3 != 3
False    # False是关键字，表示假
# python支持连续比较
>>> 10 < 20 < 30
True
```

#### 逻辑运算符

```python
# and两边表达式结果全为True，最终才为True
>>> 10 < 20 and 20 > 15
True
# or两边表达式结果全为False，最终才为False
>>> 10 < 20 or 20 > 100
True
>>> 100 < 20 or 20 > 100
False
# not是单目运算符，将真变假，将假变真
>>> 20 > 10
True
>>> not 20 > 10
False
```

## 数据类型

#### 数字

- 整数：没有小数点
- 浮点数：有小数点
- 布尔数：True为1，False为0

```python
>>> True + 1
2
>>> False * 5
0
```

- 整数在不同进制下的表示方法

```python
# python默认以10进制表示数字
>>> 11
11
# 8进制以0o或0O开头
>>> 0o11
9   # 默认以10进制输出
# 16进制以0x或0X开头
>>> 0x11
17
# 2进制以0b或0B开头
>>> 0b11
3

# 2小时3分5秒是多少秒？
>>> 2 * 60 * 60 + 3 * 60 + 5
7385
# 0x235 转成10进制怎么算？ 
>>> 2 * 16 * 16 + 3 * 16 + 5
565
>>> 0x235
565
# 0o235 转成10进制怎么算？ 
>>> 2 * 8 * 8 + 3 * 8 + 5
157
>>> 0o235
157

# 10000秒是几小时几分几秒？
>>> divmod(10000, 60)
(166, 40)  -> 166分40秒
>>> divmod(166, 60)
(2, 46)    -> 2小时46分

# 10000转换成16进制数是？
>>> divmod(10000, 16)
(625, 0)
>>> divmod(625, 16)
(39, 1)
>>> divmod(39, 16)
(2, 7)
# 10000 -> 0x2710
>>> hex(10000)
'0x2710'
```

#### 字符串

- python中字符串被定义为引号之间的字符集合
- python支持使用成对的单引号或双引号
- 无论单引号，还是双引号，表示的意义相同
- python还支持三引号（三个连续的单引号或者双引号），可以用来包含特殊字符

```python
>>> s1 = """tom
... jerry
... jack
... rose
... """
>>> print(s1)
tom
jerry
jack
rose

>>> s1
'tom\njerry\njack\nrose\n'
>>> s2 = "bj\ntj\nxa\nzz"
>>> print(s2)
bj
tj
xa
zz
```

- 常见操作

```python
>>> s1 = 'python'
>>> len(s1)   # 取长度
6
>>> s1[0]     # 第一个字符，下标为0
'p'
>>> s1[6]     # 下标为6，超出范围，报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s1[5]
'n'
>>> s1[-1]  # 负数表示从右向左，最右的一个字符
'n'
>>> s1[-6]  # 自右向左第6个字符
'p'
>>> s1[2:4]  # 切片，起始下标包含，结束下标不包含
'th'
>>> s1[2:6]  # 切片时，下标超出范围是允许的
'thon'
>>> s1[2:600]
'thon'
>>> s1[2:]   # 结束下标不写，表示取到结尾
'thon'
>>> s1[:2]   # 起始下标不写，表示从开头取
'py'
>>> s1[:]    # 从开头取到结尾
'python'
>>> s1[::2]  # 步长值为2，取切片
'pto'
>>> s1[1::2]
'yhn'

>>> 't' in s1          # t在s1中吗？
True
>>> 'th' in s1         # th在s1中吗？
True
>>> 'to' in s1         # to在s1中吗？
False
>>> 'to' not in s1     # to不在s1中吗？
True

>>> s1 + ' is good'    # 字符串拼接
'python is good'
>>> '*' * 30   # 字符串*重复30遍
'******************************'
>>> '#' * 30
'##############################'
>>> s1 * 3
'pythonpythonpython'
```




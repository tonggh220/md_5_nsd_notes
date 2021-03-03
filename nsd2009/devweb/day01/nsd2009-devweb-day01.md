# nsd2009-devweb-day01

https://www.w3school.com.cn/index.html

[TOC]

## web开发

- 前端：离用户近的一端是前端。
  - html：超文本标记语言，实现网站的内容
  - css：层叠样式表，也叫级联样式表，它实现网站的表现形式
  - javascript：简称js，实现网站的行为
- 后端：离用户远的一端，也就是服务器端，是后端。
  - python
  - java
  - php
  - asp.net

## html

- 文档结构

```html
<!DOCTYPE html>     <!--声明文档类型-->
<html lang="en">    <!--html是根标记，所有标记都需要写在html标记内部-->
<head>              <!--头部消息-->
    <meta charset="UTF-8">  <!--元数据-->
    <title>Title</title>    <!--标题-->
</head>
<body>  <!--出现在浏览器窗体中的内容-->

</body>
</html>
```

### 标签

- 标签也叫标记、元素
- 标记语法
  - 双标记：标记需要使有一对闭合的标记，如`<h1>一号标题</h1>`
  - 单标记：标记不成对出现，如`<br>`
  - 标记可以嵌套
  - 元素可以设置属性，但是不推荐。常规作法是通过css实现。
  - 注释形式是：`<!-- 被注释的内容 -->`

- 标记分类：
  - 块级元素：至少占一行。如h1~h6、div、p等
  - 行内元素：不会产生换行效果。如span、b、i等

### 标记

- 特殊字符
  - `&lt;`：`<`
  - `&gt;`：`>`
  - `&nbsp;`：空格
  - `&copy;`：&copy;

- 文本标记
  - b：加粗
  - i：倾斜
  - u：下划线
  - s：删除线
  - sub：下标
  - sup：上标

- 标题元素：h1~h6
- 段落元素：p。它是块级元素，上下默认有边距
- 换行元素：br。它是单标记
- div：块级元素。它默认没有边距，常用于页面布局
- span元素：行内元素。常用于将某一部分内容标记出来，以便对它进行操作。

- 图像元素：img

```html
<!--一般在网站目录下有一个static目录，用于存储静态文件-->
[root@localhost day01]# mkdir -p static/{css,js,imgs}
<div>
    <img src="abc/aaa.jgp" alt="如果图片无法显示，则显示此文字"> <br>
    <img src="static/imgs/html_css.jpeg"> <br>
    <img src="http://pic.people.com.cn/NMediaFile/2020/0727/MAIN202009270830000372979471030.JPG"> <br>
    <img src="http://pic1.win4000.com/wallpaper/e/584fb6774ce08.jpg" width="500px"> <br>
    <img src="http://pic1.win4000.com/wallpaper/e/584fb6774ce08.jpg" height="300px"> <br>
</div>
```

- 超链接：a标记

```html
<!--在新窗口打开链接-->
<a href="http://fanyi.sogou.com" target="_blank">sogou fanyi</a>

<!--页面内跳转，首先可以为目标添加一个id属性。然后就可以通过a标记跳转到目标-->
<a href="#img1">jump to girl image</a>
... ...
<img id="img1" src="http://pic1.win4000.com/wallpaper/e/584fb6774ce08.jpg"><br>
<a href="#">back to top</a> <!--返回到顶部-->
```

### 表格

- 表格使用table标签
- 使用tr表示行
- 使用td表示列（单元格）

```html
table>tr*5>td*3  按tab键
<table border="1px" width="500px">
<!--不规则单元格-->
    <tr>
        <td rowspan="2">aaa</td>  <!--跨两行-->
        <td colspan="2">aaa</td>  <!--跨两列-->
    </tr>
    <tr>
        <td>bbb</td>
        <td>bbb</td>
    </tr>
</table>
```

### 列表

- 有序列表

```html
ol>li*4 按tab键
	<ol type="a" start="5">
        <li>python</li>
        <li>html</li>
        <li>css</li>
        <li>javascript</li>
    </ol>
    <ol type="I" start="7">
        <li>python</li>
        <li>html</li>
        <li>css</li>
        <li>javascript</li>
    </ol>
    <ol>
        <li>python</li>
        <li>html</li>
        <li>css</li>
        <li>javascript</li>
    </ol>
```

- 无序列表

```html
ul>li*4
    <ul type="circle">
        <li>python</li>
        <li>html</li>
        <li>css</li>
        <li>javascript</li>
    </ul>
    <ul type="square">
        <li>python</li>
        <li>html</li>
        <li>css</li>
        <li>javascript</li>
    </ul>
    <ul>
        <li>python</li>
        <li>html</li>
        <li>css</li>
        <li>javascript</li>
    </ul>
```

### 表单

- 表单用于显示、收集信息，并提交信息到服务器

```html
    <form action="https://www.sogou.com/web" target="_blank">
        <input name="query" type="text">
        <input type="submit" value="搜狗搜索">
    </form>
```

- `<input type="text">`：文本框
- `<input type="password">`：密码框
- `<input type="radio">`：单选按钮
- `<input type="checkbox">`：复选框
- `<input type="submit">`：提交按钮
- `<input type="reset">`：重置按钮
- `<input type="hidden">`：隐藏域
- 多行文本域

```html
<textarea name="comment" cols="50" rows="10"></textarea>
```

- 下拉列表框

```html
        <select name="q3">
            <option value="A">html</option>
            <option value="B">css</option>
            <option value="C">javascript</option>
            <option value="D">python</option>
        </select>
```

## CSS

- 层叠样式表，也叫级联样式表
- 实现页面的表现形式
- 分类：
  - 内联：像html标签的属性一样，写在html标签内
  - 内部：集中将样式声明写在head中
  - 外部：将样式声明写在单独的文件里

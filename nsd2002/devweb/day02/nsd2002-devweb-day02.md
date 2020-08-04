# nsd2002-devweb-day02

## CSS

- 样式表由多个样式规则构成
- 每个样式规则有两个部分：选择器和样式声明
- 选择器：为谁设置样式
- 样式声明：设置成什么样的样式
- 样式表的特性：
  - 继承：子承父
  - 层叠性：样式可以来自于多处
  - 优先级：如果来自于多处的样式有冲突，优先级高的生效

### 选择器

- 通用选择器：`*`选择所有内容
- 元素选择器：元素天然就是选择器
- 类选择器：用class来将某些元素放到一个分组里，统一设置样式。一个标签可以属于多个class。在样式表中，使用`.`前缀表示class。
- 类选择器可以和元素结合使用，`p.c3`表示拥有`class="c3"`的p元素
- 后代选择器：`div .c4`表示在div中拥有`class="c4"`的元素
- id选择器：id是某一元素的唯一识别，可以只定位到这个元素上，在样式表中，使用`#`前缀表示id。
- 群组选择器：使用逗号将一组选择器放到一起，统一设置样式
- 伪类选择器：往往用于为a标签设置访问前、鼠标悬停、访问后的样式

### 尺寸

- 绝对大小：厘米cm、毫米mm等
- 相对大小：像素、em（是当前大小的几倍）、rem（是根元素大小的几倍）
- 百分比：相对于父元素的百分比大小

### 颜色

- 颜色单词
- 颜色可以使用红绿蓝三元色表示。每一种颜色都采用8位2进制数表示，转换成10进制数是0～255，转换成16进制数是00～FF。这种颜色越暗，值越小；颜色越亮，值越大。
  - 10进制，使用rgb()表示
  - 16进制，使用#xxxxxx表示

### 盒子模型

- 也叫框模型
- 在html中，一切皆框
- 元素占据页面空间由以下内容决定
  - 元素大小
  - 内边距，也叫填充，padding
  - 边框，border
  - 外边距，margin
  - 一般很少设置高度，具体的高度由内部多少决定
- 元素所占宽度＝元素宽度＋左右内边距＋左右边框＋左右外边距

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>box model</title>
    <style>
        #box {
            background-color: gray;
            width: 300px;
            height: 300px;
            /*padding: 10px;  !*四个方向，内边距全为10px*!*/
            /*padding: 10px 20px;  !*上下内边距为10px，左右为20px*!*/
            /*padding: 10px 20px 30px 40px;  !*方向为上右下左*!*/
            padding-top: 10px;  /*上内边距*/
            padding-right: 20px;  /*右内边距*/
            padding-bottom: 30px;  /*下内边距*/
            padding-left: 40px;  /*左内边距*/
            border-top: 5px solid darkgreen;
            border-right: 5px dotted darkorange;
            border-bottom: 5px dashed purple;
            /*margin: 50px;*/
            margin: 0 auto;   /*左右外边距设置为自动，则该元素居中显示*/
        }
    </style>
</head>
<body>
<div id="box">
    hello world
</div>
</body>
</html>
```

### 块级元素和行内元素的转换

- 行内元素不能设置宽高，块级元素才可以设置

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mycss4</title>
    <style>
        span {
            display: block;
        }
    </style>
</head>
<body>
<div>
    <span>Hello Word!</span><span>How Are You?</span>
</div>
</body>
</html>
```

- 块级元素至少占一行，可以通过设置浮动让它脱离文档流

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>my css 5</title>
    <style>
        .c1, .c2 {
            float: left;
            width: 300px;
        }
        .c1 {
            background-color: gray;
        }
        .c2 {
            background-color: lightblue;
        }
    </style>
</head>
<body>
<div class="c1">Hello World</div>
<div class="c2">How Are You?</div>
</body>
</html>
```

### 导航栏练习

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>nav</title>
    <style>
        .container {
            width: 1280px;
            margin: 0 auto;
        }
        ul {
            list-style-type: none;  /*去掉项目标号*/
            margin: 0;
            padding: 0;
        }
        li {
            float: left;  /*所有li左浮动，在一行显示*/
            width: 213px;
            background-color: #BEBEBE;
            height: 30px;
            text-align: center;
            line-height: 30px;
            border-bottom: 2px solid #900B09;
            color: white;
        }
        li:hover {
            background-color: #900B09;
            cursor: pointer;  /*鼠标为手型*/
        }
    </style>
</head>
<body>
<div class="container">
    <div class="nav">
        <ul>
            <li>Python</li>
            <li>html</li>
            <li>CSS</li>
            <li>JavaScript</li>
            <li>Shell</li>
            <li>Linux</li>
        </ul>
    </div>
</div>
</body>
</html>
```

## bootstrap

- bootstrap是twitter公司开发的开源前端web框架
- 可以简单的理解为它是一个大样式表。
- 中文官方站：<http://bootcss.com>
- 准备环境，将前一个班devweb/day02/目录的static目录拷贝到工作目录

```
# ls static/
css  fonts  imgs  js
css->样式表目录
fonts->字体
imgs->图片
js->javascript脚本
```

## 一、排版样式

- Bootstrap 将全局 font-size 设置为 14px,line-height 行高设置为 1.428(即20px);p段落元素被设置等于 1/2 行高(即 10px);颜色被设置为#333333。
- 标题元素大小
  - h1: 36px
  - h2: 30px
  - h3: 24px
  - h4: 18px
  - h5: 14px
  - h6: 12px
- 为了统一，bootstrap还创建了h1到h6 class，样式与标题元素一致
- 内联文本元素，各种加线条的文本、强调的文本

```
<mark>达内云计算 nsd2002</mark>
<del>达内云计算 nsd2002</del>
<s>达内云计算 nsd2002</s>
<ins>达内云计算 nsd2002</ins>
<u>达内云计算 nsd2002</u>
<small>达内云计算 nsd2002</small>
<strong>达内云计算 nsd2002</strong>
<b>达内云计算 nsd2002</b>
<em>达内云计算 nsd2002</em>
<i>达内云计算 nsd2002</i>
```

- 对齐方式

```
<p class="text-center">达内云计算 nsd2002</p>
<p class="text-left">达内云计算 nsd2002</p>
<p class="text-right">达内云计算 nsd2002</p>
```

- 颜色
  - danger: 危险红
  - muted：柔和灰
  - primary：首要蓝
  - info：信息蓝
  - success：成功绿
  - warning：警告黄

```
<p class="text-center text-primary bg-warning">达内云计算 nsd2002</p>
<p class="text-left text-danger bg-success">达内云计算 nsd2002</p>
<p class="text-right text-muted bg-info">达内云计算 nsd2002</p>
```

## 二、表格

```
<table class="table table-bordered table-striped table-hover">
```

## 三、按钮

```
<input type="submit" value="查 询"><br>
<input class="btn btn-default btn-sm" type="submit" value="查 询"><br>
<input class="btn btn-primary" type="submit" value="查 询"><br>
<input class="btn btn-info btn-lg" type="submit" value="查 询"><br>
<input class="btn btn-warning" type="submit" value="查 询"><br>
<input class="btn btn-success btn-xs" type="submit" value="查 询"><br>
<input class="btn btn-danger" type="submit" value="查 询"><br>
<input class="btn btn-primary btn-block" type="submit" value="查 询"><br>
<input type="submit" value="查 询"><br>
<input type="submit" value="查 询"><br>
```

## 四、表单

- 为了有很好的间距，应该把各个控件放到form-group中
- 每个文本类型的控件，放到form-control中

```
<form action="">
    <div class="form-group">
        <label>uname: </label><input class="form-control" type="text">
    </div>
    <div class="form-group">
        <label>upass: </label><input class="form-control" type="text">
    </div>
    <div class="form-group">
        <input class="btn btn-primary" type="submit">
    </div>
</form>
```

- 如果希望表单只占一行，只要设置form的class

```
<form action="" class="form-inline">
    <div class="form-group">
        <label>uname: </label><input class="form-control" type="text">
    </div>
    <div class="form-group">
        <label>upass: </label><input class="form-control" type="text">
    </div>
    <div class="form-group">
        <input class="btn btn-primary" type="submit">
    </div>
</form>
```

## 五、图片

```
<!-- 圆角矩形 -->
<img class="img-rounded" src="https://img01.sogoucdn.com/app/a/100520021/c0b43a061bdb06f3b983953f41e7e8d0">
<!-- 圆形 -->
<img class="img-circle" src="https://img01.sogoucdn.com/app/a/100520021/c0b43a061bdb06f3b983953f41e7e8d0">
<!-- 支持自动缩放 -->
<img class="img-thumbnail" src="https://img01.sogoucdn.com/app/a/100520021/c0b43a061bdb06f3b983953f41e7e8d0">
```

## 六、栅格系统

1. 实现页面布局
2. 布局时，要求页面所有的元素位于container中
3. container的直接子元素是row
4. row中的元素是col-xx-yy
5. 一个row最多支持12列。其中的col-xx-yy设置为占多少列
   1. col-lg-3表示大屏幕尺寸下，它占3列
   2. col-md-4表示中等屏幕尺寸下，它占4列
   3. col-sm-6表示小屏幕尺寸下，它占6列
6. 还可以设置自适应屏幕大小

```
<div class="container">
    <div class="row">
        <div class="col-lg-3 bg-primary col-md-4 col-sm-6">
            云计算<br>
            nsd 1904
        </div>
        <div class="col-lg-3 bg-danger col-md-4 col-sm-6">
            云计算<br>
            nsd 1904
        </div>
        <div class="col-lg-3 bg-success col-md-4 col-sm-6">
            云计算<br>
            nsd 1904
        </div>
        <div class="col-lg-3 bg-warning col-md-4 col-sm-6">
            云计算<br>
            nsd 1904
        </div>
    </div>
</div>

```

## 七、导航

- 水平导航

```
<div class="container" style="margin-top: 10px">
    <ul class="nav nav-tabs">
        <li class="active"><a href="#">Home</a></li>
        <li><a href="#">News</a></li>
        <li><a href="#">Contact</a></li>
        <li><a href="#">About</a></li>
    </ul>
</div>

<div class="container" style="margin-top: 10px">
    <ul class="nav nav-tabs nav-pills">
        <li class="active"><a href="#">Home</a></li>
        <li><a href="#">News</a></li>
        <li><a href="#">Contact</a></li>
        <li><a href="#">About</a></li>
    </ul>
</div>

```

- 垂直导航

```
<div class="container" style="margin-top: 10px">
    <div class="row">
        <div class="col-sm-2">
            <ul class="nav nav-stacked nav-pills">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#">News</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="#">About</a></li>
            </ul>
        </div>
        <div class="col-sm-7 bg-danger">
            这是中间区域<br>
            这是中间区域
        </div>
        <div class="col-sm-3 bg-warning">
            这是右边区域<br>
            这是右边区域
        </div>
    </div>
</div>
```

- 象形字：<https://v3.bootcss.com/components/>

```
<i class="glyphicon glyphicon-trash"></i>
<i class="glyphicon glyphicon-wrench"></i>
```


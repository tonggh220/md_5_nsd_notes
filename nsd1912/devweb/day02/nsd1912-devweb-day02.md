# nsd1912-devweb-day02

<https://www.w3school.com.cn/>

<https://www.w3school.com.cn/css/index.asp>

## CSS

- 层叠样式表，也叫级联样式表
- 分类
  - 内联：与属性类似，在标记上直接设置样式
  - 内部：在html的head标记中设置样式
  - 外部：将样式统一放在外部文件中

### css语法规范

- 样式表由一到多个样式构成
- 每个样式分为两个部分
  - 选择器：为谁设置样式
  - 样式声明：设置成什么样的样式

### 样式表特征

- 继承性：子承父
- 层叠性：元素样式可以来自于不同的地方，只要样式不冲突，就可以叠加
- 优先级：元素从不同地方得到的样式有冲突，优先级高的生效

### 选择器

- 通用选择器：`*`，匹配所有标记
- 元素选择器：html的标记（元素）天然就是选择器
- 类选择器：可以为标记设置class属性，具有相同class名称的元素分为一组，对这一组标记设置样式
- 类选择器2：元素可以属于多个类，样式不冲突则叠加，样式冲突依据优先级
- 类选择器与元素选择器结合使用：`p.c4`，表示拥有class="c4"的p元素
- 类选择器与元素选择器结合使用：`p .c5`，表示p元素中嵌套的class="c5"元素
- id选择器：某个元素的唯一标识
- 群组选择器：用逗号将多个选择器连接在一起，统一设置样式
- 伪类选择器：经常为超链接设置访问前、鼠标悬停和访问后(指的是存在历史记录中)的样式

### 尺寸

- px：像素
- 百分比：相对大小
- em：相对当前元素的倍数
- rem：相对于根元素的倍数
- 颜色使用rgb颜色：red / green / blue。每种颜色都使用1个字节表示，10进制数是0到255，16进制是00到ff。数值越小表示该颜色越暗，数值越大表示该颜色越亮。

### 框模型/盒子模型

- 在html中，一切框
- 对于块级元素可以设置它的长宽；行内元素无法设置长宽
- 某一元素在页面内占据的宽度是：元素宽度＋左右内边距＋左右边框+左右外边距

#### 导航栏示例：

<https://www.w3school.com.cn/css/css_navbar.asp>

1. 创建ul

```html
<div>
    <ul>
        <li><a href="#">HOME</a></li>
        <li><a href="#">NEWS</a></li>
        <li><a href="#">ARTICLES</a></li>
        <li><a href="#">FORUM</a></li>
        <li><a href="#">CONTACT</a></li>
        <li><a href="#">ABOUT</a></li>
    </ul>
</div>
```

1. 将ul的默认样式清除

```html
    <style>
        ul {
            padding: 0;
            margin: 0;
            list-style: none;   /*去除项目编号*/
        }
    </style>
```

1. 实现li水平排列

```html
li {
  float: left;
}
```

1. 设置div宽度

```html
div {
  width: 1200px;
  margin: 0 auto;
}
```

1. 设置每个超链接的样式

```html
a {
  display: block;    /*将a标记转换成块元素，以便设置宽度*/
  width: 200px;
  text-decoration: none;
  background: #BEBEBE;
  height: 30px;
  line-height: 30px;
  text-align: center;
  color: white;
  border-bottom: 2px solid #900B09;
  font-weight: bold;
}
a:hover {
  background: #900B09;
}
```

## bootstrap

- bootstrap是twitter公司开发的开源前端web框架
- 可以简单的理解为它是一个大样式表。
- 中文官方站：<http://bootcss.com>
- 准备环境，将nsd1911班devweb/day02/目录的static目录拷贝到工作目录

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
<mark>达内云计算 nsd1912</mark>
<del>达内云计算 nsd1912</del>
<s>达内云计算 nsd1912</s>
<ins>达内云计算 nsd1912</ins>
<u>达内云计算 nsd1912</u>
<small>达内云计算 nsd1912</small>
<strong>达内云计算 nsd1912</strong>
<b>达内云计算 nsd1912</b>
<em>达内云计算 nsd1912</em>
<i>达内云计算 nsd1912</i>
```

- 对齐方式

```
<p class="text-center">达内云计算 nsd1904</p>
<p class="text-left">达内云计算 nsd1904</p>
<p class="text-right">达内云计算 nsd1904</p>
```

- 颜色
  - danger: 危险红
  - muted：柔和灰
  - primary：首要蓝
  - info：信息蓝
  - success：成功绿
  - warning：警告黄

```
<p class="text-center text-primary bg-warning">达内云计算 nsd1904</p>
<p class="text-left text-danger bg-success">达内云计算 nsd1904</p>
<p class="text-right text-muted bg-info">达内云计算 nsd1904</p>
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
















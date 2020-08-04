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








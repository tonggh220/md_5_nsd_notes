import turtle


def move(length, degree):
    "用于控制爬行距离和转向角度"
    t.forward(length)      # 前进length像素
    t.left(degree)         # 逆时针左转degree角度

if __name__ == '__main__':
    t = turtle.Turtle()      # 创建Turtle实例
    w = t.getscreen()        # 取出屏幕对象
    t.fillcolor('yellow')    # 设置填充颜色为黄色
    t.pensize(3)             # 设置笔的粗细
    t.up()                   # 抬笔，小乌龟移动时不画线
    t.back(100)              # 向后移动100个像素，默认它在窗口正中间
    t.down()                 # 落笔，小乌龟移动时画线
    t.begin_fill()           # 开始填充
    for load in [1.2, 0.8, 0.5]:
        for i, j in [(100, 90), (load * 100, 90), (30, 90), (load * 100, 90)]:
            move(i, j)

    t.end_fill()             # 结束填充
    t.hideturtle()           # 隐藏小乌龟
    w.exitonclick()          # 点击窗口时退出
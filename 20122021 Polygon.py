import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor('red')
def polygon(n, w):
    # Hàm vẽ hình đa giác đều n - số cạnh của đa giác đều,
    # w - chiều dài của các cạnh
    # Giá trị mỗi góc của đa giác
    angle = (n - 2) * 180 / n
    for i in range(n):
        t.forward(w)
        t.right(180 - angle)
    turtle.done()

if __name__=='__main__':
    polygon(6,100)
import turtle
colors = ["red", "orange", "green", "blue", "violet"] #cycle of colors
n = 10000 #number of line
turtle.speed(100000000000000000) #speed ofr pen
for i in range(n):
    turtle.forward(300+i*(1-i/n))
    turtle.right(144.5)
    turtle.color(colors[i%5])

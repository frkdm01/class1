import turtle

def polygon(sekil, ku, ks):
    aci = 360 / ks

    for _ in range(ks):
        sekil.forward(ku)
        sekil.left(aci)


ekran = turtle.Screen()


poligon_turtle = turtle.Turtle()


polygon(poligon_turtle, 10, 100)


ekran.mainloop()
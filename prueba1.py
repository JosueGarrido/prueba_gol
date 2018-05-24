from tkinter import *
tk = Tk()
puntaje=0;

canvas = Canvas(tk, width=1200, height = 800)
canvas.pack()

my_image1 = PhotoImage(file="arco2.gif")
canvas.create_image(0,200, anchor= NW, image=my_image1)

my_image = PhotoImage(file="ball.gif")
canvas.create_image(1000,350, anchor= NW, image=my_image)


def moveimage(event):

    if event.keysym == 'Left':
        canvas.move(2,-5,0)
    else:
        canvas.move(2,5,0)

canvas.bind_all('<KeyPress-Left>', moveimage)
canvas.bind_all('<KeyPress-Right>', moveimage)

if my_image==(200,350):
    print('GOL!!!!!!!!!!!!!!!!!!!!!!')
    puntaje +=1
    print(puntaje)

tk.mainloop()

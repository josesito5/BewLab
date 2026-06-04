from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


def salirventana():
    saliendo = messagebox.askquestion("salir", "¿seguro que deseas salir?")
    if saliendo == "yes":
        messagebox.showinfo("bye", "gracias por visitar Brew Lab")
        ventana.destroy()


def abrir_cafe(nombre, imagen):
    ventana_cafe = Toplevel(ventana)
    ventana_cafe.title(nombre)
    ventana_cafe.geometry("400x500")
    ventana_cafe.config(bg="#111111")

    titulo = Label(ventana_cafe,text=nombre,font=("Arial",18,"bold"),
    bg="#111111",fg="#E8C87A")
    titulo.pack(pady=20)

    foto = Image.open(resource_path(imagen))
    foto = foto.resize((250,250))
    foto_tk = ImageTk.PhotoImage(foto)

    label_foto = Label(ventana_cafe,image=foto_tk,bg="#111111")
    label_foto.image = foto_tk
    label_foto.pack(pady=20)


def abrir_espresso():
    abrir_cafe("Espresso","espresso.png")


def abrir_capuccino():
    abrir_cafe("Capuccino","capuccino.png")


def abrir_latte():
    abrir_cafe("Latte","latte.png")


def abrir_mocha():
    abrir_cafe("Mocha","mocha.png")


def abrir_frappe():
    abrir_cafe("Frappé","frappe.png")


def ventana_3():

    ventana3 = Toplevel(ventana)

    ventana3.title("Toppings")

    ventana3.geometry("500x650")

    ventana3.configure(background="#111111")

    ventana3.resizable(0,0)

    brewmenu3 = Menu(ventana3)

    ventana3.config(menu=brewmenu3)

    archivo3 = Menu(brewmenu3,tearoff=0)

    archivo3.add_command(label="Ir al Inicio",command=ventana.deiconify)

    archivo3.add_command(label="Ir a Sabores",command=vnt)

    archivo3.add_command(label="Cerrar Toppings",command=ventana3.destroy)

    brewmenu3.add_cascade(label="Menu",menu=archivo3)

    opcion = StringVar()

    titulo3 = Label(ventana3,text="Selecciona Un Topping",
    bg="#111111",fg="#E8C87A",font=("Arial",12,"bold"))
    titulo3.pack(pady=25)

    info3 = Label(ventana3,text="Elige Un Topping Para Tu Bebida",
    bg="#111111",fg="#E8C87A",font=("Arial",10))
    info3.pack(pady=5)

    mensaje3 = Label(ventana3,
    text="Los Toppings Hacen Tu Bebida Más Especial",
    bg="#111111",fg="#CCCCCC",font=("Arial",10,"italic"))
    mensaje3.pack(pady=5)

    resultado3 = Label(ventana3,
    text="No Has Seleccionado Ningún Topping",
    bg="#111111",fg="#CCCCCC",font=("Arial",11,"bold"))
    resultado3.pack(pady=20)

    frame_toppings = LabelFrame(
    ventana3,
    bg="#111111",
    padx=20,
    pady=20,
    bd=0
    )

    frame_toppings.pack(pady=10)

    def marcar():

        valor = opcion.get()

        if valor:

            resultado3.config(
            text=f"Topping Seleccionado: {valor}",
            fg="#E8C87A"
            )

        else:

            resultado3.config(
            text="No Has Seleccionado Ningún Topping",
            fg="#CCCCCC"
            )

    Radiobutton(frame_toppings,text="Crema Batida",
    value="Crema Batida",variable=opcion,
    command=marcar,bg="#111111",
    fg="#CCCCCC").grid(row=0,column=0,sticky="w",pady=5)

    Radiobutton(frame_toppings,text="Chispas De Chocolate",
    value="Chispas De Chocolate",variable=opcion,
    command=marcar,bg="#111111",
    fg="#CCCCCC").grid(row=1,column=0,sticky="w",pady=5)

    Radiobutton(frame_toppings,text="Canela Extra",
    value="Canela Extra",variable=opcion,
    command=marcar,bg="#111111",
    fg="#CCCCCC").grid(row=2,column=0,sticky="w",pady=5)

    Radiobutton(frame_toppings,text="Jarabe De Caramelo",
    value="Jarabe De Caramelo",variable=opcion,
    command=marcar,bg="#111111",
    fg="#CCCCCC").grid(row=3,column=0,sticky="w",pady=5)

    Radiobutton(frame_toppings,text="Malvaviscos",
    value="Malvaviscos",variable=opcion,
    command=marcar,bg="#111111",
    fg="#CCCCCC").grid(row=4,column=0,sticky="w",pady=5)


def vnt():

    ventana2 = Toplevel(ventana)

    ventana2.title("Sabores")

    ventana2.geometry("400x550")

    ventana2.configure(background="#111111")

    ventana2.resizable(0,0)

    brewmenu2 = Menu(ventana2)

    ventana2.config(menu=brewmenu2)

    archivo2 = Menu(brewmenu2,tearoff=0)

    archivo2.add_command(label="Ir al Inicio",command=ventana.deiconify)

    archivo2.add_command(label="Ir a Toppings",command=ventana_3)

    archivo2.add_command(label="Cerrar Sabores",command=ventana2.destroy)

    brewmenu2.add_cascade(label="Menu",menu=archivo2)

    sabores = Label(ventana2,
    text="Selecciona Los Sabores Que Quieras Agregar",
    bg="#111111",fg="#E8C87A",
    font=("Arial",12,"bold"))
    sabores.pack(pady=20)

    descripcion2 = Label(ventana2,
    text="Cada Sabor Tiene Un Costo Diferente",
    bg="#111111",fg="#CCCCCC",
    font=("Arial",10))
    descripcion2.pack(pady=5)

    frame_sabores = LabelFrame(
    ventana2,
    bg="#111111",
    padx=20,
    pady=20,
    bd=0
    )

    frame_sabores.pack(pady=15)

    precios = {
        "Vainilla":10,
        "Caramelo":12,
        "Chocolate":15,
        "Avellana":14,
        "Canela":8
    }

    seleccion = []

    label_resultado = Label(ventana2,
    text="No Hay Sabores Seleccionados",
    bg="#111111",fg="#CCCCCC",
    font=("Arial",11))
    label_resultado.pack(pady=10)

    label_total = Label(ventana2,
    text="Total: $0",
    bg="#111111",fg="#E8C87A",
    font=("Arial",11,"bold"))

    def actualizar_label():

        total = 0

        if seleccion:

            texto = "Sabores:\n"

            i = 0

            while i < len(seleccion):

                total += precios[seleccion[i]]

                i += 1

            for sabor in seleccion:

                texto += f"{sabor}\n"

            label_resultado.config(text=texto)

        else:

            label_resultado.config(
            text="No Hay Sabores Seleccionados"
            )

        label_total.config(text=f"Total: ${total}")

    def vainilla():

        if "Vainilla" in seleccion:
            seleccion.remove("Vainilla")
        else:
            seleccion.append("Vainilla")

        actualizar_label()

    def caramelo():

        if "Caramelo" in seleccion:
            seleccion.remove("Caramelo")
        else:
            seleccion.append("Caramelo")

        actualizar_label()

    def chocolate():

        if "Chocolate" in seleccion:
            seleccion.remove("Chocolate")
        else:
            seleccion.append("Chocolate")

        actualizar_label()

    def avellana():

        if "Avellana" in seleccion:
            seleccion.remove("Avellana")
        else:
            seleccion.append("Avellana")

        actualizar_label()

    def canela():

        if "Canela" in seleccion:
            seleccion.remove("Canela")
        else:
            seleccion.append("Canela")

        actualizar_label()

    Checkbutton(frame_sabores,text="Vainilla - $10",
    command=vainilla,bg="#111111",
    fg="#CCCCCC",font=("Arial",11)
    ).grid(row=0,column=0,sticky="w")

    Checkbutton(frame_sabores,text="Caramelo - $12",
    command=caramelo,bg="#111111",
    fg="#CCCCCC",font=("Arial",11)
    ).grid(row=1,column=0,sticky="w")

    Checkbutton(frame_sabores,text="Chocolate - $15",
    command=chocolate,bg="#111111",
    fg="#CCCCCC",font=("Arial",11)
    ).grid(row=2,column=0,sticky="w")

    Checkbutton(frame_sabores,text="Avellana - $14",
    command=avellana,bg="#111111",
    fg="#CCCCCC",font=("Arial",11)
    ).grid(row=3,column=0,sticky="w")

    Checkbutton(frame_sabores,text="Canela - $8",
    command=canela,bg="#111111",
    fg="#CCCCCC",font=("Arial",11)
    ).grid(row=4,column=0,sticky="w")

    label_total.pack(pady=25)


ventana = Tk()

ventana.title("Brew Lab - Cafetería")

ventana.attributes("-fullscreen", True)

ventana.config(bg="#111111",bd=20)

logo = Image.open(resource_path("Logo.jpg"))

logo = logo.resize((220,220))

logo_tk = ImageTk.PhotoImage(logo)

label_logo = Label(ventana,image=logo_tk,bg="#111111")

label_logo.place(x=565,y=40)

brewmenu = Menu(ventana)

ventana.config(menu=brewmenu)

archivo = Menu(brewmenu,tearoff=0)

archivo.add_command(label="Ir A Sabores",command=vnt)

archivo.add_command(label="Ir A Toppings",command=ventana_3)

archivo.add_separator()

archivo.add_command(label="Salir",command=salirventana)

brewmenu.add_cascade(label="Menu",menu=archivo)

label_principal = Label(
    ventana,
    text="Brew Lab\nMás Que Solo Café, Sabor Que Inspira.",
    font=("Arial",24,"bold"),
    fg="#E8C87A",
    bg="#1A1200",
    padx=20,
    pady=15
)

label_principal.place(x=410,y=300)

label1 = Button(
    ventana,
    text="Espresso",
    font=("Arial",14,"bold"),
    fg="#E8C87A",
    bg="#1A1200",
    width=15,
    height=2,
    command=abrir_espresso
)

label1.place(x=330,y=430)

label2 = Button(
    ventana,
    text="Capuccino",
    font=("Arial",14,"bold"),
    fg="#E8C87A",
    bg="#1A1200",
    width=15,
    height=2,
    command=abrir_capuccino
)

label2.place(x=580,y=430)

label3 = Button(
    ventana,
    text="Latte",
    font=("Arial",14,"bold"),
    fg="#E8C87A",
    bg="#1A1200",
    width=15,
    height=2,
    command=abrir_latte
)

label3.place(x=830,y=430)

label4 = Button(
    ventana,
    text="Mocha",
    font=("Arial",14,"bold"),
    fg="#E8C87A",
    bg="#1A1200",
    width=15,
    height=2,
    command=abrir_mocha
)

label4.place(x=455,y=550)

label5 = Button(
    ventana,
    text="Frappé",
    font=("Arial",14,"bold"),
    fg="#E8C87A",
    bg="#1A1200",
    width=15,
    height=2,
    command=abrir_frappe
)

label5.place(x=705,y=550)

mensaje_cafe = Label(
    ventana,
    text="Disfruta Nuestros Sabores Especiales",
    font=("Arial",10,"italic"),
    fg="#CCCCCC",
    bg="#111111"
)

mensaje_cafe.place(x=580,y=680)

footer = Label(
    ventana,
    text="Brew Lab Coffee Shop",
    font=("Arial",10,"bold"),
    fg="#E8C87A",
    bg="#111111"
)

footer.place(x=620,y=720)

ventana.mainloop()

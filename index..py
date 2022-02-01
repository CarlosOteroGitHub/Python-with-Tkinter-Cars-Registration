import sys
import random
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class Auto:

    def __init__(self, id_auto, nombre, año, combustible, transmision, color):
        self.id_auto = id_auto
        self.nombre = nombre
        self.año = año
        self.combustible = combustible
        self.transmision = transmision
        self.color = color
    

    def get_ID(self):
        return self.id_auto;


    def get_Nombre(self):
        return self.nombre;
    

    def get_Año(self):
        return self.año;
    

    def get_Combustible(self):
        return self.combustible;
    

    def get_Transmision(self):
        return self.transmision;
    

    def get_Color(self):
        return self.color;


    
class Clase1:
    
    def __init__(self, frame):
        self.frame = frame
        frame.title("Registro de Automoviles")
        frame.resizable(False, False)
        frame.geometry("600x515")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.autoList = []

        self.label1 = Label(frame, text="No. Registro:")
        self.label1.place(x=10, y=10, width=100, height=25)

        self.entry1 = Entry(frame)
        self.entry1.place(x=110, y=10, width=100, height=25)

        self.label2 = Label(frame, text="Marca:")
        self.label2.place(x=210, y=10, width=100, height=25)

        self.combo1 = ttk.Combobox(frame, state="readonly")
        self.combo1.place(x=300, y=10, width=100, height=25)
        self.combo1["values"] = ["Audi", "Ford", "Honda", "Toyota"]
        self.combo1.current(0)

        self.label3 = Label(frame, text="Año:")
        self.label3.place(x=400, y=10, width=100, height=25)

        self.entry2 = Entry(frame)
        self.entry2.place(x=490, y=10, width=100, height=25)

        self.label4 = Label(frame, text="Combustible:")
        self.label4.place(x=10, y=80, width=100, height=25)

        self.combo2 = ttk.Combobox(frame, state="readonly")
        self.combo2.place(x=110, y=80, width=100, height=25)
        self.combo2["values"] = ["Magna", "Premium", "Disel"]
        self.combo2.current(0)

        self.label5 = Label(frame, text="Transmición:")
        self.label5.place(x=210, y=80, width=100, height=25)

        self.combo3 = ttk.Combobox(frame, state="readonly")
        self.combo3.place(x=300, y=80, width=100, height=25)
        self.combo3["values"] = ["Estandar", "Automático"]
        self.combo3.current(0)

        self.label6 = Label(frame, text="Color:")
        self.label6.place(x=400, y=80, width=100, height=25)

        self.combo4 = ttk.Combobox(frame, state="readonly")
        self.combo4.place(x=490, y=80, width=100, height=25)
        self.combo4["values"] = ["Azúl", "Verde", "Negro", "Blanco", "Rojo"]
        self.combo4.current(0)

        self.button1 = Button(frame, text="Guardar", command=self.guardar)
        self.button1.place(x=30, y=140, width=250, height=25)

        self.button2 = Button(frame, text="Salír", command=self.salir)
        self.button2.place(x=320, y=140, width=250, height=25)

        self.text1 = Text(frame, borderwidth=2, relief="solid")
        self.text1.place(x=10, y=200, width=580, height=305)

        self.scroll1 = Scrollbar(frame, command=self.text1.yview)
        self.text1.configure(yscrollcommand=self.scroll1.set)


    def soloNumeros(self, cadena):
        for i in range(0, len(cadena), 1):
            if(cadena[i] >= chr(33) and cadena[i] <= chr(47) or cadena[i] >= chr(58) and cadena[i] <= chr(255)):
                return True    


    def guardar(self):
        if len(self.entry1.get()) == 0 or len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "El Campo de Texto esta Vacio")
        elif self.soloNumeros(self.entry1.get()) == True or self.soloNumeros(self.entry2.get()) == True:
            messagebox.showerror("Mensaje de Advertencia", "El Campo de Texto contiene Caracteres no Validos")
        else:
            guardar=""
            self.text1.delete('1.0', END) 
            self.autoList.append(Auto(self.entry1.get(), self.combo1.get(), self.entry2.get(), self.combo2.get(), self.combo3.get(), self.combo4.get()))
            for i in range(0, len(self.autoList), 1):
                guardar+="ID:" + self.autoList[i].get_ID() + "\n" + "Nombre:" + self.autoList[i].get_Nombre() + "\n" + "Año:" + self.autoList[i].get_Año() + "\n" + "Combustible:" + self.autoList[i].get_Combustible() + "\n" + "Transmición:" + self.autoList[i].get_Transmision() + "\n" + "Color:" + self.autoList[i].get_Color() + "\n\n"
            self.text1.insert(INSERT, guardar)


    def salir(self):
        choise = messagebox.askquestion("Salír", "¿Estas seguro de salír?")
        if choise == 'yes':
            sys.exit()



class MainClass:
    objeto = Tk()
    Clase1(objeto)
    objeto.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#desarrollo de la interfaz grafica
root = Tk()
root.title('Sistema de Cursos con Base de Datos')
root.geometry("600x350")

miId = StringVar()
miNombre = StringVar()
miCodigo = StringVar()
miNota = StringVar()

def conexionBBDD():
    miConexion = sqlite3.connect("bdcursos")
    miCursor = miConexion.cursor()
    
    try:
        miCursor.execute('''
                         CREATE TABLE cursos (
                             ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             NOMBRE VARCHAR(50) NOT NULL,
                             CODIGO VARCHAR(50) NOT NULL,
                             NOTA INT NOT NULL
                         )
                         ''')
        messagebox.showinfo("CONEXION","Base de datos creada con exito")
    except:
        messagebox.showinfo("CONEXION","Conexion exitosa con la base de dtos")
    
        
def eliminarBBDD():
    miConexion = sqlite3.connect("bdcursos")
    miCursor = miConexion.cursor()
    if  messagebox.askyesno(message="La base de datos se perderá definitivamente. ¿Desea continuar?",title="Advertencia"):
        miCursor.execute("DROP TABLE cursos")
    else:
        pass
    limpiarDatos()
    mostrar()

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Está seguro que desea salir de la Aplicación?")
    if valor == "yes":
        root.destroy()
                                   
def limpiarDatos():
    miId.set("")
    miNombre.set("")
    miCodigo.set("")
    miNota.set("")
    
def mensaje():
    acerca='''
    Sistema de Cursos
    Version 1.0
    Tecnologia Python Tkinter
    '''
    messagebox.showinfo(title="Información", message=acerca)
    

######################## Metodos CRUD ####################

def crear():
    miConexion = sqlite3.connect("bdcursos")
    miCursor = miConexion.cursor()
    try:
        datos=miNombre.get(), miCodigo.get(),miNota.get()
        miCursor.execute("INSERT INTO cursos VALUES(NULL,?,?,?)",(datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexion con BBDD")
        pass
    limpiarDatos()
    mostrar()
    
def mostrar():
    miConexion = sqlite3.connect("bdcursos")
    miCursor=miConexion.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
        
    try:
        miCursor.execute("SELECT * FROM cursos")
        for row in miCursor:
            tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
    except:
        pass        

tree=ttk.Treeview(height=10,columns=('#0','#1','#2'))
tree.place(x=0,y=130)
tree.column('#0',width=100)
tree.heading('#0',text="ID", anchor=CENTER)
tree.heading('#1',text="Nombre del curso", anchor=CENTER)
tree.heading('#2',text="Código", anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3',text="Nota", anchor=CENTER)

def seleccionarUsandoClick(event):
    item=tree.identify('item',event.x, event.y)
    miId.set(tree.item(item,"text"))
    miNombre.set(tree.item(item,"values")[0])
    miCodigo.set(tree.item(item,"values")[1])
    miNota.set(tree.item(item,"values")[2])
    
tree.bind("<Double-1>",seleccionarUsandoClick)

def actualizar():
    miConexion = sqlite3.connect("bdcursos")
    miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(), miCodigo.get(),miNota.get()
        miCursor.execute("UPDATE cursos SET NOMBRE=?, CODIGO=?, NOTA=? WHERE ID="+miId.get(),(datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
        pass
    limpiarDatos()
    mostrar()
    
def borrar():
    miConexion = sqlite3.connect("bdcursos")
    miCursor=miConexion.cursor()
    try:
        if messagebox.askyesno(message="¿Realmente desea eliminar el registro?",title="Advertencia"):
            miCursor.execute("DELETE FROM cursos WHERE ID="+miId.get())
            miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al eliminar el registro")
        pass
    limpiarDatos()
    mostrar()

########################  COLOCAR ELEMENTOS EN LA VISTA ####################

############### creando lo menus ####################333
menubar = Menu(root)
menubasedat = Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/conectar Base de Datos",command=conexionBBDD)
menubasedat.add_command(label="Eliminar Base de Datos",command=eliminarBBDD)
menubasedat.add_command(label="Salir",command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudaMenu = Menu(menubar,tearoff=0)
ayudaMenu.add_command(label="Resetear Campos",command=limpiarDatos)
ayudaMenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudaMenu)

#######################creando etiquetas y cajas de texto######################
e1=Entry(root,textvariable=miId)

l2=Label(root,text="Nombre")
l2.place(x=50,y=10)
e2=Entry(root,textvariable=miNombre,width=50)
e2.place(x=100, y=10)

l3=Label(root,text="Código")
l3.place(x=50,y=40)
e3=Entry(root,textvariable=miCodigo)
e3.place(x=100, y=40)

l4=Label(root,text="Nota")
l4.place(x=280,y=40)
e4=Entry(root,textvariable=miNota,width=10)
e4.place(x=320, y=40)


###################### creando botones #####################33
b1 = Button(root, text="Crear Registro", command=crear)
b1.place(x=50, y=90)

b2 = Button(root, text="Modificar Registro", command=actualizar)
b2.place(x=180, y=90)

b3 = Button(root, text="Mostrar Lista", command=mostrar)
b3.place(x=320, y=90)

b4 = Button(root, text="Eliminar Registro", bg="red", command=borrar)
b4.place(x=450, y=90)


root.config(menu=menubar)

root.mainloop()
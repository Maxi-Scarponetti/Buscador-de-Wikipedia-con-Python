import wikipedia
import tkinter as tk

def buscar(event):
        contenido = caja_de_busqueda.get()
        resultado = wikipedia.summary(contenido, sentences=1)
        T.delete("1.0", tk.END)
        T.insert(tk.END, resultado)
        
ventana =tk.Tk()
ventana.geometry("300x300")
caja_de_busqueda = tk.Entryn(ventana)
caja_de_busqueda.place(x=0, y=0)
caja_de_busqueda.bind('<Return>', buscar)
T = tk.Text(ventana)
caja_de_busqueda.pack()
T.pack()
wikipedia.set_lang('es')
ventana.mainloop() 

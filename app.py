import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Digifico
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        Numero_ingresado = prompt("Ingrese un número", "Número")
        Numero_ingresado = int(Numero_ingresado)
        Numero_primo = 0

        for num in range(1, Numero_ingresado + 1):
            if num > 1:
                es_primo = True
                for i in range(2, num):
                    if (num % i) == 0:
                        es_primo = False
                        break
                    if es_primo:
                        Mensaje = f"Número primo encontrado: {num}"
                        alert("Mensaje", Mensaje)
                        Numero_primo += 1
                        break

        Mensaje = f"Se encontraron {Numero_primo} números primos hasta el {Numero_ingresado}"
        alert("Mensaje", Mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
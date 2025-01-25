
import customtkinter as ctk
import tkinter as tk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from Progresion_geometrica import calcular_progresion

class AplicacionConPestanas(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Álgebra")
        self.geometry("800x600")

        # Crear pestañas
        self.tabview = ctk.CTkTabview(self, width=700, height=600)
        self.tabview.pack(padx=20, pady=20)

        self.crear_pestanas()


    def crear_pestanas(self):
        # Crear y configurar las pestañas
        self.tab1 = self.tabview.add("Calcular n-ésimo término")
        self.tab2 = self.tabview.add("Teorema del binomio")

        # Configurar el contenido de la pestaña 1
        self.configurar_pestana1()

        # Configurar el contenido de la pestaña 2
        self.configurar_pestana2()

    

    def configurar_pestana1(self):
        # Dividir la pestaña en dos frames
        frame_formulario = ctk.CTkFrame(self.tab1)
        frame_formulario.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Formulario nombre
        label_indice = ctk.CTkLabel(frame_formulario, text="Índice del término")
        label_indice.pack(pady=8)
        self.entry_indice = ctk.CTkEntry(frame_formulario)
        self.entry_indice.pack(pady=8)

        #Boton de ingreso
        self.boton_ingresar=ctk.CTkButton(frame_formulario, text="Ingresar Indice", command= self.mostrar_progresion)
        self.boton_ingresar.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.label_resultado = ctk.CTkLabel(frame_formulario, text="")
        self.label_resultado.place(relx=0.5, rely=0.45, anchor=tk.CENTER)


    def mostrar_progresion(self):
        try:
            n = int((self.entry_indice.get()))

            resultado = calcular_progresion(n)

            self.label_resultado.configure(text=f"El término {n} es {resultado}")
        except ValueError:
            self.label_resultado.configure(text="Por favor ingrese un número válido")


    def configurar_pestana2(self):
        #Dividir la pestaña en tres frames

        #frame con imágenes
        frame_superior = ctk.CTkFrame(self.tab2)  #deja un frame arriba
        frame_superior.pack(side="top", fill="both", expand=True, padx=0, pady=0)

        frame_tarjetas = ctk.CTkFrame(frame_superior, fg_color="transparent", border_color="black", border_width=2)
        frame_tarjetas.pack(side="left", fill="both", expand=False, padx=10, pady=10)

        #frame con treeview y botones + label
        frame_inferior = ctk.CTkFrame(self.tab2)
        frame_inferior.pack(side="bottom", fill="both", expand=True, padx=0, pady=0)   # deja un frame abajo

        #Este será un frame entre medio de los otros 2 frames, el cual estará en el espacio sobrante del 'frame_inferior'.
        frame_boton = ctk.CTkFrame(self.tab2)  
        frame_boton.pack(fill="both", expand=True, padx=0, pady=5)


        #Boton de generar boleta
        self.boton_boleta=ctk.CTkButton(frame_inferior, text="Generar boleta")
        self.boton_boleta.pack(side="bottom", expand=False, padx=5, pady=15)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = AplicacionConPestanas()
    app.mainloop()

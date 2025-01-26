
import customtkinter as ctk
import tkinter as tk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from Progresion_geometrica import calcular_progresion
from Binomios import ciclo_repetitivo, binomio_directo
import math

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
        # Creacion del frame
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
        # Creacion del frame
        frame_formulario2 = ctk.CTkFrame(self.tab2)
        frame_formulario2.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Campo para n
        label_n = ctk.CTkLabel(frame_formulario2, text="Ingrese n:")
        label_n.pack(pady=8)
        self.entry_n = ctk.CTkEntry(frame_formulario2)
        self.entry_n.pack(pady=8)

        # Campo para a
        label_a = ctk.CTkLabel(frame_formulario2, text="Ingrese a:")
        label_a.pack(pady=8)
        self.entry_a = ctk.CTkEntry(frame_formulario2)
        self.entry_a.pack(pady=8)

        # Campo para b
        label_b = ctk.CTkLabel(frame_formulario2, text="Ingrese b:")
        label_b.pack(pady=8)
        self.entry_b = ctk.CTkEntry(frame_formulario2)
        self.entry_b.pack(pady=8)

        # Botón para calcular
        boton_calcular = ctk.CTkButton(frame_formulario2, text="Calcular", command=self.mostrar_binomios)
        boton_calcular.pack(pady=10)

        # Resultado
        self.label_resultado2 = ctk.CTkLabel(frame_formulario2, text="")
        self.label_resultado2.pack(pady=8)


    def mostrar_binomios(self):
        try:
            # Obtener valores ingresados por el usuario
            n = int(self.entry_n.get())
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())

            # Cálculo del teorema del binomio
            resultado_ciclo = ciclo_repetitivo(a, b, n)
            resultado_directo = binomio_directo(a, b, n)

            # Mostrar resultados
            resultado_texto = (f"Resultado usando el teorema del binomio: {resultado_ciclo}\n"
                               f"Resultado usando el binomio directo: {resultado_directo}\n")

            if math.isclose(float(resultado_ciclo), float(resultado_directo), rel_tol=1e-9):
                resultado_texto += "\n¡Los resultados coinciden!"
            else:
                resultado_texto += "\nHay una discrepancia en los resultados."

            self.label_resultado2.configure(text=resultado_texto)

        except ValueError:
            self.label_resultado2.configure(text="Por favor, ingrese valores válidos.")
        except Exception as e:
            self.label_resultado2.configure(text=f"Error: {str(e)}")


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = AplicacionConPestanas()
    app.mainloop()

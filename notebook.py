#importacion de Librerias
import tkinter as tk
from tkinter import messagebox, ttk

#Crear ventana principal
ventanaPrincipal= tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("400x600")

#crear contenedor Notebook(pestañas)
pestañas= ttk.Notebook(ventanaPrincipal)

#Crear Frames(uno por pestaña)
frame_Pacientes =ttk.Frame(pestañas)
frame_Doctores = ttk.Frame(pestañas)

#agregar pestañas al notebook
pestañas.add(frame_Pacientes, text="Pacientes")
pestañas.add(frame_Doctores, text="Doctores")

#mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")

# Nombre
labelNombre =tk.Label(frame_Pacientes, text="Nombre completo: ")
labelNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreP = tk.Entry(frame_Pacientes)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Fecha de nacimiento
labelFechaN =tk.Label(frame_Pacientes, text="Fecha de nacimiento: ")
labelFechaN.grid(row=1, column=0, sticky="w", padx=5, pady=5)
fechaN = tk.Entry(frame_Pacientes)
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Edad
labelEdad= tk.Label(frame_Pacientes, text="Edad:")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadP= tk.Entry(frame_Pacientes, state="readonly")
edadP.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Genero
labelGenero = tk.Label(frame_Pacientes, text="Genero: ")
labelGenero.grid(row=3, column=0, padx=5, pady=5, sticky="w")

#radiobuttons XD
genero=tk.StringVar()
genero.set("Femenino")
radioMasculino= ttk.Radiobutton(frame_Pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)

radioFemenino= ttk.Radiobutton(frame_Pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)

# Grupo sanguineo
labelGrupoSanguineo = tk.Label(frame_Pacientes, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryLabelGrupoSanguineo = tk.Entry(frame_Pacientes)
entryLabelGrupoSanguineo.grid(row=5, column=1, sticky="w", padx=5, pady=5)

# Combobox :0
labelTipoSeguro = tk.Label(frame_Pacientes, text="Tipo de seguro")
labelTipoSeguro.grid(row=6, column=0, sticky="w", padx=5, pady=5)
tipo_seguro = tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro = ttk.Combobox(frame_Pacientes, values=["Publico", "Privado", "Ninguno"], textvariable= tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", padx=5, pady=5)

labelCentroMedico = tk.Label(frame_Pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centro_medico = tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico = ttk.Combobox(frame_Pacientes, values=["Hospital Central", "Clinica Norte", "Centro sur"], textvariable= centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)



ventanaPrincipal.mainloop()
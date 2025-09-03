#importacion de libreria
import tkinter as tk
from tkinter import ttk,messagebox
from datetime import datetime

#crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("libro de paciente y doctores")
ventana_principal.geometry("700x560")

# funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio =''.join(filter(str.isdigit, texto))
    formato_final=""
    
    if len(limpio)>8:
        limpio=limpio[:8]
        
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
        
    elif len(limpio):
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
        
    else:
        formato_final = limpio
    
    
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0, formato_final)
        
    if len(fechaN.get())==10:
        fecha_actual = datetime.now().date()
        fecha_nacimiento = datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year 
        edadVar.set(edad)
    else:
        edadVar.set("")

    return True


#crear contenedor notebook
pestañas=ttk.Notebook(ventana_principal)

#crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
frame_doctores=ttk.Frame(pestañas)

#agregar pestaña al notebook
pestañas.add(frame_pacientes, text="pacientes")
pestañas.add(frame_doctores, text="doctores")


#mostrar las pestañas en la ventana 
pestañas.pack(expand=True, fill="both")

#nombre
labelNombre=tk.Label(frame_pacientes, text="Nombre completo: ")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)

#fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes, text="Fecha de Nacimiento")
labelFechaN.grid(row=1,column=0, sticky="w", pady=5, padx=5)
validacion_fecha = ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes, validate="key", validatecommand= (validacion_fecha, '%P'))
fechaN.grid(row=1, column=1, sticky="w", pady=5, padx=5)

#edad(readol)
labelEdad=tk.Label(frame_pacientes, text="Edad")
labelEdad.grid(row=2,column=0, sticky="w", pady=5, padx=5)
edadVar=tk.StringVar()
edad=tk.Entry(frame_pacientes, textvariable= edadVar, state="readonly")
edad.grid(row=2, column=1, sticky="w", pady=5, padx=5)

#genero
labelgenero=tk.Label(frame_pacientes, text="Genero")
labelgenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("femenino")#valor por defecto
redioFemenino=ttk.Radiobutton(frame_pacientes, text="femenino", variable=genero, value="femenino")
redioFemenino.grid(row=3, column=1, sticky="w", pady=5, padx=5)

radioMasculino=ttk.Radiobutton(frame_pacientes, text="masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=4, column=1, sticky="w", pady=5, padx=5)


#grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text="grupo sanguineo")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryLabelGrupoSanginineo=tk.Entry(frame_pacientes)
entryLabelGrupoSanginineo.grid(row=5, column=1, sticky="w", pady=5, padx=5)

#tipo de seguro
labelTipoSeguro = tk.Label(frame_pacientes, text="Tipo de seguro")
labelTipoSeguro.grid(row=6, column=0, sticky="w", padx=5, pady=5)
tipo_seguro = tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro = ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable= tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", padx=5, pady=5)

#centro medico
labelCentroMedico = tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centro_medico = tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico = ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro sur"], textvariable= centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)

#frame para los botones
btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")

#boton registrar
btn_registrar=tk.Button(btn_frame, text="Registrar", command="", bg="lightblue")
btn_registrar.grid(row=0,column=0, padx=5)

#boton Elimnar
btn_eliminar = tk.Button(btn_frame, text="Eliminar", command="", bg="pink")
btn_eliminar.grid(row=0, column=1, padx=5)

#crear treeview para mostrar pacientes
treeview = ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")

#definir encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo sanguineo")
treeview.heading("TipoS", text="Tipo de Seguro")
treeview.heading("CentroM", text="Centro Medico")


# definir anchos de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50, anchor="center")
treeview.column("Genero",width=60, anchor="center")
treeview.column("GrupoS",width=100, anchor="center")
treeview.column("TipoS",width=100, anchor="center")
treeview.column("CentroM",width=120)

#ubicar el treeview en la cuadricula
treeview.grid(row=10, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
#scrolbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
scroll_y.grid(row=10, column=2, sticky="ns")


#Para el frame Doctores

#titulo
titulo = tk.Label(frame_doctores, text="Registro de Doctores")

#nombre
labelNombreDoctores=tk.Label(frame_doctores, text="Nombre completo: ")
labelNombreDoctores.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreD=tk.Entry(frame_doctores)
nombreD.grid(row=0, column=1, sticky="w", pady=5, padx=5)

#especialidad
labelEspecialidad=tk.Label(frame_doctores, text="Especialidad:")
labelEspecialidad.grid(row=2, column=0, sticky="w", padx=5, pady=10)
especialidad=tk.StringVar()
especialidad.set("Neurologia")
comboEspecialidad=ttk.Combobox(frame_doctores, values=["Neurologia","Cardiologia","Pediatria","Traumatologia"], textvariable=especialidad)
comboEspecialidad.grid(row=2, column=1, sticky="w", padx=5, pady=10)

#edad
labelEdadDoctores=tk.Label(frame_doctores, text="Edad:")
labelEdadDoctores.grid(row=3, column=0, padx=5, pady=10, sticky="w")
spinEdad=ttk.Spinbox(frame_doctores, from_=0, to=99)
spinEdad.grid(row=3, column=1, padx=5, pady=10, sticky="w")

#Telefono
labelTelefonoD=tk.Label(frame_doctores, text="Telefono:")
labelTelefonoD.grid(row=4, column=0, sticky="w", pady=10, padx=5)
telefonoP=tk.Entry(frame_doctores)
telefonoP.grid(row=4, column=1, sticky="w", pady=10, padx=5)

#Frame para botones
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="w")

#registrar
btn_registrarD=tk.Button(btn_frame, text="Registrar", command="", bg="lightblue")
btn_registrarD.grid(row=5, column=0, padx=5)

#eliminar
btn_eliminarD=tk.Button(btn_frame, text="Eliminar", command="", bg="pink")
btn_eliminarD.grid(row=5, column=1, padx=5)


#crear treeview ara mostrar doctores
treeview=ttk.Treeview(frame_doctores,columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("Especialidad", text="Especialidad")
treeview.heading("Edad", text="Edad")
treeview.heading("Telefono", text="Telefono")

#anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("Especialidad", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Telefono", width=60, anchor="center")
treeview.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
scroll_y.grid(row=6, column=2, sticky="nsew")




ventana_principal.mainloop()
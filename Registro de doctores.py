import tkinter as tk
from tkinter import messagebox
 
def nuevoDoctor():
    v_Registro=tk.Toplevel(Principal)
    v_Registro.title("Sistema de Registro de Doctores")
    v_Registro.geometry("400x400")
    v_Registro.configure(bg="#dfd3dc")
   
    nombreLabel=tk.Label(v_Registro,text="Nombre completo : ",bg="#dfd3dc")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w",)
    entryNombre=tk.Entry(v_Registro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    entryNombre.configure(bg="#dfd3dc")
   
    direccionLabel=tk.Label(v_Registro,text="Direccion: ", bg="#dfd3dc")
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w",)
    entryDireccion=tk.Entry(v_Registro)
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    entryDireccion.configure(bg="#dfd3dc")
   
    telefonoLabel=tk.Label(v_Registro,text="Telefono: ", bg="#dfd3dc")
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w",)
    entryTelefono=tk.Entry(v_Registro)
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    entryTelefono.configure(bg="#dfd3dc")
   
    especialidadLabel=tk.Label(v_Registro, text="Especialidad:", bg="#dfd3dc")
    especialidadLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    especialidad=tk.StringVar(value="Pediatria")
    especialidad=tk.StringVar(value="Cardiologia")
    especialidad=tk.StringVar(value="Neurologia")
    especialidad=tk.StringVar(value="Otra")
   
    rbPediatria=tk.Radiobutton(v_Registro, text="pediatria", variable=especialidad, value="pediatria", bg="#dfd3dc")
    rbPediatria.grid(row=3, column=1, sticky="w")    
   
    rbCardiologia=tk.Radiobutton(v_Registro, text="Cardiologia", variable=especialidad, value="Cardiologia", bg="#dfd3dc")
    rbCardiologia.grid(row=4, column=1, sticky="w")
   
    rbNeurologia=tk.Radiobutton(v_Registro, text="Neurologia", variable=especialidad, value="Neurologia", bg="#dfd3dc")
    rbNeurologia.grid(row=5, column=1, sticky="w")
    
    rbOtro=tk.Radiobutton(v_Registro, text="Otro", variable=especialidad, value="Otro", bg="#dfd3dc")
    rbOtro.grid(row=6, column=1, sticky="w")
   
    turnoLabel=tk.Label(v_Registro, text="Disponibilidad", bg="#dfd3dc")
    turnoLabel.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    
    mañana=tk.BooleanVar()
    tarde=tk.BooleanVar()
    noche=tk.BooleanVar()
   
    cdMañana=tk.Checkbutton(v_Registro,text="Mañana", variable=mañana, bg="#dfd3dc")
    cdMañana.grid(row=7, column=1, sticky="w")
    
    cdTarde=tk.Checkbutton(v_Registro,text="Tarde", variable=tarde, bg="#dfd3dc")
    cdTarde.grid(row=8, column=1, sticky="w")
    
    cdNoche=tk.Checkbutton(v_Registro,text="Noche", variable=noche, bg="#dfd3dc")
    cdNoche.grid(row=9, column=1, sticky="w")
   
    def registrarDatos():
        disponibilidad=[]
        if mañana.get():
            disponibilidad.append("Mañana")
        if tarde.get():
            disponibilidad.append("Tarde")
        if noche.get():
            disponibilidad.append("Noche")
        if len(disponibilidad)>0:
            disponibilidadTexto=','.join(disponibilidad)
        else:
            disponibilidadTexto='No esta disponible'
        info = (
            f"Nombre Completo: {entryNombre.get()}\n"
            f"Dirección: {entryDireccion.get()}\n"
            f"Telefono: {entryTelefono.get()}\n"
            f"Especialidad: {especialidad.get()}\n"
            f"Disponibilidad: {disponibilidadTexto}\n"
            )
        messagebox.showinfo("Datos Registrados",info)
        v_Registro.destroy()
    btnRegistrar=tk.Button(v_Registro, text="Guardar Datos", command=registrarDatos)
    btnRegistrar.grid(row=15, column=1, columnspan=5, pady=18)
   
       
Principal = tk.Tk ()
Principal.title("Registro de Doctores")
Principal.geometry("600x400")
Principal.configure(bg="#d8c5d0")
 
barraMenu=tk.Menu(Principal)
Principal.config(menu=barraMenu)
 
menuDoctores=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=nuevoDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=Principal.quit)
 
Principal.mainloop()
import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesion")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Encabezado
        tk.Label(root, text="Bienvenido al sistema", font=("Arial", 16, "bold")).pack(pady=16)

        # Campo de texto
        tk.Label(root, text="Ingresa tu nombre de usuario:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Ingresa tu contraseña:").pack()
        self.password_entry = tk.Entry(root, show="*")  
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Iniciar Sesion", command=self.login).pack(pady=20)

   
    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        
        if not usuario or not password:
            messagebox.showwarning("Faltan datos", "Favor de ingresar el usuario y la contraseña")
            return  

     
        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario}")
            self.root.destroy()
        else:
            messagebox.showerror("Acceso denegado", "Tus datos no son correctos")



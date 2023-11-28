import tkinter as tk
import lexico as lx
import sintactio as sn

root = tk.Tk()
root.title("Analizador PHP")
root.resizable(False, False)

# Obtener el ancho y alto de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Obtener el ancho y alto de la ventana
ancho_ventana = 1100  # Ancho que estableciste para la ventana
alto_ventana = 800  # Alto que estableciste para la ventana

# Calcular la posición para centrar la ventana
posicion_x = (ancho_pantalla - ancho_ventana) // 2
posicion_y = (alto_pantalla - alto_ventana) // 2

# Establecer la posición de la ventana en el centro
root.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x-20}+{posicion_y-30}")

etiqueta = tk.Label(root, text="ANALIZADOR DE CÓDIGO PHP")
etiqueta.pack(padx=10, pady=10)

frameTrabajo = tk.Frame(root, borderwidth=2, relief="groove")
frameTrabajo.pack(padx=5, pady=5, fill="both")

frameAnalisis = tk.Frame(frameTrabajo, borderwidth=2, relief="ridge")
frameAnalisis.pack(side=tk.LEFT, padx=5, pady=5, fill="both")

frameBotonesCod = tk.Frame(frameAnalisis, borderwidth=2, relief="flat")
frameBotonesCod.pack(padx=5, pady=5)

frameCodigo = tk.Frame(frameAnalisis, borderwidth=2, relief="flat")
frameCodigo.pack(padx=5, pady=5)

frameResultado = tk.Frame(frameTrabajo, borderwidth=2, relief="ridge")
frameResultado.pack(side=tk.RIGHT, padx=5, pady=5, fill="both")

frameLexico = tk.Frame(frameResultado, borderwidth=2, relief="flat")
frameLexico.pack(padx=5, pady=5, fill="both")

frameSintactico = tk.Frame(frameResultado, borderwidth=2, relief="flat")
frameSintactico.pack(padx=5, pady=5, fill="both")

def cargarArchivo():
    limpiar()
    codigo.insert(tk.END, "COPIANDO ARCHIVO...")

botonArchivo = tk.Button(frameBotonesCod, text="Cargar archivo", command=cargarArchivo)
botonArchivo.pack(side=tk.LEFT, padx=20, pady=10)

def limpiar():
    codigo.delete("1.0", tk.END)

# Botón para obtener el texto ingresado
botonLimpiar = tk.Button(frameBotonesCod, text="Limpiar entrada", command=limpiar)
botonLimpiar.pack(side=tk.LEFT, padx=20, pady=10)

codigo = tk.Text(frameCodigo, height=60, width=60, font=("Arial", 11))
codigo.pack(padx=20, pady=10)

def analizarLexico():
    resultadoLex.config(state=tk.NORMAL)
    resultadoLex.delete("1.0", tk.END)
    code = codigo.get("1.0", tk.END)
    tokens = lx.lexico(code)
    resultadoLex.insert(tk.END, tokens)
    resultadoLex.config(state=tk.DISABLED)

botonLexico = tk.Button(frameLexico, text="Analizar Léxico", command=analizarLexico)
botonLexico.pack(padx=20, pady=10)

resultadoLex = tk.Text(frameLexico, height=17, width=60, font=("Arial", 11))
resultadoLex.pack(padx=20, pady=10)
resultadoLex.config(state=tk.DISABLED)

def analizarSintaxis():
    resultadoSin.config(state=tk.NORMAL)
    resultadoSin.delete("1.0", tk.END)
    code = codigo.get("1.0", tk.END)
    resultado = sn.sintactico(code)
    resultadoSin.insert(tk.END, code)
    resultadoSin.config(state=tk.DISABLED)

botonSintactico = tk.Button(frameSintactico, text="Analizar Sintáxis", command=analizarSintaxis)
botonSintactico.pack(padx=20, pady=10)

resultadoSin = tk.Text(frameSintactico, height=17, width=60, font=("Arial", 11))
resultadoSin.pack(padx=20, pady=10)
resultadoSin.config(state=tk.DISABLED)

root.mainloop()
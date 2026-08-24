import tkinter as tk
from tkinter import ttk, messagebox


leyes = {
    "Ley de Boyle": {
        "formula": "P1 × V1 = P2 × V2",
        "variables": ["P1", "V1", "P2", "V2"]
    },

    "Ley de Charles": {
        "formula": "V1 / T1 = V2 / T2",
        "variables": ["V1", "T1", "V2", "T2"]
    },

    "Ley de Gay-Lussac": {
        "formula": "P1 / T1 = P2 / T2",
        "variables": ["P1", "T1", "P2", "T2"]
    }
}

def elegir_variable():

    ley = combo_ley.get()

    if ley == "":
        messagebox.showerror("Error", "Elegí una ley")
        return

    ventana_variable = tk.Toplevel()
    ventana_variable.title(ley)
    ventana_variable.geometry("350x350")

    tk.Label(
        ventana_variable,
        text=ley,
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        ventana_variable,
        text=leyes[ley]["formula"],
        font=("Arial", 12)
    ).pack(pady=10)

    tk.Label(
        ventana_variable,
        text="¿Qué querés calcular?",
        font=("Arial", 12)
    ).pack(pady=10)

    variable_elegida = tk.StringVar()

    for variable in leyes[ley]["variables"]:

        tk.Radiobutton(
            ventana_variable,
            text=variable,
            variable=variable_elegida,
            value=variable
        ).pack()


    def siguiente():

        if variable_elegida.get() == "":
            messagebox.showerror(
                "Error",
                "Elegí qué querés calcular"
            )
            return

        abrir_calculadora(
            ley,
            variable_elegida.get()
        )


    tk.Button(
        ventana_variable,
        text="SIGUIENTE",
        command=siguiente,
        font=("Arial", 11, "bold")
    ).pack(pady=20)

def abrir_calculadora(ley, incognita):

    calculadora = tk.Toplevel()
    calculadora.title("Calcular " + incognita)
    calculadora.geometry("350x450")

    tk.Label(
        calculadora,
        text="Calcular " + incognita,
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        calculadora,
        text=leyes[ley]["formula"],
        font=("Arial", 12)
    ).pack(pady=10)

    entradas = {}

    for variable in leyes[ley]["variables"]:

        if variable != incognita:

            tk.Label(
                calculadora,
                text="Ingresá " + variable
            ).pack()

            entrada = tk.Entry(calculadora)
            entrada.pack(pady=5)

            entradas[variable] = entrada


    def calcular():

        try:

            datos = {}

            for variable in entradas:
                datos[variable] = float(
                    entradas[variable].get()
                )

            if ley == "Ley de Boyle":

                if incognita == "P1":
                    resultado = (
                        datos["P2"] * datos["V2"]
                        / datos["V1"]
                    )

                elif incognita == "V1":
                    resultado = (
                        datos["P2"] * datos["V2"]
                        / datos["P1"]
                    )

                elif incognita == "P2":
                    resultado = (
                        datos["P1"] * datos["V1"]
                        / datos["V2"]
                    )

                elif incognita == "V2":
                    resultado = (
                        datos["P1"] * datos["V1"]
                        / datos["P2"]
                    )

            elif ley == "Ley de Charles":

                if incognita == "V1":
                    resultado = (
                        datos["V2"] * datos["T1"]
                        / datos["T2"]
                    )

                elif incognita == "T1":
                    resultado = (
                        datos["V1"] * datos["T2"]
                        / datos["V2"]
                    )

                elif incognita == "V2":
                    resultado = (
                        datos["V1"] * datos["T2"]
                        / datos["T1"]
                    )

                elif incognita == "T2":
                    resultado = (
                        datos["V2"] * datos["T1"]
                        / datos["V1"]
                    )

            elif ley == "Ley de Gay-Lussac":

                if incognita == "P1":
                    resultado = (
                        datos["P2"] * datos["T1"]
                        / datos["T2"]
                    )

                elif incognita == "T1":
                    resultado = (
                        datos["P1"] * datos["T2"]
                        / datos["P2"]
                    )

                elif incognita == "P2":
                    resultado = (
                        datos["P1"] * datos["T2"]
                        / datos["T1"]
                    )

                elif incognita == "T2":
                    resultado = (
                        datos["P2"] * datos["T1"]
                        / datos["P1"]
                    )


            label_resultado.config(
                text=f"Resultado:\n{incognita} = {resultado:.2f}"
            )


        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingresá todos los datos correctamente"
            )

        except ZeroDivisionError:
            messagebox.showerror(
                "Error",
                "No se puede dividir por 0"
            )


    tk.Button(
        calculadora,
        text="CALCULAR",
        command=calcular,
        font=("Arial", 12, "bold")
    ).pack(pady=20)


    label_resultado = tk.Label(
        calculadora,
        text="Resultado:",
        font=("Arial", 14, "bold")
    )

    label_resultado.pack(pady=10)



# VENTANA PRINCIPAL
ventana = tk.Tk()

ventana.title("Calculadora de Leyes de los Gases")
ventana.geometry("400x300")


tk.Label(
    ventana,
    text="LEYES DE LOS GASES",
    font=("Arial", 18, "bold")
).pack(pady=30)


tk.Label(
    ventana,
    text="Elegí una ley:",
    font=("Arial", 12)
).pack()


combo_ley = ttk.Combobox(
    ventana,
    values=list(leyes.keys()),
    state="readonly"
)

combo_ley.pack(pady=10)


tk.Button(
    ventana,
    text="SIGUIENTE",
    command=elegir_variable,
    font=("Arial", 12, "bold")
).pack(pady=20)


ventana.mainloop()
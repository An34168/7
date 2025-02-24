import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
def obtener_imagen():
    response = requests.get("https://randomfox.ca/floof/")
    if response.status_code == 200:
        data = response.json()
        url_imagen = data["image"]

        img_response = requests.get(url_imagen)
        if img_response.status_code == 200:
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.resize((400, 300), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img_data)

            label_imagen.config(image=img_tk)
            label_imagen.image = img_tk
    else:
        print("Error to get image")
ventana = tk.Tk()
ventana.title("Fox image generator 🦊")
ventana.geometry("450x400")

label_imagen = tk.Label(ventana)
label_imagen.pack()

boton_cambiar = tk.Button(ventana, text="🔄 New image", command=obtener_imagen)
boton_cambiar.pack(pady=10)

obtener_imagen()

ventana.mainloop()

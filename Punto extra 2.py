import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "2EHFyh3NDh7WfCtDhxxHAcX2xmMaIfXa6Nf0KJz2"

def fetch_nasa_picture():
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        image_url = data.get("url")
        title = data.get("title", "No Title Available")
        description = data.get("explanation", "No Description Available")

        img_response = requests.get(image_url, stream=True)  
        if img_response.status_code == 200:
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.resize((500, 400), Image.Resampling.LANCZOS)
      
            img_tk = ImageTk.PhotoImage(img_data)
            label_image.configure(image=img_tk)
            label_image.image = img_tk  
            label_title.config(text=f"🌌 {title}")
            label_description.config(text=description[:300] + "...")  
        else:
            label_title.config(text="Error loading image")
            label_description.config(text="Could not download image from NASA.")
    else:
        label_title.config(text="API Error")
        label_description.config(text="Could not fetch data from NASA API.")


window = tk.Tk()
window.title("📸 NASA Picture of the Day 🚀")
window.geometry("550x650")


label_title = tk.Label(window, text="NASA Picture of the Day", font=("Arial", 14, "bold"))
label_title.pack()


label_image = tk.Label(window)
label_image.pack()

label_description = tk.Label(window, text="", wraplength=500, justify="center")
label_description.pack(pady=10)

button_refresh = tk.Button(window, text="🔄 Load New Image", command=fetch_nasa_picture)
button_refresh.pack(pady=10)

fetch_nasa_picture()

window.mainloop()


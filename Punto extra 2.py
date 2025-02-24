import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# 🚀 Enter your NASA API Key
API_KEY = "2EHFyh3NDh7WfCtDhxxHAcX2xmMaIfXa6Nf0KJz2"

# Function to fetch NASA's Astronomy Picture of the Day
def fetch_nasa_picture():
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        image_url = data.get("url")
        title = data.get("title", "No Title Available")
        description = data.get("explanation", "No Description Available")

        # Download the image
        img_response = requests.get(image_url, stream=True)  # Use stream to avoid caching
        if img_response.status_code == 200:
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.resize((500, 400), Image.Resampling.LANCZOS)
            
            # Update image and text
            img_tk = ImageTk.PhotoImage(img_data)
            label_image.configure(image=img_tk)
            label_image.image = img_tk  # Keep reference to avoid garbage collection
            label_title.config(text=f"🌌 {title}")
            label_description.config(text=description[:300] + "...")  # Limit description length
        else:
            label_title.config(text="Error loading image")
            label_description.config(text="Could not download image from NASA.")
    else:
        label_title.config(text="API Error")
        label_description.config(text="Could not fetch data from NASA API.")

# Tkinter window setup
window = tk.Tk()
window.title("📸 NASA Picture of the Day 🚀")
window.geometry("550x650")

# Title Label
label_title = tk.Label(window, text="NASA Picture of the Day", font=("Arial", 14, "bold"))
label_title.pack()

# Image Label
label_image = tk.Label(window)
label_image.pack()

# Description Label
label_description = tk.Label(window, text="", wraplength=500, justify="center")
label_description.pack(pady=10)

# Button to fetch new image
button_refresh = tk.Button(window, text="🔄 Load New Image", command=fetch_nasa_picture)
button_refresh.pack(pady=10)

# Load the first image when the app starts
fetch_nasa_picture()

# Run Tkinter event loop
window.mainloop()


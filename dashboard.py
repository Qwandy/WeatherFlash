from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import os
from dotenv import load_dotenv
from tkinter import messagebox

load_dotenv()

class gui():
    
    def __init__(self):
        pass

    def _fetch_info(self, location):

        # api details 
        url = 'https://api.openweathermap.org/data/2.5/weather'
        key = os.getenv("API_KEY")
        request_url = f"{url}?appid={key}&q={location}"
        response = requests.get(request_url)

        # request logic 
        if response.status_code == 200:
            data_weather = str(response.json()['weather'][0]['main'])
            data_main = response.json()['main']
            data_main_temp = int(response.json()['main']['temp']) - 273.15
            data_main_humidity = str(response.json()['main']['humidity'])
            data_wind = str(response.json()['wind']['speed'])
            
        else:
            print("Error", response.status_code)
        return data_weather, data_main_temp, data_main_humidity, data_wind
    
    def run_gui(self):
    
        root = Tk()
        root.title('Weather Flash')

        # mainframe
        mainframe = ttk.Frame(root, padding = "3 3 12 12")
        mainframe.grid(column=0, row=0, sticky = (N, W, E, S))
        root.columnconfigure(0, weight = 1)
        root.rowconfigure(0, weight = 1)

        # logic dictating what weather image to display
        weather, temp, humidity, wind = self._fetch_info("Didcot")
        if weather == "Fog":
            image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/fog.jpeg").resize((30,30))
            photo = ImageTk.PhotoImage(image)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=0)
        elif weather == "Snow":
            image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/snow.jpeg").resize((30,30))
            photo = ImageTk.PhotoImage(image)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=0)
        elif weather == "Lightning":
            image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/lightning.jpeg").resize((30,30))
            photo = ImageTk.PhotoImage(image)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=0)
        elif weather == "Rain":
            image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/rain.jpeg").resize((30,30))
            photo = ImageTk.PhotoImage(image)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=0)
        elif weather == "Clear":
            image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/clear.jpeg").resize((30,30))
            photo = ImageTk.PhotoImage(image)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=0)
        elif weather == "Mist":
            image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/mist.jpeg").resize((30,30))
            photo = ImageTk.PhotoImage(image)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=0)
        elif weather == "Clouds":
            image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/clouds.jpeg").resize((30,30))
            photo = ImageTk.PhotoImage(image)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=0)
        else:
            image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/clear.jpeg").resize((30,30))
            photo = ImageTk.PhotoImage(image)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=0)
            
        # weather widget
        ttk.Label(mainframe, text = f"The weather is currently: {weather}").grid(column=1, row=0, sticky=W)

        # temperature widget
        ttk.Label(mainframe, text = f"The temperature is currently: {temp:.02f}°C").grid(column=1, row=1, sticky=W)
        image_thermo = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/thermo.jpeg").resize((30,30))
        photo_thermo = ImageTk.PhotoImage(image_thermo)
        lbl_thermo = Label(mainframe, image = photo_thermo)
        lbl_thermo.image = photo
        lbl_thermo.grid(column=0,row=1)

        # humidity widget
        ttk.Label(mainframe, text = f"The humidity is currently: {humidity}%").grid(column=1, row=2, sticky=W)
        image_water = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/water.jpeg").resize((30,30))
        photo_water = ImageTk.PhotoImage(image_water)
        lbl_water = Label(mainframe, image = photo_water)
        lbl_water.image = photo
        lbl_water.grid(column=0,row=2)

        # wind widget
        ttk.Label(mainframe, text = f"The wind speed is currently: {wind} km/h").grid(column=1, row=3, sticky=W)
        image_wind = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/wind.jpeg").resize((30,30))
        photo_wind = ImageTk.PhotoImage(image_wind)
        lbl_wind = Label(mainframe, image = photo_wind)
        lbl_wind.image = photo
        lbl_wind.grid(column=0, row=3)

        root.mainloop()


test = gui().run_gui()

'''
# function call to fetch data I want to display
weather, temp, humidity, wind = fetch_info("Didcot")

# root square
root = Tk()
root.title('Weather Flash')

# mainframe
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

# logic dictating what weather image to display
if weather == "Fog":
    image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/fog.jpeg").resize((30,30))
    photo = ImageTk.PhotoImage(image)

    lbl = Label(mainframe, image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=0)
elif weather == "Snow":
    image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/snow.jpeg").resize((30,30))
    photo = ImageTk.PhotoImage(image)

    lbl = Label(mainframe, image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=0)
elif weather == "Lightning":
    image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/lightning.jpeg").resize((30,30))
    photo = ImageTk.PhotoImage(image)

    lbl = Label(mainframe, image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=0)
elif weather == "Rain":
    image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/rain.jpeg").resize((30,30))
    photo = ImageTk.PhotoImage(image)

    lbl = Label(mainframe, image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=0)
elif weather == "Clear":
    image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/clear.jpeg").resize((30,30))
    photo = ImageTk.PhotoImage(image)

    lbl = Label(mainframe, image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=0)
elif weather == "Mist":
    image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/mist.jpeg").resize((30,30))
    photo = ImageTk.PhotoImage(image)

    lbl = Label(mainframe, image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=0)
elif weather == "Clouds":
    image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/clouds.jpeg").resize((30,30))
    photo = ImageTk.PhotoImage(image)

    lbl = Label(mainframe, image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=0)
else:
    image = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/clear.jpeg").resize((30,30))
    photo = ImageTk.PhotoImage(image)

    lbl = Label(mainframe, image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=0)
    
# weather widget
ttk.Label(mainframe, text = f"The weather is currently: {weather}").grid(column=1, row=0, sticky=W)

# temperature widget
ttk.Label(mainframe, text = f"The temperature is currently: {temp:.02f}°C").grid(column=1, row=1, sticky=W)
image_thermo = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/thermo.jpeg").resize((30,30))
photo_thermo = ImageTk.PhotoImage(image_thermo)
lbl_thermo = Label(mainframe, image = photo_thermo)
lbl_thermo.image = photo
lbl_thermo.grid(column=0,row=1)

# humidity widget
ttk.Label(mainframe, text = f"The humidity is currently: {humidity}%").grid(column=1, row=2, sticky=W)
image_water = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/water.jpeg").resize((30,30))
photo_water = ImageTk.PhotoImage(image_water)
lbl_water = Label(mainframe, image = photo_water)
lbl_water.image = photo
lbl_water.grid(column=0,row=2)

# wind widget
ttk.Label(mainframe, text = f"The wind speed is currently: {wind} km/h").grid(column=1, row=3, sticky=W)
image_wind = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/wind.jpeg").resize((30,30))
photo_wind = ImageTk.PhotoImage(image_wind)
lbl_wind = Label(mainframe, image = photo_wind)
lbl_wind.image = photo
lbl_wind.grid(column=0, row=3)

root.mainloop()'''




from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import os
from dotenv import load_dotenv
from tkinter import messagebox
from bs4 import BeautifulSoup as bs
import random

load_dotenv()

dict_weather = {
    "Fog": "/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/fog.jpeg",
    "Snow": "/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/snow.jpeg",
    "Lightning": "/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/lightning.jpeg",
    "Rain": "/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/rain.jpeg",
    "Clear": "/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/clear.jpeg",
    "Mist": "/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/mist.jpeg",
    "Clouds": "/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/clouds.jpeg"
}

class gui():
    ''' The base class for running the Tkinter based GUI for OpenWeatherMap API. '''
    def __init__(self):
        self.state = 0
        self.weather = None
        self.temp = None 
        self.humidity = None 
        self.wind = None
        self.rand = None
        self.city = None

    def _fetch_info(self, location):
        ''' Background method for making the api call. '''
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
    
    def _submit_location(self):
        ''' Button command for submitting location. '''
        loc = self.location_textbox.get()
        self.weather, self.temp, self.humidity, self.wind = self._fetch_info(loc)
        self.state = 1
        self.run_gui()
    
    def _scrape_cities(self):
        ''' Internal method scraping the most populous cities in the world and returning a list. '''
        cities_list = []

        cities_url = "https://worldpopulationreview.com/cities" # base url
        page = requests.get(cities_url) # call to the website
        soup = bs(page.content, 'html.parser') # making soup
        table = soup.find('table') # scraping the table element
        for i, row in enumerate(table.find_all('tr')): # scraping table row
            row = str(row) # turning into string
            row_split = row.split("href",1) # splitting on element to find actual city name
            for k in range(len(row_split)): # using logic on which row contains the city
                if k == 1:
                    row_split2 = str(row_split).split("/") # further splitting
                    row_split3 = str(row_split2[7]).split(">")[1].split("<")[0] # further splitting: BINGO
                    cities_list.append(row_split3)
        return cities_list

    def _city_rand(self):
        ''' Internal method getting a random city from the internal scrape cities method. '''
        city_list = self._scrape_cities()
        loc = random.choice(city_list)
        self.city = loc
        self.rand = True
        self.weather, self.temp, self.humidity, self.wind = self._fetch_info(loc)
        self.state = 1
        self.run_gui()

    def run_gui(self):
        ''' The method for creating and running the actual GUI. '''
        root = Tk()
        root.title('Weather Flash')

        if self.state == 0:
            
            location_label = Label(root, text = "Enter a location")
            location_label.grid(column=0, row=0, sticky = W)

            self.location_textbox = Entry(root)
            self.location_textbox.grid(column=0, row=1, sticky = W)

            location_button = Button(root, text = "Submit", command = self._submit_location)
            location_button.grid(column = 0, row = 2, sticky = W)

            random_button = Button(root, text = 'Random City', command = self._city_rand)
            random_button.grid(column = 0, row = 3, sticky = W)

            root.mainloop()
        elif self.state == 1:

            # mainframe
            mainframe = ttk.Frame(root, padding = "3 3 12 12")
            mainframe.grid(column=0, row=0, sticky = (N, W, E, S))
            root.columnconfigure(0, weight = 1)
            root.rowconfigure(0, weight = 1)

            # empty row for neatness
            ttk.Label(mainframe, text = " ").grid(column=1, row = 0)
            # location widget
            ttk.Label(mainframe, text = f"{self.location_textbox.get()}", font = ("Helvetica", 16, "underline")).grid(column=1, row = 1)
            if self.rand == True:
                ttk.Label(mainframe, text = f"{self.city}", font = ("Helvetica", 16, "underline")).grid(column=1, row = 1)
            # Weather widget
            ttk.Label(mainframe, text = f"The weather is currently: {self.weather}").grid(column=1, row=2, sticky=W)
            image = Image.open(dict_weather[self.weather]).resize((30,30))
            photo = ImageTk.PhotoImage(image, master = mainframe)

            lbl = Label(mainframe, image = photo)
            lbl.image = photo
            lbl.grid(column=0, row=2)
           
            # temperature widget
            ttk.Label(mainframe, text = f"The temperature is currently: {self.temp:.02f}°C").grid(column=1, row=3, sticky=W)
            image_thermo = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/thermo.jpeg").resize((30,30))
            photo_thermo = ImageTk.PhotoImage(image_thermo, master = mainframe)
            lbl_thermo = Label(mainframe, image = photo_thermo)
            lbl_thermo.image = photo
            lbl_thermo.grid(column=0,row=3)

            # humidity widget
            ttk.Label(mainframe, text = f"The humidity is currently: {self.humidity}%").grid(column=1, row=4, sticky=W)
            image_water = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/water.jpeg").resize((30,30))
            photo_water = ImageTk.PhotoImage(image_water, master = mainframe)
            lbl_water = Label(mainframe, image = photo_water)
            lbl_water.image = photo
            lbl_water.grid(column=0,row=4)

            # wind widget
            ttk.Label(mainframe, text = f"The wind speed is currently: {self.wind} km/h").grid(column=1, row=5, sticky=W)
            image_wind = Image.open("/home/qwandy/CodeProjects/Code/meteor_dashboard/weather_icons/wind.jpeg").resize((30,30))
            photo_wind = ImageTk.PhotoImage(image_wind, master = mainframe)
            lbl_wind = Label(mainframe, image = photo_wind)
            lbl_wind.image = photo
            lbl_wind.grid(column=0, row=5)

            root.mainloop()


test = gui().run_gui()
#test = gui()._city_rand()




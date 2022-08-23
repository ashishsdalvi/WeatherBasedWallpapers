import requests, json 
import keys.keys as keys
import pycountry
import subprocess
import os 
import schedule
import time 

# Get the location from bashrc file and convert into a usable url ------------------------------------------------------------------------------------------------------------------
def get_location_url():
    bashrc_path = os.path.expanduser('~/.bashrc')
    location_url = None

    with open(bashrc_path, 'r') as infile:
        contents = infile.readlines()

        for row in contents:
            row = row.strip("\n")
            if "export location_url" in row:
                string_list = row.split('=', 1)

    location_url = string_list[1]

    return location_url


# Requests an API using latitude, longitude to get the locations weather and runs different bash scripts accordinly ------------------------------------------------------------------------
def change_wallpaper(location_url):

    # API Key 
    weather_key = keys.weather_key

    # Make a request to location_url to get the latitude and longitude
    res = requests.get(location_url)

    data = res.json() # data is a list
    country_data = data[0] # country_data is a dict

    lat = country_data['lat']
    lon = country_data['lon']

    # Use cities latitude and longitude to find its weather  
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}"

    res = requests.get(weather_url)

    data = res.json()
    weather_data = data['weather']
    weather = weather_data[0]["main"]

    print(weather)

    if weather == "Clouds":
        # subprocess.check_call(['chmod','u+rx','set_cloudy_wallpaper.sh'])
        # subprocess.call('set_cloudy_wallpaper.sh')

        subprocess.check_call(['chmod','u+rx','test.sh'])
        print("Working...")
        subprocess.run('test.sh')
        print("Done")
        

    elif weather == "Clear":
        subprocess.check_call(['chmod','u+rx','set_clear_wallpaper.sh'])
        # subprocess.call('set_clear_wallpaper.sh')


    elif weather == "Rain":
        subprocess.check_call(['chmod','u+rx','set_rainy_wallpaper.sh'])
        # subprocess.call('set_rainy_wallpaper.sh')
    

# Gets the url and uses it to change the wallpaper -----------------------------------------------------------------------------------------------------------------------------
def job():
    location_url = get_location_url()
    change_wallpaper(location_url)


#  Automating the process of changing the wallpaper using cron ------------------------------------------------------------------------------------------------------------
# In cron: type 1 * * * * python3 weather.py to run the python script automatically every hour


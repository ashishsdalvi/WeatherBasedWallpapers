import requests, json
import keys.keys as keys
import pycountry
import os 


# API Key 
weather_key = keys.weather_key

# Gets the city, country, and paths for each of the wallpapers for the 3 weather conditions (clear, cloudy, rainy)
def get_info():

    # Get city name and country code
    city_name = input("Please enter your city name: ")
    country_name = input("Please enter the country name: ")
    country_code = pycountry.countries.get(name=f'{country_name}').alpha_2

    # Enter the paths for your clear, cloudy, and rainy wallpapers
    clear_path = input("Please enter the path for your clear wallpaper: ")
    cloudy_path = input("Please enter the path for your cloudy wallpaper: ")
    rainy_path = input("Please enter the path for your rainy wallpaper: ")

    # Get state code ONLY if location in USA
    if country_code == "USA":
        state_code = input("Please enter the two letter abbreviation for your state")
        location_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=10&appid={weather_key}"

    # Otherwise you dont need the state code 
    else: 
        location_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=10&appid={weather_key}"


    # Save the location_url into .bashrc file so the variable persists
    # the "a" stands for append 
    with open(os.path.expanduser("~/.bashrc"), "a") as outfile:       
        outfile.write(f"export location_url={location_url}\n")

        # Setting the paths for different wallpapers
        outfile.write(f"export clear_path={clear_path}\n")
        outfile.write(f"export cloudy_path={cloudy_path}\n")
        outfile.write(f"export rainy_path={rainy_path}\n")

get_info()
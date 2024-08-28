import requests
def get_weather(city):
    api_key="d307b8a05732f39262679d03a0dc5ef0"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" 
    response=requests.get(url)
    data=response.json()
    if data.get("cod") != 200:
        print("City not found. Please try again.")
    else:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"{city.capitalize()}: {temperature}°C, {description.capitalize()}")


def main():
    print("Welcome to the  Weather App!")
    while True:
        city=input("Enter city name").strip()
        if(city.lower()=='exit'):
            print("Exiting the Weather App")
            break 
        get_weather(city)
if __name__=='__main__':
    main()
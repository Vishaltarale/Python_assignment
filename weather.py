import  requests,json
import pandas as pd
import matplotlib.pyplot as plt

api_id="a3153f5e98fbc06dcc1b06263139f5c3"       
weather_data=[]

#Taken citys as a list as given in Question
list=["new york","london","tokyo"]
for i in list:
    city=i
    main_url="https://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=a3153f5e98fbc06dcc1b06263139f5c3"
    responsedata=requests.get(main_url)
    data=responsedata.json()
    
#Question 2 : Taken current weather status from given cities and put in DataFrame df
    temperature=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    city=data["name"]
    weather=data["weather"][0]["description"]

    weather_data.append((city,temperature,humidity,weather))
    df = pd.DataFrame(weather_data,columns=['city','temperature','humididty','weather'])
    
#Question 4 : To find Hotest and Coldest City.
hottest_city = df.loc[df["temperature"].idxmax()]
coldest_city = df.loc[df["temperature"].idxmin()]

#Question 3 : To make barchart using the DataFrame Column Data.
df.plot(x="city", y="temperature", kind="bar", legend=False,grid=True, color="skyblue")
plt.ylabel("temperature")
plt.title("Temperature Comparison of Cities")
plt.xticks(rotation=0)

plt.text(hottest_city.name, hottest_city.temperature, "Hottest", ha='center', color="red", fontsize=12)
plt.text(coldest_city.name, coldest_city.temperature, "Coldest", ha='center', color="blue", fontsize=12)

plt.show()




#-----Weather forecast------


#-----Write a program that will create an information string with current weather information for a website. The values for weather type, temperature, precipitation (only the word yes or no) are entered by the user and inserted into the information string.
# Input format
# Three lines are entered: temperature, weather type, and precipitation.
# Output format
# If there is no precipitation:
# Today {temperature} degrees Celsius, {weather type}, sunny.
# If there is precipitation:
# Today {temperature} degrees Celsius, {weather type}, precipitation in the form of rain or snow.




#===========================================================================================
#==============SOLUTION=============

temperature = input()
weather_type = input()
precipitation = input()

if precipitation.strip().lower() == "нет":
    print(f"Сегодня {temperature} градусов Цельсия, {weather_type}, солнечно.")
else:
    print(f"Сегодня {temperature} градусов Цельсия, {weather_type}, осадки в виде дождя или снега.")


weather_c = {
	"Monday": 12,
	"Tuesday": 14,
	"Wednesday": 15,
	"Thursday": 14,
	"Friday": 21,
	"Saturday": 22,
	"Sunday": 24,
}
# 🚨 Don't change code above 👆

weather_f = {day: weather_c[day] * 9 / 5 + 32 for day in weather_c}

# Write your code 👇 below:


print(weather_f)

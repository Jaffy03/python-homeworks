from bs4 import BeautifulSoup

with open ('weather.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

rows = soup.find('table').find('tbody').find_all('tr')

days = []
temperatures = []
conditions = []

for row in rows:
    cols = row.find_all('td')
    days.append(cols[0].text.strip())
    temp_text = cols[1].text.strip()
    temp_value = ''.join(filter(str.isdigit, temp_text))
    temperatures.append(int(temp_value))
    conditions.append(cols[2].text.strip())

print("Weather forecast: ")
for day, temp, cond in zip(days, temperatures, conditions):
    print(f"{day}: {temp}°C, {cond}")
    
max_temp = temperatures.index(max(temperatures))
print(f"\nDay with the highest temperature: {days[max_temp]} ({temperatures[max_temp]}°C)")

sunny_days = [day for day, cond in zip(days, conditions) if cond == "Sunny"]
print("\nDays with sunny condition:", ", ".join(sunny_days))

average_temp = sum(temperatures)/ len(temperatures)
print(f"\nAverage temperature for the week: {average_temp:.2f}°C")
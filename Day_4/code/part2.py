with open("Day_5\Doc&images\input_Part1.txt",'r') as file:
    content = file.read()

content = content.split("\n")

seeds = [int(val) for val in content[0].split(':')[1].split()]
seed_soil = [[] for i in range(19-3)]
soil_fertilizer = [[] for i in range(54-21)]
fertilizer_water = [[] for i in range(82-56)]
water_light = [[] for i in range(122-84)]
light_temperature = [[] for i in range(134-125)]
temperature_humidity = [[] for i in range(173-136)]
himidity_location = [[] for i in range(197-175)]


for i, line in enumerate(content[3:19]):
    seed_soil[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[21:54]):
    soil_fertilizer[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[56:82]):
    fertilizer_water[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[84:122]):
    water_light[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[125:134]):
    light_temperature[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[136:173]):
    temperature_humidity[i] = [int(val) for val in line.split()]
for i, line in enumerate(content[175:197]):
    himidity_location[i] = [int(val) for val in line.split()]

#print(soil_fertilizer)
locations = []
for seed in seeds:
    for line in seed_soil:
        if seed - line[1] < line[2] and seed - line[1] > 0:
            soil = line[0]
            soil+=  seed - line[1]
        else:
            soil = seed
               
    for line in soil_fertilizer:
        if soil - line[1] < line[2] and soil - line[1] > 0:
            fertilizer = line[0]
            fertilizer+=  soil - line[1]
        else:
            fertilizer = soil
    
    for line in fertilizer_water:
        if fertilizer - line[1] < line[2] and fertilizer - line[1] > 0:
            water = line[0]
            water+=  fertilizer - line[1]
        else:
            water = fertilizer
    
    for line in water_light:
        if water - line[1] < line[2] and water - line[1] > 0:
            light = line[0]
            light +=  water - line[1]
        else:
            light = water
    
    for line in light_temperature:
        if light - line[1] < line[2] and light - line[1] > 0:
            temperature = line[0]
            temperature +=  light - line[1]
        else:
            temperature = light
    
    for line in temperature_humidity:
        if temperature - line[1] < line[2] and temperature - line[1] > 0:
            humidity = line[0]
            humidity +=  temperature - line[1]
        else:
            humidity = temperature

    for line in himidity_location:
        if humidity - line[1] < line[2] and humidity - line[1] > 0:
            location = line[0]
            location+=  humidity - line[1]
        else:
            location = humidity
    locations.append(location)          
print(min(locations))


with open("Day_5\Doc&images\example.txt",'r') as file:
    content = file.read()

content = content.split("\n")
seeds = []
seed_soil = []
soil_fertilizer = []
fertilizer_water = []
water_light = []
light_temperature = []
temperature_humidity = []
humidity_location = []

current_section = None
for line in content:
    colon_pos = line.find(":")
    if colon_pos >= 0:
        # Section change
        section_name = line[:colon_pos]
        line = line[colon_pos + 1:]  # Skip section name

        current_section = {
            "seeds": seeds,
            "seed-to-soil map": seed_soil,
            "soil-to-fertilizer map": soil_fertilizer,
            "fertilizer-to-water map":fertilizer_water,
            "water-to-light map":water_light,
            "light-to-temperature map":light_temperature,
            "temperature-to-humidity map":temperature_humidity,
            "humidity-to-location map":humidity_location,
        }[section_name]

    # Parse line if there's something
    line_data = line.split()
    if len(line_data) > 0:
        current_section.append([int(val) for val in line_data])

#print(seeds,seed_soil,soil_fertilizer,fertilizer_water,water_light,light_temperature,temperature_humidity,humidity_location)
locations = []
for seed in seeds[0]:
    for line in seed_soil:
        if line[1] + line[2] > seed and seed >= line[1] :
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

    for line in humidity_location:
        if humidity - line[1] < line[2] and humidity - line[1] > 0:
            location = line[0]
            location+=  humidity - line[1]
        else:
            location = humidity
    print(seed,soil,fertilizer,water,light,temperature,humidity,location)
    locations.append(location)          
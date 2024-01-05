def forecast(*args):
    forecast_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}
    for locations, weather in args:
        forecast_dict[weather].append(locations)

    result = ''
    for weather, location in forecast_dict.items():
        sort_location = sorted(location)
        for town in sort_location:
            result += f'{town} - {weather}\n'

    return result

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")
))

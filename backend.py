import requests
api_key = "6277056abe0ce5e1a893976edd2af79a"


def get_data(place, forecast_days = None, kind = None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    no_of_values = forecast_days*8
    filtered_data = filtered_data[:no_of_values]
    return filtered_data



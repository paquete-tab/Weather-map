import requests
import mysql.connector
import datetime
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_weather(api_key, lat, lon):
    # url = f"http://api.openweathermap.org/data/2.5/forecast"
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_city_data(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json',
        'zoom': 10,
        'addressdetails': 1
    }
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return data

def insert_weather_data(db_config, date, city, weather_data):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(buffered=True)
    
    insert_query = """
    INSERT INTO weather (date, city, weather_data)
    VALUES (%s, %s, %s)
    """
        
    cursor.execute(insert_query, (date, city, weather_data))
    
    connection.commit()
    cursor.close()
    connection.close()

def search_weather_data(db_config, date, city):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(buffered=True)
    
    search_query = """
    SELECT weather_data FROM weather WHERE date=%s AND city=%s
    """
        
    cursor.execute(search_query, (date, city))

    search_result = cursor.fetchone()
    
    connection.commit()
    cursor.close()
    connection.close()

    return search_result

@app.route('/', methods=['POST'])
def index():
    params = request.get_json(force=True)
    api_key = os.environ['OPEN_WEATHER_MAP_API_KEY']
    lat = params.get("lat", 35.6895) # 緯度
    lon = params.get("lon", 139.6917) # 経度
    # dt = datetime(2024, 7, 12, 12, 0)  # 日時
    year = params.get("year", 2024)
    month = params.get("month", 7)
    day = params.get("day", 12)
    date = datetime.date(year, month, day)

    db_config = {
        'user': 'weather_map',
        'host': 'localhost',
        'database': 'weather_map'
    }

    # 地名情報を取得
    city_data = get_city_data(lat, lon)
    city_name = city_data["display_name"]
    print(city_name)
    # 天気情報を取得
    weather_data = get_weather(api_key, lat, lon)
    weather = weather_data["weather"][0]["description"]
    # search_result = search_weather_data(db_config, date, city_name)
    # print(search_result)
    # if search_result == None:
    #     weather_data = get_weather(api_key, lat, lon)
    #     weather = weather_data["weather"][0]["description"]
    #     insert_weather_data(db_config, date, city_name, weather)
    # else:
    #     weather = search_result[0]

    # print(weather)
    return jsonify({"city": city_name, "weather": weather})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
    # main()

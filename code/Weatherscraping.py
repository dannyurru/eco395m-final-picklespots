import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://forecast.weather.gov/"

cities = [
    {"name": "Orlando, FL", "lat": 28.538336, "lon": -81.379234},
    {"name": "Anaheim, CA", "lat": 33.836593, "lon": -117.914301},
    {"name": "Las Vegas, NV", "lat": 36.169941, "lon": -115.139832},
    {"name": "New York, NY", "lat": 40.712776, "lon": -74.005974},
    {"name": "Denver, CO", "lat": 39.739236, "lon": -104.990251},
    {"name": "Atlanta, GA", "lat": 33.749099, "lon": -84.390185},
    {"name": "Phoenix, AZ", "lat": 33.448376, "lon": -112.074036},
    {"name": "Tampa, FL", "lat": 27.950575, "lon": -82.457178},
    {"name": "Boston, MA", "lat": 42.360083, "lon": -71.058880},
    {"name": "Fort Lauderdale, FL", "lat": 26.122439, "lon": -80.137317},
    {"name": "San Diego, CA", "lat": 32.715736, "lon": -117.161087},
    {"name": "Chicago, IL", "lat": 41.878113, "lon": -87.629799},
    {"name": "Seattle, WA", "lat": 47.606209, "lon": -122.332069},
    {"name": "Dallas, TX", "lat": 32.776664, "lon": -96.796988},
    {"name": "Miami, FL", "lat": 25.761680, "lon": -80.191790},
    {"name": "Washington, D.C.", "lat": 38.907192, "lon": -77.036871},
    {"name": "San Francisco, CA", "lat": 37.774929, "lon": -122.419418},
    {"name": "Charlotte, NC", "lat": 35.227085, "lon": -80.843124},
    {"name": "Honolulu, HI", "lat": 21.306944, "lon": -157.858337},
    {"name": "Houston, TX", "lat": 29.760427, "lon": -95.369804},
    {"name": "Philadelphia, PA", "lat": 39.952584, "lon": -75.165222},
    {"name": "Fort Myers, FL", "lat": 26.640628, "lon": -81.872308},
    {"name": "Nashville, TN", "lat": 36.162663, "lon": -86.781601},
    {"name": "Maui, HI", "lat": 20.798363, "lon": -156.331925},
    {"name": "Salt Lake City, UT", "lat": 40.760780, "lon": -111.891045},
    {"name": "Portland, OR", "lat": 45.505106, "lon": -122.675026},
    {"name": "West Palm Beach, FL", "lat": 26.715340, "lon": -80.053374},
    {"name": "Minneapolis, MN", "lat": 44.977753, "lon": -93.265011},
    {"name": "Raleigh, NC", "lat": 35.779590, "lon": -78.638179},
    {"name": "Jacksonville, FL", "lat": 30.332184, "lon": -81.655651},
    {"name": "New Orleans, LA", "lat": 29.951066, "lon": -90.071532},
    {"name": "Austin, TX", "lat": 30.267153, "lon": -97.743057},
    {"name": "Savannah, GA", "lat": 32.080899, "lon": -81.091203},
    {"name": "Cleveland, OH", "lat": 41.499320, "lon": -81.694361},
    {"name": "St. Louis, MO", "lat": 38.627003, "lon": -90.199404},
    {"name": "Baltimore, MD", "lat": 39.290385, "lon": -76.612189},
    {"name": "Pittsburgh, PA", "lat": 40.440625, "lon": -79.995886},
    {"name": "Charleston, SC", "lat": 32.776475, "lon": -79.931051},
    {"name": "Albuquerque, NM", "lat": 35.084385, "lon": -106.650421},
    {"name": "Columbus, OH", "lat": 39.961176, "lon": -82.998794},
    {"name": "Myrtle Beach, SC", "lat": 33.689060, "lon": -78.886694},
    {"name": "San Jose, CA", "lat": 37.338208, "lon": -121.886329},
    {"name": "Providence, RI", "lat": 41.824009, "lon": -71.412834},
    {"name": "Burlington, NC", "lat": 36.095691, "lon": -79.437799},
    {"name": "San Antonio, TX", "lat": 29.424122, "lon": -98.493628},
    {"name": "Kalaoa, HI", "lat": 19.728554, "lon": -155.997667},
    {"name": "Indianapolis, IN", "lat": 39.768403, "lon": -86.158068},
    {"name": "Detroit, MI", "lat": 42.331427, "lon": -83.045754},
    {"name": "Sacramento, CA", "lat": 38.581572, "lon": -121.494400},
    {"name": "Oakland, CA", "lat": 37.804364, "lon": -122.271114}
]

output_file = "Top_Cities_Current-Weather.csv"
headers = ["City", "Current Temperature", "Weather Condition", "Wind Speed"]

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for city_data in cities:
        city_name = city_data["name"]
        lat = city_data["lat"]
        lon = city_data["lon"]

        # Construct URL
        url = f"{BASE_URL}MapClick.php?lat={lat}&lon={lon}"

        # Send GET request
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract data
        try:
            city = soup.find('h2', class_='panel-title').get_text(strip=True)
            current_temp = soup.find('p', class_='myforecast-current-lrg').get_text(strip=True)
            weather_condition = soup.find('p', class_='myforecast-current').get_text(strip=True)
            wind_speed = (
                soup.find('td', text='Wind Speed')
                .find_next_sibling('td')
                .get_text(strip=True)
                if soup.find('td', text='Wind Speed')
                else "N/A"
            )

            # Write to CSV
            writer.writerow([city_name, current_temp, weather_condition, wind_speed])
            print(f"Weather data for {city_name} saved.")
        except Exception as e:
            print(f"Failed to retrieve data for {city_name}: {e}")

print(f"Weather for all cities has been saved to {output_file}.")

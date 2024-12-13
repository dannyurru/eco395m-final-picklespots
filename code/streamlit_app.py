from pathlib import Path
import streamlit as st
import psycopg2
import os
import requests
from dotenv import load_dotenv
from PIL import Image
from bs4 import BeautifulSoup

BASE_URL = "https://forecast.weather.gov/"

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 3em;
        color: #4A772F;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">🥒🎾PickleSpots🎾🥒</div>', unsafe_allow_html=True)
st.text(
    "This is an app designed to recommend a nearby pickleball court and corresponding outfit suggestions for any vacationer traveling to a destination of the top 50 most-visited cities in the United States. This recommendation will be based on proximity, weather, and the number of courts available at the nearby places."
)
load_dotenv()

BASE_URL = "https://forecast.weather.gov/"

# Function to create a connection to the database
def create_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ["DATABASE_HOST"],
            database=os.environ["DATABASE_DATABASE"],
            user=os.environ["DATABASE_USERNAME"],
            password=os.environ["DATABASE_PASSWORD"],
            port=os.environ["DATABASE_PORT"]
        )
        return conn
    except psycopg2.Error as e:
        st.error(f"Database connection error: {e}")
        st.stop()

# Function to fetch city names, latitude, and longitude from the database
def get_available_cities():
    """
    Fetch city names along with latitude and longitude from the database.
    """
    conn = create_connection()
    cursor = conn.cursor()
    query = """
        SELECT ci."CityId", ci."Name", co."Latitude", co."Longitude"
        FROM "City" ci
        JOIN "Coordinates" co ON ci."CityId" = co."CityId"
        ORDER BY ci."Name" ASC
    """
    cursor.execute(query)
    cities = [{"id": row[0], "name": row[1], "lat": row[2], "lon": row[3]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return cities

# Function to fetch court information from the database
def get_courts_by_city_and_number(city_name, min_courts):
    """
    Fetch court data for a selected city and minimum number of courts.
    """
    conn = create_connection()
    cursor = conn.cursor()

    if min_courts is None:
        query = """
        SELECT c."Name", c."NumberOfCourts", c."Lines", c."Nets"
        FROM "Courts" c
        JOIN "City" ci ON c."CityId" = ci."CityId"
        WHERE ci."Name" = %s
        """
        cursor.execute(query, (city_name,))
    else:
        query = """
        SELECT c."Name", c."NumberOfCourts", c."Lines", c."Nets"
        FROM "Courts" c
        JOIN "City" ci ON c."CityId" = ci."CityId"
        WHERE ci."Name" = %s AND c."NumberOfCourts" >= %s
        """
        cursor.execute(query, (city_name, min_courts))

    courts = cursor.fetchall()
    cursor.close()
    conn.close()
    return courts

# Function to retrieve weather data from NOAA
def get_weather_data(lat, lon):
    """
    Retrieve weather data from the NOAA website based on latitude and longitude.
    """
    url = f"{BASE_URL}MapClick.php?lat={lat}&lon={lon}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

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
        return city, current_temp, weather_condition, wind_speed
    except Exception as e:
        return None, None, None, f"Error: {e}"

# Function to retrieve Google Maps photo (optional)
def get_google_maps_photo(court_name, city_name, api_key):
    search_query = f"{court_name} {city_name}"
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_params = {"query": search_query, "key": api_key}

    response = requests.get(search_url, params=search_params)
    if response.status_code == 200:
        results = response.json().get("results")
        if results:
            photo_reference = results[0].get("photos", [{}])[0].get("photo_reference")
            if photo_reference:
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo"
                photo_params = {
                    "maxheight": 200,
                    "maxwidth": 200,
                    "photoreference": photo_reference,
                    "key": api_key,
                }
                return f"{photo_url}?maxwidth=400&photoreference={photo_reference}&key={api_key}"
    return None

# Main application
def main():
    try:
        image_path = Path("..\pickleball_stock_image.jpg")
        image = Image.open(image_path)
        st.image(image, width=1000)
    except FileNotFoundError:
        st.warning("Image file not found. Please ensure the file is in the working directory.")

    st.title("Pickleball Court Finder")
    st.markdown("Find pickleball courts in your city and receive advice on what to wear based on the weather!")

    # Dropdown for city selection
    cities = get_available_cities()
    city_names = [city["name"] for city in cities]
    city_name = st.selectbox("Select your city", options=["Select city"] + city_names)

    # Dropdown for number of courts
    court_options = ["Any"] + list(range(1, 6))
    selected_court_option = st.selectbox(
        "Select the minimum number of courts", options=court_options, index=0
    )

    min_courts = None if selected_court_option == "Any" else selected_court_option

    if city_name and city_name != "Select city":
        # Get latitude and longitude for the selected city
        selected_city = next((city for city in cities if city["name"] == city_name), None)
        if selected_city:
            lat, lon = selected_city["lat"], selected_city["lon"]

            # Fetch weather data
            with st.spinner("Fetching weather data..."):
                weather_city, temperature, condition, wind_speed = get_weather_data(lat, lon)

            if weather_city:
                st.subheader(f"Weather in {weather_city}")
                st.write(f"**Temperature**: {temperature}")
                st.write(f"**Condition**: {condition}")
                st.write(f"**Wind Speed**: {wind_speed}")
            else:
                st.warning("Unable to fetch weather data.")

        # Fetch court information
        courts = get_courts_by_city_and_number(city_name, min_courts)

        if courts:
            st.subheader(
                f"Court Information for {city_name}:" +
                (f" (Minimum {min_courts} courts)" if min_courts else "")
            )
            for court in courts:
                court_name = court[0]
                court_query = f"{court_name} {city_name}".replace(" ", "+")
                google_maps_link = f"https://www.google.com/maps/search/?api=1&query={court_query}"

                col1, col2 = st.columns([3, 2])

                with col1:
                    st.markdown(f"[**{court_name}**]({google_maps_link})", unsafe_allow_html=True)
                    st.write(f"**Number of Courts**: {court[1]}")
                    st.write(f"**Lines**: {court[2]}")
                    st.write(f"**Nets**: {court[3]}")

                with col2:
                    photo_url = get_google_maps_photo(
                        court_name, city_name, os.environ["MAPS_API_KEY"]
                    )
                    if photo_url:
                        st.image(photo_url, width=200)
                    else:
                        st.write("No photo available.")

                st.write("---")
        else:
            st.write(
                f"No court information found for {city_name}."
                + (f" with at least {min_courts} courts." if min_courts else "")
            )

    st.markdown("---")
    st.markdown("Data collected from pickleheads.com")
    st.markdown("Images taken from Google's Places API")
    st.markdown("Project created by Divya, Danny, Jisoo, Juan, Nick, and Sindhuj for ECO395M")

if __name__ == "__main__":
    main()

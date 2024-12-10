from pathlib import Path
import streamlit as st
import psycopg2
import os
from dotenv import load_dotenv
from PIL import Image

st.title("PickleSpots: Pickleball court finder")
st.text("This is an app designed to recommend a nearby pickleball court and corresponding outfit suggestions for any vacationer traveling to a destination of the top 50 most-visited cities in the United States. This recommendation will be based on proximity, weather, and the number of courts available at the nearby places.")
load_dotenv()

try:
    DATABASE_HOST = os.environ["DATABASE_HOST"]
    DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]
    DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
    DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
    DATABASE_PORT = os.environ["DATABASE_PORT"]
except KeyError as e:
    st.error(f"Missing environment variable: {e}")
    st.stop()

def create_connection():
    try:
        conn = psycopg2.connect(
            host=DATABASE_HOST,
            database=DATABASE_DATABASE,
            user=DATABASE_USERNAME,
            password=DATABASE_PASSWORD,
            port=DATABASE_PORT
        )
        return conn
    except psycopg2.Error as e:
        st.error(f"Database connection error: {e}")
        st.stop()

def get_courts_by_city(city_name):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = """
    SELECT c."Name", c."NumberOfCourts", c."Lines", c."Nets"
    FROM "Courts" c
    JOIN "City" ci ON c."CityId" = ci."CityId"
    WHERE ci."Name" = %s
    """
    
    cursor.execute(query, (city_name,))
    courts = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return courts



# Streamlit UI components
def main():
    try:
        image_path = Path("../pickleball_stock_image.jpg")
        image = Image.open(image_path)
        st.image(image, width=1000)
    except FileNotFoundError:
        st.warning("Image file not found. Please ensure the file is in the working directory.")
    
       

    st.title("Pickleball Court Finder")
    st.markdown("Find pickleball courts in your city and receive advice on what to wear based on the weather!")
    
    city_name = st.text_input("Enter the name of your city below (Case sensitive, please capitalize the name of your city)", placeholder="e.g., Austin")
    
    if city_name:
        courts = get_courts_by_city(city_name)
        
        if courts:
            st.subheader(f"Court Information for {city_name}:")
            for court in courts:
                st.write(f"**Court Name**: {court[0]}")
                st.write(f"**Number of Courts**: {court[1]}")
                st.write(f"**Lines**: {court[2]}")
                st.write(f"**Nets**: {court[3]}")
                st.write("---")
        else:
            st.write(f"No court information found for {city_name}.")
    
    st.markdown("---")
    st.markdown("Data collected from pickleheads.com")
    st.markdown("Project created by Divya, Danny, Jisoo, Juan, Nick, and Sindhuj for ECO395M")
    
if __name__ == "__main__":
    main()

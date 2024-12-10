import streamlit as st
import psycopg2
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]
DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_PORT = os.environ["DATABASE_PORT"]

def create_connection():
    return psycopg2.connect(
        host=DATABASE_HOST,
        database=DATABASE_DATABASE,
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        port=DATABASE_PORT
    )

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
    image = Image.open("pickleball_stock_image.jpg")
    st.image(image, width=1000)
    
    st.title("Pickleball Court Finder")
    st.markdown("Find pickleball courts in your city and receive advice on what to wear based on the weather!")
    
    city_name = st.text_input("Enter the name of the city", placeholder="e.g., Austin")
    
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

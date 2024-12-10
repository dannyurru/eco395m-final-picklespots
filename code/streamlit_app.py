from pathlib import Path
import streamlit as st
from PIL import Image
from database import create_connection

st.title("Safe Travels/ PickleSpots")
st.text("This is an app designed to recommend a nearby pickleball court and corresponding outfit suggestions for any vacationer traveling to a destination of the top 50 most-visited cities in the United States. This recommendation will be based on proximity, weather, and the number of courts available at the nearby places.")

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
                court_name = court[0]
                court_query = f"{court_name} {city_name}".replace(" ", "+")
                google_maps_link = f"https://www.google.com/maps/search/?api=1&query={court_query}"
            
                st.markdown(f"[**{court_name}**]({google_maps_link})", unsafe_allow_html=True)
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

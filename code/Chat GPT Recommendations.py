"""base file, basic"""

from openai import OpenAI

PROMPT_TEMPLATE = """
Hello! I am visiting the city {city} in the month of {month} and planning to hike at {trail}.
The dominant weather condition during this time is {weather}. What should I bring?
Please provide a list of recommended items specific to the trail and weather.
"""

def query_hiking_recommendation(city, trail, month, weather, client):
    """
    Generates a query for ChatGPT using city, trail, month, and weather data.
    Returns a list of recommended items or a fallback response if an error occurs.
    """
    prompt = PROMPT_TEMPLATE.format(city=city, trail=trail, month=month, weather=weather)
    try:
        response = client.completions.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error querying ChatGPT: {e}")
        return "Error retrieving recommendation."

if __name__ == "__main__":
    import os
    import dotenv

    dotenv.load_dotenv()
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    client = OpenAI(api_key=OPENAI_API_KEY)

    # Example input data (replace with actual dataset later)
    hiking_data = [
        {"city": "Denver", "trail": "Rocky Mountain National Park", "month": "June", "weather": "sunny"},
        {"city": "Seattle", "trail": "Mount Rainier", "month": "November", "weather": "rainy"},
        {"city": "Phoenix", "trail": "Camelback Mountain", "month": "August", "weather": "hot and dry"},
    ]

    # Process each entry and get ChatGPT recommendations
    for entry in hiking_data:
        city = entry["city"]
        trail = entry["trail"]
        month = entry["month"]
        weather = entry["weather"]
        
        print(f"Querying for city: {city}, trail: {trail}, month: {month}, weather: {weather}")
        recommended_items = query_hiking_recommendation(
            city=city, trail=trail, month=month, weather=weather, client=client
        )
        print(f"Recommended items: {recommended_items}\n")

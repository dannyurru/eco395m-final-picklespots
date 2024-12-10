<h1 align="center">***Tentative Pickleball Project Title (PickleSpots?)***</h1>

<h2 align="center">Project Goal of Analysis</h2>
<p>Based on a selected vacation destination of the top 50 visited cities in the United States, we want to create an interface that will recommend nearby pickleball courts as well as present weather data and corresponding outfit suggestions.</p>
<h2 align="center">Project Description and Findings</h2>
We will scrape data for the pickleballs in and nearby each city, along with daily weather information for each city from the year ***Year is Tentaive*** up to this year, which includes the average daily temperature and a generalized weather adjective to describe the weather that day. The data is then turned into a CSV abd uploaded onto an SQL database so that we can run queries through the SQLAlchemy engine. We will connect the weather data to the correswponding cities in the pickleball data through the schema of the SQL database. The interface is created through Streamlit, which is an applet that projects python code in a user-friendly manner.
=======
<h2 align="center">Project Goal</h2>
<p>Based on a list of the top 50 visited cities in the United States, we want to create an interface that will recommend nearby pickleball courts as well as present weather data and corresponding outfit suggestions to users.</p>
<h2 align="center">Project Description</h2>
We scraped data for the pickleball courts in and nearby each city, along with daily weather information for each city from the year ***Year is Tentative*** up to this year, which includes the average daily temperature and a generalized weather adjective to describe the weather that day. The data is then turned into a CSV and uploaded to a SQL database so that we can run queries through the SQLAlchemy engine. We will connect the weather data to the corresponding cities in the pickleball data through the schema of the SQL database. The interface is created through Streamlit, an applet that projects Python code in a user-friendly manner.
main
<h2 align="center">Methodology</h2>
We are scraping data for the following information for this project:
<li>Daily weather for the top 50 visited cities in the United States (Average Temperature and Weather Description)</li>
<li>Prominent pickleball courts in and nearby the aforementioned cities, including data on the number of courts available at each location, and the state of the court's lines and net.</li>
<h2 align="center">Reproducibility</h2>
<h2 align="center">Limitations of Project</h2>
<li>We are only using information for the 50 most visited cities in the United States, so we are limiting the interface's responses to the data we are scraping from.</li>
<li>We are limiting our activities to that of pickleball courts, so more urban destinations might be limited in the number of pickleball courts that are in the area, and sequentially limits the amount that can be scraped and recommended.</li>
<li>When scraping data on the NCEI, some of the data will not scrape due to certain issues with the website allowing all data to be scraped simultaneously.</li>
<h2 align="center">Extensions of Project</h2>
A good start for extending the model can be to include more cities in each state. The inclusion of all major cities in the United States can broaden the recommendations given for users of the interface for other trails. 
The inclusion of other outdoor activitues - such as parks, kayaking, and biking paths - can give users more variety what they could do in the city they select.
<h2 align="center">Sources of Datatsets</h2>
<li>The cities we are using for this project were selected by this website as the top 50 travel destinations in the United States: https://www.aaa.com/tripcanvas/article/50-top-travel-destinations-in-the-us-CM534#methodology</li>
<li>The list of pickleball courts comes from Pickleheads: https://www.pickleheads.com/</li>
<li>The weather data comes from the National Centers for Environmental Information: https://www.ncei.noaa.gov/archive</li>

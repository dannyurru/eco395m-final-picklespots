<h1 align="center">PickleSpots Project</h1>
<p align="center"> <img src="https://cdn.sanity.io/images/jvolei4i/production/805cc6aceadb385fe3e80f4c905591837d7a9c8b-736x586.webp" alt="Description" width="500"> </p>
<h2 align="center">Project Goal of Analysis</h2>
<p>Based on a selected vacation destination of the top 50 visited cities in the United States, we want to create an interface that will recommend nearby pickleball courts as well as present weather data and corresponding outfit suggestions.</p>
<h2 align="center">Project Description and Findings</h2>
We will scrape data for the pickleballs in and nearby each city, along with real-time daily weather information for each city, which includes the average daily temperature and a generalized weather adjective to describe the weather that day. The data is then turned into a CSV abd uploaded onto an SQL database so that we can run queries through the SQLAlchemy engine. We will connect the weather data to the correswponding cities in the pickleball data through the schema of the SQL database. The interface is created through Streamlit, which is an applet that projects python code in a user-friendly manner.
<h2 align="center">Project Goal</h2>
<p>Based on a list of the top 50 visited cities in the United States, we want to create an interface that will recommend nearby pickleball courts with the locations, as well as present weather data and corresponding outfit suggestions to users.</p>
<h2 align="center">Project Description</h2>
We scraped data for the pickleball courts in and nearby each city, along with the daily weather information for each city of the day of search, which includes the daily temperature, wind speed, humidity, and other weather statistics. The data is then turned into a CSV and uploaded to a SQL database so that we can run queries through the SQLAlchemy engine. We will connect the weather data to the corresponding cities in the pickleball data through the schema of the SQL database. The interface is created through Streamlit, an applet that projects Python code in a user-friendly manner.
main
<h2 align="center">Methodology</h2>
We are scraping data for the following information for this project:
<li>Daily weather for the top 50 visited cities in the United States (Average Temperature and Weather Description)</li>
<li>Prominent pickleball courts in and nearby the aforementioned cities, including data on the number of courts available at each location, and the state of the court's lines and net.</li>

<h2 align="center">Interactive Demonstration</h2>
<h3>Step 1: Input Selection</h3>
<p>Users select a city from the list of the top 50 most-visited U.S. cities. They can also specify the minimum number of pickleball courts they would like to see at a location.</p>
<p align="center">
  <img src="https://via.placeholder.com/700x400.png?text=Step+1%3A+City+Selection+Screenshot" alt="Step 1: City Selection Screenshot" width="700">
</p>
<h3>Step 2: Results</h3>
<p>The app provides a list of pickleball courts in the selected city, including key information about each court such as the number of courts, condition of lines, and available nets. The app also generates a live weather update and outfit suggestions for travelers based on local weather conditions. Google Maps links for each court location are provided for ease of navigation.</p>
<p align="center">
  <img src="https://via.placeholder.com/700x400.png?text=Step+2%3A+Court+Results+Screenshot" alt="Step 2: Court Results Screenshot" width="700">
</p>
<h3>Step 3: Interactive Visuals</h3>
<p>The interface also allows users to view court images and weather-related outfit suggestions. Images of the courts are pulled from Google’s Places API for an enhanced user experience.</p>
<p align="center">
  <img src="https://via.placeholder.com/700x400.png?text=Step+3%3A+Interactive+Visuals+Screenshot" alt="Step 3: Interactive Visuals Screenshot" width="700">
</p>

<h2 align="center">Reproducibility</h2>
The reproducibility of this project is doable, but requires a lot of information. To scrape the courts on Pickleheads, the Selenium package is needed in order to gain access to the web browser since the website uses Cloudflare to prevent scraping. After obtaining the information of courts in the cities, . 
<h2 align="center">Limitations of Project</h2>
<li>We are only using information for the 50 most visited cities in the United States, so we are limiting the interface's responses to the data we are scraping from.</li>
<li>We are limiting our activities to that of pickleball courts, so more urban destinations might be limited in the number of pickleball courts that are in the area, and sequentially limits the amount that can be scraped and recommended.</li>
<li></li>
<h2 align="center">Extensions of Project</h2>
A good start for extending the model can be to include more cities in each state. The inclusion of all major cities in the United States can broaden the recommendations given for users of the interface for other courts. 
The inclusion of other outdoor activitues - such as parks, kayaking, and biking paths - can give users more variety what they could do in the city they select.
<h2 align="center">Sources of Datatsets</h2>
<li>The cities we are using for this project were selected by this website as the top 50 travel destinations in the United States: https://www.aaa.com/tripcanvas/article/50-top-travel-destinations-in-the-us-CM534#methodology</li>
<li>The list of pickleball courts comes from Pickleheads: https://www.pickleheads.com/</li>
<li>The weather data comes from scraping the weather information on : https://dressmyrun.com/</li>

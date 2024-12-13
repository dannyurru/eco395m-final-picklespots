<h1 align="center">PickleSpots Project</h1>
<h2 align="center">By Divya Salian, Nicolas Salas, Danny Urrutia, Juan Guerra, Jisoo Yoo, Sindhuj Thapa</h2>
<p align="center"> <img src="https://cdn.sanity.io/images/jvolei4i/production/805cc6aceadb385fe3e80f4c905591837d7a9c8b-736x586.webp" alt="Description" width="500"> </p>
<h2 align="center">Project Description</h2>
Searching for a public place where you can play the fastest-growing sport in America with your friends?  We created an applet that recommends pickleball courts based on the user's selection of one of the top 50 most visited cities in the United States.  The applet includes a picture of the location, and a helpful link that takes the user straight to Google Maps.
<h2 align="center">Methodology</h2>
First and foremost, we used the <a href="https://seleniumbase.io">Selenium Base package</a> to simulate searches for publicly available, non-paid courts in each of the 50 cities on https://www.pickleheads.com/ and scraped the avaiable information on each instance. This method bypasses the Cloudflare security system that the site uses.  We then committed that information to a SQL database in GCP, through DBeaver and using the <a href="https://www.sqlalchemy.org">SQLAlchemy package</a>.<br>
<br>
We then set up a virtual interface using Streamlit that pulls specific instances of courts from the database based on user queries. For each selected court, the app links the court's name to a Google Maps query with the name and city, and uses a Google API to display the court's cover photo in the applet. Additionally, the app leverages real-time weather data from our SQL database, sourced from forecast.weather.gov, to provide users with actionable insights on current temperature, wind conditions, and overall weather suitability for outdoor activities. These updates help users decide whether it's a good time to play pickleball, ensuring their comfort and safety while enjoying the fastest-growing sport in America. 
<h2 align="center">Virtual Interface</h2>
<img src="images/applet_title.png" alt="Screenshot of the applet's title"><br>
<p align="center">The fun font of the title and the inviting image of a pickleball court identifies the project and adds an inviting feel for its users.</p>
<img src="images/city_dropdown.png" alt="Screenshot of the city dropdown menu of the applet"><br>
<p align="center">To avoid issues where the user enters a city that is not available, the dropdown menu gives an alphabetized list of cities that are covered by the project.</p>
<img src="images/courts_dropdown.png" alt="Screenshot of the minimum courts dropdown menu of the applet"><br>
<p align="center">The user can also conveniently select the minimum number of courts they are looking for, to accomodate those who are bringing a large group or organizing a small tournament.</p>
<img src="images/results_display.png" alt="Screenshot of the results when searching for pickleball courts in Austin"><br>
<p align="center">The applet then loads a list of courts, along with a helpful image and information regarding the number of courts available at that location and what kind of nets and lines there are. The name of the court takes the user to its Google Maps entry for easy navigation.</p>
<h2 align="center">Reproducibility</h2>
Someone attempting to reproduce this project would take the following steps:<br>
1. Download the required packages from requirements.txt<br>
2. Set up a postgreSQL database through Google Cloud Platform, and use the setup SQL code in <code>safe-travels.sql</code> to establish the schema.<br>
3. Create a <code>.env</code> file that contains the proper access information for your database, as well as your Google API key.<br>
4. Run <code>scraping-pickleheads.py</code>, waiting until it is through all 50 cities and has created <code>courts.csv</code> in the <code>artifacts</code> folder.<br>
5. Run <code>create_cities_table.py</code> and <code>create_courts_table.py</code> to fill in the remote database.<br>
6. Run the command <code>streamlit run code/streamlit_app.py</code> from the top level of the repository to launch the applet.<br>
<h2 align="center">Limitations of Project</h2>
<li>We are only using information for the 50 most visited cities in the United States, so users searching for pickleball courts in a city not on that list, or a more suburban/rural town, would not get any results.</li>
<li>Because this approach scrapes https://www.pickleheads.com/ once before adding its information to a database, it may lack information from any new courts that have been added since the time that the site was scraped.</li>
<li>Since it is difficult to accurately measure if the courts are currently in use, a person might show up to courts only to find out that there are none open.</li>
<h2 align="center">Extensions of Project</h2>
<li>A good start for extending the model can be to include more cities in each state. The inclusion of all major cities in the United States can broaden the recommendations given for users of the interface for other courts.</li>
<li>Additional information about each court, such as current distance from user, could be displayed onto the interface to enhance the user's experience.</li>
<li>We could also add an option to directly compare selected courts so that users can make a decision on which court to go to based on their specifications.</li>
<h2 align="center">Sources</h2>
<li>The cities we are using for this project were selected by this website as the top 50 travel destinations in the United States: https://www.aaa.com/tripcanvas/article/50-top-travel-destinations-in-the-us-CM534#methodology</li>
<li>The list of pickleball courts comes from Pickleheads: https://www.pickleheads.com/</li>
<li>Pictures of each court comes from Google Maps: https://www.google.com/maps</li>
<li>Weather data comes from: https://www.weather.gov/</li>

import os
import json
import csv

from common import get_soup

cities_list = [
    "Orlando",
    "Anaheim",
    "Las+Vegas",
    "New+York",
    "Denver",
    "Atlanta",
    "Phoenix",
    "Tampa",
    "Boston",
    "Fort+Lauderdale",
    "San Diego",
    "Chicago",
    "Seattle",
    "Dallas",
    "Miami",
    "Washington+District+of+Columbia",
    "San+Francisco",
    "Charlotte",
    "Honolulu",
    "Houston",
    "Philadelphia",
    "Fort+Myers",
    "Nashville",
    "Maui",
    "Salt+Lake+City",
    "Portland",
    "West+Palm+Beach",
    "Minneapolis",
    "Raleigh",
    "Jacksonville",
    "New+Orleans",
    "Austin",
    "Savannah",
    "Cleveland",
    "St+Louis",
    "Baltimore",
    "Pittsburgh",
    "Charleston",
    "Albuquerque",
    "Columbus",
    "Myrtle+Beach",
    "San+Jose",
    "Providence",
    "Burlington",
    "San+Antonio",
    "Kalaoa",
    "Indianapolis",
    "Detroit",
    "Sacramento",
    "Oakland",
]


def scrape_city(city):
    """Takes a city and returns a list of dicts that each represent a free pickleball court displayed on the page."""

    base_url = "https://www.pickleheads.com"

    page_url = f"{base_url}/search?q={city}&access=free"

    soup = get_soup(page_url)

    if soup.find("title").string == "404 Not Found":
        return []

    data_block = soup.find("div", class_="chakra-stack css-1iym7wy")

    data_block_indivs = data_block.find_all("a", class_="chakra-link css-13arwou")

    court_info_list = []

    for court in data_block_indivs:
        dict_ = {
            "city": city.replace("+", " "),
            "name": court.find("div", class_="chakra-stack css-1mvcjxj")
            .find("p")
            .string,
        }

        dict_ = dict_ | get_court_info(court)

        court_info_list.append(dict_)

    return court_info_list


def get_court_info(court):
    """Extracts the court's information, like the number of courts and the status of its nets and lines."""

    output = {"number_of_courts": "", "lines_status": "", "nets_status": ""}

    court_info = court.find("div", class_="css-15io43u").find_all("div", class_="css-0")

    count = 0
    for info_item in court_info:
        string_ = info_item.find("span", class_="chakra-text css-s7f8ra").string
        if string_[-6:-1] == "Court":
            output["number_of_courts"] = string_[0]
        if string_[-5:] == "Lines":
            output["lines_status"] = string_
        if string_[-4:] == "Nets":
            output["nets_status"] = string_

    return output


def scrape_all_cities():
    """Scrapes all cities, returning a list of dicts that each represent a free court in a given city."""

    all_court_details = []

    for city in cities_list:
        all_court_details += scrape_city(city)

    return all_court_details


def write_courts_to_csv(courts, path):
    fieldnames = ["name", "city", "number_of_courts", "lines_status", "nets_status"]
    with open(path, "w+") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(courts)


if __name__ == "__main__":

    BASE_DIR = "artifacts"
    CSV_PATH = os.path.join(BASE_DIR, "courts.csv")

    os.makedirs(BASE_DIR, exist_ok=True)

    courts = scrape_all_cities()

    write_courts_to_csv(courts, CSV_PATH)

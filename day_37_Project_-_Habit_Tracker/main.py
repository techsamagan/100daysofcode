import requests
from datetime import datetime
today = datetime.now()

# check results of this program:
# https://pixe.la/v1/users/azamatick/graphs/graph1.html

TOKEN = "1234567888888765432"
USERNAME = "azamatick"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
headers={
    "X-USER-TOKEN":TOKEN,
}

def main():
    create_new_pixela()
    create_new_graph(name="Quran Memorization Graph", unit="lines", type="float", color="shibafu")
    # go and check results on https://pixe.la/v1/users/azamatick/graphs/graph1.html
    lines_today = int(input("How many pages did you memorize today?\n >>"))
    add_pixels_today(lines_today)
    #delete_pixels("20230212")
    # update_pixels(25, "20230217")

def create_new_pixela():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

def create_new_graph(name, unit, type, color):
    """Creates a new Graph:
    inputs:
    name --string--: name the graph
    unit --string--: name the unit, ex: meters, KM, pages
    type --string--: int or float
    color --string--: 'shibafu'(green), 'momiji'(red), 'sora'(blue), 'ichou'(yellow), 'ajisai'(purple), 'kuro'(black) """
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    graph_config = {
        "id": GRAPH_ID,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color,
    }



    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

def add_pixels_today(quantity):
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    today = datetime.now()
    #print(today.strftime("%Y%m%d"))

    #today = datetime(year=2023, month=2, day=12)

    pixel_config = {
        "date": today.strftime("%Y%m%d"),
        "quantity" : str(quantity),
    }
    
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)

def delete_pixels(date):
    """srting date: yyyyMMdd"""
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    print(response.text)

def update_pixels(quantity, date):
    """srting date: yyyyMMdd"""
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    new_pixel_data = {
        "quantity": str(quantity),
    }

    response = requests.put(url = update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)




main()
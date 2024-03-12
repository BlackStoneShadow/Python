import os
from pprint import pprint
from module import controller

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


while True:    
    try:
        query = input("Input category or Exit:")

        os.system("cls")    
        
        if query.lower() == "exit":
            break

        foursquare = controller.Foursquare(API_KEY=os.getenv("API_KEY"), category=query)
        
        if (foursquare.status):          
            for item in foursquare.data:                
                print(f'Name\t:{item["name"]}')
                print(f'Rating\t:{item["rating"]}')
                print(f'Address\t:{item["location"]["formatted_address"]}\n')
                
    except:
        break
from module import controller

for item in controller.Toscrape():
    print(f"page:{item.page}")
    for item in item.books:
        print(f"Name\t\t:{item['name']}")
        print(f"Price\t\t:{item['price']}")
        print(f"Count\t\t:{item['count']}")
        print(f"Description\t:{item['description']}")

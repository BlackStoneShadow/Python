import os
import csv
import argparse
from module import controller
from pathlib import Path
from typing import Callable
from datetime import datetime
from datetime import timedelta

def save_to_scv():
    beginDate = datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    endDate = beginDate.replace(day=28) + timedelta(days=4)
    endDate = endDate - timedelta(days=endDate.day)

    parser = argparse.ArgumentParser(description='CBR argument parser');
    parser.add_argument('-f', metavar='filename', type=str, nargs='?', help='file name', default=Path().cwd() / "data.csv");
    parser.add_argument('-b', metavar='dateBegin', type=str, nargs='?', help='begin date period', default=beginDate.strftime("%d.%m.%Y"));
    parser.add_argument('-e', metavar='dateEnd', type=str, nargs='?', help='end date period', default=endDate.strftime("%d.%m.%Y"));

    args = parser.parse_args()   

    with open(args.f, "w", newline="", encoding="utf-8") as f:        
        names = ("date", "id", "code", "unit", "name", "price")
        csv_writer = csv.DictWriter(f, fieldnames=list(names), dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)   
        csv_writer.writeheader()
        for cbr in controller.CBR(dateBegin=args.b, dateEnd=args.e):            
            os.system("cls")
            print(f"load date {cbr.date.strftime('%d.%m.%Y')}")
            for item in cbr.price:
                csv_writer.writerow(item)  

if __name__ == "__main__":       
    save_to_scv()
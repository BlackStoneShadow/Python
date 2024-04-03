from module import controller

import os
import csv
import argparse
from module import controller
from pathlib import Path

def save_to_scv(**kwarg):    
    parser = argparse.ArgumentParser(description='wildberries argument parser');
    parser.add_argument('-f', metavar='filename', type=str, nargs='?', help='file name', default=Path().cwd() / "result.csv");
    parser.add_argument('-s', metavar='search', type=str, nargs='?', help='search string', default=kwarg["Search"]);    

    args = parser.parse_args()   
    print("start")
    with open(args.f, "w", newline="", encoding="utf-8") as f:        
        csv_writer = csv.DictWriter(f, fieldnames=["name", "price", "url"], dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)   
        csv_writer.writeheader()
        for item in controller.Scrapy(Search=args.s):                                    
            csv_writer.writerows(item.links)  
    print("finish")

if __name__ == "__main__":       
    save_to_scv(Search="IPhone 15 Pro MAX")
import requests
import json
import csv

response_string = requests.get("https://jsonplaceholder.typicode.com/todos").text
data = json.loads(response_string)
with open("homework31.csv", "w") as fw:
    writer = csv.DictWriter(fw, delimiter=";", lineterminator="\r", fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

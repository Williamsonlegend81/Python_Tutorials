import requests
import json
import time

string = input("Headlines or Everything:")
if (string=="Headlines"):
    country = input("Enter the country only first two letter:")
    category = input("Enter the category of news:")
    q = input("Enter the keyword or phrase to search for:")
    date = time.strftime('2024-03-01')
    response = requests.get(f"https://newsapi.org/v2/top-headlines?q={q}&from={date}&category={category}&country={country}&apikey=47c286c1f5214646afcee4b7e9d298c3")
    news = json.loads(response.text)
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print(article["url"])
        print("----------------------------")
elif (string=="Everything"):
    q = input("Enter the keyword or phrase to search for:")
    date = time.strftime('2024-03-01')
    response = requests.get(f"https://newsapi.org/v2/everything?q={q}&from={date}&language=en&apikey=47c286c1f5214646afcee4b7e9d298c3")
    news = json.loads(response.text)
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print(article["url"])
        print("------------------------------")



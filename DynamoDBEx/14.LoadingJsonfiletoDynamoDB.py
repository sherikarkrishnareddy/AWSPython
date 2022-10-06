import boto3
import json
from decimal import Decimal
def load_Movie(movies,dynamodb=None):
    if not dynamodb:
        dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('Movies')
    for movie in movies:
        year=int(movie['year'])
        title=movie['title']
        print("Adding Movie",title,year)
        table.put_item(Item=movie)
if __name__=="__main__":
    with open("moviedata.json") as jsonfile:
        movie_list=json.load(jsonfile,parse_float=Decimal)
    load_Movie(movie_list)
import boto3
import botocore
from decimal import Decimal
from pprint import pprint
def update_movie(title,year,rating,plot,dynamodb=None):
    if not dynamodb:
        dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('Movies')
    res=table.update_item(
        Key={
            'year':year,
            'title':title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues={
            ':r':Decimal(rating),
            ':p':plot,
        },
        ReturnValues='UPDATED_NEW'
    )
    return res

if __name__=="__main__":
    update_res=update_movie(
        "Prisoners",
        2013,
        '9.5',
        "i love you my babe"

    )
    print(update_res)
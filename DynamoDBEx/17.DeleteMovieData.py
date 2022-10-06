import boto3
import botocore
from decimal import Decimal
from pprint import pprint
def delete_movie(title,year,dynamodb=None):
    if not dynamodb:
        dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('Movies')
    try:
        res=table.delete_item(
            Key={
                'year':year,
                'title':title
            }
        )

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return res

if __name__=="__main__":
    response=delete_movie('Prisoners',2013)
    if response:
        print(response)

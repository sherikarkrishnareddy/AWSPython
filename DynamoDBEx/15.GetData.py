import boto3
from pprint import pprint
from botocore.exceptions import ClientError

def get_movie(title,year,dynamodb=None):
    if not dynamodb:
        dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('Movies')

    try:
        res=table.get_item(Key={'year':year,'title':title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return res['Item']
if __name__=="__main__":
    movie=get_movie('Prisoners',2013)
    if movie:
        pprint(movie)
import boto3
def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb=boto3.resource('dynamodb')
    table=dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName':'year',
                'KeyType':'HASH'
            },
            {
                'AttributeName':'title',
                'KeyType':'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits':1,
            'WriteCapacityUnits':1
        }
    )
    return table
if __name__=="__main__":
    movie=create_movie_table()
    print("Table Status : ", movie.table_status)
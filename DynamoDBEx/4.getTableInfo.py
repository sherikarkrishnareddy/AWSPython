import boto3
db=boto3.client('dynamodb')
response=db.describe_table(
    TableName='employee'
)
print(response)
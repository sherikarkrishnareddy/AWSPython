import boto3
db=boto3.resource('dynamodb')
table=db.Table('employee')
response=table.get_item(
    Key={
    'emp_id':'3'
    }
)
print(response)
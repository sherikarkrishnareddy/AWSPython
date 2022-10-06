import boto3
db = boto3.resource('dynamodb')
table=db.Table('employee')
table.put_item(
    Item={
        'emp_id':'1',
        'name':'reddy',
        'age':34
    }
)
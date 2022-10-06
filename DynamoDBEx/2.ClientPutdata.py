import boto3
db=boto3.client('dynamodb')
response=db.put_item(
    TableName='employee',
    Item={
        'emp_id':{
            'S':'3'
        },
        'name':{
            'S':'krishna'
        },
        'age':{
            'S':'32'
        }
    }
)
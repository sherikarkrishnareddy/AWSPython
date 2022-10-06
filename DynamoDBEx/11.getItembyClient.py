import boto3
db=boto3.client('dynamodb')
res=db.get_item(
    TableName='employee',
    Key={
        'emp_id':{
            'S':'1'
        }
    }
)
print(res)
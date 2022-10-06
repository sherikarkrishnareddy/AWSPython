import boto3
db=boto3.resource('dynamodb')
table=db.Table('employee')
res=table.scan()
print(res['Items'])
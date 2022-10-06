import boto3
db=boto3.resource('dynamodb')
table=db.Table('employee')
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'emp_id':'5',
            'name':'niki',
            'age':'35'
        }
    )
    batch.put_item(
        Item={
        'emp_id':'6',
        'name':'kritha',
        'age':'1'
    }

    )
    batch.put_item(
        Item={
            'emp_id':'7',
            'name':'shresta',
            'age':'3'
        }
    )

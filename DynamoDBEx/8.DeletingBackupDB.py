import boto3
db=boto3.client('dynamodb')
response=db.delete_backup(
BackupArn='arn:aws:dynamodb:us-east-1:520393821610:table/Article/backup/01664719283505-2b693f76'
)
print(response)
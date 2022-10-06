import boto3
db=boto3.client('dynamodb')
response=db.create_backup(
    TableName='Article',
    BackupName='ArticleBackUp'
)
print(response)
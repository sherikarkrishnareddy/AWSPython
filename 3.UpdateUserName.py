import boto3
def update_user(old_username,New_username):
    iam=boto3.client('iam')
    response=iam.update_user(
        UserName=old_username,
        NewUserName=New_username
    )
    print(response)
update_user("testuser","new_testuser")
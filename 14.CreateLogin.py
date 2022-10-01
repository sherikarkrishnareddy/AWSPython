import boto3
def createLogin(userName):
    iam=boto3.client('iam')
    response=iam.create_login_profile(
        UserName=userName,
        Password='Myword@1',
        PasswordResetRequired=False
    )
    print(response)
createLogin('new_testuser')
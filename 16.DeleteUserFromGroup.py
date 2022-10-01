import boto3
def deleteUserFromGroup(userName,groupName):
    iam=boto3.resource('iam')
    group=iam.Group(groupName)
    response=group.remove_user(
        UserName=userName
    )
    print(response)
deleteUserFromGroup('rdsuser','RDSAdmins')
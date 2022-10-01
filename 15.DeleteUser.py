import boto3

#the user must be removed from usergroups, Associated policies must be removed
#AWS console login should be disabled and Access key must be removed.
# Else DeleteConflictException occurs : An error occurred (DeleteConflict) when calling the DeleteUser operation: Cannot delete entity, must remove users from group first.

def deleteUser(userName):
    iam=boto3.client('iam')
    response=iam.delete_user(
        UserName=userName
    )
    print(response)

deleteUser('new_testuser')
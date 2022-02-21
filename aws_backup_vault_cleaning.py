import boto3
from datetime import datetime

session = boto3.Session(profile_name='<account_name>')

# establish environment variables
PLAN_ID = ""
BACKUP_VAULT_NAME = ""

# establish client session with backup service
client = boto3.client("backup")

# get list of recovery points to delete
recovery_points = client.list_recovery_points_by_backup_vault(
    BackupVaultName=BACKUP_VAULT_NAME,
    #ByResourceType="EC2"
    ByBackupPlanId=PLAN_ID,
    ByCreatedBefore=datetime(2022,1,6)
)

print(recovery_points)

#delete recovery points
for rp in recovery_points:
    response = client.delete_recovery_point(
        BackupVaultName=BACKUP_VAULT_NAME,
        RecoveryPointArn=rp
    )

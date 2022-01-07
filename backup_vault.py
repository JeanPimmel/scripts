import boto3
from datetime import datetime

session = boto3.Session(profile_name='thig-analytics')

# establish environment variables
PLAN_ID = "6032839f-0c9d-4e6f-a53a-d37f35c7a764"
BACKUP_VAULT_NAME = "protected"

# establish client session with backup service
client = boto3.client("backup")

# get list of recovery points to delete
recovery_points = client.list_recovery_points_by_backup_vault(
    BackupVaultName=BACKUP_VAULT_NAME,
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

"""
THIG-PROD
SGWVol-MediumPriorityCrossRegion - 061d541e-ccd3-4596-9699-c957ea89477f
SGWVol-HighPriorityCrossRegion - d33c2034-95b4-435d-98cf-86e612f4724c
LowPriorityCrossRegion - a5acbf9f-eec6-4d52-9d89-ee2c9e197c8b
CriticalPriorityCrossRegion - cdca971c-98f6-409e-8206-f192dd542af1
HighPriorityCrossRegion - 9b144c5d-8c80-4932-99d7-ec46f46e6655
MediumPriorityCrossRegion - 55568e2a-f397-44ae-a877-bd266382a9cc
HighPriorityCrossRegion24HR - 2815be12-3916-462d-aa1c-420658acd933
MediumPriorityCrossRegion24HR - edcdaa49-159e-4b35-8d50-aea1a2368ef7
"""

"""
THIG-ANALYTICS
MediumPriorityCrossRegion24HR - b3e498a7-e30b-48aa-8d60-0bdce1ce152d
CriticalPriorityCrossRegion - 08932cbb-a8d8-49ce-9d77-712b65bc6639
HighPriorityCrossRegion - 13a1ad0e-d6fc-41f3-8149-f73cf498a5d8
SGWVol-HighPriorityCrossRegion - 87e90001-b876-40dd-908e-2375d1f88c2d
MediumPriorityCrossRegion - 4102a24a-6de8-4a58-b7ae-3924309a2690
LowPriorityCrossRegion - 6032839f-0c9d-4e6f-a53a-d37f35c7a764
SGWVol-MediumPriorityCrossRegion - 30ff2ea9-be41-4c42-aeb9-e2f22a87896c
HighPriorityCrossRegion24HR - 25598ee0-285b-44af-b6df-d907e1723da9
"""
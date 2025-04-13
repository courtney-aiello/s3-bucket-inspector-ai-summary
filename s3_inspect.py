import boto3
import json
from typing import List, Dict

# Initialize the S3 client
s3 = boto3.client('s3')

def list_s3_buckets() -> List[str]:
    response = s3.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]

def inspect_bucket(bucket_name: str) -> Dict:
    result = {'bucket': bucket_name, 'public': False, 'encrypted': False, 'versioning': False}

    # Check public access
    try:
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl['Grants']:
            if 'AllUsers' in grant['Grantee'].get('URI', ''):
                result['public'] = True
    except Exception as e:
        result['acl_error'] = str(e)

    # Check encryption
    try:
        enc = s3.get_bucket_encryption(Bucket=bucket_name)
        if enc['ServerSideEncryptionConfiguration']:
            result['encrypted'] = True
    except Exception as e:
        result['encryption_error'] = str(e)

    # Check versioning
    try:
        versioning = s3.get_bucket_versioning(Bucket=bucket_name)
        if versioning.get('Status') == 'Enabled':
            result['versioning'] = True
    except Exception as e:
        result['versioning_error'] = str(e)

    return result

def main():
    bucket_list = list_s3_buckets()
    report = []
    for bucket in bucket_list:
        details = inspect_bucket(bucket)
        report.append(details)

    # Save report as JSON (can be used for AI input later)
    with open('s3_bucket_report.json', 'w') as f:
        json.dump(report, f, indent=2)

if __name__ == '__main__':
    main()

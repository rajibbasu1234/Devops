import boto3
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "MyDatabaseSecrets"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return decoded_binary_secret

# Use the retrieved secrets for your database credentials
import json
secrets = json.loads(get_secret())
DB_USER = secrets['username']
DB_PASS = secrets['password']

## use this credential to connect to DB

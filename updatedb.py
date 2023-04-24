import boto3

# create an instance of the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

# get a reference to the table
table_name = 'url-db'

# add a new attribute to the table
response = dynamodb.update_table(
    TableName=table_name,
    AttributeDefinitions=[
        {
            'AttributeName': 'short_url',
            'AttributeType': 'S'
        }
    ],
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'shortUrlIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'short_url',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            }
        }
    ]
)

print("New attribute added to table.")
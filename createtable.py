import boto3

# create an instance of the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# create the table
table = dynamodb.create_table(
    TableName='url-db',
    KeySchema=[
        {
            'AttributeName': 'url_id',
            'KeyType': 'HASH'  # partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'url_id',
            'AttributeType': 'N'  # number data type
        },
        {
            'AttributeName': 'url',
            'AttributeType': 'S'  # string data type
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'urlIndex',
            'KeySchema': [
                {
                    'AttributeName': 'url',
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
    ]
)

# wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName='url-db')

# add an item to the table
item = {
    'url_id': str(table.item_count + 1),  # convert item_count to a string
    'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO',
    'short_url': 'https://bit.ly/3uLRhzk'
}
table.put_item(Item=item)

print('Item added to table.')
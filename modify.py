import boto3

# create an instance of the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# get a reference to the table
table = dynamodb.Table('url-db')

# get the number of items in the table to use as the next url_id
url_id = table.item_count + 1

# add an item to the table
item = {
    'url_id': url_id,
    'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO',
    'short_url': 'https://bit.ly/3uLRhzk'
}
table.put_item(Item=item)

print('Item added to table.')
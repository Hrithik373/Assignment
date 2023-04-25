import boto3
import pyshorteners

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('url-db')

response = table.get_item(
    Key={
        'url_id': 1
    }
)

if 'Item' in response:
    long_url = response['Item']['url']
    
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    
    
    print(f"Long URL: {long_url}")
    print(f"Short URL: {short_url}")
else:
    print("No item found with the given key.")
import boto3
import os
import json


def lambda_handler(message, context):
    if ('body' not in message or
            message['httpMethod'] != 'GET'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

    table_name = os.environ.get('TABLE', 'Ecommerce')
    region = os.environ.get('REGION', 'us-west-2')

    item_table = boto3.resource(
        'dynamodb',
        region_name=region
    )

    table = item_table.Table(table_name)

    response = table.scan()
    print(response)

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Ecommerce'])
    }

import json
import urllib.parse
import uuid
import boto3
import piexif
import os
import uuid

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    print(bucket)
    print(key)

    s3 = boto3.client('s3')
    ddb = boto3.resource('dynamodb')
    table = ddb.Table(os.environ['METADATA_TABLE'])

    s3.download_file(bucket, key, "/tmp/{}".format(key))


    new_item = {
        'id': uuid.uuid4().hex
    }

    exif_dict = piexif.load("/tmp/{}".format(key))
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            #print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])

            key = piexif.TAGS[ifd][tag]["name"]
            value = exif_dict[ifd][tag]
            
            try:
                value = value.decode('utf-8')
                new_item[key] = value
            except (AttributeError, UnicodeDecodeError) as e:
                print(e)
                pass

    print(new_item)

    table.put_item(Item=new_item)
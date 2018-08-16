# exif-extractor

Lambda Function to extract EXIF data from images uploaded to an S3 bucket and store them in S3.

Flow:
[Image Uploaded To S3] -> [S3 Bucket] -> [Event Notification] -> [Lambda Function] -> [DynamoDB]

## Deployment

This function is packaged with a SAM templated and deployed using SAM.

To build the function and required modules so that it can be deployed to Lambda run the following commands.

```
rm -rf extractor/build
pip install -r requirements.txt -t extractor/build/
cp extractor/*.py extractor/build/
```

To deploy the function, update the following commands as needed to replace <YOUR_S3_BUCKET> with an S3 bucket in your account. This bucket is used by SAM for packaging artifacts.

```
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket <YOUR_S3_BUCKET>

sam deploy \
    --template-file packaged.yaml \
    --stack-name exif-extrator \
    --capabilities CAPABILITY_IAM
```

sh build.sh

sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket shhorsfi-sam-deploy

sam deploy \
    --template-file packaged.yaml \
    --stack-name exif-extrator \
    --capabilities CAPABILITY_IAM
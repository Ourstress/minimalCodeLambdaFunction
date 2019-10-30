#!/bin/sh -l

export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
export AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION
export AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN
export APINAME="$LAMBDA_FUNC_NAME-API"
export OVERLAY_S3URL="s3://${BUCKET_NAME}/${LAMBDA_FUNC_NAME}/lambda-deploy.tgz"

rm -f lambda-deploy.zip
aws s3 cp --acl public-read lambda-deploy-overlay.tgz "$OVERLAY_S3URL"

zip -r ../lambda-deploy.zip *

sam build
sam package --output-template \
    packaged.yaml --s3-bucket "$BUCKET_NAME"

if sam deploy --template-file packaged.yaml \
    --region us-east-1 --capabilities \
    CAPABILITY_IAM --stack-name "$STACK_NAME"
    then 
        exit 0
    else
        exit 1
fi
    
exit 0 
# add --use-container only because I am deploying using cloud9 and cloud9 runtime apparently uses python2.7
sam build --use-container

sam package --output-template packaged.yaml --s3-bucket hello888
    
sam deploy --template-file packaged.yaml --region us-east-1 --capabilities CAPABILITY_IAM --stack-name firebaseLogging
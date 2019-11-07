## Hello

This branch explores the use of dynamodb.

Without using AWS lambda, here's [a video](https://www.youtube.com/channel/UCoMQhQId2QMYaz9Io6SEnnQ) showing one way to connect a vue app to dynamodb for CRUD operations.

## Getting started

1. git clone this repo --branch dynamodb or copy the files in this repo to a folder on your com
2. install aws sam cli either on your computer or simply use cloud9 which comes with aws sam cli
3. make sure you are in the directory with all these files (in cloud9, you can git clone this repo --branch dynamodb into your environment or upload your code to a new repo and git clone it)
4. Edit some stuff in the files below and run the sam build / package / deploy process

   Your key files are template.yaml and deploy.sh

In template.yaml, change the following to your own:

- table name - use your own dynamodb table name instead of minimalCodeTable
- itemId - this is the key for the example dynamodb table. You may want to name it something else but make sure to edit the lambda_handler function to log that something else as a string to dynamodb

In deploy.sh, change the following to your own:

- s3 bucket name - use your own instead of hello888
- stack-name - use your own instead of minimalCodeDynamo

## References

SAM template.yaml for dynamodb

- [Example 1](https://github.com/darpanpathak/AWS-SAM-Lambda-dynamoDB/blob/master/template.yml)
- [Example 2](https://github.com/Ourstress/sam-python-logging/blob/master/sam-app/template.yaml)

[AttributeDefinitions](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html#DDB-CreateTable-request-AttributeDefinitions) are an array of attributes that describe the key schema for the table and indexes.

[KeySchema](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html) represents a single element of a key schema.

- A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
- The attributes in KeySchema must also be defined in the AttributeDefinitions array.

## Debugging notes

Cloudformation

- if rollback means deployment on cloudformation failed
- Check cloudformation events to see exactly which part caused the failure

Lambda Cloudwatch logs

- If you got error messages from post response, lambda cloudwatch logs provide clues

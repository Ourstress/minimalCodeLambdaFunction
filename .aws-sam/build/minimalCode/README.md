## Hello

This branch explores the use of dynamodb.

Without using AWS lambda, here's [a video](https://www.youtube.com/channel/UCoMQhQId2QMYaz9Io6SEnnQ) showing one way to connect a vue app to dynamodb for CRUD operations.

## References

SAM template.yaml for dynamodb

- [Example 1](https://github.com/darpanpathak/AWS-SAM-Lambda-dynamoDB/blob/master/template.yml)
- [Example 2](https://github.com/Ourstress/sam-python-logging/blob/master/sam-app/template.yaml)

[AttributeDefinitions](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html#DDB-CreateTable-request-AttributeDefinitions) are an array of attributes that describe the key schema for the table and indexes.

[KeySchema](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html) represents a single element of a key schema.

- A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.
- The attributes in KeySchema must also be defined in the AttributeDefinitions array.
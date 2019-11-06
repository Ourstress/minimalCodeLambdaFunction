## Hello

This branch explores the use of firebase to log users' answers.

## Getting started

1. Create a new firebase project at https://console.firebase.google.com
2. Setup firestore
3. Within firestore, create a collection called logs
4. Edit some stuff below

Your key files are lambda_function.py and deploy.sh

In lambda_function.py, change the following to your own:

- firebaseProject

In deploy.sh, change the following to your own:

- s3 bucket name - use your own instead of hello888
- stack-name - use your own instead of minimalCodeDynamo

## References

## Debugging notes

Cloudformation

- if rollback means deployment on cloudformation failed
- Check cloudformation events to see exactly which part caused the failure

Lambda Cloudwatch logs

- If you got error messages from post response, lambda cloudwatch logs provide clues

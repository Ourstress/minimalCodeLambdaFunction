## Hello

This branch explores the use of firebase to log users' answers.

## Getting started

1. Create a new firebase project at https://console.firebase.google.com
2. Setup a realtime database
3. Within the realtime database, set the rules of read and write to true
4. Edit some stuff below them run the sam build / package / deploy process

Your key files are lambda_function.py and deploy.sh

In lambda_function.py, change the following to your own:

- firebaseProject

In deploy.sh, change the following to your own:

- s3 bucket name - use your own instead of hello888
- stack-name - use your own instead of firebaseLogging

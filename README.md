## Hello

This branch explores the use of firebase to log users' answers.

## Getting started

1. Create a new firebase project at https://console.firebase.google.com
2. Setup a realtime database
3. Within the realtime database, set the rules of read and write to true
4. git clone this repo --branch firebaseLogging or copy the files in this repo to a folder on your com
5. install aws sam cli either on your computer or simply use cloud9 which comes with aws sam cli
6. make sure you are in the directory with all these files
7. Edit some stuff in the files below and run the sam build / package / deploy process

Your key files are lambda_function.py and deploy.sh

In lambda_function.py, change the following to your own:

- firebaseProject

In deploy.sh, change the following to your own:

- s3 bucket name - use your own instead of hello888
- stack-name - use your own instead of firebaseLogging

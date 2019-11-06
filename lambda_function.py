# Python 3.6 runtime
# Demo at https://wvf931d67j.execute-api.us-east-1.amazonaws.com/default/minimalCodeFirebase

import json
import requests

def lambda_handler(event, context):

    with open('index.html') as file:
        indexPage = file.read()
    
    method = event.get('httpMethod',{}) 
    if method == 'GET':
        return {
            "statusCode": 200,
            "headers": {
            'Content-Type': 'text/html',
            },
            "body": indexPage
        }
        
    if method == 'POST':
        bodyContent = event.get('body',{}) 
        parsedBodyContent = json.loads(bodyContent)
        answer = parsedBodyContent["hidden"]["0"]
        solution = parsedBodyContent["editable"]["0"] 
        results = "wrong"
        if answer == solution:
            results = "correct"

        firebaseProject = "https://minimalcode-10cd5.firebaseio.com/"
        url = firebaseProject+"/logs.json"   
        log = {'answers':solution} 
        response = requests.post(url=url,data=json.dumps(log))
        results = json.loads(response.text)

        return {
            "statusCode": 200,
            "headers": {
            "Content-Type": "application/json",
                },
            "body":  json.dumps({
                "isComplete": results,
                "jsonFeedback": results,
                "htmlFeedback": results,
                "textFeedback": results
            })
            }

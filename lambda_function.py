# Python 3.7 runtime
# Demo at https://o25djybnr2.execute-api.us-east-1.amazonaws.com/default/minimalFiveTabActivity

import json
    
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
        return {
            "statusCode": 200,
            "headers": {
            "Content-Type": "application/json"
                },
            "body":  json.dumps({
                "isComplete": results,
                "jsonFeedback": results,
                "htmlFeedback": results,
                "textFeedback": results
            })
            }

# Python 3.7 runtime

import json
import pandas as pd

def lambda_handler(event, context):

    with open('index.html') as file:
        indexPage = file.read()
    
    # Just to see if pandas was imported
    catData = {'cat': ['sylvester', 'timmy'], 'job': ['housecat', 'firefighter']}
    df = pd.DataFrame(data=catData)

    method = event.get('httpMethod',{}) 
    if method == 'GET':
        return {
            "statusCode": 200,
            "headers": {
            'Content-Type': 'text/html',
            },
            "body": df.to_html()  + indexPage
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

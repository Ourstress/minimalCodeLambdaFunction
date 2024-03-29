# Python 3.7 runtime
# Demo at https://o25djybnr2.execute-api.us-east-1.amazonaws.com/default/minimalFiveTabActivity

import json
    
def lambda_handler(event, context):
    indexHead = """
    <head>
        <meta charset="utf-8">
        <meta content="width=device-width,initial-scale=1,minimal-ui" name="viewport">
        <link rel="stylesheet" href="https://unpkg.com/vue-material@beta/dist/vue-material.min.css">
        <link rel="stylesheet" href="https://unpkg.com/vue-material@beta/dist/theme/default.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.32.0/codemirror.min.css" />
    </head>
    """  
    indexBody = """
    <body>
         <h1>Pythonic Code Activity</h1>
        <div id="app">
            <md-tabs>
                <md-tab v-for="question in questions" :key=question.name v-bind:md-label=question.name+question.status>
                    <doctest-activity v-bind:ui-items=question v-bind:question-name=question.name  @questionhandler="toggleQuestionStatus"/>
                </md-tab>
            </md-tabs>
            </div>
        </div>
    </body> 
    """

    indexScriptsAfterBody = """
    <script src="https://unpkg.com/vue"></script>
    <script src="https://unpkg.com/vue-material@beta"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.32.0/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/mode/python/python.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue-codemirror@4.0.6/dist/vue-codemirror.min.js"></script>
    <script>
    Vue.use(VueMaterial.default)
    Vue.use(window.VueCodemirror)
    """

    vueComponent = """
    Vue.component('doctest-activity', {
        props: ['uiItems', 'questionName'],
        data: function () {
            return {
            answer:{jsonFeedback:'',htmlFeedback:'',textFeedback:'',isComplete:false},
            uiItem: this.uiItems,
            cmOptions: {
              mode: 'python',
              lineNumbers: true
            }
        }
        },
        methods: {
            postContents: function () {
            // comment: leaving the gatewayUrl empty - API will post back to itself
            const gatewayUrl = '';
            fetch(gatewayUrl, {
        method: "POST",
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({shown:{0:this.uiItem.tabItems.test},editable:{0:this.uiItem.tabItems.editable}, hidden:{0:this.uiItem.hidden}})
        }).then(response => {
            return response.json()
        }).then(data => {
            this.answer = JSON.parse(JSON.stringify(data))
            // emit 'questionhandler' to update status of question
            return this.$emit('questionhandler',{data, questionName:this.questionName})
            })
         }
        },
        template: 
        `<md-tabs>
            <md-tab v-for="(value, name) in uiItems.tabItems" v-bind:key=name v-bind:md-label=name>  
                <md-card>
                    <md-card-media>
                    <md-button class="md-raised md-primary" v-on:click="postContents">Submit</md-button>
                    </md-card-media>
                    <md-card-content>
                        <md-field>
                            <codemirror class="editableTextarea" v-model="uiItems.tabItems[name]" :options="cmOptions"></codemirror>
                        </md-field>
                    </md-card-content>
                </md-card>
            </md-tab>
        </md-tabs>`
    })
    """

    vueApp = """
    new Vue({
        el: '#app',
        data: function () {
            return {
            questions:[
                {name:"question 1", status:" 🔴", hidden:"10 + 10", tabItems:{introduction:"add 10 and 10", editable:"#replace this comment with answer", hint:"answer should be 20"}},
                {name:"question 2", status:" 🔴", hidden:"10 - 5", tabItems:{introduction:"subtract 5 from 10", editable:"#replace this comment with answer", hint:"answer should be 5"}},
                {name:"question 3", status:" 🔴", hidden:"True", tabItems:{introduction:"what is the opposite of False?", editable:"#replace this comment with answer", hint:"answer should be opposite of False"}},
                {name:"question 4", status:" 🔴", hidden:"not", tabItems:{introduction:"logical operators are AND, OR and ?", editable:"#replace this comment with answer", hint:"no hints"}},
                {name:"question 5", status:" 🔴", hidden:"cats and dogs", tabItems:{introduction:"it was raining what and what?", editable:"#replace this comment with answer", hint:"think of animals"}}
            ]
        }
        },
         methods: {
            toggleQuestionStatus (response) {
                const {data, questionName} = response
                window.alert("you got the question "+data.htmlFeedback)
                if (data.htmlFeedback === "correct") {
                this.questions.find(item => item.name === questionName).status = " ✔️"
                }
            }
        }
      })
    </script>
    """

    indexPage=f"""
   <html>
    {indexHead}
    {indexBody}
    {indexScriptsAfterBody}
    {vueComponent}
    {vueApp}
    </html>
    """
    
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
            "Content-Type": "application/json",
                },
            "body":  json.dumps({
                "isComplete": results,
                "jsonFeedback": results,
                "htmlFeedback": results,
                "textFeedback": results
            })
            }

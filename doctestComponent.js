Vue.component("doctest-activity", {
  props: ["uiItems", "questionName"],
  data: function() {
    return {
      answer: {
        jsonFeedback: "",
        htmlFeedback: "",
        textFeedback: "",
        isComplete: false
      },
      uiItem: this.uiItems,
      cmOptions: {
        mode: "python",
        lineNumbers: true
      }
    };
  },
  methods: {
    postContents: function() {
      // comment: leaving the gatewayUrl empty - API will post back to itself
      const gatewayUrl = "";
      fetch(gatewayUrl, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          shown: { 0: this.uiItem.tabItems.test },
          editable: { 0: this.uiItem.tabItems.editable },
          hidden: { 0: this.uiItem.hidden }
        })
      })
        .then(response => {
          return response.json();
        })
        .then(data => {
          this.answer = JSON.parse(JSON.stringify(data));
          // emit 'questionhandler' to update status of question
          return this.$emit("questionhandler", {
            data,
            questionName: this.questionName
          });
        });
    }
  },
  template: `<md-tabs>
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
});

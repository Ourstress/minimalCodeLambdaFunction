Vue.use(VueMaterial.default);
Vue.use(window.VueCodemirror);

("$$doctestComponent$$");

new Vue({
  el: "#app",
  data: function() {
    return {
      questions: [
        {
          name: "question 1",
          status: " 🔴",
          hidden: "10 + 10",
          tabItems: {
            introduction: "add 10 and 10",
            editable: "#replace this comment with answer",
            hint: "answer should be 20"
          }
        },
        {
          name: "question 2",
          status: " 🔴",
          hidden: "10 - 5",
          tabItems: {
            introduction: "subtract 5 from 10",
            editable: "#replace this comment with answer",
            hint: "answer should be 5"
          }
        },
        {
          name: "question 3",
          status: " 🔴",
          hidden: "True",
          tabItems: {
            introduction: "what is the opposite of False?",
            editable: "#replace this comment with answer",
            hint: "answer should be opposite of False"
          }
        },
        {
          name: "question 4",
          status: " 🔴",
          hidden: "not",
          tabItems: {
            introduction: "logical operators are AND, OR and ?",
            editable: "#replace this comment with answer",
            hint: "no hints"
          }
        },
        {
          name: "question 5",
          status: " 🔴",
          hidden: "cats and dogs",
          tabItems: {
            introduction: "it was raining what and what?",
            editable: "#replace this comment with answer",
            hint: "think of animals"
          }
        }
      ]
    };
  },
  methods: {
    toggleQuestionStatus(response) {
      const { data, questionName } = response;
      window.alert("you got the question " + data.htmlFeedback);
      if (data.htmlFeedback === "correct") {
        this.questions.find(item => item.name === questionName).status = " ✔️";
      }
    }
  }
});

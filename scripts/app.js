new Vue({
  el: '#app',
  data: {
    message: getUrlVars()["me"]
  },
  methods: {
  	requestModel: function() {
  		alert("hi")
  	}
  }
})
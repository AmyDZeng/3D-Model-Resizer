new Vue({
    el: '#app',
    data: {
        message: ''
    },
    methods: {
        requestModel: function() {
            this.$http.get('http://10.71.134.218:5000/').then((response) => {
                this.message = response.text()
                document.getElementById('download_frame').src = response.text();
            }, (response) => {
                this.message = 'failure'
            });
        }
    }
})
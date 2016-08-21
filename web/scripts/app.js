new Vue({
    el: '#app',
    data: {
        message: ''
    },
    methods: {
        requestSword: function() {
            this.$http.get('http://10.71.134.218:5000/sword/').then((response) => {
                this.message = response.text()
                document.getElementById('download_frame').src = response.text();
            }, (response) => {
                this.message = 'failure'
            });
        },
        requestGuard: function() {
            this.$http.get('http://10.71.134.218:5000/guard/').then((response) => {
                this.message = response.text()
                document.getElementById('download_frame').src = response.text();
            }, (response) => {
                this.message = 'failure'
            });
        },
        customizeSword: function () {
            var newHTML = '<div class="card-content">'+
                '<label for="length">Length:</label>' + 
                '<input type="number" required></input>'+
                '</div>';
            $('#sword').replaceWith(newHTML);
            $('#sword-customize').hide();
            $('#sword-download').show();
        },
        customizeSword2: function () {
            var newHTML = '<div class="card-content">'+
                '<label for="length">Length:</label>' + 
                '<input type="number" required></input>'+
                '</div>';
            $('#sword2').replaceWith(newHTML);
            $('#sword2-customize').hide();
            $('#sword2-download').show();
        },
        customizeGuard: function () {
            var newHTML = '<div class="card-content">'+
                '<label for="wrist">Wrist Radius:</label>' + 
                '<input type="number" required></input>'+
                '<label for="forearm">Forearm Radius:</label>' + 
                '<input type="number" required></input>'+
                 '</div>';
            $('#guard').replaceWith(newHTML);
            $('#guard-customize').hide();
            $('#guard-download').show();
        }
    }
})
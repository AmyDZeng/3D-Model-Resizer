new Vue({
    el: '#app',
    data: {
        message: '',
        swordLength: 0,
        wristRadius: 0,
        forearmRadius: 0
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
            $('#sword').hide();
            $('#sword-params').show();
            $('#sword-customize').hide();
            $('#sword-download').show();
        },
        customizeSword2: function () {
            $('#sword2').hide();
            $('#sword2-params').show();
            $('#sword2-customize').hide();
            $('#sword2-download').show();
        },
        customizeGuard: function () {
            $('#guard').hide();
            $('#guard-params').show();
            $('#guard-customize').hide();
            $('#guard-download').show();
        }
    }
})
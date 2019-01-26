var app = new Vue({
    el: '#helloworld',
    data: {
        recentdata:[
            "2+2=4"
        ],

        keymap:[
            ['C','0','/','='],
            ['1','2','3','+'],
            ['4','5','6','-'],
            ['7','8','9','*']
            
        ],

        expression:"000"
        
    },
    delimiters: ['[[',']]'],
    methods: {
        push(char){
            this.expression += char
        },
        getRecentData(){
            this.$http.get('http://localhost:5000/').then(response => {
                this.recentdata = response.data
            }, response => {
                console.log('error')
            });
        },
        
        manInTheMiddle(){
            var data = this.displaydevice.ip
            this.$http.post('http://localhost:5000/evaluate', {"expression": data}).then(response => {
                console.log(response.data)
            }, (response) => {
                console.log(response)
            });
        }
    },
})

var app = new Vue({
    el: '#helloworld',
    data: {
        recentdata:[
        ],

        keymap:[
            ['C','0','/','*'],
            ['1','2','3','+'],
            ['4','5','6','-'],
            ['7','8','9','=']
            
        ],

        expression:""
        
    },
    delimiters: ['[[',']]'],
    methods: {
        push(char){
            if (this.expression.length > 3){
                lastchar = this.expression[this.expression.length - 1]
                console.log(lastchar)
            }
            if (char == '='){
                this.postreq(this.expression)
                this.expression = ''
            }else if (char == 'C'){
                this.expression = ''
            }
            else {
                if(isNaN(this.expression[this.expression.length - 1])){
                    if(!isNaN(char)){
                        this.expression += char
                    }
                    else{
                        this.expression = this.expression.substring(0, this.expression.length - 1) + char
                    }
                }
                else{
                    this.expression += char
                }
            }

        },
        getRecentData(){
            this.$http.get("http://localhost:5000/recent_data").then(response => {
                this.recentdata = response.body
            }, (response) => {
            });
        },
        
        postreq(data){
            this.$http.post('http://localhost:5000/evaluate', {"expression": data}).then(response => {
                console.log(response)
                this.recentdata = response.body
            }, (response) => {
                console.log(response)
            });
        }
    },
})

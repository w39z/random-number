new Vue({
    el: '#rnd'
    methods: {
    randomNumber : function setInterval(function(){
    console.log(Math.floor((Math.random()*100)+1));
}, 500);
        }
    }
)

//$setInterval(function(){
//    console.log(Math.floor((Math.random()*100)+1));
//}, 500);

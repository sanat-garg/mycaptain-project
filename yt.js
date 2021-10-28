var number = 90;
var timepercomment = 1000;
var comments = [
    "pls quasar brother remove strike from my channel callmesoham, i am sad, pls help,i will not do this again",
    "pls remove strike from my channel 'callmesoham', its a request",
    "pls remove strike quasar brother from my channel callmesoham, it would be great for me, thank you"
];

/* DONT MAKE CHANGES BELOW THIS LINE*/

var d= document.getElementById('contenteditable-root');var a=document.getElementById('submit-button');i=0;setInterval(function(){if(i<number){d.innerHTML = comments[i%(comments.length)];a.disabled = false;a.click();console.log("Comment no. "+i+" initiated.");i++;}},timepercomment)

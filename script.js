//declaring variables
var base = [];
var target = [];

//gets target and base language lists
function collect(){
    document.querySelectorAll("div.baseLanguage").forEach(i => base.push(i.innerText));
    document.querySelectorAll("div.targetLanguage").forEach(i => target.push(i.innerText));
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

//function to input text and submit
async function start(time){
    while (true){
        async function submit(answer) {
            (await document.querySelector("button#explanation-button")).click();
            document.querySelector("input#answer-text").value = answer;
        }
        
        //gets answer
        question = document.getElementById("question-text").innerText;
        answer = (target[base.indexOf(question)]);
        
        submit(answer);
        await sleep(time);
    }
}
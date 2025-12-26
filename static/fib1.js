
const prompt = require("prompt-sync")();

let x = 1;
let y = 1;
let z;
let cnt = 1
let lst = [x];
let lstl = 10;



while(1){
    z = x + y;
    x = y;
    y = z;
    let xto = x;
    while(xto > 12){
        xto -= 12;
    }
    lst.push(xto)
    cnt ++;
    
    if(lst.length % lstl === 0){
        console.log(lst);
        // console.log(lst[9] / lst[8]);
        lst = [];
        prompt("");
    }
}



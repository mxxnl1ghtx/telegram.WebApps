let tg = window.Telegram.WebApp;

tg.expand()

tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37"

let item = "";

let buttons = document.querySelectorAll(".btn");
buttons.forEach(el => {
    el.addEventListener('click', event =>{
        if (tg.MainButton.isVisible) {
            tg.MainButton.hide();
        } else {
            tg.MainButton.setText("Вы выбрали товар " + el);
            item = "1";
            RegExp.MainButton.show();
        }
    }); 
}); 

Telegram.WebApp.onEvent("mainButtonClicked", event => {
    tg.sendData(item);
})

let usercard = document.getElementById("usercard");

let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`;

usercard.appendChild(p)

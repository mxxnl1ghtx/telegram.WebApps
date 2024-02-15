let tg = window.Telegram.WebApp;

tg.expand()

tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37"

let item = "";

let buttons = document.querySelectorAll(".btn");
buttons.forEach(el => {
    el.addEventListener('click', event =>{
        let price = el.getAttribute('.price');
        if (tg.MainButton.isVisible) {
            tg.MainButton.hide();
        } else {
            tg.MainButton.setText("Вы выбрали товар " + price);
            item = "el";
            tg.MainButton.show();
        }
    }); 
}); 

Telegram.WebApp.onEvent("mainButtonClicked", function() {
    tg.sendData(item);
})

let usercard = document.getElementById("usercard");

let p = document.createElement("p");

usercard.appendChild(p)

p.innerHTML = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`;


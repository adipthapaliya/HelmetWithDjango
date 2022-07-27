const buttons = document.querySelectorAll('.button');

buttons.forEach(button => {
    button.addEventListener('click',()=>{
        for (let i = 0; i < buttons.length; i++){
            buttons[i].classList.remove('button-active');
          }
        button.classList.add('button-active');
    });
});
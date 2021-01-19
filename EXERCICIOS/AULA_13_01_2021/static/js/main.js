(function() {
    'use strict';

    const container = document.querySelector('.container');
    const guessInput = document.querySelector('#guessInput');
    const button = document.querySelector('button');    
    const lastGuesses = document.querySelector('.lastGuesses');
    const feedbackMsg = document.querySelector('.feedbackMsg');
    const tipMsg = document.querySelector('.tipMsg');
    let newGameButton;

    let sortedNumber = Math.floor(Math.random() * 100 + 1);
    let guessesCount = 1;

    function restartGameConfig() {
        let paragraphsInMsgContainer = document.querySelectorAll('.msgContainer p');
        for (let i = 0;  i < paragraphsInMsgContainer.length; i++) {
            paragraphsInMsgContainer[i].textContent = '';
        }
        guessInput.value = '';
        guessInput.focus();
        guessInput.disabled = false;
        button.disabled = false;
        newGameButton.parentNode.removeChild(newGameButton);
        sortedNumber = Math.floor(Math.random() * 100 + 1);
        guessesCount = 1;
    }

    function endGameConfig() {
        guessInput.disabled = true;
        button.disabled = true;
        newGameButton = document.createElement('button');
        newGameButton.textContent = 'Iniciar um novo jogo!';
        container.appendChild(newGameButton);
        newGameButton.addEventListener('click', restartGameConfig);
    }

    function sendGuess() {    
        console.log(sortedNumber);    
        const numberGuessed = parseInt(guessInput.value);

        if (guessesCount === 1) {
            lastGuesses.textContent = 'Palpites anteriores: ';
        }
        lastGuesses.textContent += numberGuessed + ' ';

        if (numberGuessed === sortedNumber) {
            tipMsg.textContent = ''
            feedbackMsg.textContent = 'Parabéns! Seu número está certo!';
            feedbackMsg.style.backgroundColor = 'green';
            endGameConfig();
        } else if (guessesCount === 10) {
            feedbackMsg.textContent = '!!!FIM DE JOGO!!!';
            feedbackMsg.style.backgroundColor = 'red';
            endGameConfig();
        } else {    
            feedbackMsg.textContent = 'Errado!';
            feedbackMsg.style.backgroundColor = 'red';        
            
            (numberGuessed < sortedNumber) ?
                tipMsg.textContent = 'Seu palpite está muito baixo!'
            :
                tipMsg.textContent = 'Seu palpite está muito alto!';                          
        }

        guessInput.value = '';
        guessInput.focus();
        guessesCount ++;
    }

    button.addEventListener('click', sendGuess);
})();
let displayedImg = document.querySelector('.displayed-img');
let overlay = document.querySelector('.overlay');
let btn = document.querySelector('button');
let thumbBar = document.querySelector('.thumb-bar');

// Adicionando as imagens na div
for (let i = 1; i <= 5; i++) {
    let thumbImg = document.createElement('img');
    thumbImg.setAttribute('src', `static/img/pic${i}.jpg`);
    thumbImg.addEventListener('click', e => {
        displayedImg.src = e.target.src; 
    });
    thumbBar.appendChild(thumbImg);
}

// Implementando o botão
btn.addEventListener('click', () => {
    const btnClass = btn.getAttribute('class');
    if (btnClass === 'dark') {
        btn.setAttribute('class', 'light');        
        btn.textContent = 'Clarear';
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    } else {
        btn.setAttribute('class', 'dark');
        btn.textContent = 'Escurecer';
        overlay.style.backgroundColor = 'transparent';
    }
});
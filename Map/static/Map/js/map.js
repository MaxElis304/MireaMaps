let tooltip = document.querySelector('.tooltip');
let classes = document.querySelectorAll('.aud');
let search_results = document.querySelectorAll('.search_res');
let popupBG = document.querySelector('.info__bg');
let popup = document.querySelector('.info');

classes.forEach(aud => {
    aud.addEventListener('click', function () {
        popup.querySelector('.info__title').innerText = this.dataset.title;
        popup.querySelector('.info__text').innerText = this.dataset.description;
        popupBG.classList.add('active');
    })

    aud.addEventListener('mouseenter', function (e) {
        tooltip.innerText = this.dataset.title;
        tooltip.style.top = (e.y + 20) + 'px';
        tooltip.style.left = (e.x + 20) + 'px';
    });

    aud.addEventListener('mouseenter', function () {
        tooltip.style.display = 'block';
    });

    aud.addEventListener('mouseleave', function () {
        tooltip.style.display = 'none';
    });
});

document.addEventListener('click', (e) => {
    if(e.target === popupBG){
        popupBG.classList.remove('active');
    }
})
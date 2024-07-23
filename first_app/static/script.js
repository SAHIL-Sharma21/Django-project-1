console.log("Js file added");

const btn = document.querySelector('#btn1');
btn.addEventListener('click', () => {
    const para = document.querySelector('#para1');
    const linkElement = document.createElement('a');
    linkElement.href = 'https://docs.djangoproject.com/en/5.0/'
    linkElement.textContent = "Django Documentation"
    linkElement.style.color = "red"
    para.innerHTML = '';
    para.appendChild(linkElement);
})
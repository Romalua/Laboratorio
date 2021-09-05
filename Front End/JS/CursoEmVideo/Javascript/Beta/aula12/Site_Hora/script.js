function carregar() {
    var msg = window.document.getElementById('msg');
    var img = window.document.getElementById('imagem');
    var data = new Date();
    var hora = data.getHours();
    var minuto = data.getMinutes ();

    msg.innerHTML = `São ${hora} horas e ${minuto} minutos.`;
    if (hora >= 0 && hora < 12){
        //BOM DIA!
        msg.innerHTML += `<p>BOM DIA!</p>`
        img.src = 'manha.png';
        document.body.style.background = '#e2cd9f';
    } else if (hora >= 12 && hora <= 18) {
        //BOA TARDE!
        msg.innerHTML += `<p>BOA TARDE!</p>`
        img.src = 'tare.png';
        document.body.style.background = "#b9846f";
    } else {
        //BOA NOITE!
        msg.innerHTML +=`<p>BOA NOITE PORRA!</p>`
        img.src = 'noite.png';
        document.body.style.backkkground = "#515154";
    }
}
window.onload = function () {
    /*Ejecuciones para efecto activo en menuBar*/
    var idd = { id: getPageTitle() };
    active(idd);
    
    /*Fin de ejecuciones para efecto activo en menuBar*/
}

/*Ejecuciones para efecto activo en menuBar*/
function getPageTitle(){
    var t = document.getElementsByTagName('title')[0];
    if ( !!t.childNodes.length ) {
        return t.firstChild.data;
        
    } else if ( t.innerHTML ) {
        return t.innerHTML;
    }
}
function active(idd) {
    var idds = ["inicio", "empresa", "anuncios","porfolio","contacto"];
    for (var id in idds) {
        if (idds[id].includes(idd.id.toLowerCase())) {
            document.getElementById(idds[id]).classList.add("activated");
            window.menuActive = idd;
        } else
        document.getElementById(idds[id]).classList.remove("activated");
    }
}
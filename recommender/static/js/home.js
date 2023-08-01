function send_data(){
    document.querySelector('form').addEventListener("submit",form_handler);
    var fd = new FormData(document.querySelector('form'));
    
    var xhr = new XMLHttpRequest({mozSystem: true});
    
    xhr.open('POST', 'search_results/', true);
    document.getElementById('movieList').innerHTML="Searching...";
    
    xhr.onreadystatechange = function(){
        if(xhr.readyState == XMLHttpRequest.DONE){

            const jsonResponse = JSON.parse(xhr.responseText);
            const movieNames = jsonResponse.result;
            console.log(movieNames);

            const movieListHTML = movieNames.map(movie => `<li>${movie}</li>`).join('');
            document.getElementById('movieList').innerHTML = `<ul>${movieListHTML}</ul>`;

        }
    }
    
    xhr.onload = function(){};
    
    xhr.send(fd);
}

function form_handler(event){
    event.preventDefault();
}


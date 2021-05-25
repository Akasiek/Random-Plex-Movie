// Main function which displays all movie data in the app
// window.onload makes sure the function is run when the app starts up
window.onload = document.getElementById('btn_watch').onclick = async function showMovieInHTML() {
    // Get movie data from python
    var py_movie = await eel.py_returnMovie()();

    // After loading all data, show content of the app
    document.getElementById("section").classList.remove("hidden");


    // Changing data in HTML to movie details:
    // Title
    document.getElementById("title").innerHTML = py_movie["title"];

    // Year and duration
    document.getElementById("year_duration").innerHTML = py_movie["year"] + " <span style=\"font-weight:300\">|</span> " + py_movie["duration_hours"] + "h" + " " + py_movie["duration_minutes"] + "m";

    // Director/s
    var directors_p = document.getElementById("directors");

    directors_p.innerHTML = "<span style=\"font-weight:700\">Directed by:</span>";
    py_movie["directors"].forEach(element => {
        directors_p.innerHTML += " " + element + ", ";
    });
    directors_p.innerHTML = directors_p.innerHTML.replace(/(\s+)?..$/, '');

    // Writer/s
    var writers_p = document.getElementById("writers");

    writers_p.innerHTML = "<span style=\"font-weight:700\">Written by:</span>";
    py_movie["writers"].forEach(element => {
        writers_p.innerHTML += " " + element + ", ";
    });
    writers_p.innerHTML = writers_p.innerHTML.replace(/(\s+)?..$/, '');

    // Actors
    var actors_p = document.getElementById("actors");

    actors_p.innerHTML = "<span style=\"font-weight:700\">Cast:</span>";
    py_movie["actors"].forEach(element => {
        actors_p.innerHTML += " " + element + ", ";
    });
    actors_p.innerHTML = actors_p.innerHTML.replace(/(\s+)?..$/, '');

    // Poster
    document.getElementById("poster_img").src = py_movie["poster"];

    // BG Art
    document.getElementById("img_background").style.background = 'url(' + py_movie["background"] + ')';
};


// This sections makes the "WATCH" button work...
// Hides client prompt
document.getElementById("client_prompt_close").addEventListener("click", function() {
    document.getElementById("client_prompt").classList.add("hidden");
});

// Takes list of clients and display them as options for choosing where to watch content
document.getElementById("btn_next_movie").addEventListener("click", async function() {
    // Get list of clients from python
    var clients = await eel.py_returnClients()();

    // Clear the list of clients
    list_of_clients.innerHTML = "";
    // Make client prompt visible
    document.getElementById("client_prompt").classList.remove("hidden");

    // For each client make new div
    clients.forEach(client => {
        document.getElementById("list_of_clients").innerHTML += "<div class=\"client\" onclick=\"playMovie('" + client + "');closeClientPrompt()\"><p>" + client + "</p></div>";
    });
});

function playMovie(client) {
    // Does what the name says...
    eel.py_playMovie(client);
}

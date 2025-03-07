document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("myModal");
    var btn = document.getElementById("myBtn");
    var span = document.getElementsByClassName("close")[0];

    if (btn && modal && span) {
        btn.onclick = function() {
            modal.style.display = "block";
        };

        span.onclick = function() {
            modal.style.display = "none";
        };

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        };
    } else {
        console.log("Modal elements not found on this page.");
    }
});
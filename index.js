var darklight = document.getElementById("darklight");
var darkMode = document.getElementById("darkMode")

var viewMode = 1;

if (document.cookie === "viewmode=0") {
    darkMode.innerHTML = "";
    viewMode = 0;
}

darklight.addEventListener("click", function () {
    if (viewMode === 0) {
        darkMode.innerHTML = "<link href=\"index_dark.css\" rel=\"stylesheet\">";
        viewMode = 1;
        document.cookie = "viewmode=1"
    } else {
        darkMode.innerHTML = "";
        viewMode = 0;
        document.cookie = "viewmode=0"
    }
})
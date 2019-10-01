    function changeTab(tab) {
        if (tab == "home") {
            document.getElementById("home").style.display = "block"
            document.getElementById("messages").style.display = "none"
        } else if (tab == "messages") {
            document.getElementById("home").style.display = "none"
            document.getElementById("messages").style.display = "block"
        }

}

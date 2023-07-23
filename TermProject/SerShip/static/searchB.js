function searchItems() {
    console.log("Search button clicked.");
    var input, filter, ul, li, item, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.trim().toUpperCase();
    console.log("Search query:", filter);

    // Check if the search input is not empty
    if (filter !== "") {
        ul = document.getElementById("itemsList"); // Replace "itemsList" with the ID of your items list (e.g., <ul id="itemsList">)
        li = ul.getElementsByTagName("li");

        var foundItems = [];
        // Loop through all list items and find the matching items
        for (i = 0; i < li.length; i++) {
            item = li[i].getElementsByTagName("p")[0]; // Replace "p" with the element containing the item name
            txtValue = item.textContent || item.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                foundItems.push(li[i].innerHTML);
            }
        }

        // Display the matching items in the searchResults container
        var searchResultsContainer = document.getElementById("searchResults");
        searchResultsContainer.innerHTML = foundItems.join("");
    }
}

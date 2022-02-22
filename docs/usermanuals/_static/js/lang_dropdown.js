function add_lang_dropdown(json_loc, text) {
    var dropdown = document.createElement("div");
    dropdown.className = "md-flex__cell md-flex__cell--shrink dropdown";
    var button = document.createElement("button");
    button.className = "dropdownbutton";
    var content = document.createElement("div");
    content.className = "dropdown-content md-hero";
    dropdown.appendChild(button);
    dropdown.appendChild(content);
    $.getJSON(json_loc, function(languages) {
        for (var key in languages) {
            if (languages.hasOwnProperty(key)) {
                var a = document.createElement("a");
                a.innerHTML = key;
                a.title = key;
                a.href = languages[key];
                content.appendChild(a);
            }
        }
    }).done(function() {
        button.innerHTML = text;
    }).fail(function() {
        button.innerHTML = "Languages not found";
    }).always(function() {
        $(".navheader").append(dropdown);
    });
};

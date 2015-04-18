function showResults() {
    $.ajax({
        type: "POST",
        url: "/results"
    });
}
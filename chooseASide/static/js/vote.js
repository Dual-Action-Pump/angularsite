function sendVote(pk, topicURL) {
    console.log($("#"+pk));
    console.log(topicURL);
    var opinion = $("#"+pk);
    var csrftoken = getCookie('csrftoken');
    $.post( topicURL, { vote: pk, csrfmiddlewaretoken: csrftoken}, function(data){
        console.log(data);
        opinion.text("Got it!");
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


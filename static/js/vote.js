function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


function sendVote(pk, topicURL) {

    var score = $("#"+pk+"_score");
    console.log(score);
    var opinion = $("#"+pk);
    opinion.attr('onclick', '');
    var csrftoken = getCookie('csrftoken');
    $.post( topicURL, { vote: pk, csrfmiddlewaretoken: csrftoken}, function(data){
        var parsed = JSON.parse(data);
        score.text("Score: "+parsed['current_score']);
        console.log(data['current_score']);
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


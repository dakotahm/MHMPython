


//This comes from stackoverflow http://stackoverflow.com/questions/24496751/django-403-error-on-ajax-view-with-csrf-token
//very important it gets the cookie containing the security token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

//sets head of dropdown to first selected value
function updatedrop(){
    var input =$('#measurable-dropdown li:first').children().first().text();
    var id=$('#measurable-dropdown li:first').attr('class');
    $('#MeasurableDropdownTitle').text(input);
    $('#MeasurableDropdownTitle').attr('class',id);

      $.ajax({
            type:'POST',
            url: '/display/logs/',

            //this is the data being passed into the post in JSON format
            data:{
                'measuraleId': $('#MeasurableDropdownTitle').attr('class'),
                'timeframe':$('#TimeDropdownTitle').text(),
                csrfmiddlewaretoken: csrftoken
            },
            datatype:'json',
            success:function (data) {
                //replaces the html in container with the results from the query
                $('#log-container').html(data.html);
            }
        })
}


//everything in here calls when the document loads
$("document").ready(function() {
    //this is the listener to both dropdowns
    $('.dropdown-menu li').on('click',function () {

        //update the values in the dropdown each if is what happends if a dropdown is pressed
        if($(this).parent().attr("id")=="measurable-dropdown"){
            //sets the text
            $('#MeasurableDropdownTitle').text($(this).children().first().text());

            //stores the id of the clicked item in an accessible place
            $('#MeasurableDropdownTitle').attr('class',$(this).attr('class'));
        }else if($(this).parent().attr("id")=="time-dropdown"){
            $('#TimeDropdownTitle').text($(this).children().first().text());
        }
        //now that the two values are stored in the title of the dropdown we can do an ajax call
        //this will be processed in the local views.py the ajax is directed by the url parameter
        $.ajax({
            type:'POST',
            url: '/display/logs/',

            //this is the data being passed into the post in JSON format
            data:{
                'measuraleId': $('#MeasurableDropdownTitle').attr('class'),
                'timeframe':$('#TimeDropdownTitle').text(),
                csrfmiddlewaretoken: csrftoken
            },
            datatype:'json',
            success:function (data) {
                //replaces the html in container with the results from the query
                $('#log-container').html(data.html);
            }
        })
    });

    //when the document loads the logs move to the first available measurable
    updatedrop();
});


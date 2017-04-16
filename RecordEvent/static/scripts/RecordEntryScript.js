/**
 * Created by Dakotah on 4/9/2017.
 */
$("document").ready(function() {
    $("#DatePicker").datepicker();
});


// $( function() {
//     $( "#TimePicker" ).timepicker();
//   } );

$("document").ready(function() {
    $('.dropdown-menu li').on('click', function() {
    $('#dropdownTitle').html($(this).find('a').html());
    document.getElementById("measurable").value=$(this).attr("class");
    $("#id_valueText").attr("min",$(this).attr("min"));
    $("#id_valueText").attr("max",$(this).attr("max"));
    console.log($(this).attr("max"));
    console.log($(this).attr("min"));

    if($(this).attr("max")=="None" && $(this).attr("min")=="None")
        $("#id_valueText").attr('disabled','disabled')
    else
        $("#id_valueText").removeAttr('disabled');

    // console.log($("#measurable").attr("max"));
    });
});

$("document").ready(function() {
    $('.dropdown-menu li').on('click', function() {
    $('#dropdownTitle').html($(this).find('a').html());
    document.getElementById("measurable").value=$(this).attr("class");
    $("#id_valueText").attr("min",$(this).attr("min"));
    $("#id_valueText").attr("max",$(this).attr("max"));
    console.log($(this).attr("max"));
    console.log($(this).attr("min"));

    if($(this).attr("max")=="None" && $(this).attr("min")=="None")
        $("#id_valueText").attr('disabled','disabled')
    else
        $("#id_valueText").removeAttr('disabled');

    // console.log($("#measurable").attr("max"));
    });
});

$("document").ready(function() {
    function Validate() {
        if ($('#measurable').attr("class") == -1) {
            alert("Please select a valid measurable");
            return false;
        }
        console.log("Success")
        return true;
    }
});

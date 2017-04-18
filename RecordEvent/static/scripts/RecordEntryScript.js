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
    console.log($(this));
    $("#id_valueText").attr("min",$(this).attr("min"));
    $("#id_valueText").attr("max",$(this).attr("max"));
    console.log($(this).attr("max"));
    console.log($(this).attr("min"));



try{
     if (document.getElementById("measurable").value != -1 && $('#id_valueText').val().length>0) {
           //console.log("Enter the value of asindapinsd");
           $("#submitDisabled").removeAttr('disabled');
           $("#submitDisabled").attr('class','pull-right');
     }else{
           $("#submitDisabled").attr('disabled','disabled');
           $("#submitDisabled").attr('class','pull-right disabled')

     }
}catch(ex) {

}


     if($(this).attr("max")=="None" && $(this).attr("min")=="None"){
        $("#id_valueText").attr('disabled','disabled');
        $("#submitDisabled").removeAttr('disabled');
        $("#submitDisabled").attr('class','pull-right');
        console.log(document.getElementById("id_valueText").value)
    } else{
        $("#id_valueText").removeAttr('disabled');
        document.getElementById("id_valueText").value="";
    }
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


$("document").ready(function () {
$('#id_valueText').on('input', function() {
     if (document.getElementById("measurable").value != -1 && $('#id_valueText').val().length>0) {
           //console.log("Enter the value of asindapinsd");
           $("#submitDisabled").removeAttr('disabled');
           $("#submitDisabled").attr('class','pull-right');
     }else{
           $("#submitDisabled").attr('disabled','disabled');
           $("#submitDisabled").attr('class','pull-right disabled')

     }
       // console.log( document.getElementById("measurable").value);
});
});



// ("document").ready(function() {
//     $('.dropdown-menu li').on('click', function () {
//         console.log("hey")
//     });
// });
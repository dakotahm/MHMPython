/**
 * Created by Dakotah on 4/17/2017.
 */
$("document").ready(function () {
        $('.typeSelect li').on('click',function () {
            document.getElementById("measurable").value=$(this).attr("type");
            $('#dropdownTitle').text($(this).attr("type"));
        });
    });



$("document").ready(function () {
$('#id_valueText').on('input', function() {
    console.log("triggered");
     if (document.getElementById("measurable").value != -1 && $('#id_valueText').val().length>0) {
           //console.log("Enter the value of asindapinsd");
           $("#submitDisabled").removeAttr('disabled');
           $("#submitDisabled").attr('class','pull-right');
     }else{
           $("#submitDisabled").attr('disabled','disabled');
           $("#submitDisabled").attr('class','pull-right disabled')

     }
});
});



$("document").ready(function () {

$('#id_NameText').on('input', function() {
    console.log("hey");
    if (document.getElementById("measurable").value != -1 && $('#id_NameText').val().length>0 &&$("#id_min").val()<$("#id_max").val()) {
           $("#submitDisabled").removeAttr('disabled');
           $("#submitDisabled").attr('class','pull-right');
     }else{
           $("#submitDisabled").attr('disabled','disabled');
           $("#submitDisabled").attr('class','pull-right disabled')

     }
});

$('#id_max').on('input', function() {
    console.log("hey");
    if (document.getElementById("measurable").value != -1 && $('#id_NameText').val().length>0 &&$("#id_min").val()<$("#id_max").val()) {
           $("#submitDisabled").removeAttr('disabled');
           $("#submitDisabled").attr('class','pull-right');
     }else{
           $("#submitDisabled").attr('disabled','disabled');
           $("#submitDisabled").attr('class','pull-right disabled')

     }
});

$('#id_min').on('input', function() {
    console.log("hey");
    if (document.getElementById("measurable").value != -1 && $('#id_NameText').val().length>0 &&$("#id_min").val()<$("#id_max").val()) {
           $("#submitDisabled").removeAttr('disabled');
           $("#submitDisabled").attr('class','pull-right');
     }else{
           $("#submitDisabled").attr('disabled','disabled');
           $("#submitDisabled").attr('class','pull-right disabled')

     }
});
});
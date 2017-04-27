$("document").ready(function() {
    $('.dropdown-menu li').on('click',function () {
        console.log($(this).parent());
        if($(this).parent().attr("id")=="measurable-dropdown"){
            console.log($(this).parent());
        }else if($(this).parent().attr("id")=="time-dropdown"){

        }
    });
});

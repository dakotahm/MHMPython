/**
 * Created by Dakotah on 4/18/2017.
 */
$("document").ready(function() {
    $(".download").click(function() {
        var theUrl=$(this).attr("url");
        $.ajax({
            // type:'POST',
            url: '/aids/',
            data:{
               'url':theUrl
            },
            datatype:'json',
            success:function (data) {
                console.log("success");
            }
        });
    });
});
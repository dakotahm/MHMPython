/**
 * Created by Dakotah on 4/27/2017.
 */
$("document").ready(function () {
     var input =$('#measurable-dropdown li:first').children().first().text();
    var id=$('#measurable-dropdown li:first').attr('class');
    $('#MeasurableDropdownTitle').text(input);
    $('#MeasurableDropdownTitle').attr('class',id);

var endpoint = 'api/data/';
//var endpoint = 'display/dropdown/display/api/chart/data/'
var defaultData = [];
var defaultLabels = [];
$.ajax({
	method: "GET",
    data:{
	    message:"Data goes here",
        'measurableId': $('#MeasurableDropdownTitle').attr('class'),
        'timeframe':$('#TimeDropdownTitle').text()
    },
	url: endpoint,
	success: function(data){
		defaultLabels = data.labels;
		defaultData = data.default;
		defaultName = data.name;
		console.log(data);
		var ctx = document.getElementById("myChart");
		var myChart = new Chart(ctx, {
		    type: 'line',
		    data: {
		        labels: defaultLabels,
		        datasets: [{
		            label: defaultName,
		            data: defaultData,
		            borderWidth: 1
		        }]
		    },
		    options: {
		        scales: {
		            yAxes: [{
		                ticks: {
		                    beginAtZero:true
		                }
		            }]
		        }
		    }
		});
	},
	error: function(error_data){
		console.log("error");
		console.log(error_data)
	}
});

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

        var endpoint = 'api/data/';
        //var endpoint = 'display/dropdown/display/api/chart/data/'
        var defaultData = [];
        var defaultLabels = [];
        $.ajax({
            method: "GET",
            data:{
                message:"Data goes here",
                'measurableId': $('#MeasurableDropdownTitle').attr('class'),
                'timeframe':$('#TimeDropdownTitle').text()
            },
            url: endpoint,
            success: function(data){
                defaultLabels = data.labels;
                defaultData = data.default;
                defaultName = data.name;
                console.log(data);
                var ctx = document.getElementById("myChart");
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: defaultLabels,
                        datasets: [{
                            label: defaultName,
                            data: defaultData,
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            yAxes: [{
                                ticks: {
                                    beginAtZero:true
                                }
                            }]
                        }
                    }
                });
            },
            error: function(error_data){
                console.log("error");
                console.log(error_data)
            }
        });
    });
});
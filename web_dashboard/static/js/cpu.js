var chart;

function requestData()
{
    // Ajax call to get the Data from Flask
    var requests = $.get('/cpu');


    var tm = requests.done(function (result)
    {
        var series = chart.series[0],
            shift = series.data.length > 20;

        // add the point
        chart.series[0].addPoint(result, true, shift);

        // call it again after one second
        setTimeout(requestData, 1000);
    });
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'CPU Usage'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Clock Speed (GHz)',
                margin: 30
            }
        },
        series: [{
            name: 'Time (s)',
            data: []
        }]
    });

});

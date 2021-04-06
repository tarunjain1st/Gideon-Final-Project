var data = $.get('/sensorsData');
data.done(function (resp){
    Morris.Area({
        element: 'dht11-chart',
        data: resp,
        xkey: 'period',
        ykeys: ['Temperature', 'Humidity'],
        labels: ['Temperature', 'Humidity'],
        pointSize: 0,
        fillOpacity: 0,
        pointStrokeColors: ['#20aee3', '#24d2b5', '#6772e5'],
        behaveLikeLine: true,
        gridLineColor: '#e0e0e0',
        lineWidth: 3,
        hideHover: 'auto',
        lineColors: ['#20aee3', '#24d2b5', '#6772e5'],
        resize: true

        });
})

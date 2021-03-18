$(function() {
    "use strict";
    // ============================================================== 
    // Our Visitor
    // ============================================================== 
    // ============================================================== 
    // Sales chart
    // ============================================================== 
    Morris.Area({
        element: 'sales-chart',
        data: [{
                period: '2011',
                Sales: 50,
                Earning: 80,
                Marketing: 20
            }, {
                period: '2012',
                Sales: 130,
                Earning: 100,
                Marketing: 80
            }, {
                period: '2013',
                Sales: 80,
                Earning: 60,
                Marketing: 70
            }, {
                period: '2014',
                Sales: 70,
                Earning: 200,
                Marketing: 140
            }, {
                period: '2015',
                Sales: 180,
                Earning: 150,
                Marketing: 140
            }, {
                period: '2016',
                Sales: 105,
                Earning: 100,
                Marketing: 80
            },
            {
                period: '2017',
                Sales: 250,
                Earning: 150,
                Marketing: 200
            }
        ],
        xkey: 'period',
        ykeys: ['Sales', 'Earning', 'Marketing'],
        labels: ['Temperature', 'Humidity', 'Pressure'],
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


});
var methane = new JustGage({
    id: "methane-gauge",
    value: 0,
    min: 0,
    max: 100,
    gaugeWidthScale: 0.7,
	  symbol: ' PPM',
    pointer: true,
    pointerOptions: {
          toplength: -15,
          bottomlength: 10,
          bottomwidth: 12,
          color: '#8e8e93',
          stroke: '#ffffff',
          stroke_width: 3,
          stroke_linecap: 'round'
        },
    customSectors: [{
        color : "#9FE2BF",
        lo : 0,
        hi : 100
      },{
        color : "#40E0D0",
        lo : 100,
        hi : 200
      },{
        color : "#6495ED",
        lo : 200,
        hi : 300
      },{
        color : "#CCCCFF",
        lo : 300,
        hi : 400
      },{
        color : "#DFFF00",
        lo : 400,
        hi : 500
      },{
        color : "#FFBF00",
        lo : 500,
        hi : 600
      },{
        color : "#FF7F50",
        lo : 600,
        hi : 700
      },{
        color : "#DE3163",
        lo : 700,
        hi : 800
      },{
        color : "#DC7633",
        lo : 800,
        hi : 900
      },{
        color : "#C0392B",
        lo : 900,
        hi : 1000
      }],
    title: "Methane"
  });

  setInterval(function() {
      var data = $.get('/sensorsData');
      data.done(function (resp){
      methane.refresh(resp.methane);
      })
  }, 1000);

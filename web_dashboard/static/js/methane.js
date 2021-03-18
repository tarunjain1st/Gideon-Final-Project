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
        hi : 10
      },{
        color : "#40E0D0",
        lo : 10,
        hi : 20
      },{
        color : "#6495ED",
        lo : 20,
        hi : 30
      },{
        color : "#CCCCFF",
        lo : 30,
        hi : 40
      },{
        color : "#DFFF00",
        lo : 40,
        hi : 50
      },{
        color : "#FFBF00",
        lo : 50,
        hi : 60
      },{
        color : "#FF7F50",
        lo : 60,
        hi : 70
      },{
        color : "#DE3163",
        lo : 70,
        hi : 80
      },{
        color : "#DC7633",
        lo : 80,
        hi : 90
      },{
        color : "#C0392B",
        lo : 90,
        hi : 100
      }],
    title: "Methane"
  });

  setInterval(function() {
      var data = $.get('/sensorsData');
      data.done(function (resp){
        console.log(resp);
      methane.refresh(resp.methane);
      })
  }, 1000);
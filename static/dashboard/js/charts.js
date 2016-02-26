var randomScalingFactor = function() {
    return Math.round(Math.random() * 100);
};
var lineChartData = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [{
        label: "My First dataset",
        fillColor: "rgba(220,220,220,0.2)",
        strokeColor: "rgba(220,220,220,1)",
        pointColor: "rgba(220,220,220,1)",
        pointStrokeColor: "#fff",
        pointHighlightFill: "#fff",
        pointHighlightStroke: "rgba(220,220,220,1)",
        data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
    }]
};
window.onload = function() {
  $(".network-container").click(function(){
    if( !$(this).hasClass("active") ) {
      
    } else {
      myLine.destroy()
    } 
  });
};

function drawChart(chartName) {
  setTimeout(
    function() {
      var chartName = document.getElementById(chartName).getContext("2d");
      window.myLine = new Chart(chartName).Line(lineChartData, {
        showScale: false,
        pointDot : false,
        responsive: true
      });;
    },
  350);

  return();
};
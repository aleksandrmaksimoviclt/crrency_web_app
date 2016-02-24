google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Month', 'Progress'],
    ['Nov',  -100],
    ['Dec',  0],
    ['Jan',  20],
    ['Feb',  50],
    ['Mar',  150]
  ]);

  var options = {
    //hAxis: {title: 'Year',  titleTextStyle: {color: '#333'}},
    //vAxis: {minValue: 0}
  };

  var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
  chart.draw(data);
}
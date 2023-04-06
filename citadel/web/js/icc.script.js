
function drawData() {
  var xValues = [100,200,300,400,500,600,700,800,900,1000];

  new Chart("Chart-1", {
    type: "line",
    data: {
      labels: xValues,
      datasets: [{
        data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478],
        borderColor: "#1789C9",
        fill: false
      },{
        data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
        borderColor: "#aqua",
        fill: false
      },{
        data: [300,700,2000,5000,6000,4000,2000,1000,200,100],
        borderColor: "#81C4E9",
        fill: false
      }]
    },
    options: {
      legend: {display: false}
    }
  });
}

var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
var yValues = [55, 49, 44, 24, 15];

function makeChart() {
  var xValues = [50,60,70,80,90,100,110,120,130,140,150];
  var yValues = [7,8,8,9,9,9,10,11,14,14,15];
  
  new Chart("Chart-2", {
    type: "line",
    data: {
      labels: xValues,
      datasets: [{
        backgroundColor: "rgba(152, 194, 219, 0.7)",
        borderColor: "rgba(23, 137, 201, 0.7)",
        data: yValues
      }]
    },
    options:{}
  });
}

var barColors = [
  "rgba(23, 137, 201, 0.99)",
  "rgba(23, 137, 201, 0.7)",
  "rgba(23, 137, 201, 0.5)",
  "rgba(23, 137, 201, 0.3)",
  "rgba(23, 137, 201, 0.2)"
];

function makeDonut() {
  new Chart("Chart-3", {
      type: "pie",
      data: {
        labels: xValues,
        datasets: [{
          backgroundColor: barColors,
          data: yValues
        }]
      },
      options: {
        title: {
          display: true,
          text: "World Wide Wine Production"
        }
      }
    });
}
drawData()
makeChart();
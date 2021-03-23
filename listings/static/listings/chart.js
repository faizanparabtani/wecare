$(function () {

    var $populationChart = $("#line-chart");
    $.ajax({
      url: $populationChart.data("url"),
      success: function (data) {
    
        var ctx = $populationChart[0].getContext("2d");
    
        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: "{{response1.data.labels}}",
            datasets: [{
              label: 'Steps',
              backgroundColor: 'blue',
              data: "{{response1.data.data}}"
            }]          
          },
          options: {
            responsive: true,
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Steps'
            }
          }
        });
    
      }
    });
    
    });


    // var config = {
//       type: 'bar',
//       data: {
//         datasets: [{
//           data: "{{ data|safe }}",
//           backgroundColor: [
//             '#696969', '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3'
//           ],
//           xAxisID: "Date",
//           yAxisID: "Steps",
//           label: 'Population'
//         }],
//         labels: "{{ labels|safe }}"
//       },
//       options: {
//         responsive: true
//       }
//     };

//     window.onload = function() {
//       var ctx = document.getElementById('line-chart').getContext('2d');
//       window.myPie = new Chart(ctx, config);
//     };
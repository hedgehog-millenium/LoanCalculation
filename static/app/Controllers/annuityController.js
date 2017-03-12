var annuityController = function($scope,$http,$filter,apiService){
	  $scope.loan = {
	        amount:30000,
	        rate:12,
	        duration:10,
	        addpay:0
	  }
	   $scope.colors = ['#5cb85c', '#d9534f', '#717984', '#F1C40F'];

	calculateLoan()
    $scope.calculateLoan = calculateLoan;

    function calculateLoan(){
            var path = 'https://jsonplaceholder.typicode.com/posts'
            var data = $scope.loan;
            apiService.apiPost(path,data,function(data){
                    $scope.principal = [] ;
                    $scope.interest = [] ;
                    $scope.PMT = [] ;
                    $scope.ADD_PAY = [];
                    $scope.index = [];
                    for(var i=0;i<data.length;i++){
                        $scope.index.push(i+ 1+ ' Year')
                          $scope.principal.push(data[i].Principal+data[i].Add_Pay)
                          $scope.interest.push(data[i].Interest)
                          $scope.PMT.push(data[i].PMT)
                          $scope.ADD_PAY.push(data[i].Add_Pay)
                    }

                    updateChartData()
            });
        }

    function updateChartData(){
         $scope.labels = $scope.index
         $scope.series = ['Principal', 'Interest (%)'];
         $scope.data = [
                         $scope.principal,
                         $scope.interest
                   ];

          var principal_paid = $scope.principal.sum()+ $scope.ADD_PAY.sum(),
              interest_paid =  $scope.interest.sum(),
              total_paid = principal_paid + interest_paid ;

          $scope.principal_paid =  principal_paid.toFixed(2);
          $scope.interest_paid =  interest_paid.toFixed(2);
          $scope.total_paid = total_paid.toFixed(2) ;

          $scope.labelsDoughnut = ["Principal Paid", "Interest Paid (%)"];
          $scope.dataDoughnut = [ $scope.principal_paid ,$scope.interest_paid];
    }

    // ----------------


  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };

  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }, { yAxisID: 'y-axis-2' }];
  $scope.options = {
    scales: {
      yAxes: [
        {
          id: 'y-axis-1',
          type: 'linear',
          display: true,
          position: 'left'
        },
        {
          id: 'y-axis-2',
          type: 'linear',
          display: true,
          position: 'right'
        }
      ]
    }
  }
  //   --------------------

}

Object.defineProperty(Object.prototype, 'sum',{
  value : function() {return Array.from(this).reduce(function(a,b){return a+b;},0)},
  enumerable : false
});

$('.nav-tabs a').click(function (e) {
  alert('click event')
  e.preventDefault()
  $(this).tab('show')

})

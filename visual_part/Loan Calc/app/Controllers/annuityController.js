var annuityController = function($scope,$filter){
	  $scope.greating = "Hello from annuityController"

    // Real data    --------------------
    $scope.index = ['2017-12-31', '2018-12-31', '2019-12-31', '2020-12-31','2021-12-31', '2022-12-31', '2023-12-31', 
                    '2024-12-31','2025-12-31', '2026-12-31', '2027-12-31'];
    
    //var today = $filter('date')(new Date('2017-12-31'),'yyyy-MMM-dd');  
     $scope.index.forEach(function(part, index) {
        $scope.index[index] = $filter('date')(new Date(part),'yyyy');
     });    
 
    $scope.interst = [1953.91, 2202.99, 2036.31, 1855.80, 1660.31, 1448.58, 1219.29, 970.96, 702.03, 410.77, 102.47] ;
    $scope.principal=[555.41, 808.19, 974.87, 1155.38, 1350.88, 1562.60, 1791.89, 2040.22, 2309.16, 2600.42, 2155.92]; 

     var principal_paid = $scope.interst.sum(),
         intrest_paid =  $scope.principal.sum(),
         total_paid = principal_paid + intrest_paid ;

     $scope.principal_paid =  principal_paid.toFixed(2);
     $scope.intrest_paid =  intrest_paid.toFixed(2);
     $scope.total_paid = total_paid.toFixed(2) ;

    // ------------------- Real data    

    $scope.labels = $scope.index
    $scope.series = ['Principal', 'Intrest'];

    $scope.data = [
        $scope.principal,
        $scope.interst
    ];

    $scope.calculateLoan = function(){
      alert('calculation is in process')
    }

    // ----------------
    $scope.labelsDoughnut = ["Total Paid", "", "Intrest Paid"];
    $scope.dataDoughnut = [$scope.total_paid, $scope.principal_paid ,$scope.intrest_paid];
    //   --------------------

    //   --------------------

  $scope.labelsLC = $scope.index;
  $scope.seriesLC = ['Principal', 'Intrest'];
  $scope.dataLC = [
    $scope.principal,
    $scope.interst
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  $scope.datasetOverrideLC = [{ yAxisID: 'y-axis-1' }, { yAxisID: 'y-axis-2' }];
  $scope.optionsLC = {
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

Object.prototype.sum = function(){
		return Array.from(this).reduce(function(a,b){return a+b;},0)
}
var annuityController = function($scope,$http,$filter,apiService){
	  var frequencies = [
	    {display:'Monthly',value:1},
	    {display:'Quarterly',value:3},
	    {display:'Annual',value:12}
      ]

      $scope.frequencies = frequencies 
      $scope.schedualFreq = frequencies[2]
	  $scope.loan = {
	        amount:38000,
	        rate:11,
	        duration:20,
	        addpay:0,
	        add_pay_frequency:frequencies[0]
	  }

	  $scope.house = {
	        square:78,
	        ps_price:610,
            upfront_part:9516,
            total_price:47580,
            upfront_payment_rate:20,
            loan_part:38064
	   }
	   $curr_symb = '$'
	   $scope.colors = ['#1ABB9C ', '#ad423f ', '#717984', '#F1C40F'];

	calculateLoan()
    $scope.calculateLoan = calculateLoan;

    $scope.calcHouse = function(){
        $scope.house.total_price = $scope.house.ps_price*$scope.house.square
        calcHouseLoanParts()
    }
    $scope.calcHouseTotal = function(){
        $scope.house.ps_price = $scope.house.total_price/$scope.house.square
        calcHouseLoanParts()
    }
    $scope.amountToLoan = function(){
        if($scope.house.loan_part>0)
        $scope.loan.amount = $scope.house.loan_part
        calculateLoan();
    }

    $scope.change_frequency = function(idx){
        $scope.loan.add_pay_frequency = frequencies[idx]
    }

    $scope.changeScheduleFreq = function(freq){
        $scope.schedualFreq = freq
        
        var path = 'http://127.0.0.1:5000/annuity_calc/'+freq.value
        var data =Object.assign({}, $scope.loan);
        data.add_pay_frequency = $scope.loan.add_pay_frequency.value
        apiService.apiPost(path,data,function(data){
                var loan = getLoanDataFromResponse(data)
                console.log(loan)
                updatePaymentSchedual(loan)
        });

        // alert('Sorry the functionality does not implemented yet! Selected frequency:'+freq.display)
    }

    function calcHouseLoanParts(){
        $scope.house.upfront_part=$scope.house.total_price*$scope.house.upfront_payment_rate/100
        $scope.house.loan_part=$scope.house.total_price-$scope.house.upfront_part
    }

    function calculateLoan(){
            var path = 'http://127.0.0.1:5000/annuity_calc/12'
            var data =Object.assign({}, $scope.loan);
            data.add_pay_frequency = $scope.loan.add_pay_frequency.value
            apiService.apiPost(path,data,function(data){
                    var loan = getLoanDataFromResponse(data)
                    console.log(loan)
                    $scope.PMT_MONTHLY = loan.PMT[0]  / 12
                    updateChartData(loan)
            });
        }

    function updateChartData(loan){
        updateChartLine(loan)
        updatePaymentSchedual(loan)
        updateChartDoughnut(loan)
    }

    function updateChartLine(loan){
        $scope.labels = loan.index
        $scope.series = ['Principal', 'Interest (%)'];
        $scope.data = [loan.principal, loan.interest];
    }
    
    function updatePaymentSchedual(loan){
        $scope.PMT = loan.PMT
        $scope.Interest =  loan.interest
        $scope.Principal = loan.principal
        $scope.Additional = loan.ADD_PAY
        $scope.PrincipalLeft = loan.principal_Left
    }

    function updateChartDoughnut(loan){
        $scope.principal_paid =  loan.principal.sum() //+ loan.ADD_PAY.sum()
        $scope.interest_paid =  loan.interest.sum()
        $scope.total_paid = ($scope.principal_paid+$scope.interest_paid).toFixed(2) ;

        $scope.dataDoughnut = [ $scope.principal_paid.toFixed(2) ,$scope.interest_paid.toFixed(2)];
    }

    
    
    // ----------------


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

function getLoanDataFromResponse(response){
    var loan = {
        index:[],
        principal:[],
        interest:[],
        PMT:[],
        ADD_PAY:[],
        principal_Left:[]
    }
    for(var i=0;i<response.length;i++){
          loan.index.push(i+ 1+ ' Year')
          loan.principal.push(response[i].Principal+response[i].Add_Pay)
          loan.interest.push(response[i].Interest)
          loan.PMT.push(response[i].PMT)
          loan.ADD_PAY.push(response[i].Add_Pay)
          loan.principal_Left.push(response[i].Principal_Left)
    }
    return loan
}



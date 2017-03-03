var app = angular.module('loanApp', ['ngRoute','ui.bootstrap','chart.js'])

app.controller('homeController', ['$scope', homeController])
app.controller('annuityController', ['$scope','$filter', annuityController])

app.config(['$routeProvider',function($routeProvider) {
	$routeProvider.when('/home',{
			templateUrl:'app/Views/home.html',
			controller:'homeController'
	}).
	when('/annuity',{
			templateUrl:'app/Views/annuity.html',
			controller:'annuityController'
	})

}])



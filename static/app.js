var app = angular.module('loanApp', ['ngRoute','ui.bootstrap','chart.js'])

app.service('apiService',['$http',apiService])

app.controller('homeController', ['$scope', homeController])
app.controller('annuityController', ['$scope','$http','$filter','apiService', annuityController])


app.config(['$routeProvider',function($routeProvider) {
	$routeProvider.when('/home',{
			templateUrl:'static/app/Views/home.html',
			controller:'homeController'
	}).
	when('/annuity',{
			templateUrl:'static/app/Views/annuity.html',
			controller:'annuityController'
	});
}])



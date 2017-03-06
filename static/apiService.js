var apiService = function($http){
    var result;
    this.apiGet = function(path,callback){
        result = $http.get(path).success(function(data,status){
            callback(data);
        }).error(function(error){
            callback(error);
        });
    };

    this.apiPost = function(path,data,callback){
        path='http://127.0.0.1:5000/annuity_calc'
         result = $http.post(path,data).success(function(response,status){
                    callback(response);
                }).error(function(error){
                    callback(error);
                });
    };

    return result;
}
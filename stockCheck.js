var net = require('net');
var http = require('http');


function getVal(callback)
{
	return http.get({
		host : http://finance.google.com/finance/info?client=ig&q=NASDAQ:GOOG,
		path : "\\"
	}, function(responce){
		responce.on('data', function(d))
		{
			
		}
	});

}

var server = net.createServer(function(socket){
	
	socket.on('data', function(data){
		console.log(JSON.parse(data));
	});

});


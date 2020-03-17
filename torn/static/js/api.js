const API = (function(){
	function post(url, data, headers={'Accept': '*'}){
		return fetch(url, {method:'post', headers, body: (body=>{for(let n in data)body.append(n,data[n]);return body;})(new FormData())})
	}
	function postHTML(...args){ return post(...args).then(res=>res.text()); }
	function postJSON(...args){ return post(...args).then(res=>res.json()); }
	return function(name, data, type='json', headers=undefined){
		const func = type==='json'?postJSON:postHTML
		const args = [`/torn/api/${name}`, data];
		if(headers) args.push(headers);
		return func(...args);
	}
})();


function getTweets(){
	name = $('#name').val();
	count = $('#count').val();
	$.get(
		"/tweets/",
		{'name': name, 'count': count},
		function(data, status){
			var temp ="";
			var data = JSON.parse(data);
			var tweets = data.tweets;
			for(var i in tweets){
				var temp = temp + "<li>" + tweets[i] + "</li>" ;
			}
			var html_content = "<ul>" + temp + "</ul>";
			$('#tweets').html(html_content);
			console.log(html_content)
		}
	)
}

function getrepo(){
	var git_id = $('#git_id').val();
	
	$.get(
		"/repos/",
		{'git_id': git_id},
		function(data, status){
			var temp ="";
			var data = JSON.parse(data);
			var repos = data.repos;
			for(var i in repos){
				var temp = temp + "<li>" + repos[i] + "</li>" ;
			}
			var html_content = "<ul>" + temp + "</ul>";
			$('#repos').html(html_content);
			console.log(html_content)
		}
	)
}

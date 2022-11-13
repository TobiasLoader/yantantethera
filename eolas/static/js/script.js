var searchbaropen = false;
var logintextentered = false;
var contributornameentered = false;
var contributornames = [];

function sendsearch(){
	const searchval = $('#search-input').val();
	console.log(searchval);
	if (searchval!='' && searchval!=undefined){
		window.open(window.location.origin + '/search?term='+searchval,"_self");
	}
}

$('#topright #search-icon').click(function(){
	if (searchbaropen){
		sendsearch();
	}
	$('#topright #topbar-search').addClass('search-active');
	searchbaropen = true;
});

$('#search-input').keydown(function (e) {
	if (e.keyCode == 13) {
		sendsearch();
	}
});

$("#topright #profile-name").click(function(){
	window.open(window.location.origin + "/profile?handle="+username,"_self");
});

$("#topright #profile-pic").click(function(){
	window.open(window.location.origin + "/profile?handle="+username,"_self");
});


$('#login-wallet-input').keydown(function (e) {
	if (!logintextentered){
		$('#loginactionbutton').addClass('btn-allowed');
	}
	logintextentered = true;
});

$('#loginactionbutton').click(function () {
	if (logintextentered){
		const data = JSON.stringify({'handle':$('#login-handle-input').val(),'private-address':$('#login-wallet-input').val()});
		$.ajax({
			type : 'POST',
			url : "/logindata",
			contentType: 'application/json;charset=UTF-8',
			data : data
		}).then((res)=>{
			console.log(res);
			window.open(window.location.origin,"_self");
		});
	}
});

$('#topbar h1').click(function(){
	window.open(window.location.origin);
});

$('#add-publication').click(function(){
	window.open(window.location.origin + "/uploadpage","_self");
});

$('#add-contributor-input').keydown(function(){
	if (!contributornameentered){
		$('#addcontributorbtn').addClass('btn-allowed');
	}
	contributornameentered = true;
});
$('#addcontributorbtn').click(function(){
	if (contributornameentered){
		$('#addcontributorbtn').removeClass('btn-allowed');
		contributornameentered = false;
		contributornames.push($('#add-contributor-input').val());
		$('#add-contributor-input').val('');
		$('#currentcontributors').text(contributornames.toString());
	}
});
$('#uploadpaperbtn').click(function(){
	const papertitle = $('#paper-title').val();
	const paperdesc = $('#paper-desc').val();
	const paperdata = $('#papercontent-textarea').val();
	const paperobj = JSON.stringify({'title':papertitle,'desc':paperdesc,'contributornames': contributornames,'data':paperdata});
	$.ajax({
		type : 'POST',
		url : "/upload",
		contentType: 'application/json;charset=UTF-8',
		data : paperobj
	}).then((res)=>{
		console.log(res);
		window.open(window.location.origin,"_self");
	});
});
var searchbaropen = false;
var logintextentered = false;

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

$('#login-wallet-input').keydown(function (e) {
	if (!logintextentered){
		$('#loginactionbutton').addClass('login-allowed');
	}
	logintextentered = true;
});

$('#loginactionbutton').click(function () {
	if (logintextentered){
		window.open(window.location.origin,"_self");
	}
});
function create(){
	window.location.href = '../views/createSession.html'
}

function join(){
	window.location.href = '../views/joinSession.html'
}

function goToMovies(){
	window.location.href = '../views/moviesGrid.html'
}

function like(){

}


function getMovies(){
	$.ajax({url:'http://127.0.0.1:8080/api/mts'});
}

function sendPref(){
	$.ajax({
  	type: "POST",
  	url: 'http://127.0.0.1:9995/api',
  	data: '0*Dead Man Walking (1995)-1*Bad Boys (1995)-3*Babe (1995)-1'
});
}


$(function(){

	$('.icon').click(function(){
		$(this).css({ opacity: 1 });
		$(this).parent().css({ opacity: 1 });
		$(this).addClass('clicked');
	});

	$('.movie').click(function(){
		$(this).css({ opacity: 1 });
		$(this).addClass('showw');
	});

		$('.movie').hover(
       function(){ $(this).addClass('show') },
       function(){ $(this).removeClass('show') }
);

	var availableTags = [
	    "Spectre",
	    "The Hunger Games: Mockingjay - Part 2",
	    "Star Wars: The Force Awakens",
	    "The 33",
	    "The Man from U.N.C.L.E.",
	    "Creed",
	    "Inside Out"
	];

	if($('.moviesAutocomplete')){
		$('.moviesAutocomplete').autocomplete({
			source: availableTags,
			multiselect: true
		});
	}


})

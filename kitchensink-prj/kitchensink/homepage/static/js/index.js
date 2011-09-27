$(document).ready(function(){
	$("#location-input").focus(function(e) {
		$(this).val("").css("color","#555").unbind("focus");
	});
	$("#date-input").focus(function(e) {
		$(this).val("").css("color","#555").unbind("focus");
	}).keyup(function(e) {
		if ($(this).val().length > 10) {
			$(this).val($(this).val().substring(0,10));
		};
	});
	$("#date").datepicker({onSelect:function(dateText,inst){
		$("#date-input").val(dateText).css("color","#555");
		$(this).fadeOut();
	}}).hide();
	$("#calendar-button").click(function(e) {
		$("#date").fadeToggle();
		return false;
	});
	$("#search-button").click(function(e){window.location = "search.html?l="+encodeURIComponent($("#location-input").val())+"&d="+encodeURIComponent($("#date-input").val())});
	$("#featured").mouseenter(function(e){$("#detail").animate({bottom:"0px"})}).mouseleave(function(e){$("#detail").animate({bottom:"-67px"})});
});
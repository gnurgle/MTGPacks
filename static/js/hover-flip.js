var clicked = 0;
var flipped = 0;
var $items = $('.card_click');

$('.card_click').click(function(){
  $(this).toggleClass('flipped');
  clicked = clicked + 1;
  if (clicked + flipped == 15)
    alert ("Can call New Pack");
		
	});

$('.card').one("mouseenter",function(){
  $(this).toggleClass('flipped');
  flipped = flipped + 1;
  if (clicked + flipped == 15)
    alert ("Can call New Pack");

	});


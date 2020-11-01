var clicked = 0;
var $items = $('.card_click');

$('.card_click').click(function(){
  $(this).toggleClass('flipped');
  clicked = clicked + 1;
  if ($items.length == clicked)
    alert ("Can call New Pack");
		
	});

$('.card').one("mouseenter",function(){
  $(this).toggleClass('flipped');
	});


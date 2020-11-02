var clicked = 0;
var flipped = 0;
var $items = $('.card_click');

$('.card_click').one('click',function(){
  $(this).toggleClass('flipped');
  clicked = clicked + 1;
});

$('.card').one("mouseenter",function(){
    $(this).toggleClass('flipped');
  flipped = flipped + 1;
});

function reload() {
  	if (clicked + flipped >= 15)
		loadlink();
};

function flip(){
  $(this).toggleClass('flipped');
};
function loadlink(){

    $('#outbox').load('/pullPack' + " #outbox > *");
	clicked = 0;
	flipped = 0
	$(document).on("mouseenter", ".card", function(){
			var $this=$(this);
			if ($this.data('mouseentered')){
			return false;
			}
			$this.data('mouseentered',true); 
			$(this).toggleClass('flipped'); 
			clicked = clicked + 1; 
		  });
	$(document).on('click', '.card_click', function(){
			var $this=$(this);
			if ($this.data('mouseentered')){
			return false;
			}
			$this.data('mouseentered',true);
  		$(this).toggleClass('flipped');
  		clicked = clicked + 1;
		});


}

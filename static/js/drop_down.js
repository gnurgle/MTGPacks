let sets_select = document.getElementById('sets');
let cards_select = document.getElementById('cards');

sets_select.onchange = function() {
	sets_value = sets_select.value;

	fetch('/admin/set/' + sets_value).then(function(response) {
		response.json().then(function(data) {

			let optionHTML = '';
			
			for(let card of data.cards) {
				optionHTML += '<option value="' + card[0] + '">' + card[1] + '</option>';

			}

			cards_select.innerHTML = optionHTML;
		})
	});
	
}

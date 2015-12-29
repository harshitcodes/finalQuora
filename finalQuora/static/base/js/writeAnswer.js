var writeAnswer = (function () {
	'use strict'
	function write(e){
		e.preventDefault();
		var form = this.parentElement;
		var form_data = new FormData(form);
		var url = $(form).attr('action');
		console.log(url);
		$.ajax({
			url: url,
			type: 'POST',
			data: form_data,
			processData: false,
			dataType: 'json',
			contentType: false,
			success: function(data, status, xhr) {
				console.log(data);
				var el = $(form.parentElement).find('.recent_answer');
				el.attr('data-answer-id', data['answer']['id']);
				el.html(data['answer']['text']);
				form.reset();
			},
			error: function() {
				alert('Something went Wrong');	
			}
		});
	}
	function init() {
		$('.addanswer-btn').click(writeanswer);	
	}
	return {
		init: init
	};

})();
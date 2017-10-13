function check_empty_value(element) {
	if ($(element).val() == ''){
		btn = $("#sub_btn").button('loading');
	}
	else {
		btn.button('reset');
	}
}
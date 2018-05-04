/*!
 * Twitch-Streamchecker
 * http://kbmod.com
 */

(function( $ ){
	$.fn.streamfield = function() {

		this.each(function() {
			$.fn.streamfield.fields[$(this).attr('id')] = {
				querying: false,
				timer: false,
			};

			$(this).wrap('<span class="deleteicon" />').after($('<span/>').click(function() {
				$element = $(this).siblings('input').first();
				$.fn.streamfield.clear($element.attr('id'));
				$element.keyup();
			}));
		});

		this.keyup(function(e){

			field_id = $(this).attr('id');
			if($.fn.streamfield.fields[field_id].timer) clearTimeout($.fn.streamfield.fields[field_id].timer);

			if ($(this).val()) {
				//console.debug($element.val());
				$.fn.streamfield.fields[field_id].timer = setTimeout('jQuery.fn.streamfield.reformat("'+ field_id +'");', 1000);
			} else {
				$.fn.streamfield.set_status(field_id,'');
			}
		});

		this.bind('paste', function() {
			setTimeout(function () {
				$(this).keyup();
			}, 100);
		});


		return this;
	};

	$.fn.streamfield.fields = {};

	$.fn.streamfield.reformat = function(field_id) {
		var $element = $('#' + field_id);
		var val = $element.val()

		if(val != '') {
			val = val.replace(/http[s]?:\/\//i, '');
			val = val.replace(/(www.)?twitch\.tv/, '');
			val = val.replace('/', '');
			val = val.replace(' ', '');

			$element.val(val.toLowerCase());
		}
	};
  /*
	$.fn.streamfield.check = function(field_id) {
		$.fn.streamfield.reformat(field_id);

		//console.debug($.fn.streamfield.fields);

		if ($.fn.streamfield.fields[field_id].querying) return;

		if ($('#' + field_id).attr('data-skip-streamcheck') == 'true') {
			$('#' + field_id).removeAttr('data-skip-streamcheck');
			return;
		}

		var channel_tag = $('#' + field_id).val();

		if (channel_tag) {

			if(typeof(Twitch) !== 'undefined') {

				$.fn.streamfield.fields[field_id].querying = true;
				$.fn.streamfield.set_status(field_id,'loading');

				Twitch.api({
					method: 'streams/' + channel_tag,
				}, function (error, resp_obj) {
					if(error) {
						if(error['status'] == 422 || error['status'] == 404) {
							$.fn.streamfield.set_status(field_id,'doesntexist');
						} else {
							//some other API error, give up
							$.fn.streamfield.set_status(field_id,'');
						}
					} else {
						if(resp_obj['stream']) {
							$.fn.streamfield.set_status(field_id,'existsandstreaming');
						} else {
							$.fn.streamfield.set_status(field_id,'exists');
						}
					}

					$.fn.streamfield.fields[field_id].querying = false;
				});

			}

		}
	};*/

	$.fn.streamfield.clear = function(field_id) {
		$('#'+field_id).val('').parent().siblings('.streamstatusicon').attr('data-status', '');
	};

	$.fn.streamfield.set_status = function(field_id,status) {
		if(typeof(status) === 'undefined') status = '';
		//console.log('setting status:' + field_id + '/' + status);
		$('#'+field_id).parent().siblings('.streamstatusicon').attr('data-status', status);
	};
})( jQuery );

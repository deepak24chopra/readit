from django import forms



class ReviewForm(forms.Form):
	"""
	Form for reviewing a book
	"""

	is_favourite = forms.BooleanField(
			label="Favourite?",
			help_text = 'In top of your 100 books of all time?',
			required = False,
		)

	review = forms.CharField(
			widget=forms.Textarea,
			min_length = 300,
			error_messages={
				'required': 'Please enter your review',
				'min_length': 'Please write atleast 300 characters (you have written %(show_value)s)'
			}
		)
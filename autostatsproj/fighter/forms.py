from django import forms
from fighter.models import Fighter

class FighterForm(forms.ModelForm):
	fighter_url = forms.CharField(
		label="Fightmatrix url",
		required=True,
	)

	class Meta:
		model = Fighter
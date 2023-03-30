from django import forms

EMAIL_CHOICE = [
    ('d.zlotowski@elektromaniacy.pl', 'Dawid Złotowski'),
    ('l.brunacki@elektromaniacy.pl', 'Łukasz Brunacki'),
    ('b.milewski@elektromaniacy.pl', 'Bartłomiej Milewski'),
    ('d.szwarc@elektromaniacy.pl', 'Daniel Szwarc'),
    ('k.dasiewicz@elektromaniacy.pl', 'Konrad Dasiewicz'),
    ('p.kowalski@elektromaniacy.pl', 'Paweł Kowalski'),
    ('m.pawlowski@elektromaniacy.pl', 'Marek Pawłowski'),
    ('j.cempura@elektromaniacy.pl', 'Jędrzej Cempura'),
]

class send_mail(forms.Form):
    email = forms.EmailField(label='Wybierz do kogo wysłać', widget=forms.Select(choices=EMAIL_CHOICE))
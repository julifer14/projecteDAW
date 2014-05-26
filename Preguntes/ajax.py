from dajaxice.utils import deserialize_form
from Preguntes.forms import formulariPuntuacio
from dajax.core import Dajax
from django.contrib import messages


#@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = formulariPuntuacio(deserialize_form(form))

    if form.is_valid():
        form.save()
        messages.success(request,'Dades enviadades correctament')
        dajax.remove_css_class('#my_form input', 'error')
        dajax.alert("Form is_valid(), your username is: %s" % form.cleaned_data.get('username'))
    else:
        dajax.remove_css_class('#my_form input', 'error')
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error, 'error')

    return dajax.json()
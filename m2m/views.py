from django.shortcuts import redirect, render
from m2m.models import Mail
from m2m.forms import MailStartForm, MailForm
from m2m.features import convert_mail_text


def homepage(request):
    form = MailStartForm(request.POST or None)

    if request.method == 'POST' and 'next' in request.POST:
        if form.is_valid():
            recipient = form.cleaned_data['recipient']

            mailform = MailForm(initial={'recipient': recipient})
            return render(request, template_name='mail_template.html',context={'form': mailform})
                
    if request.method == 'POST' and 'send' in request.POST:
        form = MailForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            converted_text = convert_mail_text(form_data['text'])
            Mail(**form_data).send(convert_mail_text)
            return redirect('homepage')

    return render(request, template_name='home.html', context={'form': form})
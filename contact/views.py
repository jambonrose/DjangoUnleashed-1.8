from django.shortcuts import redirect, render
from django.contrib.messages import success
from django.views.generic import View
from .forms import ContactForm


class ContactView(View):
    form_class = ContactForm
    template_name = 'contact/contact_form.html'

    def get(self, request):
        return render(request,
                      self.template_name,
                      {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            mail_sent = bound_form.send_mail()
            if mail_sent:
                # shortcut for add_message
                success(
                    request,
                    'Email successfully sent.')
                return redirect('blog_post_list')
        return render(request,
                      self.template_name,
                      {'form': bound_form})

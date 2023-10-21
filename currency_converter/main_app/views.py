from django.shortcuts import render
from .forms import CurrencyForm
from .functions import requests_exchange_rates


# Create your views here.
def home(requests):
    if requests.method == 'POST':

        form = CurrencyForm(requests.POST)

        if form.is_valid():

            quantity = form.cleaned_data['quantity']
            main_currency = form.cleaned_data['main_currency'].strip()
            translatable_currency = form.cleaned_data['translatable_currency'].strip()

            result_request_course = requests_exchange_rates(main_currency, translatable_currency)

            meaning = quantity * result_request_course

            return render(requests, 'main_app\home.html', context={'form': form, 'meaning': meaning })
    
    else:
        form = CurrencyForm()

        return render(requests, 'main_app\home.html', context={'form': form})


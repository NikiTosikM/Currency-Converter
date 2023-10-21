from django import forms


class CurrencyForm(forms.Form):

    choise_currency = {
            'EUR ': ' Евро (Европейский союз)',
            'AUD ': ' Австралийский доллар',
            'BRL ': ' Бразильский реал',
            'CAD ': ' Канадский доллар',
            'CHF ': ' Швейцарский франк',
            'CNY ': ' Китайский юань',
            'GBP ': ' Фунт стерлингов (Великобритания)',
            'HKD ': ' Гонконгский доллар',
            'INR ': ' Индийская рупия',
            'JPY ': ' Японская иена',
            'KRW ': ' Южнокорейская вона',
            'MXN ': ' Мексиканское песо',
            'NOK ': ' Норвежская крона',
            'NZD ': ' Новозеландский доллар',
            'RUB ': ' Российский рубль',
            'SEK ': ' Шведская крона',
            'SGD ': ' Сингапурский доллар',
            'TRY ': ' Турецкая лира',
            'USD ': ' Доллар США',
            'ZAR ': ' Южноафриканский рэнд'
        }

    quantity = forms.IntegerField(initial= 1, min_value=1, widget = forms.TextInput(attrs= {'class' : 'field'}))
    main_currency = forms.ChoiceField(choices=choise_currency.items())
    translatable_currency = forms.ChoiceField(choices=choise_currency.items())
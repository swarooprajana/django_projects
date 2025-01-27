import generics as generics
from django.shortcuts import render
from .models import Currency
from datetime import datetime
from .serializers import CurrencySerializer
from rest_framework import generics
from countryinfo import CountryInfo
from currency_symbols import CurrencySymbols
from rest_framework.response import Response


def currency(name):
    name = CountryInfo(name)
    name1 = name.currencies()
    result = name1[0]
    return result


def symbol(symbol):
    name3 = CurrencySymbols.get_symbol(symbol)
    return name3


class Reg(generics.GenericAPIView):
    serializer_class = CurrencySerializer

    def post(self, request, *args, **kwargs):
        date1 = datetime.now()
        country = request.data.get("country")
        cou_currency = currency(country)
        currency_symbol = symbol(cou_currency)

        Symbol = Currency()
        Symbol.country = country
        Symbol.cou_currency = cou_currency
        Symbol.currency_symbol = currency_symbol
        Symbol.time = date1.strftime("%d-%m-%y")
        Symbol.save()
        return Response(CurrencySerializer(Symbol).data)


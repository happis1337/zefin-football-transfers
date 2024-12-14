from django.shortcuts import render
from django.views import View
from .models import *


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class TryoutView(View):
    def get(self, request):
        return render(request, 'tryouts.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ClubView(View):
    def get(self, request):
        context = {
            'clubs': Club.objects.all()
        }
        return render(request, 'clubs.html', context)


class PlayersView(View):
    def get(self, request):
        context = {
            'players': Player.objects.order_by('-price')
        }
        return render(request, 'players.html', context)


class LastestTransfersView(View):
    def get(self, request):
        context = {
            'transfers': Transfer.objects.all()
        }
        return render(request, 'latest-transfers.html', context)


class ClubsByCountry(View):
    def get(self, request, country_id):
        context = {
            'clubs': Club.objects.filter(country_id=country_id),
            'country': Country.objects.get(id=country_id),
        }
        return render(request, 'clubs_by_country.html', context)


class U20PlayersView(View):
    def get(self, request):
        context = {
            'players': Player.objects.filter(age__lt=20)
        }
        return render(request, 'u20_players.html', context)


class ClubById(View):
    def get(self, request, club_id):
        context = {
            'club': Club.objects.get(id=club_id),
            'players': Player.objects.filter(club_id=club_id),
        }
        return render(request, 'club-details.html', context)


class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')


class AccuratePredictionsView(View):
    def get(self, request):
        context = {
            'transfers': Transfer.objects.all().order_by('-price_tft')[:150]
        }
        return render(request, '150-accurate-predictions.html', context)


class TransferRecordsView(View):
    def get(self, request):
        context = {
            'transfers': Transfer.objects.all().order_by('-price')[:150]
        }
        return render(request, 'transfer-records.html', context)
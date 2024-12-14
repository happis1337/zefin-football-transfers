from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tryouts/', TryoutView.as_view(), name='tryouts'),
    path('about/', AboutView.as_view(), name='about'),
    path('clubs/', ClubView.as_view(), name='clubs'),
    path('players/', PlayersView.as_view(), name='players'),
    path('lastest_transfers/', LastestTransfersView.as_view(), name='lastest_transfers'),
    path('clubs/<int:country_id>/', ClubsByCountry.as_view()),
    path('u20players/', U20PlayersView.as_view(), name='u20'),
    path('club/<int:club_id>', ClubById.as_view()),
    path('stats/', StatsView.as_view(), name='stats'),
    path('accurate_predictions/', AccuratePredictionsView.as_view(), name='accurate_predictions'),
    path('transfer_records/', TransferRecordsView.as_view(), name='transfer_records'),
]
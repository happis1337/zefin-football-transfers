from django.contrib import admin
from .models import *


class PlayerInline(admin.StackedInline):
    model = Player
    extra = 1


class CountryInline(admin.StackedInline):
    model = Country
    extra = 1


class TransferInline(admin.StackedInline):
    model = Transfer
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'president', 'coach', 'found_date', 'max_import', 'max_export', 'country')
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = (PlayerInline,)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'age', 'price', 'number', 'club', 'country', 'club')
    search_fields = ('name',)
    list_filter = ('name', )


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = (TransferInline,)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('club_old', 'club_new', 'price', 'price_tft', 'player', 'season',)
    search_fields = ('club_old__name', 'club_new__name', 'player__name', 'season_name',)
    list_filter = ('club_old', 'club_new', 'price', 'price_tft', 'player', 'season',)
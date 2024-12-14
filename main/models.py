from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'



class Club(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clubs/')
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateTimeField(auto_now_add=True)
    max_import = models.CharField(max_length=255, blank=True, null=True)
    max_export = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(BaseModel):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(16, MaxValueValidator)])
    price = models.FloatField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} ({self.club.name})"


class Season(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Transfer(BaseModel):
    club_old = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_old')
    club_new = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_new')
    price = models.FloatField(blank=True, null=True)
    price_tft = models.FloatField(blank=True, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name} - {self.club_old.name} -> {self.club_new.name}"



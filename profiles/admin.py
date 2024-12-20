from django.contrib import admin
from profiles.models.athletes import Athlete, Category
from profiles.models.trainers import Trainer
from profiles.models.sport_doctors import SportDoctor

admin.site.register(Athlete)
admin.site.register(Category)
admin.site.register(Trainer)
admin.site.register(SportDoctor)




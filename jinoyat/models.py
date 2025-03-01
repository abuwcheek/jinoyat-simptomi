from django.db import models

# Create your models here.


# Jinoyatlar haqida ma'lumotlarni saqlash uchun ma'lumotlar bazasi modeli
class Crime(models.Model):
     name = models.CharField(max_length=255)  # Jinoyat nomi
     description = models.TextField()  # Jinoyatning batafsil tavsifi
     category = models.CharField(max_length=255)  # Jinoyat toifasi (masalan, zo'ravonlik, moliyaviy va h.k.)
     common_signs = models.TextField()  # Jinoyatning umumiy belgilari JSON formatida saqlanadi

     def __str__(self):
          return self.name  # Modelning matn ko‘rinishidagi ifodasi
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Crime


# Jinoyat sodir bo‘lgan sharoit va dalillar asosida ehtimoliy jinoyatchilar yoki sabablarni aniqlash funksiyasi
@csrf_exempt  # Ushbu ko‘rinishda CSRF himoyasini o‘chiradi (API so‘rovlar uchun foydali)
def analyze_crime(request):
    if request.method == 'POST':  # Faqat POST so‘rovlarini qayta ishlaydi
        try:
            data = json.loads(request.body)  # JSON so‘rovni tahlil qiladi
            user_description = set(data.get('description', []))  # Kiritilgan tavsifni taqqoslash uchun to‘plamga aylantiradi
            
            possible_crimes = Crime.objects.all()  # Bazadagi barcha jinoyatlarni oladi
            matched_crimes = []  # Mos kelgan jinoyatlar ro‘yxati
            
            for crime in possible_crimes:
                crime_signs = set(json.loads(crime.common_signs))  # Saqlangan JSON matnni to‘plamga aylantiradi
                if user_description.intersection(crime_signs):  # Belgilar mos kelishini tekshiradi
                    matched_crimes.append({
                        "name": crime.name,
                        "category": crime.category,
                        "description": crime.description
                    })
            
            return JsonResponse({"possible_crimes": matched_crimes}, status=200)  # Mos kelgan jinoyatlarni JSON shaklida qaytaradi
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)  # Xatolik yuz bersa, uni qaytaradi
    
    return JsonResponse({"error": "Noto‘g‘ri so‘rov usuli"}, status=405)  # POST bo‘lmagan so‘rovlarga xatolik qaytaradi



# Jinoyatni tekshirish uchun HTML shaklini qaytaruvchi funksiya
def crime_analysis_view(request):
     return render(request, "crime_analysis.html")

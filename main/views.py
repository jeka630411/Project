import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie

from .forms import RegistrationForm
from .models import Rating


def index(request):
    return render(request, 'main/index.html')


def about(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверяем, что введены правильные логин и пароль
        if username == 'privet' and password == '123':
            # Если данные верны, НЕ ВЫВОДИТ СООБЩЕНЕ, а вообще перенаправляемся на другую страницу
            success_message = "Авторизация выполнена успешно"
            return redirect('success')

        else:
            # Если данные неверны, передаем сообщение об ошибке в шаблон
            error_message = 'Неправильный логин или пароль'
            return render(request, 'main/about.html', {'form': RegistrationForm(), 'error_message': error_message})
    else:
        return render(request, 'main/about.html', {'form': RegistrationForm()})


def success(request):
    if request.method == 'POST':
        if 'A' in request.POST and 'B' in request.POST:
            A = request.POST.get('A')
            B = request.POST.get('B')

            if A is not None and B is not None:
                try:
                    A = int(A)
                    B = int(B)

                    K1 = (A / B) * 100
                    result = f"К1 = {K1:.2f}%"
                    mark = 0
                    if 55 < K1 <= 59:
                        mark = 1
                    elif 60 < K1 <= 64:
                        mark = 3
                    elif 65 < K1 <= 70:
                        mark = 5

                except (ValueError, ZeroDivisionError):
                    result = "Ошибка ввода данных. Пожалуйста, введите числовые значения для A и B."
                    mark = 0
            else:
                result = "Пожалуйста, введите значения для A и B."
                mark = 0

            return render(request, 'main/success.html', {'result': result, 'mark': mark})

        elif 'A1' in request.POST and 'B1' in request.POST:
            A1 = request.POST.get('A1')
            B1 = request.POST.get('B1')

            if A1 is not None and B1 is not None:
                try:
                    A1 = int(A1)
                    B1 = int(B1)

                    K2 = (A1 / B1) * 100
                    result2 = f"К2 = {K2:.2f}%"
                    mark1 = 0
                    if 45 < K2 <= 49:
                        mark1 = 1
                    elif 50 < K2 <= 54:
                        mark1 = 3
                    elif 55 < K2 <= 60:
                        mark1 = 5

                except (ValueError, ZeroDivisionError):
                    result2 = "Ошибка ввода данных. Пожалуйста, введите числовые значения для A1 и B1."
                    mark1 = 0
            else:
                result2 = "Пожалуйста, введите значения для A1 и B1."
                mark1 = 0

            return render(request, 'main/success.html', {'result2': result2, 'mark1': mark1})

    return render(request, 'main/success.html')



# Представление для сохранения рейтинга
@ensure_csrf_cookie
def rating_view(request):
    if request.method == 'GET':
        return render(request, 'main/rating.html')
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            total_score = data.get('total_score', 0)
            Rating.objects.create(total_score=total_score)
            return JsonResponse({'status': 'success', 'message': 'Рейтинг сохранен успешно!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return HttpResponse("Method not supported", status=405)




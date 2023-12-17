from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import request
from django.db import connection
from django.shortcuts import render, redirect
import logging
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string

from .models import Classrooms
from django.shortcuts import render


def render_cover(request):
    if request.user.is_authenticated:
        return redirect('main')
    return render(request, 'cover.html')


@login_required(login_url='login')
def render_main(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def render_profile(request):
    user = request.user

    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_user_group = request.POST.get('user_group')

        # Используем cursor для выполнения SQL-запроса
        with connection.cursor() as cursor:
            # SQL-запрос для обновления данных пользователя в базе данных
            sql_query = """
            UPDATE authorization_user
            SET username = %s, user_group = %s
            WHERE username = %s
            """
            cursor.execute(sql_query, [new_username, new_user_group, user.username])

            # Сообщение об успешном обновлении
            messages.success(request, 'Профиль успешно обновлен.')
            return redirect('profile')

    return render(request, 'profile.html', {'user': user})



@login_required(login_url='login')
def render_about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def render_map(request):
    classroom1 = Classrooms.objects.all()[0:1]
    classroom2 = Classrooms.objects.all()[1:2]
    classroom3 = Classrooms.objects.all()[2:3]
    classroom4 = Classrooms.objects.all()[3:4]
    classroom5 = Classrooms.objects.all()[4:5]
    classroom6 = Classrooms.objects.all()[5:6]
    classroom7 = Classrooms.objects.all()[6:7]
    classroom8 = Classrooms.objects.all()[7:8]
    classroom9 = Classrooms.objects.all()[8:9]
    classroom10 = Classrooms.objects.all()[9:10]
    classroom11 = Classrooms.objects.all()[10:11]
    classroom12 = Classrooms.objects.all()[11:12]
    classroom13 = Classrooms.objects.all()[12:13]
    classroom14 = Classrooms.objects.all()[13:14]

    cs = Classrooms.objects.all()
    classroom_title_query = request.GET.get('query', '')

    classroom_title_query = request.GET.get('query', '')
    if classroom_title_query is not None and classroom_title_query != '':
        cs = cs.filter(classroom_title__icontains=classroom_title_query)

    context = {'classrooms': cs}
    classrooms = list(cs.values())
    # Проверяем, является ли запрос AJAX-запросом
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print(cs)
        return JsonResponse({'classrooms': classrooms})

    return render(request, 'map.html', {'classroom1': classroom1, 'classroom2': classroom2,'classroom3': classroom3,
                                        'classroom4': classroom4,'classroom5': classroom5,'classroom6': classroom6,
                                        'classroom7': classroom7,'classroom8': classroom8,'classroom9': classroom9,
                                        'classroom10': classroom10,'classroom11': classroom11,'classroom12': classroom12,
                                        'classroom13': classroom13,'classroom14': classroom14, 'classrooms':cs})


@login_required(login_url='login')
def render_security(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Обновляет хеш сессии, необходимо для безопасности
            messages.success(request, 'Пароль успешно изменен.')
            return redirect('profile')  # Замените 'profile' на ваш URL профиля
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')

        if 'delete_account' in request.POST:
            # Выход из системы
            request.session.flush()

            # Удаление пользователя из базы данных
            request.user.delete()

            # Перенаправление на страницу входа
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'security.html', {'form': form})


def get_table_data(request, table_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name};")
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            # Format data as an HTML table
            table_html = '<table border="1"><tr>'
            table_html += ''.join(f'<th>{col}</th>' for col in columns) + '</tr>'
            for row in data:
                table_html += '<tr>' + ''.join(f'<td>{cell}</td>' for cell in row) + '</tr>'
            table_html += '</table>'

            return f"Table: {table_name}\n{table_html}"
    except Exception as e:
        return f"Error retrieving data from {table_name}: {str(e)}"

@login_required(login_url='login')
def update_user_groups(request):
    # Вывести данные из таблицы authorization_user
    response_user = get_table_data(request, 'authorization_user')

    # Вывести данные из таблицы auth_group
    response_group = get_table_data(request, 'auth_group')

    # Вывести данные из таблицы authorization_user_groups
    response_user_group = get_table_data(request, 'authorization_user_groups')

    return HttpResponse(response_user + '\n' + response_group + '\n' + response_user_group)







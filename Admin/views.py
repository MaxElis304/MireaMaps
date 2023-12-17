from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from django.views import View
from django.db import connection, OperationalError


def is_admin(user):
    return user.is_superuser and user.is_authenticated


class AdminPanelView(View):
    template_name = 'adminpanel.html'

    def get(self, request, *args, **kwargs):
        filter_value = request.GET.get('filter', 'user')
        user_filter_value = request.GET.get('user_filter', '')
        user_filter_value2 = request.GET.get('user_filter2', '')
        classroom_filter_value = request.GET.get('classroom_filter', 'low_attendance')
        classroom_filter_value2 = request.GET.get('classroom_filter2', None)

        try:
            query = ""
            with connection.cursor() as cursor:
                if filter_value == 'user':
                    if user_filter_value == 'is_admin' and user_filter_value2 == '2_days':
                        query = "SELECT * FROM authorization_user WHERE is_superuser = 1 AND TIMESTAMPDIFF(DAY, last_login, NOW()) < 2"
                    elif user_filter_value == 'is_admin' and user_filter_value2 == '4_days':
                        query = "SELECT * FROM authorization_user WHERE is_superuser = 1 AND TIMESTAMPDIFF(DAY, last_login, NOW()) < 4"
                    elif user_filter_value == 'is_staff' and user_filter_value2 == '2_days':
                        query = "SELECT * FROM authorization_user WHERE is_staff = 1 AND TIMESTAMPDIFF(DAY, last_login, NOW()) < 2"
                    elif user_filter_value == 'is_staff' and user_filter_value2 == '4_days':
                        query = "SELECT * FROM authorization_user WHERE is_staff = 1 AND TIMESTAMPDIFF(DAY, last_login, NOW()) < 4"
                    elif user_filter_value == 'is_user' and user_filter_value2 == '2_days':
                        query = "SELECT * FROM authorization_user WHERE is_staff = 0 AND is_superuser = 0 AND TIMESTAMPDIFF(DAY, last_login, NOW()) < 2"
                    elif user_filter_value == 'is_user' and user_filter_value2 == '4_days':
                        query = "SELECT * FROM authorization_user WHERE is_staff = 0 AND is_superuser = 0 AND TIMESTAMPDIFF(DAY, last_login, NOW()) < 4"
                elif filter_value == 'classroom':
                    if classroom_filter_value == 'low_attendance':
                        query = f"SELECT * FROM classrooms WHERE classroom_pops < 10"
                    elif classroom_filter_value == 'medium_attendance':
                        query = f"SELECT * FROM classrooms WHERE (classroom_pops BETWEEN 10 AND 20)"
                    elif classroom_filter_value == 'high_attendance':
                        query = f"SELECT * FROM classrooms WHERE classroom_pops >= 20"

                cursor.execute(query)
                columns = [col[0] for col in cursor.description]
                items = [dict(zip(columns, row)) for row in cursor.fetchall()]

        except OperationalError as e:
            items = []  # Handle the error or log it

        context = {
            'items': items,
            'filter_value': filter_value,
            'user_filter_value': user_filter_value,
            'user_filter_value2': user_filter_value,
            'classroom_filter_value': classroom_filter_value,
            'classroom_filter_value2': classroom_filter_value,
        }
        print(context)
        return render(request, self.template_name, context)



from django.shortcuts import HttpResponse, render
from django.views import View


class MenuPageView(View):
    """Представление начальной страницы сайта c категориями меню."""

    def get(self, request):
        """Отображает шаблон главной страницы сайта."""

        return render(request, 'menu_app/home_page.html')
        
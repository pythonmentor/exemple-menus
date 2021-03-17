from .views import View
from . import validators
from .models import Category


class AppController:
    def __init__(self):
        self.view = View()
        self.categories_choice = None

    def run(self):
        self.method_to_execute = self.welcome_menu
        while self.method_to_execute is not None:
            next_method = self.method_to_execute()
            self.method_to_execute = next_method

    def welcome_menu(self):
        while True:
            response = self.view.welcome_menu()
            if validators.is_valid_welcome_response(response):
                break

        if response == '1':
            return self.first_menu
        elif response == '2':
            return self.help_menu
        elif response == '3':
            return self.quit

    def help_menu(self):
        self.view.help_menu()
        return self.quit

    def first_menu(self):
        while True:
            response = self.view.first_menu()
            if validators.is_valid_first_menu_response(response):
                break
        if response == '1':
            return self.categories_menu
        elif response == '2':
            return self.help_menu
        elif response == '3':
            return self.welcome_menu
        elif response == '4':
            return self.quit

    def second_menu(self):
        self.view.second_menu()
        return self.categories_menu

    def categories_menu(self):
        categories = Category.objects.get_all_categories()
        while True:
            response = self.view.categories_menu(categories)
            if validators.is_valid_category_choice(response, categories):
                break

        if response in [
            str(index) for index, category in enumerate(categories, start=1)
        ]:
            self.categories_choice = categories[int(response) - 1]
            return self.third_menu
        elif response == str(len(categories) + 1):
            return self.welcome_menu
        elif response == str(len(categories) + 2):
            return self.quit

    def third_menu(self):
        if self.categories_choice is not None:
            print(f"La catégorie choisie est {self.categories_choice.name}")
        else:
            print(f"aucune categorie n'a été choisie")
        return self.quit

    def quit(self):
        self.view.quit()
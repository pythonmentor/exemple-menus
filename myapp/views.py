class View:
    def welcome_menu(self):
        return input(
            "Veuillez choisir la prochaine action\n"
            "1. Aller sur le premier menu\n"
            "2. Demander de l'aide\n"
            "3. Quitter le programme\n\n"
            "Quel est votre choix ? "
        )

    def help_menu(self):
        print('In help_menu')

    def first_menu(self):
        return input(
            "Bienvenue dans le premier menu !\n"
            "Veuillez choisir la prochaine action\n"
            "1. Aller sur le choix des catégories\n"
            "2. Demander de l'aide\n"
            "3. Revenir à l'accueil\n"
            "4. Quitter le programme\n\n"
            "Quel est votre choix ? "
        )

    def second_menu(self):
        print('In second_menu')

    def categories_menu(self, categories):
        menu_options = {}
        for position, category in enumerate(categories, start=1):
            menu_options[position] = category.name
        menu_options[position + 1] = "Revenir à l'accueil"
        menu_options[position + 2] = "Quitter le programme"

        # fabriquer une liste avec les options du menu
        menu_options_as_str = []
        for key, entry in menu_options.items():
            entry_string = f"{key}. {entry}\n"
            menu_options_as_str.append(entry_string)

        # fabriquer le menu lui-même sous forme d'une chaine de caractère
        menu = "".join(menu_options_as_str)

        return input(
            "Bienvenue dans le menu de choix des catégories !\n"
            "Veuillez sélectionner une catégorie\n"
            f"{menu}"
            "\n"
            "Quel est votre choix ? "
        )

    def quit(self):
        print('In quit')
        print('Goodbye !')
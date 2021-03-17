def is_valid_welcome_response(response):
    if response in [str(number) for number in range(1, 4)]:
        return True
    else:
        return False


def is_valid_first_menu_response(response):
    if response in [str(number) for number in range(1, 5)]:
        return True
    else:
        return False


def is_valid_category_choice(response, categories):
    if response in [str(number) for number in range(1, len(categories) + 3)]:
        return True
    else:
        return False
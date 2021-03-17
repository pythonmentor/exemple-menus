class CategoryManager:
    def get_all_categories(self):
        return [
            Category(name='category 1'),
            Category(name='category 2'),
            Category(name='category 3'),
            Category(name='category 4'),
        ]


class Category:

    objects = CategoryManager()

    def __init__(self, name):
        self.name = name

from DataBase import SQLQueries

class Word:
    _word_instances = []
    _categories = set()

    def __init__(self, name, category, download_link):
        self._name = name
        self._category = category
        self._download_link = download_link
        Word._word_instances.append(self)
        Word._categories.add(category)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def download_link(self):
        return self._download_link

    @download_link.setter
    def download_link(self, value):
        self._download_link = value

    def __str__(self):
        return f"Word: {self._name}, Category: {self._category}, Download Link: {self._download_link}"

    @classmethod
    def search(cls, word_name=None, category=None):
        results = []

        for instance in cls._word_instances:
            name_match = word_name.lower() in instance.name.lower() if word_name else True
            category_match = category.lower() == instance.category.lower() if category else True

            if name_match and category_match:
                results.append(instance)

        return results

    @classmethod
    def get_categories(cls):
        return list(cls._categories)

    @classmethod
    def display_all(cls):
        return _word_instances
    
    @classmethod
    def add_wordfromDB(cls):
        word_data = SQLQueries.wordGetter()
        if word_data:
            for word in word_data:
                word_name, category, download_link = word[0], word[1], word[2]
                cls(word_name,category,download_link)
        else:
            print("cant")


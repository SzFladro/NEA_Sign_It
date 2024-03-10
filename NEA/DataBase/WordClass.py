from DataBase import SQLQueries

class Word:
    # stores all word instances
    _word_instances = []
    #set to store unique categories
    _categories = set()

    def __init__(self, name, category, download_link):
        self._name = name
        self._category = category
        self._download_link = download_link
        Word._word_instances.append(self)
        Word._categories.add(category)

    #returns the name of the word
    @property
    def name(self):
        return self._name

    #sets the name of a word
    @name.setter
    def name(self, value):
        self._name = value

    #returns the category
    @property
    def category(self):
        return self._category

    #sets the category of a word
    @category.setter
    def category(self, value):
        self._category = value

    #returns the download_link
    @property
    def download_link(self):
        return self._download_link

    #sets the downloadlinks for words
    @download_link.setter
    def download_link(self, value):
        self._download_link = value

    '''
        searches for words based on name and category(filter) 
        returns the word instances that match the search criteria
    '''
    @classmethod
    def search(cls, word_name=None, category=None):
        results = []

        for instance in cls._word_instances:
            name_match = word_name.lower() in instance.name.lower() if word_name else True
            category_match = category.lower() == instance.category.lower() if category else True

            if name_match and category_match:
                results.append(instance)

        return results

    #returns a list of all categories
    @classmethod
    def get_categories(cls):
        return list(cls._categories)

    #creates a word instance for every word within the database
    @classmethod
    def add_wordfromDB(cls):
        word_data = SQLQueries.wordGetter()
        if word_data:
            for word in word_data:
                word_name, category, download_link = word[0], word[1], word[2]
                cls(word_name,category,download_link)


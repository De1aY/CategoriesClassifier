import wikipedia as wiki

class CategoriesParser:
    _Search = ""
    _RequestText = ""
    _WikiPage = ""

    def __init__(self, search, requestText):
        self._Search = search
        self._RequestText = requestText
        wiki.set_lang("ru")

    def WikiSearch(self):
        resp = wiki.search(self._Search, 500)
        self._WikiPage = wiki.page(resp[0])


    def ParseCategories(self):
        result = []
        categories = self._WikiPage.categories
        for category in categories:
            index = category.find(":")
            result.append(category[index+1:len(category)])
        return result
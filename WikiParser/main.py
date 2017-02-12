import wikipedia
from WikiParser.categories_parser import CategoriesParser
from WikiParser.request_parser import RequestParser
from WikiParser.categories_comparative import CategoriesComparative

RParser = RequestParser()
CatComparative = CategoriesComparative()
while True:
    Request = RParser.GetRequest()
    if Request is False:
        break
    else:
        CParser = CategoriesParser(Request, Request)
        CParser.WikiSearch()
        Categories = CParser.ParseCategories()
        CatComparative.FindCategories(Categories)

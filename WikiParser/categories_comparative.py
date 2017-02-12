class CategoriesComparative:
    __Categories = []
    __Categories_Path = "Data/categories.txt"
    __Result = ""
    __Result_Path = "Data/result.txt"

    def __init__(self):
        self.__ParseCategories()
        self.__Result = open(self.__Result_Path, 'w')

    def __ParseCategories(self):
        file = open(self.__Categories_Path, 'r', encoding='utf-8-sig')
        self.__Categories= file.read().split(",")
        file.close()

    def FindCategories(self, category):
        result = []
        for i in range(len(self.__Categories)):
            if self.__Categories[i] in category:
                result.append(i+1)
        self.__PrintCategories(result)
        self.__WriteCategoriesToFile(result)

    def Close(self):
        self.__Result.close()

    def __PrintCategories(self, categories):
        for category in categories:
            print(category, end=" ")
        print(end="\n")

    def __WriteCategoriesToFile(self, categories):
        for category in categories:
            self.__Result.write(str(category) + " ")
        self.__Result.write("\n")
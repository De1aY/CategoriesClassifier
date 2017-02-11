class RequestParser:
    _File = ""

    def __init__(self):
        self._File = open('Data/request.txt', 'r', encoding='utf-8')

    def __GetLine(self):
        line = self._File.readline()
        if len(line) > 0:
            return line
        else:
            return None

    def __Close(self):
        self._File.close()
        return False

    def __ParseRequest(self, request):
        request = request.replace("[1]", "")
        request = request.replace("[2]", "")
        request = request.replace("[3]", "")
        if len(request) > 300:
            index = request.find(".")
            request = request[0:index]
        if request[0] == "«":
            index = request.find("»")
            request = request[1:index]
        return request

    def GetRequest(self):
        RequestText = self.__GetLine()
        if RequestText is not None:
            return self.__ParseRequest(RequestText)
        else:
            return self.__Close()
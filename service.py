class Service:

    @staticmethod
    def getStatus():
        f = open("status.txt", "r")
        letter = f.read()
        f.close()
        return letter

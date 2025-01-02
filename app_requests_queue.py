from queue import Queue


class AppRequest:
    def __init__(self, data):
        self.__data = data

    def __repr__(self):
        return self.__data

    def __str__(self):
        return f"AppRequest({self.__data})"


class AppRequestsQueue():
    def __init__(self):
        self.__queue = Queue()

    def generate_request(self, data):
        request = AppRequest(data)
        self.__queue.put(request)
        return request

    def process_request(self):
        return self.__queue.get()

    def is_empty(self):
        return self.__queue.empty()

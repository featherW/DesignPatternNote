import threading


class SafeLazyInitialization(object):
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        raise Exception("禁用new")

    @classmethod
    def getinstance(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = object.__new__(SafeLazyInitialization)
        return cls.__instance


if __name__ == '__main__':
    e1 = SafeLazyInitialization.getinstance()
    e2 = SafeLazyInitialization.getinstance()
    print("e1->addr: {}\ne2->addr: {}".format(e1, e2))
    print(e1 == e2)

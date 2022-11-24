class LazyInitialization(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        raise Exception("禁用new")

    @classmethod
    def getinstance(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(LazyInitialization)
        return cls.__instance


if __name__ == '__main__':
    e1 = LazyInitialization.getinstance()
    e2 = LazyInitialization.getinstance()
    print("e1->addr: {}\ne2->addr: {}".format(e1, e2))
    print(e1 == e2)

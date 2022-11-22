class EagerInitialization(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        raise Exception("禁用new")

    @staticmethod
    def getinstance():
        if EagerInitialization.__instance is None:
            EagerInitialization.__instance = object.__new__(EagerInitialization)
        return EagerInitialization.__instance


if __name__ == '__main__':
    e1 = EagerInitialization.getinstance()
    e2 = EagerInitialization.getinstance()
    print("e1->addr: {}\ne2->addr: {}".format(e1, e2))
    print(e1 == e2)

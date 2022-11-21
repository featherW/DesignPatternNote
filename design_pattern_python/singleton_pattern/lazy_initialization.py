class EagerInitialization(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if EagerInitialization.__instance is None:
            EagerInitialization.__instance = object.__new__(EagerInitialization)
        return EagerInitialization.__instance

    def hello(self):
        print("hello")


if __name__ == '__main__':
    e1 = EagerInitialization()
    e2 = EagerInitialization()
    print("e1->addr: {}\ne2->addr: {}".format(e1, e2))
    print(e1 == e2)

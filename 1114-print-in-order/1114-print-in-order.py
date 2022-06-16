class Foo:
    def __init__(self):
        self.firstDone = False
        self.secondDone = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.firstDone = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.firstDone:
            continue
        printSecond()
        self.secondDone = True
        

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.secondDone:
            continue
        printThird()

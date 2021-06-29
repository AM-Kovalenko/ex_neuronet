'''
модуль свзей нейрона
'''


class Link:
    def __init__(self, n_in, n_out, w=0):       #ссылка на входной и выходной нейрон, значение веса связи
        self.__in = n_in
        self.__out = n_out
        self.__w = w

    @property
    def n_in(self):
        return self.__in

    @property
    def n_out(self):
        return self.__out

    @property
    def w(self):
        return self.__w
from random import randint
from string import punctuation, ascii_lowercase, ascii_uppercase


class GeneratorDigit:

    def __init__(self, start_range=0, end_range=9):
        self._start_range = start_range
        self._end_range = end_range

    def get_generator_digit(self):
        return str(randint(self._start_range, self._end_range))


class GeneratorLetters:

    def __init__(self, start_range=0, end_range=len(ascii_lowercase)):
        self._start_range = start_range
        self._end_range = end_range

    def get_lowercase_letters(self):
        return ascii_lowercase[randint(self._start_range, self._end_range) - 1]

    def get_uppercase_letters(self):
        return ascii_uppercase[randint(self._start_range, self._end_range) - 1]


class GeneratorPunctuation:

    def __init__(self, start_range=0, end_range=len(punctuation)):
        self._start_range = start_range
        self._end_range = end_range

    def get_punctuation(self):
        return punctuation[randint(self._start_range, self._end_range) - 1]


class GeneratorsUsersPasswords:

    @staticmethod
    def generator_password(quantity, password=None):
        if password is None:
            password = []
            for i in range(quantity // 4):
                password.append(GeneratorDigit().get_generator_digit())
                password.append(GeneratorLetters().get_uppercase_letters())
                password.append(GeneratorLetters().get_lowercase_letters())
                password.append(GeneratorPunctuation().get_punctuation())

            return ''.join(password)


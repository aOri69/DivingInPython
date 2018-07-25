import re
from abc import ABC, abstractmethod


class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text):
        pass


class System:
    def __init__(self, text: str) -> None:
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor: TextProcessor):
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class WordCounter:
    def count_words(self, text: str):
        self.__words = {}
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word: str):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()


class WordCounterAdapter(TextProcessor):
    """
    Inheriting from abstract
    This is an ADAPTER
    """

    def __init__(self, adaptee: WordCounter) -> None:
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words,
                      key=lambda x: self.adaptee.get_count(x),
                      reverse=True)


if __name__ == '__main__':
    text = """
    In software engineering, a software design pattern is a general, reusable solution to a commonly 
    occurring problem within a given context in software design. It is not a finished design that can be transformed 
    directly into source or machine code. It is a description or template for how to solve a problem that can be used 
    in many different situations. Design patterns are formalized best practices that the programmer can use to solve 
    common problems when designing an application or system. 
    Object-oriented design patterns typically show relationships and interactions between classes or objects, 
    without specifying the final application classes or objects that are involved. Patterns that imply mutable state may 
    be unsuited for functional programming languages, some patterns can be rendered unnecessary in languages that have 
    built-in support for solving the problem they are trying to solve, and object-oriented patterns are not necessarily 
    suitable for non-object-oriented languages. 
    Design patterns may be viewed as a structured approach to computer programming intermediate between the levels of a 
    programming paradigm and a concrete algorithm. 
    """
    system = System(text)
    counter = WordCounter()
    adapter = WordCounterAdapter(counter)
    # Importing an adapter as processor to system
    system.get_processed_text(adapter)

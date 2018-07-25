"""Метаклассы - это классы которые создают классы"""
# def dummy_factory():
#     class Class:
#         pass
#     return Class


class Meta(type):
    def __new__(cls, name, parents, attrs):
        print('Creating {}'.format(name))
        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()
        return super().__new__(cls, name, parents, attrs)


class A(metaclass=Meta):
    pass


def main():
    print('A.class_id: {}'.format(A.class_id))
    # Создание класса на лету
    NewClass = type('NewClass', (), {})
    print(NewClass, NewClass())


if __name__ == '__main__':
    main()

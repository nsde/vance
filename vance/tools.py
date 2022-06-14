from typing import Union

def contains(text: str, strings: Union[list, str]) -> bool:
    if isinstance(strings, str):
        strings = [strings]
    return all([string in text for string in strings])

def grab(text: str, begin: str, end: str) -> bool:
    return text.split(begin)[1].split(end)[0]

if __name__ == '__main__':
    print(contains('Hello there, Pat!', 'Pat'))
    print(contains('Hello there, Pat!', ['Pat', 'Rick']))
    
    print(grab('Never gonna give you up', 'Never ', ' give'))
    print(grab('Never gonna give you up', 'Never ', ' give you '))
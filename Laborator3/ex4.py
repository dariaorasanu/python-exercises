"""
4. Fie functia build_xml_element care primeste urmatorii parametri: tag, content si elemente cheie-valoare date ca parametri cu nume.
Sa se construiasca si sa se returneze un string care reprezinta elementul XML aferent.
Exemplu: build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid") => "<a href="http://python.org" class_="my-link” id="someid">Hello there</a>"
"""


def build_xml_element(tag, content, **dictionary):
    result = f'<{tag}'
    for key in dictionary.keys():
        if key[0] == '_':
            result = f'{result} {key[1:]}_="{dictionary[key]}"'
        else:
            result = f'{result} {key}="{dictionary[key]}"'
    result = f'{result}>{content}</{tag}>'
    return result

print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))




import unicodedata
import re


def strip_accents(s):
    s = ''.join(c for c in unicodedata.normalize(
        'NFD', s) if unicodedata.category(c) != 'Mn')
    s = s.encode('ascii', 'ignore').decode("utf-8")
    return s


def strip_duplicated_char(s, char):
    while 2*char in s:
        s = s.replace(2*char, char)
    return s


def string_norm(s):
    s = s.strip().replace(" ", "_")
    s = strip_accents(s)
    s = re.sub(r'\W+', '', s)
    s = s.lower()
    s = strip_duplicated_char(s, "_")
    return s

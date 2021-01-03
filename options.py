from re import sub
from warnings import warn


VALUES = {
    'true': True,
    'false': False,
}
OPTIONS = {}


with open('options.txt') as file:
    content = sub(r'\n+', '\n', file.read().strip())
    for key, value in (line.split(':') for line in content.split('\n')):
        if value not in VALUES:
            warn(f'invalid value {value!r} for key {key!r} in options.txt')
            OPTIONS[key] = None
        OPTIONS[key] = VALUES[value]


warned_cache = {*()}


def get_option(key):
    if key not in OPTIONS:
        if key not in warned_cache:
            warn(f'key {key!r} not found in options.txt')
            warned_cache.add(key)
        return
    return OPTIONS[key]

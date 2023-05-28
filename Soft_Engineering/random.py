import random
import string

def generate_random_string(length, letters=True, digits=True):
    pool = ''
    if letters:
        pool += string.ascii_letters
    if digits:
        pool += string.digits

    if not pool:
        return ""

    return ''.join(random.choices(pool, k=length))

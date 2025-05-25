import random
import time

#BASE62 Charset
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62[0]
    result = []
    while num > 0:
        num, rem = divmod(num, len(BASE62))
        result.append(BASE62[rem])
    return ''.join(reversed(result))

# Short Generate URL
def generate_short_url(length: int) -> str:
    # Current Time NS
    now_ns = time.time_ns()

    # Random number for duplicate prevention
    random_number = random.randint(0, 9999)

    # BASE 62 Hashing
    value = now_ns + random_number
    result = encode_base62(value)

    # length slice
    return result[:length]
import roughpy as rp
import numpy as np

word = "stream"
for i, letter in enumerate(word):
    vec = np.zeros(26, dtype=np.int8)
    vec[ord(letter) - 97] = 1
    print(i, letter, vec)

CTX = rp.get_context(width=26, depth=3, coeffs=rp.Rational)


def word_to_stream(word):
    increment_array = np.zeros((len(word), 26), dtype=np.int8)
    for i, letter in enumerate(word):
        letter_idx = ord(letter)
        assert 97 <= letter_idx <= 122, f"expected lower case letter, got {letter}"
        increment_array[i, letter_idx - 97] = 1

    return rp.LieIncrementStream.from_increments(increment_array, resolution=2, ctx=CTX)

stream = word_to_stream(word)
signature = stream.signature()
print(signature)

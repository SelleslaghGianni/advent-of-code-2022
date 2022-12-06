X = [l.strip() for l in open('input6.txt')]


def get_idx(signal, marker):
    for char_idx in range(len(signal)):
        chars = set(signal[char_idx:char_idx + marker])
        if len(chars) == marker:
            return char_idx + marker


print(get_idx(X[0], 4))
print(get_idx(X[0], 14))

# python3
# Miks Zeltiņš  13.Grupa  221RDB123

def read_input():
    if "I" in input():
        pat=input().strip()
        txt=input().strip()
    else:
        file=open("tests/06","r")
        pat=file.readline().strip()
        txt=file.readline()
        file.close()

    return (pat, txt)

def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash(string, rolling_total = None):
    if not string:
      return rolling_total

    if rolling_total == None:
      return hash(string[1:], ord(string[0]))

    return hash(string[1:], ((rolling_total * 256) % 101 + ord(string[0])) % 101)


def rehash(old_letter, old_hash, new_letter, pattern_len):
    base_value = 256

    
    for i in range(pattern_len - 2):
      base_value = (base_value % 101) * 256
    
    base_value %= 101
    
    return ((old_hash + 101 - ord(old_letter) * base_value) * 256 + ord(new_letter)) % 101

def get_occurrences(pattern, text):
    pattern_hash = hash(pattern)
    slice_hash = None
    text_slice = ""
    pattern_len = len(pattern)

    occurrences = []
    
    for i in range(len(text) - pattern_len + 1):
      new_slice = text[i:i + pattern_len]

      if not slice_hash:
        slice_hash = hash(new_slice)
      else:
        slice_hash = rehash(text_slice[0], slice_hash, new_slice[-1], pattern_len)
        
      text_slice = new_slice

      if pattern_hash == slice_hash and text_slice == pattern:
        occurrences.append(i)

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
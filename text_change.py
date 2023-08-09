st = "FOO"

char_change = "a"

changed_str = ""

for ch in st:

    if ch.lower() in 'aeiou':

        if ch.islower():

            changed_str += char_change.lower()

        else:

            changed_str += char_change.upper()

    else:

        changed_str += ch

print(changed_str)

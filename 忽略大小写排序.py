def cmp_ignore_case(s1, s2):
    if s1.upper()>s2.upper():
        return -1
    if s1.upper()<s2.upper():
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
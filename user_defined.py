def length(s):
    print("Length:", len(s))

def upper(s):
    print("Uppercase:", s.upper())

def lower(s):
    print("Lowercase:", s.lower())

def reverse(s):
    print("Reverse:", s[::-1])

def vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    print("Vowels:", count)


text = input("Enter a string: ")

length(text)
upper(text)
lower(text)
reverse(text)
vowels(text)
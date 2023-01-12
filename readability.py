from cs50 import get_string

s = get_string("Text: ").strip()
num_word, num_letters, num_sentences = 0, 0, 0

for i in range(len(s)):
    if (i == 0 and s[i] != ' ') or (i != len(s) - 1 and s[i] == ' ' and s[i + 1] != ' '):
        num_word += 1
    if s[i].isalpha():
        num_letters += 1
    if s[i] == '.' or s[i] == '?' or s[i] == '!':
        num_sentences += 1


L = num_letters / num_word * 100
S = num_sentences / num_word * 100
index = round(0.0588 * L - 0.296 * S - 15.8)
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")

# # your code goes here!

# # Solution1 (Using set)
# class Anagram:
#     def __init__(self, word):
#         print(f"word: {word}")
#         self.word = word

#     def match(self, possible_anagrams):
#         matches = []

#         for wrd in possible_anagrams:
#             if len(wrd) == len(self.word) and set(wrd) == set(self.word):
#                 matches.append(wrd)

#         return matches


# Solution2 (Using sorted)
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        matches = []

        for wrd in possible_anagrams:
            if sorted(self.word) == sorted(wrd):
                matches.append(wrd)

        return matches

# Solution3 (provided solution)
# at initialization: self.word_letters = sorted([letter for letter in word])
# for every word in the list argument: if sorted([letter for letter in word]) == self.word_letters:

# Test
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
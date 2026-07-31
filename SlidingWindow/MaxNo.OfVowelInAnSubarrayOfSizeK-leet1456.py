# Problem Statement :

# Given a string s and an integer k, return the maximum number of vowels in any substring of length k.

# Vowels are: a, e, i, o, u.

# Example
# Input:
# s = "abciiidef"
# k = 3

# Output:
# 3

# Explanation:
# Substrings of size 3:

# abc → 1 vowel
# bci → 1 vowel
# cii → 2 vowels
# iii → 3 vowels  ← Maximum
# iid → 2 vowels
# ide → 2 vowels
# def → 1 vowel

# Sliding Window Idea :

# Instead of recounting vowels for every window:

# Count vowels in the first window.
# Slide the window:
# If the left character is a vowel, subtract 1.
# If the new right character is a vowel, add 1.
# Keep track of the maximum count.
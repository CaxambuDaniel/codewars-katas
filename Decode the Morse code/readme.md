# Morse Code Decoder

In this kata, you have to write a simple Morse code decoder. While Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.

Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as `·−`, letter Q is coded as `−−·−`, and digit 1 is coded as `·−−−−`. Morse code is case-insensitive, and traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate character codes, and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is `···· · −·−−   ·−−− ··− −·· ·`.

**Note:** Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits, and some punctuation, there are some special service codes, the most notorious of which is the international distress signal SOS (first issued by Titanic), coded as `···−−−···`. These special codes are treated as single special characters and are usually transmitted as separate words.

## Task

Your task is to implement a function that takes Morse code as input and returns a decoded human-readable string.

For example:

```python
decode_morse('.... . -.--   .--- ..- -.. .')
# should return "HEY JUDE" 
```

**Note:** For coding purposes, you have to use ASCII characters `.` and `-`, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it. The usage depends on the language you are using.

All test strings will contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception; please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.

Good luck!

After you complete this kata, you may try yourself at [Decode the Morse code, advanced](https://www.codewars.com/kata/54b72c16cd7f5154e9000457).

# Nickname Generator

This script generates random nicknames using the letters from a given set of words.

## Usage
Enter words separated by ', ' when prompted.
Enter minimum and maximum length of the word when prompted.
Enter number of words to generate when prompted.

## Example
```shell
Enter words separated by ', ': You, me, and, I
Enter minimum length of the word: 3
Enter maximum length of the word: 4
Enter number of words to generate: 2

YoMe
AyeI
DoM
```

## Functionality

The script performs the following actions:

1. Accepts input words and shuffles the letters to generate a new word.
2. Filters the shuffled letters by the given minimum and maximum length to generate a list of possible nicknames.
3. Capitalizes the first letter of each nickname.
4. Selects the number of words to generate randomly from the list of possible nicknames and prints them out.

## Notes
- If no words are entered, the script will exit.
- If the number of letters generated is less than 3, the script will exit.
- If the minimum length is less than 3, the script will exit.
- If the maximum length is greater than the number of letters, the script will exit.
- If the number of words to generate is less than 1, the script will exit.
- If no words can be generated with the given constraints, the script will exit.

## Author
- [**@Nysioko**](https://github.com/Nysioko)

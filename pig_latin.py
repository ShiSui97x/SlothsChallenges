"""                        PIG LATIN                        """

def pig_latin(sentence: str) -> str:
    """
    Converts a sentence into Pig Latin.

    Rules for converting to Pig Latin:

    For words that begin with a vowel (a, e, i, o, u), add "way".

    Otherwise, move all letters before the first vowel to the end and add "ay".

    For simplicity, no punctuation will be present in the inputs.
    """
    result = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            result.append(word + 'way')
        else:
            for i, char in enumerate(word):
                if char in 'aeiou':
                    result.append(word[i:] + word[:i] + 'ay')
                    break
    return ' '.join(result)


if __name__ == '__main__':
    print(pig_latin("this is pig latin"))
    print(pig_latin("wall street journal"))
        

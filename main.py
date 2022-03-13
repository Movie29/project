while(1):

    s = input('Enter a Sentence: ').lower()

    if s != "quit":

        words = s.split()

        for i, w in enumerate(words):

# if first letter is a vowel simply postfix "ay" for each word

            if w[0] in 'aeiou':

                words[i] = words[i]+ "ay"

    else:

# if 1st letter isn't vowel then get vowel position and postfix

# all the consonants present before that vowel to the end of

# the word along with "ay"

        contains_vowel = False

        for k, character in enumerate(w):

            if character in 'aeiou':

                words[i] = w[k:] + w[:k] + "ay"

                contains_vowel = True

                break

#if the word doesn't have any vowel then simply postfix "ay"

                    if(contains_vowel == False):

                        words[i] = words[i]+ "ay"

                        pig_latin = ' '.join(words)

                        print("Pig Latin: ",pig_latin)

                    else:

                        break


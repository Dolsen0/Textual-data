from textblob import TextBlob

# Docs for textblob can be found:
# https://textblob.readthedocs.io/en/latest/quickstart.html#part-of-speech-tagging

text = input("Enter a sentence to determine sentence: tags, noun phrases, polarity, and sentiment \n")

blob = TextBlob(text)

#defines sentiment polarity. If the sentence is "positive" a positive message appears
#if the message is negative it will inform you the message is not positive
def sentimentAnalysis():
    if (blob.sentiment[0] < .5):
        return("im sorry, that doesn't sound great.")
    else :
        return("That sounds great!")





#print(f" \n the following are tags: \n {blob.tags}")    # prints part of speech tags
#print(f" \n the following are noun phrases: \n{blob.noun_phrases}")    #noun phrases 
#print(f" \n the following shows the polarity and sentiment: \n {blob.sentiment}")   # "The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective."

print(sentimentAnalysis())

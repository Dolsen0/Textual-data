from textblob import TextBlob

# Docs for textblob can be found:
# https://textblob.readthedocs.io/en/latest/quickstart.html#part-of-speech-tagging

text = input("\nEnter a sentence\n")

blob = TextBlob(text)

#defines sentiment polarity. If the sentence is "positive" a positive message appears
#if the message is negative it will inform you the message is not positive
def polarity_Analysis():
    if (blob.sentiment[0] < .15):
        return("Negative")
    elif (blob.sentiment[0] < .35):
        return("Less positive")
    elif (blob.sentiment[0] < .45):
        return("Fairly positive")
    else :
        return("Positive!")

def objectivity_analysis():
    if blob.sentiment[1] < .5:
        return("\nThis may be an objective")
    else:
        return("\nThis is most likely subjective/opinion based")





#print(f"\nThe following are tags: \n {blob.tags}")    # prints part of speech tags
#print(f"\nThe following are noun phrases: \n{blob.noun_phrases}")    #noun phrases 
print(f"\nThe following shows the polarity and sentiment:\n{blob.sentiment}\n")   # "The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective."

print(polarity_Analysis())
print(objectivity_analysis())

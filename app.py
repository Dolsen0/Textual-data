from textblob import TextBlob


text = input("\nEnter a sentence\n")
correction = TextBlob(text).correct()
blob = TextBlob(text)

def polarity_Analysis():
    if (blob.sentiment[0] < .15):
        return("...doesn't sound great")
    elif (blob.sentiment[0] < .35):
        return("...alright that sounds okay")
    elif (blob.sentiment[0] < .45):
        return("...sounds pretty good.")
    else :
        return("...sounds great!")

def objectivity_analysis():
    if blob.sentiment[1] < .5:
        return("\nThis may be an objective")
    else:
        return("\nThis is most likely subjective/opinion based")





#print(f"\nThe following are tags: \n {blob.tags}")    # prints part of speech tags
#print(f"\nThe following are noun phrases: \n{blob.noun_phrases}")    #noun phrases 
#print(f"\nThe following shows the polarity and sentiment:\n{blob.sentiment}\n")   # "The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective."

print(polarity_Analysis())
print(objectivity_analysis())

#word correction
print(blob.tags)
print(blob)
print(blob.words)
#print(f" potential correction: '{correction}")


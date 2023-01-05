from textblob import TextBlob

text = "Hello everyone. I'm here today to inform you that there is a new technology that we would like to implement which will allow us to process textual data. Let's see the results provided with the previous two sentences."

blob = TextBlob(text)

print(blob.noun_phrases)
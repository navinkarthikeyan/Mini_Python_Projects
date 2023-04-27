#first you have to install better_profanity library by"pip install better_profanity"
from better_profanity import profanity
text = "shit ! I left my keys back in the car "
censored = profanity.censor(text)
print(censored)

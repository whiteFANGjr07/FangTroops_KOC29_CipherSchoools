#first we enter sentence.
user=input('Enter: ').upper()
#split the sentence.
everyword=user.split(' ')
# make a emp to store outcome
s=''
#we remove is the and a such a word
#and store in s
#cut first letter of each split word
for i in everyword:
    if len(i)>3:
        s=s+i[0]+'.'
# remove last dot that comes in right side of outcome
print(s.rstrip('.'))
# your code is ready

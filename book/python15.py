# random: Import the random class
# random.choice(): Use the random function to generate characters randomly
import random
when = ['20 years ago', 'yesterday', 'the night before last', 'a long time ago', 'one day in the future']
who = ['beautiful woman', 'elderly person', 'handsome man', 'child', 'foreigner']
name = ['Zhang San', 'Li Si', 'Wang Wu', 'Zhao Liu', 'Sun Qi']
residence = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chongqing']
went = ['library', 'movie theater', 'park', 'restaurant', 'shopping mall']
happened = ['picked up a penny', 'it started to rain heavily', 'discovered a secret', 'helped an elderly person', 'fell down']
print(random.choice(when) + ', a person from ' + random.choice(residence) + ', named ' + random.choice(name) + ', went to ' + random.choice(went) + ', and on the way ' + random.choice(happened) + '.')
input()  # This last line is just waiting for user input and does not produce any output.
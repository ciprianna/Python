from sys import argv

script, user_name, cat_name = argv
prompt = "--> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions about %s."  % cat_name
print "Do you pet him often, %s?" % user_name
pets = raw_input(prompt)

print "Where does %s sleep, %s?" % (cat_name, user_name)
sleeps = raw_input(prompt)

print "What color is %s?"  % cat_name
colors = raw_input(prompt)

print """
Alright, so you said %r about lots of pets.
Your cat sleeps in %r.  Not sure where that is.
And he has %r fur.  Cutes!
""" % (pets, sleeps, colors)
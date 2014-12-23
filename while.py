while True:
    print "What word am I thinking of?"
    answer = raw_input(">")
    if answer == "cheese":
        print "You guessed it!"
        break
    else:
        print "Nope, try again"

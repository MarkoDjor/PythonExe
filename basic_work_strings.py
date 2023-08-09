#def main():

word = "octopus"

# if ( word.lower()[0] in 'aeiou' ):
#
#     article = "an" #print( f'We see an {word}' )
#
# else:
#
#     article = "a" #print( f'We see a {word}' )

article = "an" if word.lower()[0] in 'aeiou' else "a"

#print( f'We see {article} {word}' )

print( 'We see {} {}'.format(article,word) )


#if _name_ == '_main_':

 #   main()


import sys
import MailParser

text = sys.stdin.read()

# print( text )
mail=MailParser.MailParser(text)

print( mail.get_attr_data() )
'''
	created by: Ricardo dos S A Nunes
	date: 09/18/2017
	class: NLP
	Assignment: HW2
'''

import nltk
import re

# input file test
# f_in = open("all-OANC.txt")
# input file
f_in = open("test_dollar_phone_corpus.txt")

test_string_currency = ["$50 billion 400 million 3 thousand 3 hundred 5 dollars and 50 cents","     $50 billion dollars and 50 cents","    million people","500.000.000,31", "500","","millions of dollars","$5 billion dollars and 50 cents","millions of dollars","billions of dollars"," $5 thousand ", "5 thousand dollars","$5 million ","3 billion dollar", "300 dollars", "$300.00",  "$433,123,111.03", "$312 dollars", "1 dollar"]
# function to replace match in new line
def replace_string(match):
	n_line = "["+match.group()+"]"
	return n_line

# pattern for currency
currency_pattern = re.compile(r"""						
(							# values can start anywhere
	\$\d{1,3}
	([,\.]\d{1,3})*						# informal for thousands, millions and billions etc	
	((\s\d{1,3})?
		(
		([\s-](([gG]az)|([tT]r)|[bB]|[mM])illions?)
		|
		([\s-][tT]housands?)
		|
		([\s-][hH]undreds?)
		|
		(\sof)?
		|
		(\sand)?
		|			
		(\s\d{1,3})
		)*
	)*
	(\s[dD]ollars?)?
	(\sand\s\d{1,2}\scents?)?
)

""", re.VERBOSE)

# output files
f_out_currency = open("regex_dollar.txt", "+w")
f_out_currency_list = open("output_dollar.txt", "+w")
f_out_currency_match = open("dollar.txt", "+w")

# Algorithm to filter currency regex
for line in f_in:
	n_line = currency_pattern.sub(replace_string, line, re.VERBOSE)
	f_out_currency.write(n_line)
	if len(n_line) != len(line):
		f_out_currency_list.write(n_line+"\n")
		match = currency_pattern.search(line)
		f_out_currency_match.write(match.group(1) + "\n")

f_out_currency.close()
f_out_currency_list.close()
f_out_currency_match.close()
f_in.close()

# input test
# f_in = open("all-OANC.txt")

# input 
f_in = open("test_dollar_phone_corpus.txt")
# pattern for phones
phone_patterns = re.compile(r"""						
(
	(
		[\.\(\[\-]?
		(\d{3})					# XXXXXX000-0000
		[\s\.\)\]\-]?
		(\s?)
	)?
	(\d{3})						# 0(000)XXXX0000
	\D
	(\d{4})						# 0(000)0000XXXX
	(
		[\.,\s]*
		([eE][xX][tT])
	)?
	(\d*)?
	$						
)
""", re.VERBOSE)

# output files for phone regex
f_out_phone = open("regex_phone.txt", "+w")
f_out_phone_list = open("output_phone.txt", "+w")
f_out_phone_match = open("phones.txt", "+w")

# Algorithm to filter phone regex
for line in f_in:
	n_line = phone_patterns.sub(replace_string, line, re.VERBOSE)
	f_out_phone.write(n_line)
	if len(n_line) != len(line):
		f_out_phone_list.write(n_line+"\n")
		match = phone_patterns.search(line)
		f_out_phone_match.write(match.group(1)+"\n")
		
f_out_phone.close()
f_out_phone_list.close()
f_out_phone_match.close()
f_in.close()

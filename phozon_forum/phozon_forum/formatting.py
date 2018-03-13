import urllib.parse

def html_safe( input ):
	return urllib.parse.quote_plus( input )

def sexy_number( numero ):
	return "{:,}".format( numero )
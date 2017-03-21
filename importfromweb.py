import urllib2
# urllib2 is built into python, no extra installation needed
# gutenburg.org is a collection of free ebooks

response = urllib2.urlopen(
    'http://www.gutenberg.org/')
html = response.read()

print html

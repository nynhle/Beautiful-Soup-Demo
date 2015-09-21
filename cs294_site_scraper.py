from bs4 import BeautifulSoup
import urllib2

#Downloading the HTML-file via a GET-request.
site = urllib2.urlopen('http://bruab.github.io/cs294_fall2015/')

#Parsing the HTML-file into a iterable tree.
tree = BeautifulSoup(site, 'html.parser')

#Printing the whole mess...
print '====PRINTING ALL THE MESS===='
print tree

#Printing each single HTML node, kinda looks like the source HTML.
print '====PRINTING NODES ALMOST LIKE HTML===='
for node in tree:
	print node
 
#Were looking for links.. So were gonna filter out these.
print '====PRINTING THE WHOLE LINK NODES===='
for link in tree.find_all('a'):
	print link

#We just want the actual HTML attribute href though, the actual link. Not the whole node.
print '====PRINTING THE ACTUAL LINKS===='
for link in tree.find_all('a'):
	print link.get('href')

#Now it's easy to filter all the links with only cs294. 
print '====PRINTING ONLY THE LINKS ON THE SAME DOMAIN===='
for link in tree.find_all('a'):
	if link.get('href').startswith('/cs294_fall2015'):
		print link.get('href')

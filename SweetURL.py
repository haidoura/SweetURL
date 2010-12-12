'''
Created on Nov 16, 2010

@author: H.Haidoura
'''
import pygtk
pygtk.require('2.0')
import gtk
import sys
import time
import re

#def main(sysargs=sys.argv[:]):
def main():
	#item initialization
	aCopyText = ""
	newCpText = ""
	
	while True:
		try:
			time.sleep(0.1)
			# get text from clipboard
			clipboard = gtk.clipboard_get()
			clipboard.wait_is_text_available()
			rawText = clipboard.wait_for_text()
			
			#handle text check if this a different text to process
			if (rawText != aCopyText and rawText != None) :
				aCopyText = rawText
				
				#make sure its not the text we processed before
				if ( rawText != newCpText or newCpText == "" ):
					print ">> RAW Text:: " 
					print  aCopyText
				
					all_original_links = readTextFromClip(rawText)
					print ">> URLS captured:: "
					print all_original_links
				
					if all_original_links:
						#clear clipboard to gain time for conversion
						clipboard.clear()
						all_tiny_links = makeTextTiny( all_original_links)
						print ">> tiny links:: "
						print all_tiny_links
						newCpText = updateRawText(rawText , all_tiny_links)
						setTextToClip( newCpText , clipboard)
				
		except KeyboardInterrupt:				
			break
			
				
#
# handle the raw text form clipboard 
# return a list of urls in that text
#				
def readTextFromClip(aText):

	links_list = find_urls(aText)
	
	if( links_list ):
		return links_list
	else:
		return None

# replace old text with our new text
def updateRawText(rawText , all_tiny_links):
	
	newText = rawText
	for key, value in all_tiny_links.items():
		try:
			newText = newText.replace(key , value)
			print "* converted " + key + " to " + value
			
		except:
			print "* cannot convert " + key
			
	
	return newText

#
# add the new text in the clipboard
# make sure to store to make data available for other applications

def setTextToClip(updatedText , clipboard):
	clipboard.set_text(updatedText)
	clipboard.store()

#use regular expression to check if its has a link
# return list of links captured
def find_urls(html):
	
	url_list = []
#	for tag in re.findall('(?:http://|www.)[^"\' ]+', html): # find the a tags
#TODO upgrade this to handle https links also
	for tag in re.findall('(?:http://|www.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html):
		m = tag
		if m:
			url_list.append(m) # add the sub match
			
	return url_list

# process all urls gather them and return a mapped list (Dictionary)
# the dictionary will include original links (as keys) while tiny links are the values of its original link 
def makeTextTiny( all_original_links):
	
	alinksList = {}
	
	for alink in all_original_links:
		#print "Url:: " + alink
		
		if (alinksList.has_key(alink)):
			print "--duplicate links--"
		else:
			import UrlShortener
			cls = service(1)
			urlShorter =  getattr(UrlShortener , cls)(cls)
			tiny_link = urlShorter.shorten(alink)
			print "tiny url:: " 
			print tiny_link
			#add to dictionary
			alinksList[alink] = tiny_link
			
	return alinksList



#####################################
def service(x):
	return { 1:'TinyUrl', 
		    2:'Googl', 
		    3:'Bitly'}[x]

if __name__ == '__main__':

	
	sys.exit( main() )
	
	
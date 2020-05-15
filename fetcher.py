from google_images_download import google_images_download  
import urllib.request
import re

# Your username
usr = ""

fp = urllib.request.urlopen("https://myanimelist.net/animelist/" + usr + "?status=2")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

beg = mystr.find("<table class=\"list-table\" data-items=")
end = mystr.find(">",beg)

mystr = mystr[beg:end+1]

animelist = []
pos = [m.start() for m in re.finditer('anime_url', mystr)]

for position in pos:
	j = 0
	anime = ""
	for letter in mystr[position:]:
		if letter == "&" and j == 3:
			break
		if j == 3:
			anime+=letter 
		if letter == "/":
			j+=1
	anime+= " minimalist wallpaper"
	animelist.append(anime)

print("\n\n",*animelist, sep = "\n")
#print("\n\n",animelist)
print("\n\nWhich of these do you want? [A]all")
keyword = input()

keywordanimelist = []

if keyword != "a" and keyword != "A":
	for anime in animelist:
		if keyword in anime:
			keywordanimelist.append(anime)


# creating object 
response = google_images_download.googleimagesdownload()  

def downloadimages(query): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query,"limit":4, "print_urls":True} 
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query, "format": "jpg", "limit":4, "print_urls":True, "size": "medium"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
  
# Driver Code 
if keyword != "a" and keyword != "A":
	for query in keywordanimelist: 
	    downloadimages(query)  
	    print()
else:
	for query in animelist: 
	    downloadimages(query)  
	    print()


#print(pos, len(pos))

from urllib.parse import urlparse

address = input("Insert the Address to get all URL details: ")
url = (address)

o = urlparse(url)
print (o)
if o.scheme != "":
    print("Scheme: ", o.scheme) 
    
if o.netloc != "":
    print("Netloc: ", o.netloc)

if o.path != "":
    print("Path: ", o.path)

if o.params != "":
    print("Params: ", o.params)

if o.query != "":
    print("Query: ", o.query)
    
if o.fragment != "":
    print("Fragment: ", o.fragment)
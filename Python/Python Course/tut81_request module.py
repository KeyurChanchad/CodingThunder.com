"""
What is HTTP?
HTTP stands for the 'Hypertext Transfer Protocol,'.
 It is a set of protocols that are designed to enable communication between clients and servers.
 Between clients and servers, it works as a request-response protocol.
 To request a response from the server, we can request data from the server, or we can submit data to be processed to the server.

What Is Requests Module?
The response data depends on our type of request. The requests module is not a built-in Python module;
instead, we have to download it manually. Requests module is used to send all kinds of HTTP requests.
It is also one of the most downloaded modules in Python because all the web related software and programs must have it in them.

requests.get(URL, params={key: value}, args)

URL: this is the URL of the website where we want to send the request.

Params: this is a dictionary or a list of tuples used to send a query string.

Args: It is optional. It can be any named arguments offered by the get method.


put():          It is used to send a put request to a variable.
                It is usually used to update or completely change the resources of a specific URL.

delete():       Delete is used to delete the specific resource, specified by URL.

head():         The head method returns a header for a specific resource

post( ):        Post requests take with it the data to the server to update it with.

patch( ):       The patch is used to send patch requests. It is used to apply partial modifications to a resource.
                It carries with it the instructions for the modification.


"""

import requests

# r = requests.get("https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-81")
# print(r.text)
# print(r.status_code)
# print(r.encoding)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)

# ```````````````````````````````````````````````````````````````````````````
# The Get Requeste:
# One of the most common HTTP methods is GET. The GET method indicates that you’re trying to get or retrieve data from a specified resource.
# To make a GET request, invoke requests.get().

requests.get('https://api.github.com')

# The Response
# A Response is a powerful object for inspecting the results of the request. Let’s make that same request again,
# but this time store the return value in a variable so that you can get a closer look at its attributes and behaviors:

response = requests.get('https://api.github.com')

""" 
Status Code
The first bit of information that you can gather from Response is the status code.
A status code informs you of the status of the request.

For example, a 200 OK status means that your request was successful,
whereas a 404 NOT FOUND status means that the resource you were looking for was not found.

    Informational responses(100–199)
    Successfulresponses(200–299)
    Redirects(300–399)
    Client errors(400–499)
    Server errors(500–599)
  
    100 Continue  
    101 Switching Protocol
    102 processing 
    
    200 Ok
    201 Created
    202 Accepted
    203 Non Authoritative Information
    204 No Content
    205 Reset content 

"""
r = response.status_code
print(r)

#Content
c = response.content
# print(c)

# Headers
# The response headers can give you useful information, such as the content type of the response payload and a time limit on
# how long to cache the response. To view these headers, access .headers:

# response.headers

 # requests.post('https://httpbin.org/post', data={'key':'value'})
 # requests.put('https://httpbin.org/put', data={'key':'value'})
 # requests.delete('https://httpbin.org/delete')
 # requests.head('https://httpbin.org/get')
 # requests.patch('https://httpbin.org/patch', data={'key':'value'})
 # requests.options('https://httpbin.org/get')

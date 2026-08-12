# Why HTTP?

## Communicating on the web

A "client" is a computer making an HTTP request
A "server" is a computer responding to an HTTP request
A computer can be a client, a server, both, or neither. "Client" and "server" are just words we use to describe what computers are doing within a communication system.
Clients send requests and receive responses
Servers receive requests and send responses
HTTP is the most common internet protocol
URLs (uniform resource locator) can use more than just the HTTP protocol

## PyFetch

response is the data that comes back from the server
url is the URL we are making a request to
method specifies the HTTP method to use (GET, POST, etc.)
headers is a dictionary containing HTTP headers to send with the request
await response.json() converts the JSON response data from the server into a Python object

## Web Clients

A client can be any type of device but is often something users physically interact with. For example:

    A desktop computer
    A mobile phone
    A tablet

In a website or web application, we call the user's device the "front-end".

A front-end client makes requests to a back-end server.

## Web Servers

### The Server Is the Back-End

While the "front-end" of a website or web application is the device the user interacts with, the "back-end" is the server that keeps all the data housed in a central location.

### A Server Is Just a Computer

"Server" is just the name we give to a computer that is taking on the role of serving data across a network connection. A good server is turned on and available 24 hours a day, 7 days a week. While your laptop can be used as a server, it makes more sense to use a computer in a data center that's designed to be up and running constantly.

# DNS

## Web Address

web addresses are just converted into an IP address in order for a computer to know where to point a request on the internet

Used the below code to address a nested dictionary in a list in a dictionary which was technically JSON - return resp_object["Answer"][0]["data"]
from pyodide.http import pyfetch

async def fetch_ip_address(domain: str) -> str | None:
resp = await pyfetch(
f"https://1.1.1.1/dns-query?name={domain}&type=A",
method="GET",
headers={
"accept": "application/dns-json",
},
)
resp_object = await resp.json()

    return resp_object["Answer"][0]["data"]

Deploying a real website to the internet is actually quite simple. It involves only a couple of steps:

1. Create a server that hosts your website files and connect it to the internet
2. Acquire a domain name
3. Connect the domain name to the IP address of your server
4. Your server is accessible via the internet!

## DNS (Domain Name System)

A "domain name" or "hostname" is just one portion of a URL. We'll get to the other parts of a URL later.
For example, the URL https://homestarrunner.com/toons has a hostname of homestarrunner.com. The https:// and /toons portions aren't part of the domain name -> IP address mapping that we've been talking about.
Parsing a URL in Python

Python provides the urlparse function from the urllib.parse module that helps parse URLs into their components:

from urllib.parse import urlparse

parsed_url = urlparse("https://homestarrunner.com/toons")

And then you can extract just the hostname using the hostname attribute:

hostname = parsed_url.hostname
print(hostname) # homestarrunner.com

### How Does DNS Work?

We'll go into more detail on DNS in a future course, but to give you a simplified idea, let's just introduce ICANN. ICANN is a not-for-profit organization that manages DNS for the entire internet.

Whenever your computer attempts to resolve a domain name, it contacts one of ICANN's "root nameservers" whose address is included in your computer's networking configuration. From there, that nameserver can gather the domain records for a specific domain name from their distributed DNS database.

If you think of DNS as a phonebook, ICANN is the publisher that keeps the phonebook in print and available.

## Subdomains

A subdomain prefixes a domain name, allowing a domain to route network traffic to many different servers and resources.

For example, docs.github.com is a subdomain of github.com. The docs subdomain likely routes to a different server than the main github.com domain.

# URIs (Uniform Resource Identifiers)

A URI, or Uniform Resource Identifier, is a unique character sequence that identifies a resource that is (almost always) accessed via the internet.
URIs come in two main types:

- URLs
- URNs

## Further dissecting a URL

There are 8 main parts to a URL, though not all the sections are always present.
Part Required
Protocol Yes
Username No
Password No
Domain Yes
Port No (defaults to 80 or 443)
Path No (defaults to /)
Query No
Fragment No

## URL PORTS

The port in a URL is a virtual point where network connections are made. Ports are managed by a computer's operating system and are numbered from 0 to 65,535 (Though port 0 is reserved for the system API).

Whenever you connect to another computer over a network, you're connecting to a specific port on that computer, which is listened to by a program on that computer. A port can only be used by one program at a time, which is why there are so many possible ports.

The port component of a URL is often not visible when browsing normal sites on the internet, because 99% of the time you're using the default ports for the HTTP and HTTPS schemes: 80 and 443 respectively.

## URL Paths

Paths in URLs are essentially just another type of parameter that can be passed to the server when making a request.

# JSON

## Sending JSON

In python we use the JSON module which has two main methods, json.loads() and json.dumps()
dumps() does the opposite of loads(). It takes a python dictionary or list and serialises the object into a string which is useful we need to store it in a database.

async def update_project_by_id(project_id: str, project_obj: Project) -> Project:
path = f"https://api.boot.dev/v1/courses_rest_api/learn-http/projects/{project_id}"
response = await pyfetch(
path,
method="PUT",
headers=get_headers(),
body=json.dumps(project_obj),
)
return await response.json()

import json

data: dict[str, str | bool] = {"name": "waseem", "chad": True}
json_string = json.dumps(data)
print(json_string) # {"name": "waseem", "chad": true}

# only the boolean changed!

## Parsing JSON

### Parse

Use only 'raise' keyword when deliberately wanting to halt a program from running.

def parse_project(project_string: str) -> None:
try:
parsed = json.loads(project_string)
return print_project_obj(parsed)
except Exception:
print("invalid json string")

## XML (Extensible Markup Language)

XML is a markup language like HTML, but it's more generalized in that it does not use predefined tags. Just like how in a JSON object keys can be called anything, XML tags can also have any name.

XML
<root>
<id>1</id>
<genre>Action</genre>

  <title>Iron Man</title>
  <director>Jon Favreau</director>
</root>

JSON
{
"id": "1",
"genre": "Action",
"title": "Iron Man",
"director": "Jon Favreau"
}

XML used to be used for the same things that today JSON is primarily used for. Configuration files, HTTP bodies, and other data-transfer can work with either JSON or XML.
JSON is:

    Lighter-weight
    Easier to read
    Has better support in most programming languages

There are cases where XML might still be better, or maybe even necessary, but that tends to be the exception rather than the rule.

# Methods
HTTP methods typically align by convention with CRUD actions; create, read, update, delete. 

## HTTP Methods - GET
GET aligns with read in CRUD. Below is an example of a get request using pyfetch.

async def get_users(url: str, api_key: str) -> list[User]:
    response = await pyfetch(
        url,
        method="GET",
        headers={
            "X-API-Key": api_key,
        },
    )
    return await response.json()

## POST Requests
### Adding a body
The body is the payload request sent to the server.
The Content-Type header is the header which indicates to the server format the body is in e.g. 'application/json'


async def create_user(api_key: str, url: str, data: User) -> User:
    response = await pyfetch(
        url,
        method="POST",
        headers={
            "X-API-Key":api_key,
            "Content-Type":"application/json",
        },
        body=json.dumps(data)
    )
    return await response.json()


## Status Codes
The Status Code of an HTTP response tells the client whether or not the server was able to fulfill the request. Status codes are 3-digit numbers that are grouped into categories:

    100-199: Informational responses. These are very rare.
    200-299: Successful responses. Hopefully, most responses are 200's!
    300-399: Redirection messages. These are typically invisible because the browser or HTTP client will automatically do the redirect.
    400-499: Client errors. You'll see these often, especially when trying to debug a client application
    500-599: Server errors. You'll see these sometimes, usually only if there is a bug on the server.

Here are some of the most common status codes, but there is also a full list here if you're interested.

    200 - OK. This is by far the most common code, it just means that everything worked as expected.
    201 - Created. This means that a resource was created successfully. Typically in response to a POST request.
    301 - Moved permanently. This means the resource was moved to a new place, and the response will include where that new place is. Websites often use 301 redirects when they change their domain name, for example.
    400 - Bad request. A general error indicating the client made a mistake in their request.
    401 - Unauthorized. This means the client doesn't have the correct permissions. Maybe they didn't include a required authorization header, for example.
    404 - Not found. You'll see this on websites quite often. It just means the resource doesn't exist.
    500 - Internal server error. This means something went wrong on the server, likely a bug on their end.

Don't Memorize

It's good to know the basics by heart, like "2XX is good", "4XX is a client error", and "5XX is a server error". But don't memorize all the status codes... they're easy to look up.

## Status code property
The response object from pyfetch has a .status property that contains the status code of the response.

async def get_user_code(url: str, api_key: str) -> int:
    response = await pyfetch(
        url,
        method="GET",
        headers={
            "X-API-Key": api_key,
        },
    )
    return response.status

## PUT Method
This is the update in the CRUD analogy. It updates a representation of the target resource with the contents of the request's body.
### POST vs PUT
While POST and PUT are both used for creating resources, PUT is more common for updates and is idempotent, meaning it's safe to make the request multiple times without changing the server state. For example:

POST /users/bob (create bob user)
POST /users/bob (create duplicate bob user)
POST /users/bob (create duplicate bob user)

PUT /users/bob (create bob user if it doesn't exist)
PUT /users/bob (update bob user with the same data)
PUT /users/bob (update bob user with the same data)

## Delete 
This deletes things. Doesn't require a 'Content-Type' header.

# Paths
## URL Paths
The URL Path comes right after the domain (or port if one is provided) in a URL string.

In this URL:

`http://testdomain.com/root/next`

The path is:

/root/next

### Path Conventions
Many static websites (websites where the content does not change, as opposed to dynamic web applications) use paths as a direct mapping to the path to the server's file system. For example, If I was running a static web server for "mystaticstate.com" from the root of my file system, a GET request to http://mystaticstate.com/documents/hello.txt would serve the file at /documents/hello.txt from my server.

Most dynamic web applications don't use this simple mapping of URL path -> file path. Technically, a URL path is just a string that the web server can do what it wants with, and modern websites take advantage of that flexibility. Some common examples of what paths are used for include:

    The hierarchy of pages on a website, whether or not that reflects a server's file structure
    Parameters passed into an HTTP request, like the ID of a resource
    The version of the API
    The type of resource being requested


## RESTful APIs
Representational State Transfer, or REST, is a popular convention that many dynamic HTTP servers follow. 
RESTful servers follow a loose set of rules that makes it easy to build reliable and predictable web APIs. REST is a set of conventions about how HTTP APIs should be built.

### Separate and Agnostic
The big idea behind REST is that resources are transferred via well-recognized, language-agnostic client/server interactions. A RESTful style means the implementation of the client and server can be created independently of one another, as long as some simple standards, like the names of the available resources, have been established.

### Stateless
A RESTful architecture is stateless, which means the server does not need to know what state the client is in, nor does the client need to know what state the server is in. Statelessness in REST is enforced by interacting with resources instead of commands. Keep in mind, this doesn't mean the applications are stateless - what would "updating a resource" even mean if the server wasn't keeping track of its state?

### Paths in REST
In a RESTful API, the last section of the path of a URL specifies the resource. In Jello, this means an issue, a user, or a project. Depending on whether the request is a GET, POST, PUT or DELETE, the resource is read, created, updated, or deleted.

The Jello API we have been working with is a RESTful API! Take a look at the URLs we've been using:

- https://api.boot.dev/v1/courses_rest_api/learn-http/projects
- https://api.boot.dev/v1/courses_rest_api/learn-http/users
- https://api.boot.dev/v1/courses_rest_api/learn-http/issues

1. The first part of the path specifies the version. In this case, version 1, or v1.
2. The second part of the path tells our server that this is a REST API for the "Learn HTTP" course.
3. The last part denotes which resource is being accessed, be it a project, user, or issue.

## Query Parameters
async def get_users(url: str, api_key: str) -> list[User]:
    full_url = f"{url}?sort=experience"
    response = await pyfetch(
        full_url,
        method="GET",
        headers={
            "X-API-Key": api_key,
        },
    )
    return await response.json()

## Documentation of a HTTP Server
The server has complete control over how the path in a URL is interpreted and used in a request. The same goes for query parameters. While there are a lot of strong conventions around how servers should interpret paths and query parameters, the server can do whatever it wants. That's why you need docs.

# HTTPS
Hypertext Transfer Protocol Secure or HTTPS is an extension of the HTTP protocol. HTTPS secures the data transfer between client and server by encrypting all of the communication.

HTTPS allows a client to safely share sensitive information with the server through an HTTP request, such as credit card information, passwords, or bank account numbers.


async def get_user_by_id(base_url: str, user_id: str) -> User:
    secure_base_url = base_url.replace("http://", "https://")
    path = f"{secure_base_url}/{user_id}"
    response = await safe_fetch(
        path,
        method="GET",
        headers={
            "X-API-Key": api_key,
            "Content-Type": "application/json",
        },
    )
    return cast(User, await response.json())


## Security and Encryption
HTTPS requires that the client use SSL or TLS to protect requests and traffic by encrypting the information in the request. HTTPS is just HTTP with extra security!

### HTTPS Keeps Your Messages Private, but Not Your Identity
It's important to note that while HTTPS encrypts what you are saying, it doesn't necessarily protect who you are. Tools like VPNs are needed for added privacy.

### HTTPS Ensures That You're Talking to the Right Person (or Server)
In addition to encrypting the information within a request, HTTPS uses digital signatures to prove that you're communicating with the server that you think you are. If a hacker were to intercept an HTTPS request by tapping into a network cable, they wouldn't be able to successfully pretend they are your bank's web server.
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
print(hostname)  # homestarrunner.com

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
Part 	    Required
Protocol 	Yes
Username 	No
Password 	No
Domain 	    Yes
Port 	    No (defaults to 80 or 443)
Path 	    No (defaults to /)
Query 	    No
Fragment 	No
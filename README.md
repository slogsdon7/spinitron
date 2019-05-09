Python wrapper for [Spinitron's](https://spinitron.com) API.


## Quick-start
```python
from spinitron.client import Spinitron

#The api key can also be stored in an environment variable called SPINITRON_KEY
spinitron = Spinitron(api_key='API_KEY')
```

Each endpoint is represented as a method on the `spinitron` client object. 
These methods accept an id as their first parameter and will pass additional keyword arguments as query parameters when making the HTTP request.

Individual objects are instances of a Model class which contains methods for accessing related objects. 
Fields on these objects are also accessible as properties. 

```python
#get the most recent spin
spin = spinitron.spins().items[0]

#print spin's artist
print(last_spin.artist)

#get the playlist for last_spin
playlist = spin.playlists()

#get the spins for the playlist, 50 per page
spins = playlist.spins(count=50)

##iterate through all of the playlists
for page in spinitron.playlists():
    for playlist in page.items:
        #do something with your playlist
        
##get a specific playlist using the playlist's ID
playlist = spinitron.playlists(54728)

##get spins starting starting in 2019
spins_2019 = spinitron.spins(start="2019-01-01")

```

See [Spinitron's API docs](https://spinitron.github.io/v2api/) for the different parameters each endpoint accepts.



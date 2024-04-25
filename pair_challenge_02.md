
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

# 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Home route
GET / spaces

# space/new route
POST / space
# parameter: name
# availability: 


```

# 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /spaces
#  Expected response (200 OK):
"""
This is a list of airBnB spaces!
"""


# POST /space?name=benshouse&availability=free
#  Expected response (200 OK):
"""
Ben's house
Availability: Free
"""




```

# 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /spaces
  Expected response (200 OK):
  "This is a list of airBnB spaces!"
"""


def test_get_spaces(web_client):
    response = web_client.get('/spaces')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is a list of airBnB spaces!'


"""
POST /space
  Parameters:
    name: Ben's house
    availability: Free
  Expected response (200 OK):
  "Ben's house
Availability: Free"
"""


def test_post_space(web_client):
    response = web_client.post(
        '/spaces/new', data={'name': 'Ben\'s house', 'availability': 'free'})
    assert response.status_code == 200
    assert response.data.decode(
        'utf-8') == 'Ben\'s house\nAvailability: Free'


```

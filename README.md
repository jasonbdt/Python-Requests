# Python-Requests

This repository serves as contributors playground for using Pythons
`requests` library.

## How to install

```bash
pip install requests
```

## How to use `requests`

### Send GET Request

```python
import requests

res = requests.get(url, params={key: value}, args)
print(res.text)
```

More Information: [Click here](https://www.w3schools.com/python/ref_requests_get.asp)

### Send POST Request

```python
import requests

res = requests.post(url, data={key: value}, json={key: value}, args)
print(res.text)
```

More Information: [Click here](https://www.w3schools.com/python/ref_requests_post.asp)

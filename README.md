# Token HMAC
About 4x times faster than [PyJWT](https://github.com/jpadilla/pyjwt).

## Installation
```
$ pip install tokenhmac
```

[![Downloads](https://pepy.tech/badge/tokenhmac)](https://pepy.tech/project/tokenhmac)
[![Downloads](https://pepy.tech/badge/tokenhmac/month)](https://pepy.tech/project/tokenhmac/month)
[![Downloads](https://pepy.tech/badge/tokenhmac/week)](https://pepy.tech/project/tokenhmac/week)

## Examples

```python
import tokenhmac

KEY = "Secret Key"

token = tokenhmac.TokenHMAC(KEY)

value = "Message"
encoded = token.encode(value.encode("utf-8"))
print(encoded)
# b'TWVzc2FnZQ==.aKA0izCttsIOAWvblvsB5xdY17DlaOzlMVeKG1f0u0o='

token.decode(encoded).decode("utf-8")
# "Message"
```


```python
import tokenhmac

KEY = "Secret Key"

token = tokenhmac.TokenHMAC(KEY)

value = 123
encoded = token.encode(value.to_bytes(8, "big"))
print(encoded)
# b'AAAAAAAAAHs=.FAqptzNnojMDx_bfoH6PKTBWP7tFpo4CQyGseVUM9vA='

int.from_bytes(token.decode(encoded), "big")
# 123
```

```python
import tokenhmac
import json

KEY = "Secret Key"

token = tokenhmac.TokenHMAC(KEY)

value = {"id": 123, "msg": "Message"}
encoded = token.encode(json.dumps(value).encode("utf-8"))
print(encoded)
# b'eyJpZCI6MTIzLCJtc2ciOiJNZXNzYWdlIn0=.NlnFLagfGDSn5XmSBmVnmDgqAsBApGx6GFXuvYtjPb4='

json.loads(token.decode(encoded).decode("utf-8"))
# {"id": 123, "msg": "Message"}
```
## License
`tokenhmac` is offered under the MIT license.

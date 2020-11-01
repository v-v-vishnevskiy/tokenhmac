# Token HMAC
Like JWT but more faster as it possible.

About 4x times faster than [PyJWT](https://github.com/jpadilla/pyjwt).

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

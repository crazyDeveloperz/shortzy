<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kevinnadar22/shortzy">
    <img src="https://play-lh.googleusercontent.com/v_bqvNUR5tNZlIkXe3oe8e5WDFjj4ApHKN-6H3U-rcvi0X0qjQlOefzb05RPxTNBU8A" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Shortzy</h3>

  <p align="center">
   A Unofficial Wrapper for Adlinkfly Site and Alternative Sites
    <br />
    ·
    <a href="https://www.telegram.dog/ask_admin001">Report Bug / Request Feature</a>
    ·
    <a href="#usage">Usage</a>
    ·
    <a href="#reference">Reference</a>
  </p>
</div>


---

# Shortzy
An Unofficial Python version of Adlinkfly and Alternative Website API wrapper. Used to Short your long link and let you earn from it.


## Installation

Install shortzy with pip

```bash
pip install shortzy
```
    
To Upgrade

```bash
pip install --upgrade shortzy
```
    
    
## Usage

```python
from shortzy import Shortzy
import asyncio

shortzy = Shortzy('<YOUR API KEY>')

async def main():
    link = await shortzy.convert('https://example.com/')
    print(link)

asyncio.run(main())
```

```python
Output: https://droplink.co/mVkra
```

## Available Websites

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Available list of Websites</summary>
  <ol>
    <li><a href="https://droplink.co" target="_blank">droplink.co</a></li>
    <li><a href="https://gplinks.in" target="_blank">gplinks.in</a></li>
    <li><a href="https://tnlink.in" target="_blank">tnlink.in</a></li>
    <li><a href="https://za.gl" target="_blank">za.gl</a></li>
    <li><a href="https://du-link.in" target="_blank">du-link.in</a></li>
    <li><a href="https://viplink.in" target="_blank">viplink.in</a></li>
    <li><a href="https://shorturllink.in" target="_blank">shorturllink.in</a></li>
    <li><a href="https://shareus.in" target="_blank">shareus.in</a></li>
    <li><a href="https://sahiurl.in" target="_blank">sahiurl.in</a> ✨ NEW</li>
    <li><a href="https://siteprotector.vercel.app" target="_blank">siteprotector.vercel.app</a> ✨ NEW</li>
    <li><a href="https://telegram.me/ask_admin001">Request For Your Website !</a></li>
  </ol>
</details>

---

## Using sahiurl.in

```python
from shortzy import Shortzy
import asyncio

shortzy = Shortzy(api_key="YOUR_SAHIURL_API_KEY", base_site="sahiurl.in")

async def main():
    # Single URL shorten
    link = await shortzy.convert("https://example.com/")
    print(link)
    # Output: https://sahi.to/abc123

    # With custom alias
    link = await shortzy.convert("https://example.com/", alias="mylink")
    print(link)

    # Bulk convert
    links = ["https://github.com/", "https://google.com/"]
    short_links = await shortzy.bulk_convert(links)
    print(short_links)

    # Convert all links inside a text
    text = "Visit https://example.com/ and https://google.com/"
    result = await shortzy.convert_from_text(text)
    print(result)

asyncio.run(main())
```

> **API Key**: Get from [sahiurl.in](https://sahiurl.in) Dashboard → Tools
>
> **Response field**: `shortenedUrl`

---

## Using siteprotector.vercel.app

```python
from shortzy import Shortzy
import asyncio

shortzy = Shortzy(api_key="YOUR_SITEPROTECTOR_API_KEY", base_site="siteprotector.vercel.app")

async def main():
    # Single URL shorten
    link = await shortzy.convert("https://example.com/")
    print(link)
    # Output: https://siteprotector.vercel.app/go/8k2N9x

    # Bulk convert
    links = ["https://github.com/", "https://google.com/"]
    short_links = await shortzy.bulk_convert(links)
    print(short_links)

    # Convert all links inside a text
    text = "Visit https://example.com/ and https://google.com/"
    result = await shortzy.convert_from_text(text)
    print(result)

asyncio.run(main())
```

> **API Key**: `583e61f4-6920-4a26-a8fc-397eea598a08` (example — use your own)
>
> **Response field**: `shortened_url`

---

## Features

- Single URL Convert
- Batch Convert from List
- Convert from Text

## Contributing

Contributions are always welcome!

## Reference

### Init
```python
from shortzy import Shortzy
import asyncio

shortzy = Shortzy(api_key="Your API Key", base_site="droplink.co") 

# Base site defaults to "droplink.co". You can add your own site here which is alternative to this default site
# Please Refer https://github.com/kevinnadar22/shortzy#available-websites for more information
```

### Convert a single URL

```python
convert(link, alias, silently_fail, quick_link) -> str
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `link` | `string` | **Required**. Long URL Link |
| `alias` | `string` | Custom alias for the link |
| `silently_fail` | `bool` | Raise an exception or not if error ocuurs |
| `quick_link` | `bool` | Returns the quick link |


Example:

```python
async def main():
    link = await shortzy.convert('https://www.youtube.com/watch?v=d8RLHL3Lizw')
    print(link)

asyncio.run(main())

## Output: https://droplink.co/Ly4fCxZ
## Quick Link: https://droplink.co/st?api=<YOUR API KEY>&url=https://www.youtube.com/watch?v=d8RLHL3Lizw
```

### Bulk Convert

```python
bulk_convert(urls:list, silently_fail, quick_link:bool=False) -> list
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `urls`      | `list` | **Required**. List of URLs to convert |

Example:

```python
async def main():
    links = ['https://github.com/', 'https://twitter.com/', 'https://google.com/']
    link = await shortzy.bulk_convert(links)
    print(link)

asyncio.run(main())

## Output: ['https://droplink.co/ihu1e', 'https://droplink.co/AkY2Nt', 'https://droplink.co/mK1eVTV']
```

### Convert from Text

```python
convert_from_text(text:str, silently_fail:bool=True, quick_link:bool=False) -> str
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text`      | `str` | **Required**. Text containing Long URLS to short|

Example:

```python
async def main():
    text = """
Unstoppable:-https://www.youtube.com/watch?v=330xlOv8p9M
Night Changes:-https://www.youtube.com/watch?v=syFZfO_wfMQ
"""
    link = await shortzy.convert_from_text(text)
    print(link)

asyncio.run(main())

# Output:
# "Unstoppable:-https://droplink.co/T6jbHlU
# Night Changes:-https://droplink.co/ajIRE"
```

### Get quick link

```python
get_quick_link(link:str)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `link`      | `str` | **Required**. Long Link|

Example:

```python
async def main():
    link = "https://www.youtube.com/watch?v=syFZfO_wfMQ"
    quick_link = await shortzy.get_quick_link(link)
    print(quick_link)

asyncio.run(main())

## Quick Link: https://droplink.co/st?api=<YOUR API KEY>&url=https://www.youtube.com/watch?v=syFZfO_wfMQ
```

## Support

For support, email jesikamaraj@gmail.com or PM [Dev](https://t.me/ask_admin001)

## Roadmap

- Add more integrations

## Disclaimer

[![GNU Affero General Public License v3.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL v3.0.](https://github.com/kevinnadar22/shortzy/blob/main/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.


## Credits
 - [Thanks To Me](https://github.com/Kevinnadar22)

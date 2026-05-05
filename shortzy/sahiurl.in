import asyncio
import re
from urllib.parse import urlparse
import aiohttp


class SahiUrl:
    """
    API Wrapper for sahiurl.in
    GET https://sahiurl.in/api?api=API_KEY&url=URL
    Response: {"status":"success","shortenedUrl":"https://sahi.to/abc123"}
    """

    def __init__(self, api_key: str, base_site: str = "sahiurl.in"):
        self.api_key = api_key
        self.base_site = base_site
        self.base_url = "https://sahiurl.in/api"

        if not self.api_key:
            raise Exception("API key not provided")

    async def __fetch(self, session: aiohttp.ClientSession, params: dict) -> dict:
        async with session.get(
            self.base_url, params=params, raise_for_status=True, ssl=False
        ) as response:
            result = await response.json(content_type=None)
            return result

    async def convert(
        self,
        link: str,
        alias: str = "",
        silently_fail: bool = False,
        quick_link: bool = False,
        **kwargs,
    ) -> str:
        is_short_link = await self.is_short_link(link)

        if is_short_link:
            return link

        if quick_link:
            return await self.get_quick_link(url=link, alias=alias)

        params = {
            "api": self.api_key,
            "url": link,
            "format": "json",
        }
        if alias:
            params["alias"] = alias

        try:
            my_conn = aiohttp.TCPConnector(limit=10)
            async with aiohttp.ClientSession(connector=my_conn) as session:
                data = await self.__fetch(session, params)

                if data.get("status") == "success":
                    return data["shortenedUrl"]

                if silently_fail:
                    return link

                raise Exception(data.get("message", "Unknown error from sahiurl.in"))

        except Exception as e:
            raise Exception(e) from e

    async def get_quick_link(self, url: str, alias: str = "", **kwargs) -> str:
        """Returns a direct (non-interstitial) short link using text format."""
        params = f"api={self.api_key}&url={url}&format=text"
        if alias:
            params += f"&alias={alias}"
        return f"{self.base_url}?{params}"

    async def bulk_convert(
        self, urls: list, silently_fail: bool = True, quick_link: bool = False, **kwargs
    ) -> list:
        tasks = [
            asyncio.ensure_future(
                self.convert(link=url, silently_fail=silently_fail, quick_link=quick_link)
            )
            for url in urls
        ]
        return await asyncio.gather(*tasks, return_exceptions=True)

    async def convert_from_text(
        self, text: str, silently_fail: bool = True, quick_link: bool = False, **kwargs
    ) -> str:
        links = await self.__extract_url(text)
        shortened_links = await self.bulk_convert(
            links, silently_fail=silently_fail, quick_link=quick_link
        )
        for i, short_link in enumerate(shortened_links):
            text = text.replace(links[i], short_link)
        return text

    async def is_short_link(self, link: str) -> bool:
        domain = urlparse(link).netloc
        # sahiurl.in short links go to sahi.to domain
        return "sahi.to" in domain or self.base_site in domain

    async def __extract_url(self, string: str) -> list:
        regex = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|in|io|co)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»""''])|\b(?:https?://)[^\s<>"']+)"""
        urls = re.findall(regex, string)
        return ["".join(x) for x in urls]

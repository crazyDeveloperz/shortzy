import asyncio
import re
from urllib.parse import urlparse
import aiohttp


class SiteProtector:
    """
    API Wrapper for siteprotector.vercel.app
    GET https://siteprotector.vercel.app/api?api=API_KEY&url=URL
    Response: {"status":"success","shortened_url":"https://siteprotector.vercel.app/go/8k2N9x"}
    """

    def __init__(self, api_key: str, base_site: str = "siteprotector.vercel.app"):
        self.api_key = api_key
        self.base_site = base_site
        self.base_url = f"https://{self.base_site}/api"

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
            return await self.get_quick_link(url=link)

        params = {
            "api": self.api_key,
            "url": link,
        }

        try:
            my_conn = aiohttp.TCPConnector(limit=10)
            async with aiohttp.ClientSession(connector=my_conn) as session:
                data = await self.__fetch(session, params)

                if data.get("status") == "success":
                    return data["shortened_url"]

                if silently_fail:
                    return link

                raise Exception(
                    data.get("message", "Unknown error from siteprotector.vercel.app")
                )

        except Exception as e:
            raise Exception(e) from e

    async def get_quick_link(self, url: str, **kwargs) -> str:
        """Returns the direct API URL (acts as quick link since no interstitial page)."""
        return f"{self.base_url}?api={self.api_key}&url={url}"

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
        return self.base_site in domain

    async def __extract_url(self, string: str) -> list:
        regex = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|in|io|co)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»""''])|\b(?:https?://)[^\s<>"']+)"""
        urls = re.findall(regex, string)
        return ["".join(x) for x in urls]

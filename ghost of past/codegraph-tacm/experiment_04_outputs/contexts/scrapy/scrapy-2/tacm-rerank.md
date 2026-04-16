# scrapy-2 :: tacm-rerank

query: Fix scrapy.utils.datatypes.LocalCache limit issue

## selected nodes

- rank=1 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::LocalWeakReferencedCache.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=2 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::LocalCache.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=3 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=4 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=5 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=6 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=7 layer=FUNCTION tokens=1211 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_parse.py::TestParseCommand.create_files file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_parse.py
- rank=8 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapydocs.py::issue_role file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapydocs.py
- rank=9 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py::scrapy_components_versions file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py
- rank=10 layer=FUNCTION tokens=214 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py::MemoryUsage.engine_started file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py
- rank=11 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::walk_modules_iter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py
- rank=12 layer=FUNCTION tokens=264 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.close file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=13 layer=FUNCTION tokens=372 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py::MemoryUsage._check_limit file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py
- rank=14 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/urllength.py::UrlLengthMiddleware.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/urllength.py
- rank=15 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_download_warnsize_spider_attr file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=16 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/depth.py::DepthMiddleware.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/depth.py
- rank=17 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.logger file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::LocalWeakReferencedCache.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def __init__(self, limit: int | None = None):
        super().__init__()
        self.data: LocalCache = LocalCache(limit=limit)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::LocalCache.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def __init__(self, limit: int | None = None):
        super().__init__()
        self.limit: int | None = limit

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.__new__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        # circular import
        from scrapy.http.headers import Headers  # noqa: PLC0415

        if issubclass(cls, CaselessDict) and not issubclass(cls, Headers):
            warnings.warn(
                "scrapy.utils.datatypes.CaselessDict is deprecated,"
                " please use scrapy.utils.datatypes.CaseInsensitiveDict instead",
                category=ScrapyDeprecationWarning,
                stacklevel=2,
            )
        return super().__new__(cls, *args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
    def get(self, name: _SettingsKey, default: Any = None) -> Any:
        """
        Get a setting value without affecting its original type.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        if name == "CONCURRENT_REQUESTS_PER_IP" and (
            isinstance(self[name], int) and self[name] != 0
        ):
            warnings.warn(
                "The CONCURRENT_REQUESTS_PER_IP setting is deprecated, use CONCURRENT_REQUESTS_PER_DOMAIN instead.",
                ScrapyDeprecationWarning,
                stacklevel=2,
            )

        if name == "DNS_RESOLVER":
            warnings.warn(
                "The DNS_RESOLVER setting is deprecated, please use "
                "TWISTED_DNS_RESOLVER instead.",
                ScrapyDeprecationWarning,
                stacklevel=2,
            )

        return self[name] if self[name] is not None else default

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_parse.py::TestParseCommand.create_files [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_parse.py]
    def create_files(self, proj_path: Path) -> None:
        proj_mod_path = proj_path / self.project_name
        (proj_mod_path / "spiders" / "myspider.py").write_text(
            f"""
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.test import get_from_asyncio_queue
import asyncio


class BaseSpider(scrapy.Spider):
    custom_settings = {{
        "DOWNLOAD_DELAY": 0,
    }}


class AsyncDefAsyncioReturnSpider(BaseSpider):
    name = "asyncdef_asyncio_return"

    async def parse(self, response):
        await asyncio.sleep(0.2)
        status = await get_from_asyncio_queue(response.status)
        self.logger.info(f"Got response {{status}}")
        return [{{'id': 1}}, {{'id': 2}}]

class AsyncDefAsyncioReturnSingleElementSpider(BaseSpider):
    name = "asyncdef_asyncio_return_single_element"

    async def parse(self, response):
        await asyncio.sleep(0.1)
        status = await get_from_asyncio_queue(response.status)
        self.logger.info(f"Got response {{status}}")
        return {{'foo': 42}}

class AsyncDefAsyncioGenLoopSpider(BaseSpider):
    name = "asyncdef_asyncio_gen_loop"

    async def parse(self, response):
        for i in range(10):
            await asyncio.sleep(0.1)
            yield {{'foo': i}}
        self.logger.info(f"Got response {{response.status}}")

class AsyncDefAsyncioSpider(BaseSpider):
    name = "asyncdef_asyncio"

    async def parse(self, response):
        await asyncio.sleep(0.2)
        status = await get_from_asyncio_queue(response.status)
        self.logger.debug(f"Got response {{status}}")

class AsyncDefAsyncioGenExcSpider(BaseSpider):
    name = "asyncdef_asyncio_gen_exc"

    async def parse(self, response):
        for i in range(10):
            await asyncio.sleep(0.1)
            yield {{'foo': i}}
            if i > 5:
                raise ValueError("Stopping the processing")

class CallbackSignatureDownloaderMiddleware:
    def process_request(self, request, spider):
        from inspect import signature
        spider.logger.debug(f"request.callback signature: {{signature(request.callback)}}")


class MySpider(scrapy.Spider):
    name = '{self.spider_name}'

    custom_settings = {{
        "DOWNLOADER_MIDDLEWARES": {{
            CallbackSignatureDownloaderMiddleware: 0,
        }},
        "DOWNLOAD_DELAY": 0,
    }}

    def parse(self, response):
        if getattr(self, 'test_arg', None):
            self.logger.debug('It Works!')
        return [scrapy.Item(), dict(foo='bar')]

    def parse_request_with_meta(self, response):
        foo = response.meta.get('foo', 'bar')

        if foo == 'bar':
            self.logger.debug('It Does Not Work :(')
        else:
            self.logger.debug('It Works!')

    def parse_request_with_cb_kwargs(self, response, foo=None, key=None):
        if foo == 'bar' and key == 'value':
            self.logger.debug('It Works!')
        else:
            self.logger.debug('It Does Not Work :(')

    def parse_request_without_meta(self, response):
        foo = response.meta.get('foo', 'bar')

        if foo == 'bar':
            self.logger.debug('It Works!')
        else:
            self.logger.debug('It Does Not Work :(')

class MyGoodCrawlSpider(CrawlSpider):
    name = 'goodcrawl{self.spider_name}'

    custom_settings = {{
        "DOWNLOAD_DELAY": 0,
    }}

    rules = (
        Rule(LinkExtractor(allow=r'/html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/text'), follow=True),
    )

    def parse_item(self, response):
        return [scrapy.Item(), dict(foo='bar')]

    def parse(self, response):
        return [scrapy.Item(), dict(nomatch='default')]


class MyBadCrawlSpider(CrawlSpider):
    '''Spider which doesn't define a parse_item callback while using it in a rule.'''
    name = 'badcrawl{self.spider_name}'

    custom_settings = {{
        "DOWNLOAD_DELAY": 0,
    }}

    rules = (
        Rule(LinkExtractor(allow=r'/html'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        return [scrapy.Item(), dict(foo='bar')]
""",
            encoding="utf-8",
        )

        (proj_mod_path / "pipelines.py").write_text(
            """
import logging

class MyPipeline:
    component_name = 'my_pipeline'

    def process_item(self, item):
        logging.info('It Works!')
        return item
""",
            encoding="utf-8",
        )

        with (proj_mod_path / "settings.py").open("a", encoding="utf-8") as f:
            f.write(
                f"""
ITEM_PIPELINES = {{'{self.project_name}.pipelines.MyPipeline': 1}}
"""
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapydocs.py::issue_role [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapydocs.py]
def issue_role(
    name, rawtext, text: str, lineno, inliner, options=None, content=None
) -> tuple[list[Any], list[Any]]:
    ref = "https://github.com/scrapy/scrapy/issues/" + text
    node = nodes.reference(rawtext, "issue " + text, refuri=ref)
    return [node], []

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py::scrapy_components_versions [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py]
def scrapy_components_versions() -> list[tuple[str, str]]:  # pragma: no cover
    warn(
        (
            "scrapy.utils.versions.scrapy_components_versions() is deprecated, "
            "use scrapy.utils.versions.get_versions() instead."
        ),
        ScrapyDeprecationWarning,
        stacklevel=2,
    )
    return get_versions()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py::MemoryUsage.engine_started [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py]
    def engine_started(self) -> None:
        assert self.crawler.stats
        self.crawler.stats.set_value("memusage/startup", self.get_virtual_size())
        self.tasks: list[AsyncioLoopingCall | LoopingCall] = []
        tsk = create_looping_call(self.update)
        self.tasks.append(tsk)
        tsk.start(self.check_interval, now=True)
        if self.limit:
            tsk = create_looping_call(self._check_limit)
            self.tasks.append(tsk)
            tsk.start(self.check_interval, now=True)
        if self.warning:
            tsk = create_looping_call(self._check_warning)
            self.tasks.append(tsk)
            tsk.start(self.check_interval, now=True)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::walk_modules_iter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py]
def walk_modules_iter(path: str) -> Iterable[ModuleType]:
    """Loads a module and all its submodules from the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.

    For example:
    >>> list(walk_modules_iter('scrapy.utils'))
    [<module 'scrapy.utils' from '...'>, ...]
    >>> gen = walk_modules_iter('scrapy.utils.nonexistent') # error not raised until the generator is consumed
    >>> list(gen)
    Traceback (most recent call last):
        ...
    ModuleNotFoundError: No module named 'scrapy.utils.nonexistent'
    """

    mod = import_module(path)
    yield mod
    if hasattr(mod, "__path__"):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + "." + subpath
            if ispkg:
                yield from walk_modules_iter(fullpath)
            else:
                yield import_module(fullpath)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.close [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    async def close(self) -> None:
        from twisted.internet import reactor

        d: Deferred[None] = self._pool.closeCachedConnections()
        # closeCachedConnections will hang on network or server issues, so
        # we'll manually timeout the deferred.
        #
        # Twisted issue addressing this problem can be found here:
        # https://github.com/twisted/twisted/issues/7738
        #
        # closeCachedConnections doesn't handle external errbacks, so we'll
        # issue a callback after `_disconnect_timeout` seconds.
        #
        # See also https://github.com/scrapy/scrapy/issues/2653
        delayed_call = reactor.callLater(self._disconnect_timeout, d.callback, ())

        try:
            await maybe_deferred_to_future(d)
        finally:
            if delayed_call.active():
                delayed_call.cancel()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py::MemoryUsage._check_limit [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py]
    def _check_limit(self) -> None:
        assert self.crawler.engine
        assert self.crawler.stats
        peak_mem_usage = self.get_virtual_size()
        if peak_mem_usage > self.limit:
            self.crawler.stats.set_value("memusage/limit_reached", 1)
            mem = self.limit / 1024 / 1024
            logger.error(
                "Memory usage exceeded %(memusage)dMiB. Shutting down Scrapy...",
                {"memusage": mem},
                extra={"crawler": self.crawler},
            )
            if self.notify_mails:
                subj = (
                    f"{self.crawler.settings['BOT_NAME']} terminated: "
                    f"memory usage exceeded {mem}MiB at {socket.gethostname()}"
                )
                self._send_report(self.notify_mails, subj)
                self.crawler.stats.set_value("memusage/limit_notified", 1)

            if self.crawler.engine.spider is not None:
                _schedule_coro(
                    self.crawler.engine.close_spider_async(reason="memusage_exceeded")
                )
            else:
                _schedule_coro(self.crawler.stop_async())
        else:
            logger.info(
                "Peak memory usage is %(virtualsize)dMiB",
                {"virtualsize": peak_mem_usage / 1024 / 1024},
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/urllength.py::UrlLengthMiddleware.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/urllength.py]
    def from_crawler(cls, crawler: Crawler) -> Self:
        maxlength = crawler.settings.getint("URLLENGTH_LIMIT")
        if not maxlength:
            raise NotConfigured
        o = cls(maxlength)
        o.crawler = crawler
        return o

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_download_warnsize_spider_attr [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py]
    def _test_download_warnsize_spider_attr(self, compression_id):
        class DownloadWarnSizeSpider(Spider):
            download_warnsize = 10_000_000

        crawler = get_crawler(DownloadWarnSizeSpider)
        spider = crawler._create_spider("scrapytest.org")
        mw = HttpCompressionMiddleware.from_crawler(crawler)
        mw.open_spider(spider)
        response = self._getresponse(f"bomb-{compression_id}")

        with LogCapture(
            "scrapy.downloadermiddlewares.httpcompression",
            propagate=False,
            level=WARNING,
        ) as log:
            mw.process_response(response.request, response)
        log.check(
            (
                "scrapy.downloadermiddlewares.httpcompression",
                "WARNING",
                (
                    "<200 http://scrapytest.org/> body size after "
                    "decompression (11511612 B) is larger than the download "
                    "warning size (10000000 B)."
                ),
            ),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/depth.py::DepthMiddleware.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/depth.py]
    def from_crawler(cls, crawler: Crawler) -> Self:
        settings = crawler.settings
        maxdepth = settings.getint("DEPTH_LIMIT")
        verbose = settings.getbool("DEPTH_STATS_VERBOSE")
        prio = settings.getint("DEPTH_PRIORITY")
        assert crawler.stats
        o = cls(maxdepth, crawler.stats, verbose, prio)
        o.crawler = crawler
        return o

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.logger [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py]
    def logger(self) -> SpiderLoggerAdapter:
        # circular import
        from scrapy.utils.log import SpiderLoggerAdapter  # noqa: PLC0415

        logger = logging.getLogger(self.name)
        return SpiderLoggerAdapter(logger, {"spider": self})
```

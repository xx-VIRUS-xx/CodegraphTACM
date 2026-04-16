# scrapy-30 :: tacm-full

query: PY3 fix test cmdline

## selected nodes

- rank=1 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py::TestCmdline.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py
- rank=2 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.process_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=3 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=4 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=5 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py::TestFTPFeedStorage.get_test_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py
- rank=6 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py::TestBlockingFeedStorage.get_test_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py
- rank=7 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=8 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=9 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::NotGeneratorCallbackSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=10 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py::TestMain._test_start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py
- rank=11 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::GeneratorCallbackSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=12 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/utils/cmdline.py::call file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/utils/cmdline.py
- rank=13 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::AsyncGeneratorCallbackSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=14 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py::TestMain._test_sleep file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py
- rank=15 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline_crawl_with_pipeline/__init__.py::TestCmdlineCrawlPipeline._execute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline_crawl_with_pipeline/__init__.py
- rank=16 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::spider_loader_env file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py
- rank=17 layer=FUNCTION tokens=487 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_header_redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=18 layer=FUNCTION tokens=1211 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_parse.py::TestParseCommand.create_files file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_parse.py
- rank=19 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.f file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=20 layer=FUNCTION tokens=232 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestProcessStartSimple._get_processed_start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py
- rank=21 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pqueues.py::QueueProtocol.close file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pqueues.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py::TestCmdline.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py]
    def setup_method(self):
        self.env = get_testenv()
        tests_path = Path(__file__).parent.parent
        self.env["PYTHONPATH"] += os.pathsep + str(tests_path.parent)
        self.env["SCRAPY_SETTINGS_MODULE"] = "tests.test_cmdline.settings"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.process_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py]
    def process_options(self, args: list[str], opts: argparse.Namespace) -> None:
        assert self.settings is not None
        try:
            self.settings.setdict(arglist_to_dict(opts.set), priority="cmdline")
        except ValueError:
            raise UsageError(
                "Invalid -s value, use -s NAME=VALUE", print_help=False
            ) from None

        if opts.logfile:
            self.settings.set("LOG_ENABLED", True, priority="cmdline")
            self.settings.set("LOG_FILE", opts.logfile, priority="cmdline")

        if opts.loglevel:
            self.settings.set("LOG_ENABLED", True, priority="cmdline")
            self.settings.set("LOG_LEVEL", opts.loglevel, priority="cmdline")

        if opts.nolog:
            self.settings.set("LOG_ENABLED", False, priority="cmdline")

        if opts.pidfile:
            Path(opts.pidfile).write_text(
                str(os.getpid()) + os.linesep, encoding="utf-8"
            )

        if opts.pdb:
            failure.startDebugMode()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py]
    def __init__(self) -> None:
        self.settings: Settings | None = None  # set in scrapy.cmdline

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py::TestFTPFeedStorage.get_test_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py]
    def get_test_spider(self, settings=None):
        class TestSpider(scrapy.Spider):
            name = "test_spider"

        crawler = get_crawler(settings_dict=settings)
        return TestSpider.from_crawler(crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py::TestBlockingFeedStorage.get_test_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py]
    def get_test_spider(self, settings=None):
        class TestSpider(scrapy.Spider):
            name = "test_spider"

        crawler = get_crawler(settings_dict=settings)
        return TestSpider.from_crawler(crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::NotGeneratorCallbackSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    def parse(self, response):
        return [{"test": 1}, {"test": 1 / 0}]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py::TestMain._test_start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py]
    async def _test_start(self, start_, expected_items=None):
        class TestSpider(Spider):
            name = "test"
            start = start_

        await self._test_spider(TestSpider, expected_items)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::GeneratorCallbackSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    def parse(self, response):
        yield {"test": 1}
        yield {"test": 2}
        raise ImportError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/utils/cmdline.py::call [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/utils/cmdline.py]
def call(*args: str, **popen_kwargs: Any) -> int:
    args = (sys.executable, "-m", "scrapy.cmdline", *args)
    return subprocess.call(
        args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=get_testenv(),
        **popen_kwargs,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::AsyncGeneratorCallbackSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    async def parse(self, response):
        yield {"test": 1}
        yield {"test": 2}
        raise ImportError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py::TestMain._test_sleep [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py]
    async def _test_sleep(self, spider_middlewares):
        class TestSpider(Spider):
            name = "test"

            async def start(self):
                yield ITEM_A

        await self._test(spider_middlewares, TestSpider, [ITEM_A])

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline_crawl_with_pipeline/__init__.py::TestCmdlineCrawlPipeline._execute [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline_crawl_with_pipeline/__init__.py]
    def _execute(self, spname):
        args = (sys.executable, "-m", "scrapy.cmdline", "crawl", spname)
        cwd = Path(__file__).resolve().parent
        proc = Popen(args, stdout=PIPE, stderr=PIPE, cwd=cwd)
        _, stderr = proc.communicate()
        return proc.returncode, stderr

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::spider_loader_env [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py]
def spider_loader_env(tmp_path):
    orig_spiders_dir = module_dir / "test_spiders"
    spiders_dir = tmp_path / "test_spiders_xxx"
    _copytree(orig_spiders_dir, spiders_dir)
    sys.path.append(str(tmp_path))
    settings = Settings({"SPIDER_MODULES": ["test_spiders_xxx"]})

    yield settings, spiders_dir

    sys.modules.pop("test_spiders_xxx", None)
    sys.path.remove(str(tmp_path))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_header_redirect [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def _test_cookie_header_redirect(
        self,
        source,
        target,
        *,
        cookies2,
    ):
        """Test the handling of a user-defined Cookie header when building a
        redirect follow-up request.

        We follow RFC 6265 for cookie handling. The Cookie header can only
        contain a list of key-value pairs (i.e. no additional cookie
        parameters like Domain or Path). Because of that, we follow the same
        rules that we would follow for the handling of the Set-Cookie response
        header when the Domain is not set: the cookies must be limited to the
        target URL domain (not even subdomains can receive those cookies).

        .. note:: This method tests the scenario where the cookie middleware is
                  disabled. Because of known issue #1992, when the cookies
                  middleware is enabled we do not need to be concerned about
                  the Cookie header getting leaked to unintended domains,
                  because the middleware empties the header from every request.
        """
        if not isinstance(source, dict):
            source = {"url": source}
        if not isinstance(target, dict):
            target = {"url": target}
        target.setdefault("status", 301)

        request1 = Request(headers={"Cookie": b"a=b"}, **source)

        response = Response(
            headers={
                "Location": target["url"],
            },
            **target,
        )

        request2 = self.redirect_middleware.process_response(request1, response)
        assert isinstance(request2, Request)

        cookies = request2.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies2 else None)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.f [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py]
                def f(self):
                    # For rationale of this see:
                    # https://github.com/python/cpython/blob/ee1a81b77444c6715cbe610e951c655b6adab88b/Lib/test/test_super.py#L222
                    return __class__

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestProcessStartSimple._get_processed_start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py]
    async def _get_processed_start(
        self, *mw_classes: type[Any]
    ) -> AsyncIterator[Any] | None:
        class TestSpider(Spider):
            name = "test"

            async def start(self):
                for i in range(2):
                    yield Request(f"https://example.com/{i}", dont_filter=True)
                yield {"name": "test item"}

        setting = self._construct_mw_setting(*mw_classes)
        self.crawler = get_crawler(
            TestSpider, {"SPIDER_MIDDLEWARES_BASE": {}, "SPIDER_MIDDLEWARES": setting}
        )
        self.crawler.spider = self.crawler._create_spider()
        self.mwman = SpiderMiddlewareManager.from_crawler(self.crawler)
        return await self.mwman.process_start()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pqueues.py::QueueProtocol.close [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pqueues.py]
    def close(self) -> None: ...
```

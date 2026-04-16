# scrapy-39 :: tacm-full

query: fix make_requests_from_url deprcation implementation, add tests

## selected nodes

- rank=1 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=2 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py
- rank=3 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::add_http_if_no_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=4 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=5 layer=FUNCTION tokens=399 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=6 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py
- rank=7 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py::load_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py
- rank=8 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py
- rank=9 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::guess_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=10 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::RedirectedMediaDownloadSpider._process_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py
- rank=11 layer=FUNCTION tokens=242 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py
- rank=12 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py::TestCmdline.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py
- rank=13 layer=FUNCTION tokens=297 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.scraped_data file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=14 layer=FUNCTION tokens=356 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager.process_start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=15 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::pytest_configure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py
- rank=16 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/utils/__init__.py::get_script_run_env file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/utils/__init__.py
- rank=17 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=18 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py::H2ClientProtocol._send_pending_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py
- rank=19 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=20 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.from_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=21 layer=FUNCTION tokens=583 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=22 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_downloaded_responses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-l",
            "--list",
            dest="list",
            action="store_true",
            help="only list contracts, without checking them",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            default=False,
            action="store_true",
            help="print contract tests for all spiders",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::add_http_if_no_scheme [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py]
def add_http_if_no_scheme(url: str) -> str:
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.IGNORECASE)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def add_requests(self, lvl: int, new_reqs: list[Request]) -> None:
        old_reqs = self.requests.get(lvl, [])
        self.requests[lvl] = old_reqs + new_reqs

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py]
    def _extract_links(
        self,
        selector: Selector,
        response_url: str,
        response_encoding: str,
        base_url: str,
    ) -> list[Link]:
        links: list[Link] = []
        # hacky way to get the underlying lxml parsed document
        for el, _, attr_val in self._iter_links(selector.root):
            # pseudo lxml.html.HtmlElement.make_links_absolute(base_url)
            try:
                if self.strip:
                    attr_val = strip_html5_whitespace(attr_val)  # noqa: PLW2901 this is intended
                attr_val = urljoin(base_url, attr_val)  # noqa: PLW2901
            except ValueError:
                continue  # skipping bogus links
            else:
                url = self.process_attr(attr_val)
                if url is None:
                    continue
            try:
                url = safe_url_string(url, encoding=response_encoding)
            except ValueError:
                logger.debug(f"Skipping extraction of link with bad URL {url!r}")
                continue

            # to fix relative links after process_value
            url = urljoin(response_url, url)
            link = Link(
                url,
                _collect_string_content(el) or "",
                nofollow=rel_has_nofollow(el.get("rel")),
            )
            links.append(link)
        return self._deduplicate_if_needed(links)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py]
    def make_request(index, data):
        meta = {}
        if data.get("start", False):
            meta["is_start_request"] = True
        return Request(
            url=make_url(index),
            priority=data.get("priority", 0),
            meta=meta,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py::load_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py]
def load_response(url: str, filename: str) -> HtmlResponse:
    input_path = Path(__file__).parent / "_tests" / filename
    return HtmlResponse(url, body=input_path.read_bytes())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py]
    def make_url(index):
        return f"https://toscrape.com/{index}"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::guess_scheme [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py]
def guess_scheme(url: str) -> str:
    """Add an URL scheme if missing: file:// for filepath-like input or
    http:// otherwise."""
    if _is_filesystem_path(url):
        return _any_to_uri(url)
    return add_http_if_no_scheme(url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::RedirectedMediaDownloadSpider._process_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py]
    def _process_url(self, url):
        return add_or_replace_parameter(
            self.mockserver.url("/redirect-to"), "goto", url
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.start_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py]
    def start_requests(self) -> Iterable[Any]:
        warnings.warn(
            (
                "The Spider.start_requests() method is deprecated, use "
                "Spider.start() instead. If you are calling "
                "super().start_requests() from a Spider.start() override, "
                "iterate super().start() instead."
            ),
            ScrapyDeprecationWarning,
            stacklevel=2,
        )
        if not self.start_urls and hasattr(self, "start_url"):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)"
            )
        for url in self.start_urls:
            yield Request(url, dont_filter=True)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py::TestCmdline.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py]
    def setup_method(self):
        self.env = get_testenv()
        tests_path = Path(__file__).parent.parent
        self.env["PYTHONPATH"] += os.pathsep + str(tests_path.parent)
        self.env["SCRAPY_SETTINGS_MODULE"] = "tests.test_cmdline.settings"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.scraped_data [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def scraped_data(
        self,
        args: tuple[
            list[Any], list[Request], argparse.Namespace, int, Spider, CallbackT
        ],
    ) -> list[Any]:
        items, requests, opts, depth, spider, callback = args
        if opts.pipelines:
            assert self.pcrawler.engine
            itemproc = self.pcrawler.engine.scraper.itemproc
            if hasattr(itemproc, "process_item_async"):
                for item in items:
                    _schedule_coro(itemproc.process_item_async(item))
            else:
                for item in items:
                    itemproc.process_item(item, spider)
        self.add_items(depth, items)
        self.add_requests(depth, requests)

        scraped_data = items if opts.output else []
        if depth < opts.depth:
            for req in requests:
                req.meta["_depth"] = depth + 1
                req.meta["_callback"] = req.callback
                req.callback = callback
            scraped_data += requests

        return scraped_data

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager.process_start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py]
    async def process_start(
        self, spider: Spider | None = None
    ) -> AsyncIterator[Any] | None:
        if spider:
            if self.crawler:
                msg = (
                    "Passing a spider argument to SpiderMiddlewareManager.process_start() is deprecated"
                    " and the passed value is ignored."
                )
            else:
                msg = (
                    "Passing a spider argument to SpiderMiddlewareManager.process_start() is deprecated,"
                    " SpiderMiddlewareManager should be instantiated with a Crawler instance instead."
                )
            warn(msg, category=ScrapyDeprecationWarning, stacklevel=2)
            self._set_compat_spider(spider)
        self._check_deprecated_start_requests_use()
        if self._use_start_requests:
            sync_start = iter(self._spider.start_requests())
            sync_start = await self._process_chain(
                "process_start_requests", sync_start, always_add_spider=True
            )
            start: AsyncIterator[Any] = as_async_generator(sync_start)
        else:
            start = self._spider.start()
            start = await self._process_chain("process_start", start)
        return start

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::pytest_configure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py]
def pytest_configure(config):
    if config.getoption("--reactor") == "asyncio":
        # Needed on Windows to switch from proactor to selector for Twisted reactor compatibility.
        # If we decide to run tests with both, we will need to add a new option and check it here.
        set_asyncio_event_loop_policy()
    elif config.getoption("--reactor") == "none":
        install_reactor_import_hook()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/utils/__init__.py::get_script_run_env [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/utils/__init__.py]
def get_script_run_env() -> dict[str, str]:
    """Return a OS environment dict suitable to run scripts shipped with tests."""

    tests_path = Path(__file__).parent.parent
    pythonpath = str(tests_path) + os.pathsep + os.environ.get("PYTHONPATH", "")
    env = os.environ.copy()
    env["PYTHONPATH"] = pythonpath
    return env

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    def parse(self, response):
        self.parsed.add(response.url[-3:])

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py::H2ClientProtocol._send_pending_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py]
    def _send_pending_requests(self) -> None:
        """Initiate all pending requests from the deque following FIFO
        We make sure that at any time {allowed_max_concurrent_streams}
        streams are active.
        """
        while (
            self._pending_request_stream_pool
            and self.metadata["active_streams"] < self.allowed_max_concurrent_streams
            and self.h2_connected
        ):
            self.metadata["active_streams"] += 1
            stream = self._pending_request_stream_pool.popleft()
            stream.initiate_request()
            self._write_to_transport()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def start_requests(self) -> Iterable[Request]:
        for url in self.sitemap_urls:
            yield Request(url, self._parse_sitemap)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.from_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py]
    def from_spider(self, spider: Spider, results: TestResult) -> list[Request | None]:
        requests: list[Request | None] = []
        for method in self.tested_methods_from_spidercls(type(spider)):
            bound_method = spider.__getattribute__(method)
            try:
                requests.append(self.from_method(bound_method, results))
            except Exception:
                case = _create_testcase(bound_method, "contract")
                results.addError(case, sys.exc_info())

        return requests

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "--spider",
            dest="spider",
            default=None,
            help="use this spider without looking for one",
        )
        parser.add_argument(
            "--pipelines", action="store_true", help="process items through pipelines"
        )
        parser.add_argument(
            "--nolinks",
            dest="nolinks",
            action="store_true",
            help="don't show links to follow (extracted requests)",
        )
        parser.add_argument(
            "--noitems",
            dest="noitems",
            action="store_true",
            help="don't show scraped items",
        )
        parser.add_argument(
            "--nocolour",
            dest="nocolour",
            action="store_true",
            help="avoid using pygments to colorize the output",
        )
        parser.add_argument(
            "-r",
            "--rules",
            dest="rules",
            action="store_true",
            help="use CrawlSpider rules to discover the callback",
        )
        parser.add_argument(
            "-c",
            "--callback",
            dest="callback",
            help="use this callback for parsing, instead looking for a callback",
        )
        parser.add_argument(
            "-m",
            "--meta",
            dest="meta",
            help="inject extra meta into the Request, it must be a valid raw json string",
        )
        parser.add_argument(
            "--cbkwargs",
            dest="cbkwargs",
            help="inject extra callback kwargs into the Request, it must be a valid raw json string",
        )
        parser.add_argument(
            "-d",
            "--depth",
            dest="depth",
            type=int,
            default=1,
            help="maximum depth for parsing requests [default: %(default)s]",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            action="store_true",
            help="print each depth level one by one",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_downloaded_responses [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py]
    def _assert_downloaded_responses(run: CrawlerRun, count: int) -> None:
        # response tests
        assert len(run.respplug) == count
        assert len(run.reqreached) == count

        for response, _ in run.respplug:
            if run.getpath(response.url) == "/static/item999.html":
                assert response.status == 404
            if run.getpath(response.url) == "/redirect":
                assert response.status == 302
```

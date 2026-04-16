# scrapy-39 :: tacm

query: fix make_requests_from_url deprcation implementation, add tests

## selected nodes

- rank=1 layer=FILE tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=2 layer=FILE tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=3 layer=FILE tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py
- rank=4 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py
- rank=5 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=6 layer=CLASS tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=7 layer=CLASS tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py::TestRequest file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py
- rank=8 layer=CLASS tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=9 layer=CLASS tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=10 layer=CLASS tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=11 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::PostDataJsonMixin file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=12 layer=CLASS tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_middleware.py::MyMiddlewareManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_middleware.py
- rank=13 layer=CLASS tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scheduler.py::BaseScheduler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scheduler.py
- rank=14 layer=CLASS tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::TestItem.C file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=15 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=16 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::add_http_if_no_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=17 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=18 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::guess_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=19 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager.process_start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=20 layer=FUNCTION tokens=257 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.scraped_data file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=21 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::pytest_configure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py
- rank=22 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._check_deprecated_start_requests_use file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=23 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=24 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py
- rank=25 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.make_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=26 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.print_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=27 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::url_is_from_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=28 layer=FUNCTION tokens=326 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._add_middleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=29 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._check_deprecated_process_start_requests_use file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=30 layer=FUNCTION tokens=320 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.add_cookie_header file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=31 layer=FUNCTION tokens=351 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=32 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py::__getattr__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py
- rank=33 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py
- rank=34 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=35 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.syntax file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py

## context

```text
file scrapy/utils/url.py
imports: __future__, re, warnings, importlib, typing, urllib, w3lib, scrapy
defines: __getattr__, url_is_from_any_domain, _spider_domains, url_is_from_spider, url_has_any_extension, escape_ajax, add_http_if_no_scheme, _is_posix_path, _is_windows_path, _is_filesystem_path, guess_scheme, strip_url

file http/response/text.py
imports: __future__, json, contextlib, typing, urllib, parsel, w3lib, scrapy
defines: TextResponse, _InvalidSelector, _url_from_selector

file CodegraphTACM/scrapy/conftest.py
imports: __future__, importlib, pathlib, typing, pytest, twisted, scrapy, tests
defines: _py_files, pytest_addoption, mockserver, reactor_pytest, pytest_configure, pytest_runtest_setup

file scrapy/settings/default_settings.py
imports: sys, importlib, pathlib
defines: __getattr__

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

class Command(BaseRunSpiderCommand):  [scrapy/commands/parse.py:38]
methods: _get_callback, _get_items_and_requests, add_items
         add_options, add_requests, callback
         get_callback_from_rules, handle_exception
         iterate_spider_output, iterate_spider_output
         iterate_spider_output, max_level, prepare_request
         print_items, print_requests, print_results
         process_options, process_request_cb_kwargs
         process_request_meta, run, run_callback
         scraped_data, set_spidercls, short_desc, start
         start_parsing, syntax

class TestRequest:  [scrapy/tests/test_http_request.py:12]
methods: a_function, somecallback, test_body
         test_callback_and_errback
         test_callback_and_errback_type, test_copy
         test_copy_inherited_classes, test_eq
         test_from_curl
         test_from_curl_ignore_unknown_options
         test_from_curl_with_kwargs, test_headers
         test_immutable_attributes, test_init
         test_method_always_str, test_no_callback
         test_replace, test_setter_mutable_lazy_loading
         test_setters, test_url, test_url_encoding
         test_url_encoding_nonutf8_untouched
         test_url_encoding_other, test_url_encoding_query
         test_url_encoding_query_latin1
         test_url_no_scheme, test_url_quoting
         test_url_scheme

class CookieJar:  [scrapy/http/cookies.py:27]
methods: _cookies, add_cookie_header, clear, clear_session_cookies
         extract_cookies, make_cookies, set_cookie
         set_cookie_if_ok, set_policy, __init__, __iter__
         __len__

class SpiderMiddlewareManager(MiddlewareManager):  [scrapy/core/spidermw.py:54]
methods: _add_middleware
         _check_deprecated_process_start_requests_use
         _check_deprecated_start_requests_use
         _evaluate_iterable, _get_async_method_pair
         _get_mwlist_from_settings
         _process_callback_output
         _process_spider_exception, _process_spider_input
         _process_spider_output, process_async
         process_callback_output, process_spider_exception
         process_start, process_sync, scrape_func_wrapped
         scrape_response, scrape_response_async, __init__

class CrawlSpider(Spider):  [scrapy/spiders/crawl.py:95]
methods: _build_request, _callback, _compile_rules, _errback
         _handle_failure, _parse, _parse_response
         _requests_to_follow, from_crawler
         parse_start_url, parse_with_rules
         process_results, __init__

class PostDataJsonMixin:  [scrapy/tests/test_http2_client_protocol.py:102]
methods: make_response

class MyMiddlewareManager(MiddlewareManager):  [scrapy/tests/test_middleware.py:51]
methods: _add_middleware, _get_mwlist_from_settings

class BaseScheduler(metaclass=BaseSchedulerMeta):  [scrapy/core/scheduler.py:55]
methods: close, enqueue_request, from_crawler, has_pending_requests
         next_request, open

class C:  [scrapy/tests/test_item.py:220]
methods: —

    def add_requests(self, lvl: int, new_reqs: list[Request]) -> None:
        old_reqs = self.requests.get(lvl, [])
        self.requests[lvl] = old_reqs + new_reqs

def add_http_if_no_scheme(url: str) -> str:
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.IGNORECASE)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url

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

def guess_scheme(url: str) -> str:
    """Add an URL scheme if missing: file:// for filepath-like input or
    http:// otherwise."""
    if _is_filesystem_path(url):
        return _any_to_uri(url)
    return add_http_if_no_scheme(url)

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

def pytest_configure(config):
    if config.getoption("--reactor") == "asyncio":
        # Needed on Windows to switch from proactor to selector for Twisted reactor compatibility.
        # If we decide to run tests with both, we will need to add a new option and check it here.
        set_asyncio_event_loop_policy()
    elif config.getoption("--reactor") == "none":
        install_reactor_import_hook()

    def _check_deprecated_start_requests_use(self) -> None:
        start_requests_cls = None
        start_cls = None
        spidercls = self._spider.__class__
        mro = spidercls.__mro__

        for cls in mro:
            cls_dict = cls.__dict__
            if start_requests_cls is None and "start_requests" in cls_dict:
                start_requests_cls = cls
            if start_cls is None and "start" in cls_dict:
                start_cls = cls
    # ... truncated

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
    # ... truncated

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

    def make_cookies(self, response: Response, request: Request) -> Sequence[Cookie]:
        wreq = WrappedRequest(request)
        wrsp = WrappedResponse(response)
        return self.jar.make_cookies(wrsp, wreq)  # type: ignore[arg-type]

    def print_requests(self, lvl: int | None = None, colour: bool = True) -> None:
        if lvl is not None:
            requests = self.requests.get(lvl, [])
        elif self.requests:
            requests = self.requests[max(self.requests)]
        else:
            requests = []

        print("# Requests ", "-" * 65)
        display.pprint(requests, colorize=colour)

def url_is_from_spider(url: UrlT, spider: type[Spider]) -> bool:
    """Return True if the url belongs to the given spider"""
    return url_is_from_any_domain(url, _spider_domains(spider))

    def _add_middleware(self, mw: Any) -> None:
        if hasattr(mw, "process_spider_input"):
            self.methods["process_spider_input"].append(mw.process_spider_input)
            self._check_mw_method_spider_arg(mw.process_spider_input)

        if self._use_start_requests:
            if hasattr(mw, "process_start_requests"):
                self.methods["process_start_requests"].appendleft(
                    mw.process_start_requests
                )
        elif hasattr(mw, "process_start"):
            self.methods["process_start"].appendleft(mw.process_start)

        process_spider_output = self._get_async_method_pair(mw, "process_spider_output")
        self.methods["process_spider_output"].appendleft(process_spider_output)
        if callable(process_spider_output):
            self._check_mw_method_spider_arg(process_spider_output)
        elif isinstance(process_spider_output, tuple):
            for m in process_spider_output:
                self._check_mw_method_spider_arg(m)

        process_spider_exception = getattr(mw, "process_spider_exception", None)
        self.methods["process_spider_exception"].appendleft(process_spider_exception)
        if process_spider_exception is not None:
            self._check_mw_method_spider_arg(process_spider_exception)

    def _check_deprecated_process_start_requests_use(
        self, middlewares: tuple[Any, ...]
    ) -> None:
        deprecated_middlewares = [
            middleware
            for middleware in middlewares
            if hasattr(middleware, "process_start_requests")
            and not hasattr(middleware, "process_start")
        ]
        modern_middlewares = [
            middleware
            for middleware in middlewares
    # ... truncated

    def add_cookie_header(self, request: Request) -> None:
        wreq = WrappedRequest(request)
        self.policy._now = self.jar._now = int(time.time())  # type: ignore[attr-defined]

        # the cookiejar implementation iterates through all domains
        # instead we restrict to potential matches on the domain
        req_host = urlparse_cached(request).hostname
        if not req_host:
            return

        if not IPV4_RE.search(req_host):
            hosts = potential_domain_matches(req_host)
            if "." not in req_host:
                hosts.append(req_host + ".local")
        else:
            hosts = [req_host]

        cookies = []
        for host in hosts:
            if host in self.jar._cookies:  # type: ignore[attr-defined]
                cookies.extend(self.jar._cookies_for_domain(host, wreq))  # type: ignore[attr-defined]

        attrs = self.jar._cookie_attrs(cookies)  # type: ignore[attr-defined]
        if attrs and not wreq.has_header("Cookie"):
            wreq.add_unredirected_header("Cookie", "; ".join(attrs))

        self.processed += 1
        if self.processed % self.check_expired_frequency == 0:
            # This is still quite inefficient for large number of cookies
            self.jar.clear_expired_cookies()

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

def __getattr__(name: str):
    if name == "CONCURRENT_REQUESTS_PER_IP":
        import warnings  # noqa: PLC0415

        from scrapy.exceptions import ScrapyDeprecationWarning  # noqa: PLC0415

        warnings.warn(
            "The scrapy.settings.default_settings.CONCURRENT_REQUESTS_PER_IP attribute is deprecated, use scrapy.settings.default_settings.CONCURRENT_REQUESTS_PER_DOMAIN instead.",
            ScrapyDeprecationWarning,
            stacklevel=2,
        )
        return 0

    raise AttributeError

    def make_request(index, data):
        meta = {}
        if data.get("start", False):
            meta["is_start_request"] = True
        return Request(
            url=make_url(index),
            priority=data.get("priority", 0),
            meta=meta,
        )

    def url(self) -> str:
        return self._url

    def syntax(self) -> str:
        return "[options] <url>"
```

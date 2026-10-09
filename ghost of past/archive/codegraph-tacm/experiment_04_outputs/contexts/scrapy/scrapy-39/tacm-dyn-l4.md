# scrapy-39 :: tacm-dyn-l4

query: fix make_requests_from_url deprcation implementation, add tests

## selected nodes

- rank=1 layer=FILE tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=2 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=3 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::add_http_if_no_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=4 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::guess_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=5 layer=CLASS tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=6 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=7 layer=FUNCTION tokens=257 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.scraped_data file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=8 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=9 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py
- rank=10 layer=CLASS tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py::TestRequest file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py
- rank=11 layer=CLASS tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=12 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.make_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=13 layer=FUNCTION tokens=320 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.add_cookie_header file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=14 layer=FUNCTION tokens=351 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=15 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py
- rank=16 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=17 layer=CLASS tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=18 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager.process_start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=19 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._check_deprecated_start_requests_use file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=20 layer=CLASS tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=21 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._requests_to_follow file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=22 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py::load_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py
- rank=23 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=24 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::PostDataJsonMixin file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=25 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py
- rank=26 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py
- rank=27 layer=CLASS tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_startproject.py::TestStartprojectTemplates file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_startproject.py
- rank=28 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_startproject.py::TestStartprojectTemplates._make_read_only file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_startproject.py
- rank=29 layer=CLASS tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_middleware.py::MyMiddlewareManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_middleware.py
- rank=30 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py::H2ClientProtocol._send_pending_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py
- rank=31 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::RedirectedMediaDownloadSpider._process_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py
- rank=32 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=33 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=34 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::url_is_from_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=35 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=36 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py::UniversalWrapSpiderMiddleware.process_start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py
- rank=37 layer=FUNCTION tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py::TestRequest.a_function file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py

## context

```text
file scrapy/utils/url.py
imports: __future__, re, warnings, importlib, typing, urllib, w3lib, scrapy
defines: __getattr__, url_is_from_any_domain, _spider_domains, url_is_from_spider, url_has_any_extension, escape_ajax, add_http_if_no_scheme, _is_posix_path, _is_windows_path, _is_filesystem_path, guess_scheme, strip_url

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

def add_http_if_no_scheme(url: str) -> str:
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.IGNORECASE)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url

def guess_scheme(url: str) -> str:
    """Add an URL scheme if missing: file:// for filepath-like input or
    http:// otherwise."""
    if _is_filesystem_path(url):
        return _any_to_uri(url)
    return add_http_if_no_scheme(url)

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

    def add_requests(self, lvl: int, new_reqs: list[Request]) -> None:
        old_reqs = self.requests.get(lvl, [])
        self.requests[lvl] = old_reqs + new_reqs

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

    def make_cookies(self, response: Response, request: Request) -> Sequence[Cookie]:
        wreq = WrappedRequest(request)
        wrsp = WrappedResponse(response)
        return self.jar.make_cookies(wrsp, wreq)  # type: ignore[arg-type]

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

    def make_request(index, data):
        meta = {}
        if data.get("start", False):
            meta["is_start_request"] = True
        return Request(
            url=make_url(index),
            priority=data.get("priority", 0),
            meta=meta,
        )

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

class CrawlSpider(Spider):  [scrapy/spiders/crawl.py:95]
methods: _build_request, _callback, _compile_rules, _errback
         _handle_failure, _parse, _parse_response
         _requests_to_follow, from_crawler
         parse_start_url, parse_with_rules
         process_results, __init__

    def _requests_to_follow(self, response: Response) -> Iterable[Request | None]:
        if not isinstance(response, HtmlResponse):
            return
        seen: set[Link] = set()
        for rule_index, rule in enumerate(self._rules):
            links: list[Link] = [
                lnk
                for lnk in rule.link_extractor.extract_links(response)
                if lnk not in seen
            ]
            for link in cast("ProcessLinksT", rule.process_links)(links):
                seen.add(link)
                request = self._build_request(rule_index, link)
                yield cast("ProcessRequestT", rule.process_request)(request, response)

def load_response(url: str, filename: str) -> HtmlResponse:
    input_path = Path(__file__).parent / "_tests" / filename
    return HtmlResponse(url, body=input_path.read_bytes())

    def url(self) -> str:
        return self._url

class PostDataJsonMixin:  [scrapy/tests/test_http2_client_protocol.py:102]
methods: make_response

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

    def make_url(index):
        return f"https://toscrape.com/{index}"

class TestStartprojectTemplates:  [scrapy/tests/test_command_startproject.py:108]
methods: _make_read_only
         test_startproject_permissions_from_read_only
         test_startproject_permissions_from_writable
         test_startproject_permissions_umask_022
         test_startproject_permissions_unchanged_in_destination
         test_startproject_template_override, umask

        def _make_read_only(path: Path):
            current_permissions = path.stat().st_mode
            path.chmod(current_permissions & ~ANYONE_WRITE_PERMISSION)

class MyMiddlewareManager(MiddlewareManager):  [scrapy/tests/test_middleware.py:51]
methods: _add_middleware, _get_mwlist_from_settings

    def _process_url(self, url):
        return add_or_replace_parameter(
            self.mockserver.url("/redirect-to"), "goto", url
        )

# --- Layer 04: Variable context ---
# call-chain context
  called by: _get_agent [http11.py]
  called by: guess_scheme [url.py]

# call-chain context
  called by: run [shell.py]

# call-chain context
  called by: scraped_data [parse.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: execute [cmdline.py]
  called by: setup_method [test_commands.py]

# call-chain context
  called by: process_response [cookies.py]
  called by: _get_request_cookies [cookies.py]

# call-chain context
  called by: process_request [cookies.py]

# call-chain context
  called by: extract_links [lxmlhtml.py]
  called by: _extract_links [lxmlhtml.py]

# call-chain context
  called by: execute [cmdline.py]
  called by: setup_method [test_commands.py]

# call-chain context
  called by: open_spider_async [engine.py]

# call-chain context
  called by: process_start [spidermw.py]

# call-chain context
  called by: parse_with_rules [crawl.py]

# call-chain context
  called by: __init__ [spiders.py]
  called by: start [spiders.py]

# call-chain context
  called by: process_start [spidermw.py]
  called by: start [__init__.py]

# call-chain context
  called by: make_request [test_pqueues.py]

```

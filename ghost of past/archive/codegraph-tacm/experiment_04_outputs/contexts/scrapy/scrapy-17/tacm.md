# scrapy-17 :: tacm

query: response_status_message should not fail on non-standard HTTP codes

## selected nodes

- rank=1 layer=FILE tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=2 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=3 layer=FILE tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/html.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/html.py
- rank=4 layer=FILE tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/xml.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/xml.py
- rank=5 layer=FILE tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/json.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/json.py
- rank=6 layer=FILE tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py
- rank=7 layer=FILE tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py
- rank=8 layer=CLASS tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestScrapyHTTPPageGetter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=9 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=10 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/html.py::HtmlResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/html.py
- rank=11 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/json.py::JsonResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/json.py
- rank=12 layer=CLASS tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/xml.py::XmlResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/xml.py
- rank=13 layer=CLASS tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=14 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::Status file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=15 layer=CLASS tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=16 layer=CLASS tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=17 layer=CLASS tokens=255 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpBase file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py
- rank=18 layer=CLASS tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_deprecate.py::TestWarnWhenSubclassed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_deprecate.py
- rank=19 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=20 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::response_status_message file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=21 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_fail file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=22 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory.gotStatus file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=23 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=24 layer=FUNCTION tokens=359 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=25 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=26 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=27 layer=FUNCTION tokens=358 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy._compute_freshness_lifetime file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=28 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=29 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=30 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_succeed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=31 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=32 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.is_cached_response_valid file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=33 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=34 layer=FUNCTION tokens=329 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::open_in_browser file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=35 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.should_cache_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=36 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::get_meta_refresh file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=37 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=38 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response.__repr__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=39 layer=FUNCTION tokens=354 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.download_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=40 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy._compute_current_age file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=41 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py::format_engine_status file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py
- rank=42 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py::print_engine_status file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py
- rank=43 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response.url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=44 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response.body file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py

## context

```text
file scrapy/utils/response.py
imports: __future__, os, re, tempfile, webbrowser, typing, weakref, twisted
defines: get_base_url, get_meta_refresh, response_status_message, _remove_html_comments, open_in_browser

file http/response/__init__.py
imports: __future__, typing, urllib, scrapy, collections, ipaddress, twisted, typing_extensions
defines: Response

file http/response/html.py
imports: scrapy
defines: HtmlResponse

file http/response/xml.py
imports: scrapy
defines: XmlResponse

file http/response/json.py
imports: scrapy
defines: JsonResponse

file scrapy/utils/engine.py
imports: __future__, time, typing, scrapy
defines: get_engine_status, format_engine_status, print_engine_status

file scrapy/docs/conftest.py
imports: doctest, pathlib, sybil, scrapy
defines: load_response, setup

class TestScrapyHTTPPageGetter:  [scrapy/tests/test_webclient.py:59]
methods: _test, test_earlyHeaders, test_non_standard_line_endings

class DummyPolicy:  [scrapy/extensions/httpcache.py:35]
methods: is_cached_response_fresh, is_cached_response_valid
         should_cache_request, should_cache_response
         __init__

class HtmlResponse(TextResponse):  [http/response/html.py:11]
methods: —

class JsonResponse(TextResponse):  [http/response/json.py:11]
methods: —

class XmlResponse(TextResponse):  [http/response/xml.py:11]
methods: —

class TestContractsManager:  [scrapy/tests/test_contracts.py:249]
methods: setup_method, should_error, should_fail, should_succeed
         test_cb_kwargs, test_contracts
         test_custom_contracts, test_errback
         test_form_contract, test_inherited_contracts
         test_meta, test_regex, test_returns
         test_returns_async, test_same_url, test_scrapes

class Status(LeafResource):  [tests/mockserver/http_resources.py:163]
methods: render_GET

class Response(object_ref):  [http/response/__init__.py:36]
methods: _set_body, _set_url, body, cb_kwargs, copy, css, flags
         flags, follow, follow_all, headers, headers
         jmespath, meta, replace, replace, replace, text
         url, urljoin, xpath, __init__, __repr__

class RFC2616Policy:  [scrapy/extensions/httpcache.py:59]
methods: _compute_current_age, _compute_freshness_lifetime
         _get_max_age, _parse_cachecontrol
         _set_conditional_validators
         is_cached_response_fresh
         is_cached_response_valid, should_cache_request
         should_cache_response, __init__

class TestHttpBase(ABC):  [scrapy/tests/test_downloader_handlers_http_base.py:56]
methods: download_handler_cls, get_dh
         test_content_length_zero_bodyless_post_only_one
         test_content_length_zero_bodyless_post_request_headers
         test_download
         test_download_has_correct_http_status_code
         test_download_has_correct_response_headers
         test_download_head
         test_download_is_not_automatically_gzip_decoded
         test_get_duplicate_header, test_host_header
         test_no_cookie_processing_or_persistence
         test_payload, test_redirect_status
         test_redirect_status_head
         test_request_header_duplicate
         test_request_header_none, test_response_class
         test_response_header_content_length
         test_server_receives_correct_request_body
         test_server_receives_correct_request_headers
         test_timeout_download_from_spider_nodata_rcvd
         test_timeout_download_from_spider_server_hangs
         test_unsupported_scheme

class TestWarnWhenSubclassed:  [scrapy/tests/test_utils_deprecate.py:24]
methods: _mywarnings, test_clsdict, test_custom_class_paths
         test_deprecate_a_class_with_custom_metaclass
         test_deprecate_subclass_of_deprecated_class
         test_inspect_stack, test_isinstance
         test_issubclass, test_no_warning_on_definition
         test_subclassing_warning_message
         test_subclassing_warns_once_by_default
         test_subclassing_warns_only_on_direct_children
         test_warning_auto_message, test_warning_on_instance

    def should_cache_response(self, response: Response, request: Request) -> bool:
        return response.status not in self.ignore_http_codes

def response_status_message(status: bytes | float | str) -> str:
    """Return status code plus status text descriptive message"""
    status_int = int(status)
    message = http.RESPONSES.get(status_int, "Unknown Status")
    return f"{status_int} {to_unicode(message)}"

    def should_fail(self):
        assert self.results.failures
        assert not self.results.errors

    def gotStatus(self, version, status, message):
        """
        Set the status of the request on us.
        @param version: The HTTP version.
        @type version: L{bytes}
        @param status: The HTTP status code, an integer represented as a
        bytestring.
        @type status: L{bytes}
        @param message: The HTTP status message.
        @type message: L{bytes}
        """
        self.version, self.status, self.message = version, status, message

    def process_response(
        self,
        request: Request,
        response: Response,
        spider: scrapy.Spider | None = None,
    ) -> Request | Response:
        if request.meta.get("dont_retry", False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason) or response
        return response

    def should_cache_response(self, response: Response, request: Request) -> bool:
        # What is cacheable - https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9.1
        # Response cacheability - https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.4
        # Status code 206 is not included because cache can not deal with partial contents
        cc = self._parse_cachecontrol(response)
        # obey directive "Cache-Control: no-store"
        if b"no-store" in cc:
            return False
        # Never cache 304 (Not Modified) responses
        if response.status == 304:
            return False
        # Cache unconditionally if configured to do so
        if self.always_store:
            return True
        # Any hint on response expiration is good
        if b"max-age" in cc or b"Expires" in response.headers:
            return True
        # Firefox fallbacks this statuses to one year expiration if none is set
        if response.status in {300, 301, 308}:
            return True
        # Other statuses without expiration requires at least one validator
        if response.status in {200, 203, 401}:
            return b"Last-Modified" in response.headers or b"ETag" in response.headers
        # Any other is probably not eligible for caching
        # Makes no sense to cache responses that does not contain expiration
        # info and can not be revalidated
        return False

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

    def __init__(self, settings: BaseSettings):
        self.ignore_schemes: list[str] = settings.getlist("HTTPCACHE_IGNORE_SCHEMES")
        self.ignore_http_codes: list[int] = [
            int(x) for x in settings.getlist("HTTPCACHE_IGNORE_HTTP_CODES")
        ]

    def _compute_freshness_lifetime(
        self, response: Response, request: Request, now: float
    ) -> float:
        # Reference nsHttpResponseHead::ComputeFreshnessLifetime
        # https://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsHttpResponseHead.cpp#706
        cc = self._parse_cachecontrol(response)
        maxage = self._get_max_age(cc)
        if maxage is not None:
            return maxage

        # Parse date header or synthesize it if none exists
        date = rfc1123_to_epoch(response.headers.get(b"Date")) or now

        # Try HTTP/1.0 Expires header
        if b"Expires" in response.headers:
            expires = rfc1123_to_epoch(response.headers[b"Expires"])
            # When parsing Expires header fails RFC 2616 section 14.21 says we
            # should treat this as an expiration time in the past.
            return max(0, expires - date) if expires else 0

        # Fallback to heuristic using last-modified header
        # This is not in RFC but on Firefox caching implementation
        lastmodified = rfc1123_to_epoch(response.headers.get(b"Last-Modified"))
        if lastmodified and lastmodified <= date:
            return (date - lastmodified) / 10

        # This request can be cached indefinitely
        if response.status in {300, 301, 308}:
            return self.MAXAGE

        # Insufficient information to compute freshness lifetime
        return 0

    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

    def should_succeed(self):
        assert not self.results.failures
        assert not self.results.errors

    def should_cache_request(self, request: Request) -> bool:
        return urlparse_cached(request).scheme not in self.ignore_schemes

    def is_cached_response_valid(
        self, cachedresponse: Response, response: Response, request: Request
    ) -> bool:
        # Use the cached response if the new response is a server error,
        # as long as the old response didn't specify must-revalidate.
        if response.status >= 500:
            cc = self._parse_cachecontrol(cachedresponse)
            if b"must-revalidate" not in cc:
                return True

        # Use the cached response if the server says it hasn't changed.
        return response.status == 304

    def on_error(self, failure):
        if isinstance(failure.value, HttpError):
            response = failure.value.response
            if response.status in self.bypass_status_codes:
                self.skipped.add(response.url[-3:])
                return self.parse(response)

        # it assumes there is a response attached to failure
        self.failed.add(failure.value.response.url[-3:])
        return failure

def open_in_browser(
    response: TextResponse,
    _openfunc: Callable[[str], Any] = webbrowser.open,
) -> Any:
    """Open *response* in a local web browser, adjusting the `base tag`_ for
    external links to work, e.g. so that images and styles are displayed.

    .. _base tag: https://www.w3schools.com/tags/tag_base.asp

    For example:

    .. code-block:: python

        from scrapy.utils.response import open_in_browser


        def parse_details(self, response):
            if "item name" not in response.body:
                open_in_browser(response)
    """
    # circular imports
    from scrapy.http import HtmlResponse, TextResponse  # noqa: PLC0415

    # XXX: this implementation is a bit dirty and could be improved
    body = response.body
    if isinstance(response, HtmlResponse):
        if b"<base" not in body:
            _remove_html_comments(body)
            repl = rf'\0<base href="{response.url}">'
            body = re.sub(rb"<head(?:[^<>]*?>)", to_bytes(repl), body, count=1)
        ext = ".html"
    elif isinstance(response, TextResponse):
        ext = ".txt"
    else:
        raise TypeError(f"Unsupported response type: {response.__class__.__name__}")
    fd, fname = tempfile.mkstemp(ext)
    os.write(fd, body)
    os.close(fd)
    return _openfunc(f"file://{fname}")

    def should_cache_request(self, request: Request) -> bool:
        if urlparse_cached(request).scheme in self.ignore_schemes:
            return False
        cc = self._parse_cachecontrol(request)
        # obey user-agent directive "Cache-Control: no-store"
        return b"no-store" not in cc

def get_meta_refresh(
    response: TextResponse,
    ignore_tags: Iterable[str] = ("script", "noscript"),
) -> tuple[None, None] | tuple[float, str]:
    """Parse the http-equiv refresh parameter from the given response"""
    if response not in _metaref_cache:
        text = response.text[0:4096]
        _metaref_cache[response] = html.get_meta_refresh(
            text, get_base_url(response), response.encoding, ignore_tags=ignore_tags
        )
    return _metaref_cache[response]

    def should_error(self):
        assert self.results.errors

    def __repr__(self) -> str:
        return f"<{self.status} {self.url}>"

    async def download_request(self, request: Request) -> Response:
        """Return a deferred for the HTTP download"""
        if hasattr(self._crawler.spider, "download_maxsize"):  # pragma: no cover
            warn_on_deprecated_spider_attribute("download_maxsize", "DOWNLOAD_MAXSIZE")
        if hasattr(self._crawler.spider, "download_warnsize"):  # pragma: no cover
            warn_on_deprecated_spider_attribute(
                "download_warnsize", "DOWNLOAD_WARNSIZE"
            )

        agent = ScrapyAgent(
            contextFactory=self._contextFactory,
            bindAddress=self._bind_address,
            pool=self._pool,
            maxsize=getattr(
                self._crawler.spider, "download_maxsize", self._default_maxsize
            ),
            warnsize=getattr(
                self._crawler.spider, "download_warnsize", self._default_warnsize
            ),
            fail_on_dataloss=self._fail_on_dataloss,
            crawler=self._crawler,
            tls_verbose_logging=self._tls_verbose_logging,
        )
        try:
            with wrap_twisted_exceptions():
                return await maybe_deferred_to_future(agent.download_request(request))
        except ResponseDataLossError:
            if not self._fail_on_dataloss_warned:
                logger.warning(get_dataloss_msg(request.url))
                self._fail_on_dataloss_warned = True
            raise

    def _compute_current_age(
        self, response: Response, request: Request, now: float
    ) -> float:
        # Reference nsHttpResponseHead::ComputeCurrentAge
        # https://dxr.mozilla.org/mozilla-central/source/netwerk/protocol/http/nsHttpResponseHead.cpp#658
        currentage: float = 0
        # If Date header is not set we assume it is a fast connection, and
        # clock is in sync with the server
        date = rfc1123_to_epoch(response.headers.get(b"Date")) or now
        if now > date:
            currentage = now - date

        if b"Age" in response.headers:
            try:
                age = int(response.headers[b"Age"])  # type: ignore[arg-type]
                currentage = max(currentage, age)
            except ValueError:
                pass

        return currentage

def format_engine_status(engine: ExecutionEngine) -> str:
    checks = get_engine_status(engine)
    s = "Execution engine status\n\n"
    for test, result in checks:
        s += f"{test:<47} : {result}\n"
    s += "\n"

    return s

def print_engine_status(engine: ExecutionEngine) -> None:
    print(format_engine_status(engine))

    def url(self) -> str:
        return self._url

    def body(self) -> bytes:
        return self._body
```

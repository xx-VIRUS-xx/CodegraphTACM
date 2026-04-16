# scrapy-24 :: tacm

query: https proxy tunneling - add a test (not perfect, but covers all impl) and fix for py3

## selected nodes

- rank=1 layer=FILE tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/spider.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/spider.py
- rank=2 layer=FILE tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=3 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py
- rank=4 layer=CLASS tokens=315 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpproxy.py::TestHttpProxyMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpproxy.py
- rank=5 layer=CLASS tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=6 layer=CLASS tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpProxyBase file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py
- rank=7 layer=CLASS tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_http2.py::TestHttps2Proxy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_http2.py
- rank=8 layer=CLASS tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_http10.py::TestHttp10Proxy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_http10.py
- rank=9 layer=CLASS tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::TestSpiderMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=10 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=11 layer=CLASS tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::TestItem.A file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=12 layer=FUNCTION tokens=218 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=13 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=14 layer=FUNCTION tokens=258 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._set_proxy_and_creds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=15 layer=FUNCTION tokens=419 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent._get_agent file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=16 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=17 layer=FUNCTION tokens=276 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http2.py::ScrapyH2Agent._get_agent file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http2.py
- rank=18 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpProxyBase.proxy_mockserver file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py
- rank=19 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._get_proxy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=20 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=21 layer=FUNCTION tokens=295 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_reactor_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=22 layer=FUNCTION tokens=453 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=23 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::UriResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=24 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._warn_unsupported_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=25 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=26 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.f file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=27 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.teardown_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=28 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::_Slot.add_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py

## context

```text
file scrapy/utils/spider.py
imports: __future__, inspect, logging, typing, scrapy, collections, types, twisted
defines: DefaultSpider, iterate_spider_output, iterate_spider_output, iterate_spider_output, iterate_spider_output, iter_spider_classes, spidercls_for_request, spidercls_for_request, spidercls_for_request, spidercls_for_request

file scrapy/utils/test.py
imports: __future__, asyncio, os, warnings, ftplib, importlib, pathlib, posixpath
defines: assert_gcs_environ, skip_if_no_boto, get_gcs_content_and_delete, get_ftp_content_and_delete, buffer_data, get_reactor_settings, get_crawler, get_pythonpath, get_testenv, get_from_asyncio_queue, mock_google_cloud_storage, get_web_client_agent_req

file scrapy/settings/default_settings.py
imports: sys, importlib, pathlib
defines: __getattr__

class TestHttpProxyMiddleware:  [scrapy/tests/test_downloadermiddleware_httpproxy.py:12]
methods: setup_method, teardown_method, test_add_credentials
         test_add_proxy_with_credentials
         test_add_proxy_without_credentials
         test_change_credentials
         test_change_proxy_add_credentials
         test_change_proxy_change_credentials
         test_change_proxy_keep_credentials
         test_change_proxy_remove_credentials
         test_change_proxy_remove_credentials_preremoved_header
         test_environment_proxies
         test_no_environment_proxies, test_no_proxy
         test_no_proxy_invalid_values, test_not_enabled
         test_proxy_already_seted, test_proxy_auth
         test_proxy_auth_empty_passwd
         test_proxy_auth_encoding
         test_proxy_authentication_header_disabled_proxy
         test_proxy_authentication_header_proxy_with_different_credentials
         test_proxy_authentication_header_proxy_with_same_credentials
         test_proxy_authentication_header_proxy_without_credentials
         test_proxy_authentication_header_undefined_proxy
         test_proxy_precedence_meta
         test_remove_credentials
         test_remove_proxy_with_credentials
         test_remove_proxy_without_credentials

class TestProxyConnect:  [scrapy/tests/test_proxy_connect.py:65]
methods: _assert_got_response_code, _assert_got_tunnel_error
         setup_class, setup_method, teardown_class
         teardown_method, test_https_connect_tunnel
         test_https_tunnel_auth_error
         test_https_tunnel_without_leak_proxy_authorization_header

class TestHttpProxyBase(ABC):  [scrapy/tests/test_downloader_handlers_http_base.py:975]
methods: download_handler_cls, get_dh, proxy_mockserver
         test_download_with_proxy
         test_download_with_proxy_https_timeout
         test_download_with_proxy_without_http_scheme
         test_download_without_proxy

class TestHttps2Proxy(H2DownloadHandlerMixin, TestHttpProxyBase):  [scrapy/tests/test_downloader_handler_twisted_http2.py:215]
methods: test_download_with_proxy_https_timeout
         test_download_with_proxy_without_http_scheme

class TestHttp10Proxy(HTTP10DownloadHandlerMixin, TestHttpProxyBase):  [scrapy/tests/test_downloader_handler_twisted_http10.py:50]
methods: test_download_with_proxy_https_timeout
         test_download_with_proxy_without_http_scheme

class TestSpiderMiddleware:  [scrapy/tests/test_spidermiddleware_output_chain.py:321]
methods: crawl_log, setup_class, teardown_class
         test_async_generator_callback
         test_generator_callback
         test_generator_callback_right_after_callback
         test_generator_output_chain
         test_not_a_generator_callback
         test_not_a_generator_callback_right_after_callback
         test_not_a_generator_output_chain
         test_process_spider_input_with_errback
         test_process_spider_input_without_errback
         test_recovery, test_recovery_asyncgen

class HttpProxyMiddleware:  [scrapy/downloadermiddlewares/httpproxy.py:26]
methods: _basic_auth_header, _get_proxy, _set_proxy_and_creds
         from_crawler, process_request, __init__

class A(Item):  [scrapy/tests/test_item.py:213]
methods: —

    def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None:
        creds, proxy_url, scheme = None, None, None
        if "proxy" in request.meta:
            if request.meta["proxy"] is not None:
                creds, proxy_url = self._get_proxy(request.meta["proxy"], "")
        elif self.proxies:
            parsed = urlparse_cached(request)
            _scheme = parsed.scheme
            if (
                # 'no_proxy' is only supported by http schemes
                _scheme not in {"http", "https"}
                or (parsed.hostname and not proxy_bypass(parsed.hostname))
            ) and _scheme in self.proxies:
                scheme = _scheme
                creds, proxy_url = self.proxies[scheme]

        self._set_proxy_and_creds(request, proxy_url, creds, scheme)
        return None

    def setup_method(self):
        self._oldenv = os.environ.copy()
        self._proxy = MitmProxy()
        proxy_url = self._proxy.start()
        os.environ["https_proxy"] = proxy_url
        os.environ["http_proxy"] = proxy_url

    def _set_proxy_and_creds(
        self,
        request: Request,
        proxy_url: str | None,
        creds: bytes | None,
        scheme: str | None,
    ) -> None:
        if scheme:
            request.meta["_scheme_proxy"] = True
        if proxy_url:
            request.meta["proxy"] = proxy_url
        elif request.meta.get("proxy") is not None:
            request.meta["proxy"] = None
        if creds:
            request.headers[b"Proxy-Authorization"] = b"Basic " + creds
            request.meta["_auth_proxy"] = proxy_url
        elif "_auth_proxy" in request.meta:
            if proxy_url != request.meta["_auth_proxy"]:
                if b"Proxy-Authorization" in request.headers:
                    del request.headers[b"Proxy-Authorization"]
                del request.meta["_auth_proxy"]
        elif b"Proxy-Authorization" in request.headers:
            if proxy_url:
                request.meta["_auth_proxy"] = proxy_url
            else:
                del request.headers[b"Proxy-Authorization"]

    def _get_agent(self, request: Request, timeout: float) -> Agent:
        from twisted.internet import reactor

        bindaddress = request.meta.get("bindaddress") or self._bindAddress
        bindaddress = normalize_bind_address(bindaddress)
        proxy = request.meta.get("proxy")
        if proxy:
            proxy = add_http_if_no_scheme(proxy)
            proxy_parsed = urlparse(proxy)
            proxy_host = proxy_parsed.hostname
            proxy_port = proxy_parsed.port
            if not proxy_port:
                proxy_port = 443 if proxy_parsed.scheme == "https" else 80
            if urlparse_cached(request).scheme == "https":
                assert proxy_host is not None
                proxyAuth = request.headers.get(b"Proxy-Authorization", None)
                proxyConf = (proxy_host, proxy_port, proxyAuth)
                return self._TunnelingAgent(
                    reactor=reactor,
                    proxyConf=proxyConf,
                    contextFactory=self._contextFactory,
                    connectTimeout=timeout,
                    bindAddress=bindaddress,
                    pool=self._pool,
                )
            return self._ProxyAgent(
                reactor=reactor,
                proxyURI=to_bytes(proxy, encoding="ascii"),
                connectTimeout=timeout,
                bindAddress=bindaddress,
                pool=self._pool,
            )

        return self._Agent(  # type: ignore[no-untyped-call]
            reactor=reactor,
            contextFactory=self._contextFactory,
            connectTimeout=timeout,
            bindAddress=bindaddress,
            pool=self._pool,
        )

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

    def _get_agent(self, request: Request, timeout: float | None) -> H2Agent:
        from twisted.internet import reactor

        bind_address = request.meta.get("bindaddress") or self._bind_address
        bind_address = normalize_bind_address(bind_address)
        proxy = request.meta.get("proxy")
        if proxy:
            if urlparse_cached(request).scheme == "https":
                # ToDo
                raise NotImplementedError(
                    "Tunneling via CONNECT method using HTTP/2.0 is not yet supported"
                )
            return self._ProxyAgent(
                reactor=reactor,
                context_factory=self._context_factory,
                proxy_uri=URI.fromBytes(to_bytes(proxy, encoding="ascii")),
                connect_timeout=timeout,
                bind_address=bind_address,
                pool=self._pool,
            )

        return self._Agent(
            reactor=reactor,
            context_factory=self._context_factory,
            connect_timeout=timeout,
            bind_address=bind_address,
            pool=self._pool,
        )

    def proxy_mockserver(self) -> Generator[ProxyEchoMockServer]:
        with ProxyEchoMockServer() as proxy:
            yield proxy

    def _get_proxy(self, url: str, orig_type: str) -> tuple[bytes | None, str]:
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type or orig_type, hostport, "", "", "", ""))

        creds = self._basic_auth_header(user, password) if user else None

        return creds, proxy_url

    def __init__(self, auth_encoding: str | None = "latin-1"):
        self.auth_encoding: str | None = auth_encoding
        self.proxies: dict[str, tuple[bytes | None, str]] = {}
        for type_, url in getproxies().items():
            try:
                self.proxies[type_] = self._get_proxy(url, type_)
            # some values such as '/var/run/docker.sock' can't be parsed
            # by _parse_proxy and as such should be skipped
            except ValueError:
                continue

def get_reactor_settings() -> dict[str, Any]:
    """Return a settings dict that works with the installed reactor.

    ``Crawler._apply_settings()`` checks that the installed reactor matches the
    settings, so tests that run the crawler in the current process may need to
    pass a correct :setting:`TWISTED_REACTOR` setting value when creating it.
    """
    settings: dict[str, Any] = {}
    if is_reactor_installed():
        if not is_asyncio_reactor_installed():
            settings["TWISTED_REACTOR"] = None
    else:
        # We are either running Scrapy tests for the reactorless mode, or
        # running some 3rd-party library tests for the reactorless mode, or
        # running some 3rd-party library tests without initializing a reactor
        # properly. The first two cases are fine, but we cannot distinguish the
        # last one from them.
        settings["TWISTED_REACTOR_ENABLED"] = False
        settings["DOWNLOAD_HANDLERS"] = {
            "ftp": None,
            "http": "scrapy.core.downloader.handlers._httpx.HttpxDownloadHandler",
            "https": "scrapy.core.downloader.handlers._httpx.HttpxDownloadHandler",
        }
    return settings

    def processProxyResponse(self, data: bytes) -> None:
        """Processes the response from the proxy. If the tunnel is successfully
        created, notifies the client that we are ready to send requests. If not
        raises a TunnelError.
        """
        assert self._protocol.transport
        self._connectBuffer += data
        # make sure that enough (all) bytes are consumed
        # and that we've got all HTTP headers (ending with a blank line)
        # from the proxy so that we don't send those bytes to the TLS layer
        #
        # see https://github.com/scrapy/scrapy/issues/2491
        if b"\r\n\r\n" not in self._connectBuffer:
            return
        self._protocol.dataReceived = self._protocolDataReceived  # type: ignore[method-assign]
        respm = TunnelingTCP4ClientEndpoint._responseMatcher.match(self._connectBuffer)
        if respm and int(respm.group("status")) == 200:
            # set proper Server Name Indication extension
            sslOptions = self._contextFactory.creatorForNetloc(  # type: ignore[call-arg,misc]
                self._tunneledHost, self._tunneledPort
            )
            self._protocol.transport.startTLS(sslOptions, self._protocolFactory)
            self._tunnelReadyDeferred.callback(self._protocol)
        else:
            extra: Any
            if respm:
                extra = {
                    "status": int(respm.group("status")),
                    "reason": respm.group("reason").strip(),
                }
            else:
                extra = data[: self._truncatedLength]
            self._tunnelReadyDeferred.errback(
                TunnelError(
                    "Could not open CONNECT tunnel with proxy "
                    f"{self._host}:{self._port} [{extra!r}]"
                )
            )

    def render(self, request):
        # Note: this is an ugly hack for CONNECT request timeout test.
        #       Returning some data here fail SSL/TLS handshake
        # ToDo: implement proper HTTPS proxy tests, not faking them.
        if request.method != b"CONNECT":
            return request.uri
        request.transport.write(b"HTTP/1.1 200 Connection established\r\n\r\n")
        return NOT_DONE_YET

    def _warn_unsupported_meta(self, meta: dict[str, Any]) -> None:
        if meta.get("bindaddress"):
            # configurable only per-client:
            # https://github.com/encode/httpx/issues/755#issuecomment-2746121794
            logger.error(
                f"The 'bindaddress' request meta key is not supported by"
                f" {type(self).__name__} and will be ignored."
            )
        if meta.get("proxy"):
            # configurable only per-client:
            # https://github.com/encode/httpx/issues/486
            logger.error(
                f"The 'proxy' request meta key is not supported by"
                f" {type(self).__name__} and will be ignored."
            )

    def _get_request_headers(self) -> list[tuple[str, str]]:
        url = urlparse_cached(self._request)

        path = url.path
        if url.query:
            path += "?" + url.query

        # This pseudo-header field MUST NOT be empty for "http" or "https"
        # URIs; "http" or "https" URIs that do not contain a path component
        # MUST include a value of '/'. The exception to this rule is an
        # OPTIONS request for an "http" or "https" URI that does not include
        # a path component; these MUST include a ":path" pseudo-header field
    # ... truncated

                def f(self):
                    # For rationale of this see:
                    # https://github.com/python/cpython/blob/ee1a81b77444c6715cbe610e951c655b6adab88b/Lib/test/test_super.py#L222
                    return __class__

    def teardown_method(self):
        self._proxy.stop()
        os.environ = self._oldenv

    def add_request(self, request: Request) -> None:
        self.inprogress.add(request)
```

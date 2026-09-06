# scrapy-24 :: tacm-full

query: https proxy tunneling - add a test (not perfect, but covers all impl) and fix for py3

## selected nodes

- rank=1 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=2 layer=FUNCTION tokens=467 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent._get_agent file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=3 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=4 layer=FUNCTION tokens=325 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http2.py::ScrapyH2Agent._get_agent file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http2.py
- rank=5 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=6 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::UriResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=7 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._warn_unsupported_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=8 layer=FUNCTION tokens=508 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=9 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._set_proxy_and_creds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=10 layer=FUNCTION tokens=568 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=11 layer=FUNCTION tokens=337 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory._set_connection_attributes file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=12 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=13 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.f file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=14 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py
- rank=15 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_squeues.py::_test_procesor file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_squeues.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent._get_agent [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http2.py::ScrapyH2Agent._get_agent [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http2.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
    def setup_method(self):
        self._oldenv = os.environ.copy()
        self._proxy = MitmProxy()
        proxy_url = self._proxy.start()
        os.environ["https_proxy"] = proxy_url
        os.environ["http_proxy"] = proxy_url

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::UriResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        # Note: this is an ugly hack for CONNECT request timeout test.
        #       Returning some data here fail SSL/TLS handshake
        # ToDo: implement proper HTTPS proxy tests, not faking them.
        if request.method != b"CONNECT":
            return request.uri
        request.transport.write(b"HTTP/1.1 200 Connection established\r\n\r\n")
        return NOT_DONE_YET

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._warn_unsupported_meta [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._set_proxy_and_creds [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py]
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
        # with a value of '*' (refer RFC 7540 - Section 8.1.2.3)
        if not path:
            path = "*" if self._request.method == "OPTIONS" else "/"

        # Make sure pseudo-headers comes before all the other headers
        headers = [
            (":method", self._request.method),
            (":authority", url.netloc),
        ]

        # The ":scheme" and ":path" pseudo-header fields MUST
        # be omitted for CONNECT method (refer RFC 7540 - Section 8.3)
        if self._request.method != "CONNECT":
            headers += [
                (":scheme", self._protocol.metadata["uri"].scheme),
                (":path", path),
            ]

        content_length = str(len(self._request.body))
        headers.append(("Content-Length", content_length))

        content_length_name = self._request.headers.normkey(b"Content-Length")
        for name, values in self._request.headers.items():
            for value_bytes in values:
                value = str(value_bytes, "utf-8")
                if name == content_length_name:
                    if value != content_length:
                        logger.warning(
                            "Ignoring bad Content-Length header %r of request %r, "
                            "sending %r instead",
                            value,
                            self._request,
                            content_length,
                        )
                    continue
                headers.append((str(name, "utf-8"), value))

        return headers

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory._set_connection_attributes [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def _set_connection_attributes(self, request):
        proxy = request.meta.get("proxy")
        if proxy:
            proxy_parsed = urlparse(to_bytes(proxy, encoding="ascii"))
            self.scheme = proxy_parsed.scheme
            self.host = proxy_parsed.hostname
            self.port = proxy_parsed.port
            self.netloc = proxy_parsed.netloc
            if self.port is None:
                self.port = 443 if proxy_parsed.scheme == b"https" else 80
            self.path = self.url
        else:
            parsed = urlparse_cached(request)
            path_str = urlunparse(
                ("", "", parsed.path or "/", parsed.params, parsed.query, "")
            )
            self.path = to_bytes(path_str, encoding="ascii")
            assert parsed.hostname is not None
            self.host = to_bytes(parsed.hostname, encoding="ascii")
            self.port = parsed.port
            self.scheme = to_bytes(parsed.scheme, encoding="ascii")
            self.netloc = to_bytes(parsed.netloc, encoding="ascii")
            if self.port is None:
                self.port = 443 if self.scheme == b"https" else 80

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def _apply_reactorless_default_settings(self) -> None:
        """Change some setting defaults when not using a Twisted reactor.

        Some settings need different defaults when using and not using a
        reactor, but as we can't put this logic into default_settings.py we
        change them here when the reactor is not used.
        """
        self.settings.set("TELNETCONSOLE_ENABLED", False, priority="default")
        for scheme in ("http", "https"):
            self.settings["DOWNLOAD_HANDLERS_BASE"][scheme] = (
                "scrapy.core.downloader.handlers._httpx.HttpxDownloadHandler"
            )
        self.settings["DOWNLOAD_HANDLERS_BASE"]["ftp"] = None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.f [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py]
                def f(self):
                    # For rationale of this see:
                    # https://github.com/python/cpython/blob/ee1a81b77444c6715cbe610e951c655b6adab88b/Lib/test/test_super.py#L222
                    return __class__

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestSpider.start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py]
            async def start(self):
                for i in range(2):
                    yield Request(f"https://example.com/{i}", dont_filter=True)
                yield {"name": "test item"}

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_squeues.py::_test_procesor [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_squeues.py]
def _test_procesor(x):
    return x + x
```

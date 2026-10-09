# scrapy-24 :: hybrid

query: https proxy tunneling - add a test (not perfect, but covers all impl) and fix for py3

## selected nodes

- rank=1 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::UriResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=2 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=3 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=4 layer=FUNCTION tokens=508 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=5 layer=FUNCTION tokens=467 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent._get_agent file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=6 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyProxyAgent.request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=7 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingAgent._requestWithEndpoint file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=8 layer=FUNCTION tokens=337 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory._set_connection_attributes file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=9 layer=FUNCTION tokens=325 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http2.py::ScrapyH2Agent._get_agent file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http2.py
- rank=10 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._warn_unsupported_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=11 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=12 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.port file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=13 layer=FUNCTION tokens=512 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::main_factory file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=14 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._set_proxy_and_creds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::UriResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        # Note: this is an ugly hack for CONNECT request timeout test.
        #       Returning some data here fail SSL/TLS handshake
        # ToDo: implement proper HTTPS proxy tests, not faking them.
        if request.method != b"CONNECT":
            return request.uri
        request.transport.write(b"HTTP/1.1 200 Connection established\r\n\r\n")
        return NOT_DONE_YET

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
    def setup_method(self):
        self._oldenv = os.environ.copy()
        self._proxy = MitmProxy()
        proxy_url = self._proxy.start()
        os.environ["https_proxy"] = proxy_url
        os.environ["http_proxy"] = proxy_url

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyProxyAgent.request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def request(
        self,
        method: bytes,
        uri: bytes,
        headers: TxHeaders | None = None,
        bodyProducer: IBodyProducer | None = None,
    ) -> Deferred[IResponse]:
        """
        Issue a new request via the configured proxy.
        """
        # Cache *all* connections under the same key, since we are only
        # connecting to a single destination, the proxy:
        return self._requestWithEndpoint(
            key=(b"http-proxy", self._proxyURI.host, self._proxyURI.port),
            endpoint=self._getEndpoint(self._proxyURI),  # type: ignore[no-untyped-call]
            method=method,
            parsedURI=URI.fromBytes(uri),
            headers=headers,
            bodyProducer=bodyProducer,
            requestPath=uri,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingAgent._requestWithEndpoint [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def _requestWithEndpoint(
        self,
        key: Any,
        endpoint: TCP4ClientEndpoint,
        method: bytes,
        parsedURI: URI,
        headers: TxHeaders | None,
        bodyProducer: IBodyProducer | None,
        requestPath: bytes,
    ) -> Deferred[IResponse]:
        # proxy host and port are required for HTTP pool `key`
        # otherwise, same remote host connection request could reuse
        # a cached tunneled connection to a different proxy
        key += self._proxyConf
        return super()._requestWithEndpoint(
            key=key,
            endpoint=endpoint,
            method=method,
            parsedURI=parsedURI,
            headers=headers,
            bodyProducer=bodyProducer,
            requestPath=requestPath,
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
    def __init__(self) -> None:
        if not self.listen_http and not self.listen_https:
            raise ValueError("At least one of listen_http and listen_https must be set")

        self.proc: Popen | None = None
        self.host: str = "127.0.0.1"
        self.http_port: int | None = None
        self.https_port: int | None = None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.port [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
    def port(self, is_secure: bool = False) -> int:
        if not is_secure and not self.listen_http:
            raise ValueError("This server doesn't provide HTTP")
        if is_secure and not self.listen_https:
            raise ValueError("This server doesn't provide HTTPS")
        port = self.https_port if is_secure else self.http_port
        assert port is not None
        return port

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::main_factory [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
def main_factory(
    resource_class: type[resource.Resource],
    *,
    listen_http: bool = True,
    listen_https: bool = True,
) -> Callable[[], None]:
    if not listen_http and not listen_https:
        raise ValueError("At least one of listen_http and listen_https must be set")

    def main() -> None:
        from twisted.internet import reactor

        root = resource_class()
        factory = Site(root)

        if listen_http:
            http_port = reactor.listenTCP(0, factory)

        if listen_https:
            parser = argparse.ArgumentParser()
            parser.add_argument("--keyfile", help="SSL key file")
            parser.add_argument("--certfile", help="SSL certificate file")
            parser.add_argument(
                "--cipher-string",
                default=None,
                help="SSL cipher string (optional)",
            )
            args = parser.parse_args()
            context_factory_kw = {}
            if args.keyfile:
                context_factory_kw["keyfile"] = args.keyfile
            if args.certfile:
                context_factory_kw["certfile"] = args.certfile
            if args.cipher_string:
                context_factory_kw["cipher_string"] = args.cipher_string
            context_factory = ssl_context_factory(**context_factory_kw)
            https_port = reactor.listenSSL(0, factory, context_factory)

        def print_listening():
            if listen_http:
                http_host = http_port.getHost()
                http_address = f"http://{http_host.host}:{http_host.port}"
                print(http_address)
            if listen_https:
                https_host = https_port.getHost()
                https_address = f"https://{https_host.host}:{https_host.port}"
                print(https_address)

        reactor.callWhenRunning(print_listening)
        reactor.run()

    return main

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
```

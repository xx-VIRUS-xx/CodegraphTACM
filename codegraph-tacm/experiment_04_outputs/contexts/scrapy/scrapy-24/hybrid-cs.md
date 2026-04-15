# scrapy-24 :: hybrid-cs

query: https proxy tunneling - add a test (not perfect, but covers all impl) and fix for py3

## selected nodes

- rank=1 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=2 layer=FUNCTION tokens=508 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=3 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=4 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._get_proxy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=5 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._set_proxy_and_creds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=6 layer=FUNCTION tokens=512 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::main_factory file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=7 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py::TestMain._test_sleep file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py
- rank=8 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingAgent._requestWithEndpoint file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=9 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=10 layer=FUNCTION tokens=337 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory._set_connection_attributes file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=11 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::ScrapyProxyH2Agent.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py
- rank=12 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=13 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.requestTunnel file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=14 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpProxyBase.proxy_mockserver file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py
- rank=15 layer=FUNCTION tokens=434 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=16 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::tunnel_request_data file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=17 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClient.server_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._get_proxy [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py]
    def _get_proxy(self, url: str, orig_type: str) -> tuple[bytes | None, str]:
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type or orig_type, hostport, "", "", "", ""))

        creds = self._basic_auth_header(user, password) if user else None

        return creds, proxy_url

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py::TestMain._test_sleep [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py]
    async def _test_sleep(self, spider_middlewares):
        class TestSpider(Spider):
            name = "test"

            async def start(self):
                yield ITEM_A

        await self._test(spider_middlewares, TestSpider, [ITEM_A])

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
    def __init__(self) -> None:
        if not self.listen_http and not self.listen_https:
            raise ValueError("At least one of listen_http and listen_https must be set")

        self.proc: Popen | None = None
        self.host: str = "127.0.0.1"
        self.http_port: int | None = None
        self.https_port: int | None = None

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::ScrapyProxyH2Agent.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py]
    def __init__(
        self,
        reactor: ReactorBase,
        proxy_uri: URI,
        pool: H2ConnectionPool,
        context_factory: BrowserLikePolicyForHTTPS = BrowserLikePolicyForHTTPS(),  # noqa: B008
        connect_timeout: float | None = None,
        bind_address: tuple[str, int] | None = None,
    ) -> None:
        super().__init__(
            reactor=reactor,
            pool=pool,
            context_factory=context_factory,
            connect_timeout=connect_timeout,
            bind_address=bind_address,
        )
        self._proxy_uri = proxy_uri

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
def _wrong_credentials(proxy_url):
    bad_auth_proxy = list(urlsplit(proxy_url))
    bad_auth_proxy[1] = bad_auth_proxy[1].replace("scrapy:scrapy@", "wrong:wronger@")
    return urlunsplit(bad_auth_proxy)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.requestTunnel [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def requestTunnel(self, protocol: Protocol) -> Protocol:
        """Asks the proxy to open a tunnel."""
        assert protocol.transport
        tunnelReq = tunnel_request_data(
            self._tunneledHost, self._tunneledPort, self._proxyAuthHeader
        )
        protocol.transport.write(tunnelReq)
        self._protocolDataReceived = protocol.dataReceived
        protocol.dataReceived = self.processProxyResponse  # type: ignore[method-assign]
        self._protocol = protocol
        return protocol

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpProxyBase.proxy_mockserver [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py]
    def proxy_mockserver(self) -> Generator[ProxyEchoMockServer]:
        with ProxyEchoMockServer() as proxy:
            yield proxy

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::main [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::tunnel_request_data [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
def tunnel_request_data(
    host: str, port: int, proxy_auth_header: bytes | None = None
) -> bytes:
    r"""
    Return binary content of a CONNECT request.

    >>> from scrapy.utils.python import to_unicode as s
    >>> s(tunnel_request_data("example.com", 8080))
    'CONNECT example.com:8080 HTTP/1.1\r\nHost: example.com:8080\r\n\r\n'
    >>> s(tunnel_request_data("example.com", 8080, b"123"))
    'CONNECT example.com:8080 HTTP/1.1\r\nHost: example.com:8080\r\nProxy-Authorization: 123\r\n\r\n'
    >>> s(tunnel_request_data(b"example.com", "8090"))
    'CONNECT example.com:8090 HTTP/1.1\r\nHost: example.com:8090\r\n\r\n'
    """
    host_value = to_bytes(host, encoding="ascii") + b":" + to_bytes(str(port))
    tunnel_req = b"CONNECT " + host_value + b" HTTP/1.1\r\n"
    tunnel_req += b"Host: " + host_value + b"\r\n"
    if proxy_auth_header:
        tunnel_req += b"Proxy-Authorization: " + proxy_auth_header + b"\r\n"
    tunnel_req += b"\r\n"
    return tunnel_req

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClient.server_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py]
    def server_url(self, server_port):
        return f"http://127.0.0.1:{server_port}/"
```

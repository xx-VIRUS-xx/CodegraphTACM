# scrapy-24 :: codesearch

query: https proxy tunneling - add a test (not perfect, but covers all impl) and fix for py3

## selected nodes

- rank=1 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.requestTunnel file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=2 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::tunnel_request_data file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=3 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._get_proxy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=4 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingAgent._getEndpoint file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=5 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=6 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py::TestXmlRpcRequest._test_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py
- rank=7 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::ScrapyProxyH2Agent.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py
- rank=8 layer=FUNCTION tokens=508 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=9 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py::TestMain._test_sleep file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py
- rank=10 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py::TestCrawlerProcessSubprocessBase._test_shutdown_forced file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py
- rank=11 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http10.py::HTTP10DownloadHandler._connect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http10.py
- rank=12 layer=FUNCTION tokens=222 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=13 layer=FUNCTION tokens=189 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py::TestCrawlerProcessSubprocessBase._test_shutdown_graceful file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py
- rank=14 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py
- rank=15 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py::MockDNSServer.__enter__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py
- rank=16 layer=FUNCTION tokens=212 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_spider_attr file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=17 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py
- rank=18 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/contextfactory.py::_ScrapyClientContextFactory.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/contextfactory.py
- rank=19 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyProxyAgent.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=20 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClientCustomCiphersSSL.testPayloadDisabledCipher file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=21 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerRunner/no_reactor.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerRunner/no_reactor.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._get_proxy [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py]
    def _get_proxy(self, url: str, orig_type: str) -> tuple[bytes | None, str]:
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type or orig_type, hostport, "", "", "", ""))

        creds = self._basic_auth_header(user, password) if user else None

        return creds, proxy_url

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingAgent._getEndpoint [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def _getEndpoint(self, uri: URI) -> TunnelingTCP4ClientEndpoint:
        return TunnelingTCP4ClientEndpoint(
            reactor=self._reactor,
            host=uri.host,
            port=uri.port,
            proxyConf=self._proxyConf,
            contextFactory=self._contextFactory,
            timeout=self._endpointFactory._connectTimeout,
            bindAddress=self._endpointFactory._bindAddress,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
    def setup_method(self):
        self._oldenv = os.environ.copy()
        self._proxy = MitmProxy()
        proxy_url = self._proxy.start()
        os.environ["https_proxy"] = proxy_url
        os.environ["http_proxy"] = proxy_url

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py::TestXmlRpcRequest._test_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request.py]
    def _test_request(self, **kwargs):
        r = self.request_class("http://scrapytest.org/rpc2", **kwargs)
        assert r.headers[b"Content-Type"] == b"text/xml"
        assert r.body == to_bytes(
            xmlrpc.client.dumps(**kwargs), encoding=kwargs.get("encoding", "utf-8")
        )
        assert r.method == "POST"
        assert r.encoding == kwargs.get("encoding", "utf-8")
        assert r.dont_filter

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py::TestMain._test_sleep [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py]
    async def _test_sleep(self, spider_middlewares):
        class TestSpider(Spider):
            name = "test"

            async def start(self):
                yield ITEM_A

        await self._test(spider_middlewares, TestSpider, [ITEM_A])

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py::TestCrawlerProcessSubprocessBase._test_shutdown_forced [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py]
    async def _test_shutdown_forced(self, script: str = "sleeping.py") -> None:
        sig = signal.SIGINT if sys.platform != "win32" else signal.SIGBREAK  # type: ignore[attr-defined]
        args = self.get_script_args(script, "10")
        p = PopenSpawn(args, timeout=5, env=get_script_run_env())
        p.expect_exact("Spider opened")
        p.expect_exact("Crawled (200)")
        p.kill(sig)
        p.expect_exact("shutting down gracefully")
        # sending the second signal too fast often causes problems
        await async_sleep(0.01)
        p.kill(sig)
        p.expect_exact("forcing unclean shutdown")
        p.wait()  # type: ignore[no-untyped-call]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http10.py::HTTP10DownloadHandler._connect [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http10.py]
    def _connect(self, factory: ScrapyHTTPClientFactory) -> IConnector:
        from twisted.internet import reactor

        host, port = to_unicode(factory.host), factory.port
        if factory.scheme == b"https":
            client_context_factory = build_from_crawler(
                self.ClientContextFactory,
                self._crawler,
            )
            return reactor.connectSSL(host, port, factory, client_context_factory)
        return reactor.connectTCP(host, port, factory)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def __init__(
        self,
        reactor: ReactorBase,
        host: str,
        port: int,
        proxyConf: tuple[str, int, bytes | None],
        contextFactory: IPolicyForHTTPS,
        timeout: float = 30,
        bindAddress: tuple[str, int] | None = None,
    ):
        proxyHost, proxyPort, self._proxyAuthHeader = proxyConf
        super().__init__(reactor, proxyHost, proxyPort, timeout, bindAddress)
        self._tunnelReadyDeferred: Deferred[Protocol] = Deferred()
        self._tunneledHost: str = host
        self._tunneledPort: int = port
        self._contextFactory: IPolicyForHTTPS = contextFactory
        self._connectBuffer: bytearray = bytearray()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py::TestCrawlerProcessSubprocessBase._test_shutdown_graceful [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py]
    def _test_shutdown_graceful(self, script: str = "sleeping.py") -> None:
        sig = signal.SIGINT if sys.platform != "win32" else signal.SIGBREAK  # type: ignore[attr-defined]
        args = self.get_script_args(script, "3")
        p = PopenSpawn(args, timeout=5, env=get_script_run_env())
        p.expect_exact("Spider opened")
        p.expect_exact("Crawled (200)")
        p.kill(sig)
        p.expect_exact("shutting down gracefully")
        p.expect_exact("Spider closed (shutdown)")
        p.wait()  # type: ignore[no-untyped-call]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py::main [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py]
def main() -> None:
    from twisted.internet import reactor

    clients = [MockDNSResolver()]
    factory = DNSServerFactory(clients=clients)
    protocol = dns.DNSDatagramProtocol(controller=factory)
    listener = reactor.listenUDP(0, protocol)

    def print_listening():
        host = listener.getHost()
        print(f"{host.host}:{host.port}")

    reactor.callWhenRunning(print_listening)
    reactor.run()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py::MockDNSServer.__enter__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py]
    def __enter__(self):
        self.proc = Popen(
            [sys.executable, "-u", "-m", "tests.mockserver.dns"],
            stdout=PIPE,
            env=get_script_run_env(),
        )
        self.host = "127.0.0.1"
        self.port = int(
            self.proc.stdout.readline().strip().decode("ascii").split(":")[1]
        )
        return self

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_spider_attr [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py]
    def _test_compression_bomb_spider_attr(self, compression_id):
        class DownloadMaxSizeSpider(Spider):
            download_maxsize = 1_000_000

        crawler = get_crawler(DownloadMaxSizeSpider)
        spider = crawler._create_spider("scrapytest.org")
        mw = HttpCompressionMiddleware.from_crawler(crawler)
        mw.open_spider(spider)

        response = self._getresponse(f"bomb-{compression_id}")
        with pytest.raises(IgnoreRequest) as exc_info:
            mw.process_response(response.request, response)
        assert exc_info.value.__cause__.decompressed_size < 1_100_000

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py::main [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py]
def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("-d", "--directory", required=True)
    args = parser.parse_args()

    authorizer = DummyAuthorizer()
    full_permissions = "elradfmwMT"
    authorizer.add_anonymous(args.directory, perm=full_permissions)
    handler = FTPHandler
    handler.authorizer = authorizer
    address = ("127.0.0.1", 0)
    server = FTPServer(address, handler)
    server.serve_forever()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/contextfactory.py::_ScrapyClientContextFactory.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/contextfactory.py]
    def __init__(
        self,
        method: int = SSL.SSLv23_METHOD,  # noqa: S503
        tls_verbose_logging: bool = False,
        tls_ciphers: str | None = None,
        *args: Any,
        verify_certificates: bool = False,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)  # type: ignore[no-untyped-call]
        self._ssl_method: int = method
        self.tls_verbose_logging: bool = tls_verbose_logging  # unused
        self.tls_ciphers: AcceptableCiphers
        if tls_ciphers:
            self.tls_ciphers = AcceptableCiphers.fromOpenSSLCipherString(tls_ciphers)
        else:
            self.tls_ciphers = DEFAULT_CIPHERS
        with _filter_method_warning():
            self._certificate_options = CertificateOptions(
                method=self._ssl_method,
                fixBrokenPeers=True,
                acceptableCiphers=self.tls_ciphers,
            )
        self._ctx = self._get_context()
        self._verify_certificates = verify_certificates

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyProxyAgent.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def __init__(
        self,
        reactor: ReactorBase,
        proxyURI: bytes,
        connectTimeout: float | None = None,
        bindAddress: tuple[str, int] | None = None,
        pool: HTTPConnectionPool | None = None,
    ):
        super().__init__(  # type: ignore[no-untyped-call]
            reactor=reactor,
            connectTimeout=connectTimeout,
            bindAddress=bindAddress,
            pool=pool,
        )
        self._proxyURI: URI = URI.fromBytes(proxyURI)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClientCustomCiphersSSL.testPayloadDisabledCipher [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py]
    def testPayloadDisabledCipher(self, server_url):
        s = "0123456789" * 10
        crawler = get_crawler(
            settings_dict={
                "DOWNLOADER_CLIENT_TLS_CIPHERS": "ECDHE-RSA-AES256-GCM-SHA384"
            }
        )
        client_context_factory = build_from_crawler(
            _ScrapyClientContextFactory, crawler
        )
        with pytest.raises(OpenSSL.SSL.Error):
            yield getPage(
                server_url + "payload", body=s, contextFactory=client_context_factory
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerRunner/no_reactor.py::main [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerRunner/no_reactor.py]
async def main() -> None:
    configure_logging()
    runner = AsyncCrawlerRunner()
    await runner.crawl(NoRequestsSpider)
```

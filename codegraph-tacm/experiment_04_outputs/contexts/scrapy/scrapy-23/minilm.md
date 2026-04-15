# scrapy-23 :: minilm

query: py3 fix HttpProxy and Retry Middlewares

## selected nodes

- rank=1 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=2 layer=FUNCTION tokens=508 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=3 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyProxyAgent.request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=4 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=5 layer=FUNCTION tokens=807 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py::H2ClientProtocol.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py
- rank=6 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.requestTunnel file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=7 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._set_proxy_and_creds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=8 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingAgent._requestWithEndpoint file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=9 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestMaxRetryTimes._test_retry file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=10 layer=FUNCTION tokens=337 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory._set_connection_attributes file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=11 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=12 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/middleware.py::DownloaderMiddlewareManager._add_middleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/middleware.py
- rank=13 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::H2ConnectionPool._new_connection file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py
- rank=14 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=15 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::H2ConnectionPool.put_connection file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
    def setup_method(self):
        self._oldenv = os.environ.copy()
        self._proxy = MitmProxy()
        proxy_url = self._proxy.start()
        os.environ["https_proxy"] = proxy_url
        os.environ["http_proxy"] = proxy_url

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py::H2ClientProtocol.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py]
    def __init__(
        self,
        uri: URI,
        settings: Settings,
        conn_lost_deferred: Deferred[list[BaseException]],
        *,
        tls_verbose_logging: bool = False,
    ) -> None:
        """
        Arguments:
            uri -- URI of the base url to which HTTP/2 Connection will be made.
                uri is used to verify that incoming client requests have correct
                base URL.
            settings -- Scrapy project settings
            conn_lost_deferred -- Deferred fires with the reason: Failure to notify
                that connection was lost
            tls_verbose_logging -- Whether to log TLS details
        """
        self._conn_lost_deferred: Deferred[list[BaseException]] = conn_lost_deferred
        self._tls_verbose_logging: bool = tls_verbose_logging

        config = H2Configuration(client_side=True, header_encoding="utf-8")
        self.conn = H2Connection(config=config)

        # ID of the next request stream
        # Following the convention - 'Streams initiated by a client MUST
        # use odd-numbered stream identifiers' (RFC 7540 - Section 5.1.1)
        self._stream_id_generator = itertools.count(start=1, step=2)

        # Streams are stored in a dictionary keyed off their stream IDs
        self.streams: dict[int, Stream] = {}

        # If requests are received before connection is made we keep
        # all requests in a pool and send them as the connection is made
        self._pending_request_stream_pool: deque[Stream] = deque()

        # Save an instance of errors raised which lead to losing the connection
        # We pass these instances to the streams ResponseFailed() failure
        self._conn_lost_errors: list[BaseException] = []

        # Some meta data of this connection
        # initialized when connection is successfully made
        self.metadata: dict[str, Any] = {
            # Peer certificate instance
            "certificate": None,
            # Address of the server we are connected to which
            # is updated when HTTP/2 connection is  made successfully
            "ip_address": None,
            # URI of the peer HTTP/2 connection is made
            "uri": uri,
            # Both ip_address and uri are used by the Stream before
            # initiating the request to verify that the base address
            # Variables taken from Project Settings
            "default_download_maxsize": settings.getint("DOWNLOAD_MAXSIZE"),
            "default_download_warnsize": settings.getint("DOWNLOAD_WARNSIZE"),
            # Counter to keep track of opened streams. This counter
            # is used to make sure that not more than MAX_CONCURRENT_STREAMS
            # streams are opened which leads to ProtocolError
            # We use simple FIFO policy to handle pending requests
            "active_streams": 0,
            # Flag to keep track if settings were acknowledged by the remote
            # This ensures that we have established a HTTP/2 connection
            "settings_acknowledged": False,
        }

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestMaxRetryTimes._test_retry [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py]
    def _test_retry(
        self,
        req,
        exception,
        max_retry_times,
        middleware=None,
    ):
        middleware = middleware or self.mw

        for _ in range(max_retry_times):
            req = middleware.process_exception(req, exception)
            assert isinstance(req, Request)

        # discard it
        req = middleware.process_exception(req, exception)
        assert req is None

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
def _wrong_credentials(proxy_url):
    bad_auth_proxy = list(urlsplit(proxy_url))
    bad_auth_proxy[1] = bad_auth_proxy[1].replace("scrapy:scrapy@", "wrong:wronger@")
    return urlunsplit(bad_auth_proxy)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/middleware.py::DownloaderMiddlewareManager._add_middleware [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/middleware.py]
    def _add_middleware(self, mw: Any) -> None:
        if hasattr(mw, "process_request"):
            self.methods["process_request"].append(mw.process_request)
            self._check_mw_method_spider_arg(mw.process_request)
        if hasattr(mw, "process_response"):
            self.methods["process_response"].appendleft(mw.process_response)
            self._check_mw_method_spider_arg(mw.process_response)
        if hasattr(mw, "process_exception"):
            self.methods["process_exception"].appendleft(mw.process_exception)
            self._check_mw_method_spider_arg(mw.process_exception)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::H2ConnectionPool._new_connection [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py]
    def _new_connection(
        self, key: ConnectionKeyT, uri: URI, endpoint: HostnameEndpoint
    ) -> Deferred[H2ClientProtocol]:
        self._pending_requests[key] = deque()

        conn_lost_deferred: Deferred[list[BaseException]] = Deferred()
        conn_lost_deferred.addCallback(self._remove_connection, key)

        factory = H2ClientFactory(
            uri,
            self.settings,
            conn_lost_deferred,
            tls_verbose_logging=self._tls_verbose_logging,
        )
        conn_d = endpoint.connect(factory)
        conn_d.addCallback(self.put_connection, key)

        d: Deferred[H2ClientProtocol] = Deferred()
        self._pending_requests[key].append(d)
        return d

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::H2ConnectionPool.put_connection [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py]
    def put_connection(
        self, conn: H2ClientProtocol, key: ConnectionKeyT
    ) -> H2ClientProtocol:
        self._connections[key] = conn

        # Now as we have established a proper HTTP/2 connection
        # we fire all the deferred's with the connection instance
        pending_requests = self._pending_requests.pop(key, None)
        while pending_requests:
            d = pending_requests.popleft()
            d.callback(conn)

        return conn
```

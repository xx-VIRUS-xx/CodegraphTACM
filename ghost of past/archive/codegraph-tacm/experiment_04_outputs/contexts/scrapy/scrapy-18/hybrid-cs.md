# scrapy-18 :: hybrid-cs

query: More liberal Content-Disposition header parsing

## selected nodes

- rank=1 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._headers_encoding file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=2 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::GCSFilesStore._get_content_type file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=3 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_disposition file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=4 layer=FUNCTION tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::parse_cachecontrol file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=5 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=6 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_type file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=7 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::PayloadResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=8 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::EncodingResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=9 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::ResponseHeadersResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=10 layer=FUNCTION tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._body_inferred_encoding file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=11 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::ContentLengthHeaderResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=12 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::Compress.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=13 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.header_items file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=14 layer=FUNCTION tokens=568 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=15 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::EmptyContentTypeHeaderResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=16 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::BrokenDownloadResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=17 layer=FUNCTION tokens=137 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware._handle_encoding file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py
- rank=18 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.get_header file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=19 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::ErrorResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=20 layer=FUNCTION tokens=697 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py
- rank=21 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.has_header file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=22 layer=FUNCTION tokens=290 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::_has_ajaxcrawlable_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
- rank=23 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_ajaxcrawlable.py::TestAjaxCrawlMiddleware._ajaxcrawlable_body file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_ajaxcrawlable.py
- rank=24 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleEndHeaders file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._headers_encoding [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py]
    def _headers_encoding(self) -> str | None:
        content_type = self.headers.get(b"Content-Type") or b""
        return http_content_type_encoding(to_unicode(content_type, encoding="latin-1"))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::GCSFilesStore._get_content_type [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py]
    def _get_content_type(self, headers: dict[str, str] | None) -> str:
        if headers and "Content-Type" in headers:
            return headers["Content-Type"]
        return "application/octet-stream"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_disposition [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py]
    def from_content_disposition(
        self, content_disposition: str | bytes
    ) -> type[Response]:
        try:
            filename = (
                to_unicode(content_disposition, encoding="latin-1", errors="replace")
                .split(";")[1]
                .split("=")[1]
                .strip("\"'")
            )
            return self.from_filename(filename)
        except IndexError:
            return Response

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::parse_cachecontrol [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
def parse_cachecontrol(header: bytes) -> dict[bytes, bytes | None]:
    """Parse Cache-Control header

    https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9

    >>> parse_cachecontrol(b'public, max-age=3600') == {b'public': None,
    ...                                                 b'max-age': b'3600'}
    True
    >>> parse_cachecontrol(b'') == {}
    True

    """
    directives = {}
    for directive in header.split(b","):
        key, sep, val = directive.strip().partition(b"=")
        if key:
            directives[key.lower()] = val if sep else None
    return directives

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_headers [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py]
    def from_headers(self, headers: Mapping[bytes, bytes]) -> type[Response]:
        """Return the most appropriate Response class by looking at the HTTP
        headers"""
        cls = Response
        if b"Content-Type" in headers:
            cls = self.from_content_type(
                content_type=headers[b"Content-Type"],
                content_encoding=headers.get(b"Content-Encoding"),
            )
        if cls is Response and b"Content-Disposition" in headers:
            cls = self.from_content_disposition(headers[b"Content-Disposition"])
        return cls

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_type [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py]
    def from_content_type(
        self, content_type: str | bytes, content_encoding: bytes | None = None
    ) -> type[Response]:
        """Return the most appropriate Response class from an HTTP Content-Type
        header"""
        if content_encoding:
            return Response
        mimetype = (
            to_unicode(content_type, encoding="latin-1").split(";")[0].strip().lower()
        )
        return self.from_mimetype(mimetype)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::PayloadResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        data = request.content.read()
        contentLength = request.requestHeaders.getRawHeaders(b"content-length")[0]
        if len(data) != 100 or int(contentLength) != 100:
            return b"ERROR"
        return data

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::EncodingResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py]
    def render(self, request):
        body = to_unicode(request.content.read())
        request.setHeader(b"content-encoding", self.out_encoding)
        return body.encode(self.out_encoding)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::ResponseHeadersResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        body = json.loads(request.content.read().decode())
        for header_name, header_value in body.items():
            request.responseHeaders.addRawHeader(header_name, header_value)
        return json.dumps(body).encode("utf-8")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._body_inferred_encoding [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py]
    def _body_inferred_encoding(self) -> str:
        if self._cached_benc is None:
            content_type = to_unicode(
                cast("bytes", self.headers.get(b"Content-Type", b"")),
                encoding="latin-1",
            )
            benc, ubody = html_to_unicode(
                content_type,
                self.body,
                auto_detect_fun=self._auto_detect_fun,
                default_encoding=self._DEFAULT_ENCODING,
            )
            self._cached_benc = benc
            self._cached_ubody = ubody
        return self._cached_benc

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::ContentLengthHeaderResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        return request.requestHeaders.getRawHeaders(b"content-length")[0]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::Compress.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        data = request.args.get(b"data")[0]

        accept_encoding_header = request.getHeader(b"accept-encoding")

        # include common encoding schemes here
        if accept_encoding_header == b"gzip":
            request.setHeader(b"Content-Encoding", b"gzip")
            return gzip.compress(data)

        # just set this to trigger a test failure if no valid accept-encoding header was set
        request.setResponseCode(500)
        return b"Did not receive a valid accept-encoding header"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.header_items [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def header_items(self) -> list[tuple[str, list[str]]]:
        return [
            (
                to_unicode(k, errors="replace"),
                [to_unicode(x, errors="replace") for x in v],
            )
            for k, v in self.request.headers.items()
        ]

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::EmptyContentTypeHeaderResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        request.setHeader("content-type", "")
        return request.content.read()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::BrokenDownloadResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py]
    def render(self, request):
        # only sends 3 bytes even though it claims to send 5
        request.setHeader(b"content-length", b"5")
        request.write(b"abc")
        return b""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware._handle_encoding [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py]
    def _handle_encoding(
        self, body: bytes, content_encoding: list[bytes], max_size: int
    ) -> tuple[bytes, list[bytes]]:
        to_decode, to_keep = self._split_encodings(content_encoding)
        for encoding in to_decode:
            body = self._decode(body, encoding, max_size)
        return body, to_keep

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.get_header [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def get_header(self, name: str, default: str | None = None) -> str | None:
        value = self.request.headers.get(name, default)
        return to_unicode(value, errors="replace") if value is not None else None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::ErrorResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py]
    def render(self, request):
        request.setResponseCode(401)
        if request.args.get(b"showlength"):
            request.setHeader(b"content-length", b"0")
        return b""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py]
    def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response:
        if request.method == "HEAD":
            return response
        if isinstance(response, Response):
            content_encoding = response.headers.getlist("Content-Encoding")
            if content_encoding:
                max_size = request.meta.get("download_maxsize", self._max_size)
                warn_size = request.meta.get("download_warnsize", self._warn_size)
                try:
                    decoded_body, content_encoding = self._handle_encoding(
                        response.body, content_encoding, max_size
                    )
                except _DecompressionMaxSizeExceeded as e:
                    raise IgnoreRequest(
                        f"Ignored response {response} because its body "
                        f"({len(response.body)} B compressed, "
                        f"{e.decompressed_size} B decompressed so far) exceeded "
                        f"DOWNLOAD_MAXSIZE ({max_size} B) during decompression."
                    ) from e
                if len(response.body) < warn_size <= len(decoded_body):
                    logger.warning(
                        f"{response} body size after decompression "
                        f"({len(decoded_body)} B) is larger than the "
                        f"download warning size ({warn_size} B)."
                    )
                if content_encoding:
                    self._warn_unknown_encoding(response, content_encoding)
                response.headers["Content-Encoding"] = content_encoding
                if self.stats:
                    self.stats.inc_value(
                        "httpcompression/response_bytes",
                        len(decoded_body),
                    )
                    self.stats.inc_value("httpcompression/response_count")
                respcls = responsetypes.from_args(
                    headers=response.headers, url=response.url, body=decoded_body
                )
                kwargs: dict[str, Any] = {"body": decoded_body}
                if issubclass(respcls, TextResponse):
                    # force recalculating the encoding until we make sure the
                    # responsetypes guessing is reliable
                    kwargs["encoding"] = None
                response = response.replace(cls=respcls, **kwargs)
                if not content_encoding:
                    del response.headers["Content-Encoding"]

        return response

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.has_header [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def has_header(self, name: str) -> bool:
        return name in self.request.headers

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::_has_ajaxcrawlable_meta [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py]
def _has_ajaxcrawlable_meta(text: str) -> bool:
    """
    >>> _has_ajaxcrawlable_meta('<html><head><meta name="fragment"  content="!"/></head><body></body></html>')
    True
    >>> _has_ajaxcrawlable_meta("<html><head><meta name='fragment' content='!'></head></html>")
    True
    >>> _has_ajaxcrawlable_meta('<html><head><!--<meta name="fragment"  content="!"/>--></head><body></body></html>')
    False
    >>> _has_ajaxcrawlable_meta('<html></html>')
    False
    """

    # Stripping scripts and comments is slow (about 20x slower than
    # just checking if a string is in text); this is a quick fail-fast
    # path that should work for most pages.
    if "fragment" not in text:
        return False
    if "content" not in text:
        return False

    text = html.remove_tags_with_content(text, ("script", "noscript"))
    text = html.replace_entities(text)
    text = html.remove_comments(text)
    return _ajax_crawlable_re.search(text) is not None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_ajaxcrawlable.py::TestAjaxCrawlMiddleware._ajaxcrawlable_body [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_ajaxcrawlable.py]
    def _ajaxcrawlable_body(self):
        return b'<html><head><meta name="fragment" content="!"/></head><body></body></html>'

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleEndHeaders [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def handleEndHeaders(self):
        self.factory.gotHeaders(self.headers)
```

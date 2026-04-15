# scrapy-18 :: minilm

query: More liberal Content-Disposition header parsing

## selected nodes

- rank=1 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=2 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::GCSFilesStore._get_content_type file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=3 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_disposition file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=4 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_type file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=5 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._headers_encoding file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=6 layer=FUNCTION tokens=259 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_body file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=7 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent._headers_from_twisted_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=8 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.get_header file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=9 layer=FUNCTION tokens=572 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/iterators.py::xmliter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/iterators.py
- rank=10 layer=FUNCTION tokens=568 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=11 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::RequestHeaders.render_GET file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=12 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::Echo.render_GET file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=13 layer=FUNCTION tokens=233 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._getresponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=14 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.to_string file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=15 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::CrawlerRun.headers_received file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=16 layer=FUNCTION tokens=475 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/iterators.py::csviter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/iterators.py
- rank=17 layer=FUNCTION tokens=309 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::_parse_headers_and_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py
- rank=18 layer=FUNCTION tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=19 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.headers_received file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._headers_encoding [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py]
    def _headers_encoding(self) -> str | None:
        content_type = self.headers.get(b"Content-Type") or b""
        return http_content_type_encoding(to_unicode(content_type, encoding="latin-1"))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_body [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py]
    def from_body(self, body: bytes) -> type[Response]:
        """Try to guess the appropriate response based on the body content.
        This method is a bit magic and could be improved in the future, but
        it's not meant to be used except for special cases where response types
        cannot be guess using more straightforward methods."""
        chunk = body[:5000]
        chunk = to_bytes(chunk)
        if not binary_is_text(chunk):
            return self.from_mimetype("application/octet-stream")
        lowercase_chunk = chunk.lower()
        if b"<html>" in lowercase_chunk:
            return self.from_mimetype("text/html")
        if b"<?xml" in lowercase_chunk:
            return self.from_mimetype("text/xml")
        if b"<!doctype html>" in lowercase_chunk:
            return self.from_mimetype("text/html")
        return self.from_mimetype("text")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent._headers_from_twisted_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def _headers_from_twisted_response(response: TxResponse) -> Headers:
        headers = Headers()
        if response.length != UNKNOWN_LENGTH:
            headers[b"Content-Length"] = str(response.length).encode()
        headers.update(response.headers.getAllRawHeaders())
        return headers

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.get_header [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def get_header(self, name: str, default: str | None = None) -> str | None:
        value = self.request.headers.get(name, default)
        return to_unicode(value, errors="replace") if value is not None else None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/iterators.py::xmliter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/iterators.py]
def xmliter(obj: Response | str | bytes, nodename: str) -> Iterator[Selector]:
    """Return a iterator of Selector's over all nodes of a XML document,
       given the name of the node to iterate. Useful for parsing XML feeds.

    obj can be:
    - a Response object
    - a unicode string
    - a string encoded as utf-8
    """
    warn(
        (
            "xmliter is deprecated and its use strongly discouraged because "
            "it is vulnerable to ReDoS attacks. Use xmliter_lxml instead. See "
            "https://github.com/scrapy/scrapy/security/advisories/GHSA-cc65-xxvf-f7r9"
        ),
        ScrapyDeprecationWarning,
        stacklevel=2,
    )

    nodename_patt = re.escape(nodename)

    DOCUMENT_HEADER_RE = re.compile(r"<\?xml[^>]+>\s*", re.DOTALL)
    HEADER_END_RE = re.compile(rf"<\s*/{nodename_patt}\s*>", re.DOTALL)
    END_TAG_RE = re.compile(r"<\s*/([^\s>]+)\s*>", re.DOTALL)
    NAMESPACE_RE = re.compile(r"((xmlns[:A-Za-z]*)=[^>\s]+)", re.DOTALL)
    text = _body_or_str(obj)

    document_header_match = re.search(DOCUMENT_HEADER_RE, text)
    document_header = (
        document_header_match.group().strip() if document_header_match else ""
    )
    header_end_idx = re_rsearch(HEADER_END_RE, text)
    header_end = text[header_end_idx[1] :].strip() if header_end_idx else ""
    namespaces: dict[str, str] = {}
    if header_end:
        for tagname in reversed(re.findall(END_TAG_RE, header_end)):
            assert header_end_idx
            tag = re.search(
                rf"<\s*{tagname}.*?xmlns[:=][^>]*>",
                text[: header_end_idx[1]],
                re.DOTALL,
            )
            if tag:
                for x in re.findall(NAMESPACE_RE, tag.group()):
                    namespaces[x[1]] = x[0]

    r = re.compile(rf"<{nodename_patt}[\s>].*?</{nodename_patt}>", re.DOTALL)
    for match in r.finditer(text):
        nodetext = (
            document_header
            + match.group().replace(
                nodename, f"{nodename} {' '.join(namespaces.values())}", 1
            )
            + header_end
        )
        yield Selector(text=nodetext, type="xml")

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::RequestHeaders.render_GET [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
    def render_GET(self, request: TxRequest):
        request.setHeader("Content-Type", "application/json; charset=UTF-8")
        request.setHeader("Content-Encoding", "UTF-8")
        headers = {}
        for k, v in request.requestHeaders.getAllRawHeaders():
            headers[str(k, "utf-8")] = str(v[0], "utf-8")

        return bytes(json.dumps(headers), "utf-8")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::Echo.render_GET [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render_GET(self, request):
        output = {
            "headers": {
                to_unicode(k): [to_unicode(v) for v in vs]
                for k, vs in request.requestHeaders.getAllRawHeaders()
            },
            "body": to_unicode(request.content.read()),
        }
        return to_bytes(json.dumps(output))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._getresponse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py]
    def _getresponse(self, coding):
        if coding not in FORMAT:
            raise ValueError

        samplefile, contentencoding = FORMAT[coding]

        body = (SAMPLEDIR / samplefile).read_bytes()

        headers = {
            "Server": "Yaws/1.49 Yet Another Web Server",
            "Date": "Sun, 08 Mar 2009 00:41:03 GMT",
            "Content-Length": len(body),
            "Content-Type": "text/html",
            "Content-Encoding": contentencoding,
        }

        response = Response("http://scrapytest.org/", body=body, headers=headers)
        response.request = Request(
            "http://scrapytest.org", headers={"Accept-Encoding": "gzip, deflate"}
        )
        return response

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.to_string [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def to_string(self) -> bytes:
        return headers_dict_to_raw(self)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::CrawlerRun.headers_received [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py]
    def headers_received(
        self, headers: Headers, body_length: int, request: Request, spider: Spider
    ) -> None:
        self.headers[request] = headers

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/iterators.py::csviter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/iterators.py]
def csviter(
    obj: Response | str | bytes,
    delimiter: str | None = None,
    headers: list[str] | None = None,
    encoding: str | None = None,
    quotechar: str | None = None,
) -> Iterator[dict[str, str]]:
    """Returns an iterator of dictionaries from the given csv object

    obj can be:
    - a Response object
    - a unicode string
    - a string encoded as utf-8

    delimiter is the character used to separate fields on the given obj.

    headers is an iterable that when provided offers the keys
    for the returned dictionaries, if not the first row is used.

    quotechar is the character used to enclosure fields on the given obj.
    """

    if encoding is not None:  # pragma: no cover
        warn(
            "The encoding argument of csviter() is ignored and will be removed"
            " in a future Scrapy version.",
            category=ScrapyDeprecationWarning,
            stacklevel=2,
        )

    lines = StringIO(_body_or_str(obj, unicode=True))

    kwargs: dict[str, Any] = {}
    if delimiter:
        kwargs["delimiter"] = delimiter
    if quotechar:
        kwargs["quotechar"] = quotechar
    csv_r = csv.reader(lines, **kwargs)

    if not headers:
        try:
            headers = next(csv_r)
        except StopIteration:
            return

    for row in csv_r:
        if len(row) != len(headers):
            logger.warning(
                "ignoring row %(csvlnum)d (length: %(csvrow)d, "
                "should be: %(csvheader)d)",
                {
                    "csvlnum": csv_r.line_num,
                    "csvrow": len(row),
                    "csvheader": len(headers),
                },
            )
            continue
        yield dict(zip(headers, row, strict=False))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::_parse_headers_and_cookies [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py]
def _parse_headers_and_cookies(
    parsed_args: argparse.Namespace,
) -> tuple[list[tuple[str, bytes]], dict[str, str]]:
    headers: list[tuple[str, bytes]] = []
    cookies: dict[str, str] = {}
    for header in parsed_args.headers or ():
        name, val = header.split(":", 1)
        name = name.strip()
        val = val.strip()
        if name.title() == "Cookie":
            for name, morsel in SimpleCookie(val).items():
                cookies[name] = morsel.value
        else:
            headers.append((name, val))

    for cookie_param in parsed_args.cookies or ():
        # curl can treat this parameter as either "key=value; key2=value2" pairs, or a filename.
        # Scrapy will only support key-value pairs.
        if "=" not in cookie_param:
            continue
        for name, morsel in SimpleCookie(cookie_param).items():
            cookies[name] = morsel.value

    if parsed_args.auth:
        user, password = parsed_args.auth.split(":", 1)
        headers.append(("Authorization", basic_auth_header(user, password)))

    return headers, cookies

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py]
    def add_options(self, parser: ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument("--spider", dest="spider", help="use this spider")
        parser.add_argument(
            "--headers",
            dest="headers",
            action="store_true",
            help="print response HTTP headers instead of body",
        )
        parser.add_argument(
            "--no-redirect",
            dest="no_redirect",
            action="store_true",
            default=False,
            help="do not handle HTTP 3xx status codes and print response as-is",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.headers_received [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def headers_received(self, headers, body_length, request, spider):
        self.meta["headers_received"] = headers
        raise StopDownload(fail=False)
```

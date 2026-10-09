# scrapy-18 :: tacm-full

query: More liberal Content-Disposition header parsing

## selected nodes

- rank=1 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_disposition file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=2 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=3 layer=FUNCTION tokens=598 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::S3FilesStore._headers_to_botocore_kwargs file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=4 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=5 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_GET file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=6 layer=FUNCTION tokens=405 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_POST_json file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=7 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=8 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=9 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::ResponseHeadersResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=10 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_type file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=11 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::_print_commands file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py
- rank=12 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._log_warnsize file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=13 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::Compress.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=14 layer=FUNCTION tokens=982 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._read_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=15 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::CurlParser.error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py
- rank=16 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_cb_kwargs.py::KeywordArgumentsSpider.parse_takes_more file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_cb_kwargs.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::S3FilesStore._headers_to_botocore_kwargs [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py]
    def _headers_to_botocore_kwargs(self, headers: dict[str, Any]) -> dict[str, Any]:
        """Convert headers to botocore keyword arguments."""
        # This is required while we need to support both boto and botocore.
        mapping = CaseInsensitiveDict(
            {
                "Content-Type": "ContentType",
                "Cache-Control": "CacheControl",
                "Content-Disposition": "ContentDisposition",
                "Content-Encoding": "ContentEncoding",
                "Content-Language": "ContentLanguage",
                "Content-Length": "ContentLength",
                "Content-MD5": "ContentMD5",
                "Expires": "Expires",
                "X-Amz-Grant-Full-Control": "GrantFullControl",
                "X-Amz-Grant-Read": "GrantRead",
                "X-Amz-Grant-Read-ACP": "GrantReadACP",
                "X-Amz-Grant-Write-ACP": "GrantWriteACP",
                "X-Amz-Object-Lock-Legal-Hold": "ObjectLockLegalHoldStatus",
                "X-Amz-Object-Lock-Mode": "ObjectLockMode",
                "X-Amz-Object-Lock-Retain-Until-Date": "ObjectLockRetainUntilDate",
                "X-Amz-Request-Payer": "RequestPayer",
                "X-Amz-Server-Side-Encryption": "ServerSideEncryption",
                "X-Amz-Server-Side-Encryption-Aws-Kms-Key-Id": "SSEKMSKeyId",
                "X-Amz-Server-Side-Encryption-Context": "SSEKMSEncryptionContext",
                "X-Amz-Server-Side-Encryption-Customer-Algorithm": "SSECustomerAlgorithm",
                "X-Amz-Server-Side-Encryption-Customer-Key": "SSECustomerKey",
                "X-Amz-Server-Side-Encryption-Customer-Key-Md5": "SSECustomerKeyMD5",
                "X-Amz-Storage-Class": "StorageClass",
                "X-Amz-Tagging": "Tagging",
                "X-Amz-Website-Redirect-Location": "WebsiteRedirectLocation",
            }
        )
        extra: dict[str, Any] = {}
        for key, value in headers.items():
            try:
                kwarg = mapping[key]
            except KeyError:
                raise TypeError(
                    f'Header "{key}" is not supported by botocore'
                ) from None
            extra[kwarg] = value
        return extra

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_GET [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
    async def _check_GET(
        self,
        client: H2ClientProtocol,
        request: Request,
        expected_body: bytes,
        expected_status: int,
    ) -> None:
        response = await make_request(client, request)
        assert response.status == expected_status
        assert response.body == expected_body

        content_length_header = response.headers.get("Content-Length")
        assert content_length_header is not None
        content_length = int(content_length_header)
        assert len(response.body) == content_length

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_POST_json [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
    async def _check_POST_json(
        client: H2ClientProtocol,
        request: Request,
        expected_request_body: dict[str, str],
        expected_extra_data: str,
        expected_status: int,
    ) -> None:
        response = await make_request(client, request)

        assert response.status == expected_status

        content_length_header = response.headers.get("Content-Length")
        assert content_length_header is not None
        content_length = int(content_length_header)
        assert len(response.body) == content_length

        # Parse the body
        content_encoding_header = response.headers[b"Content-Encoding"]
        assert content_encoding_header is not None
        content_encoding = str(content_encoding_header, "utf-8")
        body = json.loads(str(response.body, content_encoding))
        assert "request-body" in body
        assert "extra-data" in body
        assert "request-headers" in body

        request_body = body["request-body"]
        assert request_body == expected_request_body

        extra_data = body["extra-data"]
        assert extra_data == expected_extra_data

        # Check if headers were sent successfully
        request_headers = body["request-headers"]
        for k, v in request.headers.items():
            k_str = str(k, "utf-8")
            assert k_str in request_headers
            assert request_headers[k_str] == str(v[0], "utf-8")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::ResponseHeadersResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        body = json.loads(request.content.read().decode())
        for header_name, header_value in body.items():
            request.responseHeaders.addRawHeader(header_name, header_value)
        return json.dumps(body).encode("utf-8")

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::_print_commands [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py]
def _print_commands(settings: BaseSettings, inproject: bool) -> None:
    _print_header(settings, inproject)
    print(
        "Usage:\n",
        "  scrapy <command> [options] [args]\n",
        "Available commands:\n",
    )
    cmds = _get_commands_dict(settings, inproject)
    print(
        "\n".join(
            f"  {cmdname:<13} {cmdclass.short_desc()}"
            for cmdname, cmdclass in sorted(cmds.items())
        )
    )
    if not inproject:
        print(
            "\n",
            "  [ more ]      More commands available when run from project directory",
        )
    print("\n", 'Use "scrapy <command> -h" to see more info about a command')

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._log_warnsize [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py]
    def _log_warnsize(self) -> bool:
        """Checks if we have received data which exceeds the download warnsize
        and whether we have not already logged about it.

        Returns:
            True if both the above conditions hold true
            False if any of the conditions is false
        """
        content_length_header = int(
            self._response["headers"].get(b"Content-Length", -1)
        )
        return (
            self._download_warnsize
            and (
                self._response["flow_controlled_size"] > self._download_warnsize
                or content_length_header > self._download_warnsize
            )
            and not self.metadata["reached_warnsize"]
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._read_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py]
    async def _read_response(
        self, httpx_response: httpx.Response, request: Request
    ) -> Response:
        maxsize: int = request.meta.get("download_maxsize", self._default_maxsize)
        warnsize: int = request.meta.get("download_warnsize", self._default_warnsize)

        content_length = httpx_response.headers.get("Content-Length")
        expected_size = int(content_length) if content_length is not None else None
        if maxsize and expected_size and expected_size > maxsize:
            self._cancel_maxsize(expected_size, maxsize, request, expected=True)

        reached_warnsize = False
        if warnsize and expected_size and expected_size > warnsize:
            reached_warnsize = True
            logger.warning(
                get_warnsize_msg(expected_size, warnsize, request, expected=True)
            )

        headers = Headers(httpx_response.headers.multi_items())
        network_stream: AsyncNetworkStream = httpx_response.extensions["network_stream"]

        make_response_base_args: _BaseResponseArgs = {
            "status": httpx_response.status_code,
            "url": request.url,
            "headers": headers,
            "ip_address": self._get_server_ip(network_stream),
            "protocol": httpx_response.http_version,
        }

        self._log_tls_info(network_stream)

        if stop_download := check_stop_download(
            signals.headers_received,
            self.crawler,
            request,
            headers=headers,
            body_length=expected_size,
        ):
            return make_response(
                **make_response_base_args,
                stop_download=stop_download,
            )

        response_body = BytesIO()
        bytes_received = 0
        try:
            async for chunk in httpx_response.aiter_raw():
                response_body.write(chunk)
                bytes_received += len(chunk)

                if stop_download := check_stop_download(
                    signals.bytes_received, self.crawler, request, data=chunk
                ):
                    return make_response(
                        **make_response_base_args,
                        body=response_body.getvalue(),
                        stop_download=stop_download,
                    )

                if maxsize and bytes_received > maxsize:
                    response_body.truncate(0)
                    self._cancel_maxsize(
                        bytes_received, maxsize, request, expected=False
                    )

                if warnsize and bytes_received > warnsize and not reached_warnsize:
                    reached_warnsize = True
                    logger.warning(
                        get_warnsize_msg(
                            bytes_received, warnsize, request, expected=False
                        )
                    )
        except httpx.RemoteProtocolError as e:
            # special handling of the dataloss case
            if (
                "peer closed connection without sending complete message body"
                not in str(e)
            ):
                raise
            fail_on_dataloss: bool = request.meta.get(
                "download_fail_on_dataloss", self._fail_on_dataloss
            )
            if not fail_on_dataloss:
                return make_response(
                    **make_response_base_args,
                    body=response_body.getvalue(),
                    flags=["dataloss"],
                )
            self._log_dataloss_warning(request.url)
            raise ResponseDataLossError(str(e)) from e

        return make_response(
            **make_response_base_args,
            body=response_body.getvalue(),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::CurlParser.error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py]
    def error(self, message: str) -> NoReturn:
        error_msg = f"There was an error parsing the curl command: {message}"
        raise ValueError(error_msg)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_cb_kwargs.py::KeywordArgumentsSpider.parse_takes_more [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_cb_kwargs.py]
    def parse_takes_more(self, response, key, number, callback, other):
        """
        Should raise
        TypeError: parse_takes_more() missing 1 required positional argument: 'other'
        """
```

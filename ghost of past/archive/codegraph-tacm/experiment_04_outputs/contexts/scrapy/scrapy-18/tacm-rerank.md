# scrapy-18 :: tacm-rerank

query: More liberal Content-Disposition header parsing

## selected nodes

- rank=1 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_disposition file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=2 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=3 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.from_content_type file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=4 layer=FUNCTION tokens=598 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::S3FilesStore._headers_to_botocore_kwargs file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=5 layer=FUNCTION tokens=697 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py
- rank=6 layer=FUNCTION tokens=982 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._read_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=7 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=8 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=9 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=10 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_GET file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=11 layer=FUNCTION tokens=405 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_POST_json file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=12 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py::TestFTPFeedStorage._store file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py::TestFTPFeedStorage._store [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_storages.py]
    async def _store(self, uri, content, feed_options=None, settings=None):
        crawler = get_crawler(settings_dict=settings or {})
        storage = FTPFeedStorage.from_crawler(
            crawler,
            uri,
            feed_options=feed_options,
        )
        verifyObject(IFeedStorage, storage)
        spider = self.get_test_spider()
        file = storage.open(spider)
        file.write(content)
        await maybe_deferred_to_future(storage.store(file))
```

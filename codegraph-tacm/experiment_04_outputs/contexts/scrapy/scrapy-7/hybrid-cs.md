# scrapy-7 :: hybrid-cs

query: FormRequest: handle whitespaces in action attribute properly

## selected nodes

- rank=1 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_form_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=2 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=3 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=4 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=5 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=6 layer=FUNCTION tokens=328 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=7 layer=FUNCTION tokens=378 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_form file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=8 layer=FUNCTION tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=9 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::attribute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=10 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py::TestSettingsAttribute.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py
- rank=11 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.custom_form file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=12 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py
- rank=13 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomFormContract.adjust_request_args file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=14 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=15 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::warn_on_deprecated_spider_attribute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=16 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomFailContract.adjust_request_args file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=17 layer=FUNCTION tokens=262 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::NO_CALLBACK file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=18 layer=FUNCTION tokens=233 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::FormRequest.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=19 layer=FUNCTION tokens=504 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=20 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py
- rank=21 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_form_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py]
def _get_form_url(form: FormElement, url: str | None) -> str:
    assert form.base_url is not None  # typing
    if url is None:
        action = form.get("action")
        if action is None:
            return form.base_url
        return urljoin(form.base_url, strip_html5_whitespace(action))
    return urljoin(form.base_url, url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py]
    def _assert_request_no3xx(self, pipeline_class, settings):
        pipe = pipeline_class(crawler=get_crawler(None, settings))
        request = Request("http://url")
        pipe._modify_media_request(request)

        assert "handle_httpstatus_list" in request.meta
        for status, check in [
            (200, True),
            # These are the status codes we want
            # the downloader to handle itself
            (301, False),
            (302, False),
            (302, False),
            (307, False),
            (308, False),
            # we still want to get 4xx and 5xx
            (400, True),
            (404, True),
            (500, True),
        ]:
            if check:
                assert status in request.meta["handle_httpstatus_list"]
            else:
                assert status not in request.meta["handle_httpstatus_list"]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py]
    def process_spider_input(
        self, response: Response, spider: Spider | None = None
    ) -> None:
        if 200 <= response.status < 300:  # common case
            return
        meta = response.meta
        if meta.get("handle_httpstatus_all", False):
            return
        if "handle_httpstatus_list" in meta:
            allowed_statuses = meta["handle_httpstatus_list"]
        elif self.handle_httpstatus_all:
            return
        else:
            allowed_statuses = getattr(
                self.crawler.spider,
                "handle_httpstatus_list",
                self.handle_httpstatus_list,
            )
        if response.status in allowed_statuses:
            return
        raise HttpError(response, "Ignoring non-200 response")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _modify_media_request(self, request: Request) -> None:
        if self.handle_httpstatus_list:
            request.meta["handle_httpstatus_list"] = self.handle_httpstatus_list
        else:
            request.meta["handle_httpstatus_all"] = True

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py]
    def run(self, args: list[str], opts: Namespace) -> None:
        if len(args) != 1 or not is_url(args[0]):
            raise UsageError
        request = Request(
            args[0],
            callback=self._print_response,
            cb_kwargs={"opts": opts},
            dont_filter=True,
        )
        # by default, let the framework handle redirects,
        # i.e. command handles all codes expect 3xx
        if not opts.no_redirect:
            request.meta["handle_httpstatus_list"] = SequenceExclude(range(300, 400))
        else:
            request.meta["handle_httpstatus_all"] = True

        spidercls: type[Spider] = DefaultSpider
        assert self.crawler_process
        spider_loader = self.crawler_process.spider_loader
        if opts.spider:
            spidercls = spider_loader.load(opts.spider)
        else:
            spidercls = spidercls_for_request(spider_loader, request, spidercls)

        async def start(self: Spider) -> AsyncIterator[Any]:
            yield request

        spidercls.start = start  # type: ignore[method-assign]

        self.crawler_process.crawl(spidercls)
        self.crawler_process.start()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_form [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py]
def _get_form(
    response: TextResponse,
    formname: str | None,
    formid: str | None,
    formnumber: int,
    formxpath: str | None,
) -> FormElement:
    """Find the wanted form element within the given response."""
    root = response.selector.root
    forms = root.xpath("//form")
    if not forms:
        raise ValueError(f"No <form> element found in {response}")

    if formname is not None:
        f = root.xpath(f'//form[@name="{formname}"]')
        if f:
            return cast("FormElement", f[0])

    if formid is not None:
        f = root.xpath(f'//form[@id="{formid}"]')
        if f:
            return cast("FormElement", f[0])

    # Get form element from xpath, if not found, go up
    if formxpath is not None:
        nodes = root.xpath(formxpath)
        if nodes:
            el = nodes[0]
            while True:
                if el.tag == "form":
                    return cast("FormElement", el)
                el = el.getparent()
                if el is None:
                    break
        raise ValueError(f"No <form> element found with {formxpath}")

    # If we get here, it means that either formname was None or invalid
    try:
        form = forms[formnumber]
    except IndexError:
        raise IndexError(f"Form number {formnumber} not found in {response}") from None
    return cast("FormElement", form)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::attribute [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py]
def attribute(obj: Any, oldattr: str, newattr: str, version: str = "0.12") -> None:
    cname = obj.__class__.__name__
    warnings.warn(
        f"{cname}.{oldattr} attribute is deprecated and will be no longer supported "
        f"in Scrapy {version}, use {cname}.{newattr} attribute instead",
        ScrapyDeprecationWarning,
        stacklevel=3,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py::TestSettingsAttribute.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py]
    def setup_method(self):
        self.attribute = SettingsAttribute("value", 10)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.custom_form [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def custom_form(self, response):
        """
        @url http://scrapy.org
        @custom_form
        """

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py]
    def add_options(self, parser: ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-c",
            dest="code",
            help="evaluate the code in the shell, print the result and exit",
        )
        parser.add_argument("--spider", dest="spider", help="use this spider")
        parser.add_argument(
            "--no-redirect",
            dest="no_redirect",
            action="store_true",
            default=False,
            help="do not handle HTTP 3xx status codes and print response as-is",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomFormContract.adjust_request_args [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def adjust_request_args(self, args):
        args["formdata"] = {"name": "scrapy"}
        return args

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py]
            def __init__(self, *args, **kwargs):  # pylint: disable=useless-parent-delegation
                # This call to super() trigger the __classcell__ propagation
                # requirement. When not done properly raises an error:
                # TypeError: __class__ set to <class '__main__.MyItem'>
                # defining 'MyItem' as <class '__main__.MyItem'>
                super().__init__(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::warn_on_deprecated_spider_attribute [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py]
def warn_on_deprecated_spider_attribute(attribute_name: str, setting_name: str) -> None:
    warnings.warn(
        f"The '{attribute_name}' spider attribute is deprecated. "
        "Use Spider.custom_settings or Spider.update_settings() instead. "
        f"The corresponding setting name is '{setting_name}'.",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomFailContract.adjust_request_args [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def adjust_request_args(self, args):
        raise TypeError("Error in adjust_request_args")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::NO_CALLBACK [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py]
def NO_CALLBACK(*args: Any, **kwargs: Any) -> NoReturn:
    """When assigned to the ``callback`` parameter of
    :class:`~scrapy.Request`, it indicates that the request is not meant
    to have a spider callback at all.

    For example:

    .. code-block:: python

       Request("https://example.com", callback=NO_CALLBACK)

    This value should be used by :ref:`components <topics-components>` that
    create and handle their own requests, e.g. through
    :meth:`scrapy.core.engine.ExecutionEngine.download`, so that downloader
    middlewares handling such requests can treat them differently from requests
    intended for the :meth:`~scrapy.Spider.parse` callback.
    """
    raise RuntimeError(
        "The NO_CALLBACK callback has been called. This is a special callback "
        "value intended for requests whose callback is never meant to be "
        "called."
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::FormRequest.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py]
    def __init__(
        self, *args: Any, formdata: FormdataType = None, **kwargs: Any
    ) -> None:
        if formdata and kwargs.get("method") is None:
            kwargs["method"] = "POST"

        super().__init__(*args, **kwargs)

        if formdata:
            items = formdata.items() if isinstance(formdata, dict) else formdata
            form_query_str = _urlencode(items, self.encoding)
            if self.method == "POST":
                self.headers.setdefault(
                    b"Content-Type", b"application/x-www-form-urlencoded"
                )
                self._set_body(form_query_str)
            else:
                self._set_url(
                    urlunsplit(urlsplit(self.url)._replace(query=form_query_str))
                )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response:
        if (
            request.meta.get("dont_redirect", False)
            or response.status
            in getattr(self.crawler.spider, "handle_httpstatus_list", ())
            or response.status in request.meta.get("handle_httpstatus_list", ())
            or request.meta.get("handle_httpstatus_all", False)
        ):
            return response

        if "Location" not in response.headers or response.status not in {
            301,
            302,
            303,
            307,
            308,
        }:
            return response

        assert response.headers["Location"] is not None
        location = safe_url_string(response.headers["Location"])
        if response.headers["Location"].startswith(b"//"):
            request_scheme = urlparse_cached(request).scheme
            location = request_scheme + "://" + location.lstrip("/")

        redirected_url = urljoin(request.url, location)

        if not urlparse(redirected_url).fragment:
            fragment = urlparse_cached(request).fragment
            if fragment:
                redirected_url = urljoin(redirected_url, f"#{fragment}")

        redirected = self._build_redirect_request(request, response, url=redirected_url)
        if urlparse_cached(redirected).scheme not in {"http", "https"}:
            return response

        if (response.status in {301, 302} and request.method == "POST") or (
            response.status == 303 and request.method not in {"GET", "HEAD"}
        ):
            redirected = self._redirect_request_using_get(
                request, response, redirected_url
            )

        return self._redirect(redirected, request, response.status)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-l",
            "--list",
            dest="list",
            action="store_true",
            help="only list contracts, without checking them",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            default=False,
            action="store_true",
            help="print contract tests for all spiders",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py]
    def handle_spider_output(
        self,
        result: Iterable[_T] | AsyncIterator[_T],
        request: Request,
        response: Response | Failure,
        spider: Spider | None = None,
    ) -> Deferred[None]:  # pragma: no cover
        """Pass items/requests produced by a callback to ``_process_spidermw_output()`` in parallel."""
        warnings.warn(
            "Scraper.handle_spider_output() is deprecated, use handle_spider_output_async() instead",
            ScrapyDeprecationWarning,
            stacklevel=2,
        )
        return deferred_from_coro(
            self.handle_spider_output_async(result, request, response)
        )
```

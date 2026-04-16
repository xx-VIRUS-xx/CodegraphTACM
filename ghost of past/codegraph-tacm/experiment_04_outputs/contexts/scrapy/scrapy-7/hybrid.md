# scrapy-7 :: hybrid

query: FormRequest: handle whitespaces in action attribute properly

## selected nodes

- rank=1 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_form_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=2 layer=FUNCTION tokens=286 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::BaseRunSpiderCommand.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=3 layer=FUNCTION tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=4 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py
- rank=5 layer=FUNCTION tokens=194 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::_url_from_selector file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=6 layer=FUNCTION tokens=583 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=7 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::attribute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=8 layer=FUNCTION tokens=303 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py
- rank=9 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py
- rank=10 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=11 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomFailContract.adjust_request_args file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=12 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py
- rank=13 layer=FUNCTION tokens=303 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::FormRequest.from_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=14 layer=FUNCTION tokens=208 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/rpc.py::XmlRpcRequest.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/rpc.py
- rank=15 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/feed.py::XMLFeedSpider._register_namespaces file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/feed.py
- rank=16 layer=FUNCTION tokens=380 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_inputs file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=17 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=18 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomFormContract.adjust_request_args file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=19 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=20 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::MethodsSpider.handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::BaseRunSpiderCommand.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-a",
            dest="spargs",
            action="append",
            default=[],
            metavar="NAME=VALUE",
            help="set spider argument (may be repeated)",
        )
        parser.add_argument(
            "-o",
            "--output",
            metavar="FILE",
            action="append",
            help="append scraped items to the end of FILE (use - for stdout),"
            " to define format set a colon at the end of the output URI (i.e. -o FILE:FORMAT)",
        )
        parser.add_argument(
            "-O",
            "--overwrite-output",
            metavar="FILE",
            action="append",
            help="dump scraped items into FILE, overwriting any existing file,"
            " to define format set a colon at the end of the output URI (i.e. -O FILE:FORMAT)",
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::_url_from_selector [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py]
def _url_from_selector(sel: parsel.Selector) -> str:
    if isinstance(sel.root, str):
        # e.g. ::attr(href) result
        return strip_html5_whitespace(sel.root)
    if not hasattr(sel.root, "tag"):
        raise _InvalidSelector(f"Unsupported selector: {sel}")
    if sel.root.tag not in {"a", "link"}:
        raise _InvalidSelector(
            f"Only <a> and <link> elements are supported; got <{sel.root.tag}>"
        )
    href = sel.root.get("href")
    if href is None:
        raise _InvalidSelector(f"<{sel.root.tag}> element has no href attribute: {sel}")
    return strip_html5_whitespace(href)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "--spider",
            dest="spider",
            default=None,
            help="use this spider without looking for one",
        )
        parser.add_argument(
            "--pipelines", action="store_true", help="process items through pipelines"
        )
        parser.add_argument(
            "--nolinks",
            dest="nolinks",
            action="store_true",
            help="don't show links to follow (extracted requests)",
        )
        parser.add_argument(
            "--noitems",
            dest="noitems",
            action="store_true",
            help="don't show scraped items",
        )
        parser.add_argument(
            "--nocolour",
            dest="nocolour",
            action="store_true",
            help="avoid using pygments to colorize the output",
        )
        parser.add_argument(
            "-r",
            "--rules",
            dest="rules",
            action="store_true",
            help="use CrawlSpider rules to discover the callback",
        )
        parser.add_argument(
            "-c",
            "--callback",
            dest="callback",
            help="use this callback for parsing, instead looking for a callback",
        )
        parser.add_argument(
            "-m",
            "--meta",
            dest="meta",
            help="inject extra meta into the Request, it must be a valid raw json string",
        )
        parser.add_argument(
            "--cbkwargs",
            dest="cbkwargs",
            help="inject extra callback kwargs into the Request, it must be a valid raw json string",
        )
        parser.add_argument(
            "-d",
            "--depth",
            dest="depth",
            type=int,
            default=1,
            help="maximum depth for parsing requests [default: %(default)s]",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            action="store_true",
            help="print each depth level one by one",
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-l",
            "--list",
            dest="list",
            action="store_true",
            help="List available templates",
        )
        parser.add_argument(
            "-e",
            "--edit",
            dest="edit",
            action="store_true",
            help="Edit spider after creating it",
        )
        parser.add_argument(
            "-d",
            "--dump",
            dest="dump",
            metavar="TEMPLATE",
            help="Dump template to standard output",
        )
        parser.add_argument(
            "-t",
            "--template",
            dest="template",
            default="basic",
            help="Uses a custom template.",
        )
        parser.add_argument(
            "--force",
            dest="force",
            action="store_true",
            help="If the spider already exists, overwrite it with the template",
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _modify_media_request(self, request: Request) -> None:
        if self.handle_httpstatus_list:
            request.meta["handle_httpstatus_list"] = self.handle_httpstatus_list
        else:
            request.meta["handle_httpstatus_all"] = True

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomFailContract.adjust_request_args [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def adjust_request_args(self, args):
        raise TypeError("Error in adjust_request_args")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
def handle_error(failure):
    pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::FormRequest.from_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py]
    def from_response(
        cls,
        response: TextResponse,
        formname: str | None = None,
        formid: str | None = None,
        formnumber: int = 0,
        formdata: FormdataType = None,
        clickdata: dict[str, str | int] | None = None,
        dont_click: bool = False,
        formxpath: str | None = None,
        formcss: str | None = None,
        **kwargs: Any,
    ) -> Self:
        kwargs.setdefault("encoding", response.encoding)

        if formcss is not None:
            formxpath = HTMLTranslator().css_to_xpath(formcss)

        form = _get_form(response, formname, formid, formnumber, formxpath)
        formdata = _get_inputs(form, formdata, dont_click, clickdata)
        url = _get_form_url(form, kwargs.pop("url", None))

        method = kwargs.pop("method", form.method)
        if method is not None:
            method = method.upper()
            if method not in cls.valid_form_methods:
                method = "GET"

        return cls(url=url, method=method, formdata=formdata, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/rpc.py::XmlRpcRequest.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/rpc.py]
    def __init__(self, *args: Any, encoding: str | None = None, **kwargs: Any):
        if "body" not in kwargs and "params" in kwargs:
            kw = {k: kwargs.pop(k) for k in DUMPS_ARGS if k in kwargs}
            kwargs["body"] = xmlrpclib.dumps(**kw)

        # spec defines that requests must use POST method
        kwargs.setdefault("method", "POST")

        # xmlrpc query multiples times over the same url
        kwargs.setdefault("dont_filter", True)

        # restore encoding
        if encoding is not None:
            kwargs["encoding"] = encoding

        super().__init__(*args, **kwargs)
        self.headers.setdefault("Content-Type", "text/xml")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/feed.py::XMLFeedSpider._register_namespaces [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/feed.py]
    def _register_namespaces(self, selector: Selector) -> None:
        for prefix, uri in self.namespaces:
            selector.register_namespace(prefix, uri)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_inputs [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py]
def _get_inputs(
    form: FormElement,
    formdata: FormdataType,
    dont_click: bool,
    clickdata: dict[str, str | int] | None,
) -> list[FormdataKVType]:
    """Return a list of key-value pairs for the inputs found in the given form."""
    try:
        formdata_keys = dict(formdata or ()).keys()
    except (ValueError, TypeError):
        raise ValueError("formdata should be a dict or iterable of tuples") from None

    if not formdata:
        formdata = []
    inputs = form.xpath(
        "descendant::textarea"
        "|descendant::select"
        "|descendant::input[not(@type) or @type["
        ' not(re:test(., "^(?:submit|image|reset)$", "i"))'
        " and (../@checked or"
        '  not(re:test(., "^(?:checkbox|radio)$", "i")))]]',
        namespaces={"re": "http://exslt.org/regular-expressions"},
    )
    values: list[FormdataKVType] = [
        (k, "" if v is None else v)
        for k, v in (_value(e) for e in inputs)
        if k and k not in formdata_keys
    ]

    if not dont_click:
        clickable = _get_clickable(clickdata, form)
        if clickable and clickable[0] not in formdata and clickable[0] is not None:
            values.append(clickable)

    formdata_items = formdata.items() if isinstance(formdata, dict) else formdata
    values.extend((k, v) for k, v in formdata_items if v is not None)
    return values

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomFormContract.adjust_request_args [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def adjust_request_args(self, args):
        args["formdata"] = {"name": "scrapy"}
        return args

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::MethodsSpider.handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
    def handle_error(self, failure):
        pass
```

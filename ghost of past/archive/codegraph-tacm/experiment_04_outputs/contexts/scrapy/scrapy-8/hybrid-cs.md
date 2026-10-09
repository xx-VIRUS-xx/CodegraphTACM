# scrapy-8 :: hybrid-cs

query: BUG: Fix __classcell__ propagation.

## selected nodes

- rank=1 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=2 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::ItemMeta.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py
- rank=3 layer=FUNCTION tokens=1243 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::create_deprecated_class file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=4 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyHelpFormatter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=5 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::DeprecatedClass.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=6 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/version.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/version.py
- rank=7 layer=FUNCTION tokens=445 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/utils/linkfix.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/utils/linkfix.py
- rank=8 layer=FUNCTION tokens=237 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.enqueue_scrape file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=9 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapyfixautodoc.py::maybe_skip_member file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapyfixautodoc.py
- rank=10 layer=FUNCTION tokens=370 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/console.py::_embed_ipython_shell file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/console.py
- rank=11 layer=FUNCTION tokens=399 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=12 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=13 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineCloseSpider.cb file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=14 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapydocs.py::make_setting_element file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapydocs.py
- rank=15 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_python.py::Callable.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_python.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py]
            def __init__(self, *args, **kwargs):  # pylint: disable=useless-parent-delegation
                # This call to super() trigger the __classcell__ propagation
                # requirement. When not done properly raises an error:
                # TypeError: __class__ set to <class '__main__.MyItem'>
                # defining 'MyItem' as <class '__main__.MyItem'>
                super().__init__(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::ItemMeta.__new__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py]
    def __new__(
        mcs, class_name: str, bases: tuple[type, ...], attrs: dict[str, Any]
    ) -> ItemMeta:
        classcell = attrs.pop("__classcell__", None)
        new_bases = tuple(base._class for base in bases if hasattr(base, "_class"))
        _class = super().__new__(mcs, "x_" + class_name, new_bases, attrs)

        fields = getattr(_class, "fields", {})
        new_attrs = {}
        for n in dir(_class):
            v = getattr(_class, n)
            if isinstance(v, Field):
                fields[n] = v
            elif n in attrs:
                new_attrs[n] = attrs[n]

        new_attrs["fields"] = fields
        new_attrs["_class"] = _class
        if classcell is not None:
            new_attrs["__classcell__"] = classcell
        return super().__new__(mcs, class_name, bases, new_attrs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::create_deprecated_class [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py]
def create_deprecated_class(
    name: str,
    new_class: type,
    clsdict: dict[str, Any] | None = None,
    warn_category: type[Warning] = ScrapyDeprecationWarning,
    warn_once: bool = True,
    old_class_path: str | None = None,
    new_class_path: str | None = None,
    subclass_warn_message: str = "{cls} inherits from deprecated class {old}, please inherit from {new}.",
    instance_warn_message: str = "{cls} is deprecated, instantiate {new} instead.",
) -> type:
    """
    Return a "deprecated" class that causes its subclasses to issue a warning.
    Subclasses of ``new_class`` are considered subclasses of this class.
    It also warns when the deprecated class is instantiated, but do not when
    its subclasses are instantiated.

    It can be used to rename a base class in a library. For example, if we
    have

        class OldName(SomeClass):
            # ...

    and we want to rename it to NewName, we can do the following::

        class NewName(SomeClass):
            # ...

        OldName = create_deprecated_class('OldName', NewName)

    Then, if user class inherits from OldName, warning is issued. Also, if
    some code uses ``issubclass(sub, OldName)`` or ``isinstance(sub(), OldName)``
    checks they'll still return True if sub is a subclass of NewName instead of
    OldName.
    """

    # https://github.com/python/mypy/issues/4177
    class DeprecatedClass(new_class.__class__):  # type: ignore[misc,name-defined]
        # pylint: disable=no-self-argument
        deprecated_class: type | None = None
        warned_on_subclass: bool = False

        def __new__(  # pylint: disable=bad-classmethod-argument
            metacls, name: str, bases: tuple[type, ...], clsdict_: dict[str, Any]
        ) -> type:
            cls = super().__new__(metacls, name, bases, clsdict_)
            if metacls.deprecated_class is None:
                metacls.deprecated_class = cls
            return cls

        def __init__(cls, name: str, bases: tuple[type, ...], clsdict_: dict[str, Any]):
            meta = cls.__class__
            old = meta.deprecated_class
            if old in bases and not (warn_once and meta.warned_on_subclass):
                meta.warned_on_subclass = True
                msg = subclass_warn_message.format(
                    cls=_clspath(cls),
                    old=_clspath(old, old_class_path),
                    new=_clspath(new_class, new_class_path),
                )
                if warn_once:
                    msg += " (warning only on first subclass, there may be others)"
                warnings.warn(msg, warn_category, stacklevel=2)
            super().__init__(name, bases, clsdict_)

        # see https://www.python.org/dev/peps/pep-3119/#overloading-isinstance-and-issubclass
        # and https://docs.python.org/reference/datamodel.html#customizing-instance-and-subclass-checks
        # for implementation details
        def __instancecheck__(cls, inst: Any) -> bool:
            return any(cls.__subclasscheck__(c) for c in (type(inst), inst.__class__))

        def __subclasscheck__(cls, sub: type) -> bool:
            if cls is not DeprecatedClass.deprecated_class:
                # we should do the magic only if second `issubclass` argument
                # is the deprecated class itself - subclasses of the
                # deprecated class should not use custom `__subclasscheck__`
                # method.
                return super().__subclasscheck__(sub)

            if not inspect.isclass(sub):
                raise TypeError("issubclass() arg 1 must be a class")

            mro = getattr(sub, "__mro__", ())
            return any(c in {cls, new_class} for c in mro)

        def __call__(cls, *args: Any, **kwargs: Any) -> Any:
            old = DeprecatedClass.deprecated_class
            if cls is old:
                msg = instance_warn_message.format(
                    cls=_clspath(cls, old_class_path),
                    new=_clspath(new_class, new_class_path),
                )
                warnings.warn(msg, warn_category, stacklevel=2)
            return super().__call__(*args, **kwargs)

    deprecated_cls = DeprecatedClass(name, (new_class,), clsdict or {})

    try:
        frm = inspect.stack()[1]
        parent_module = inspect.getmodule(frm[0])
        if parent_module is not None:
            deprecated_cls.__module__ = parent_module.__name__
    except Exception as e:
        # Sometimes inspect.stack() fails (e.g. when the first import of
        # deprecated class is in jinja2 template). __module__ attribute is not
        # important enough to raise an exception as users may be unable
        # to fix inspect.stack() errors.
        warnings.warn(f"Error detecting parent module: {e!r}", stacklevel=2)

    return deprecated_cls

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyHelpFormatter.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py]
    def __init__(
        self,
        prog: str,
        indent_increment: int = 2,
        max_help_position: int = 24,
        width: int | None = None,
    ):
        super().__init__(
            prog,
            indent_increment=indent_increment,
            max_help_position=max_help_position,
            width=width,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::DeprecatedClass.__call__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py]
        def __call__(cls, *args: Any, **kwargs: Any) -> Any:
            old = DeprecatedClass.deprecated_class
            if cls is old:
                msg = instance_warn_message.format(
                    cls=_clspath(cls, old_class_path),
                    new=_clspath(new_class, new_class_path),
                )
                warnings.warn(msg, warn_category, stacklevel=2)
            return super().__call__(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/version.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/version.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "--verbose",
            "-v",
            dest="verbose",
            action="store_true",
            help="also display twisted/python/platform info (useful for bug reports)",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/utils/linkfix.py::main [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/utils/linkfix.py]
def main():
    # Used for remembering the file (and its contents)
    # so we don't have to open the same file again.
    _filename = None
    _contents = None

    # A regex that matches standard linkcheck output lines
    line_re = re.compile(r"(.*)\:\d+\:\s\[(.*)\]\s(?:(.*)\sto\s(.*)|(.*))")

    # Read lines from the linkcheck output file
    try:
        with Path("build/linkcheck/output.txt").open(encoding="utf-8") as out:
            output_lines = out.readlines()
    except OSError:
        print("linkcheck output not found; please run linkcheck first.")
        sys.exit(1)

    # For every line, fix the respective file
    for line in output_lines:
        match = re.match(line_re, line)

        if match:
            newfilename = match.group(1)
            errortype = match.group(2)

            # Broken links can't be fixed and
            # I am not sure what do with the local ones.
            if errortype.lower() in ["broken", "local"]:
                print("Not Fixed: " + line)
            else:
                # If this is a new file
                if newfilename != _filename:
                    # Update the previous file
                    if _filename:
                        Path(_filename).write_text(_contents, encoding="utf-8")

                    _filename = newfilename

                    # Read the new file to memory
                    _contents = Path(_filename).read_text(encoding="utf-8")

                _contents = _contents.replace(match.group(3), match.group(4))
        else:
            # We don't understand what the current line means!
            print("Not Understood: " + line)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.enqueue_scrape [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py]
    def enqueue_scrape(
        self, result: Response | Failure, request: Request, spider: Spider | None = None
    ) -> Generator[Deferred[Any], Any, None]:
        if self.slot is None:
            raise RuntimeError("Scraper slot not assigned")
        dfd = self.slot.add_response_request(result, request)
        self._scrape_next()
        try:
            yield dfd  # fired in _wait_for_processing()
        except Exception:
            logger.error(
                "Scraper bug processing %(request)s",
                {"request": request},
                exc_info=True,
                extra={"spider": self.crawler.spider},
            )
        finally:
            self.slot.finish_response(result, request)
            self._check_if_closing()
            self._scrape_next()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapyfixautodoc.py::maybe_skip_member [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapyfixautodoc.py]
def maybe_skip_member(app: Sphinx, what, name: str, obj, skip: bool, options) -> bool:
    if not skip:
        # autodocs was generating a text "alias of" for the following members
        return name in {"default_item_class", "default_selector_class"}
    return skip

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/console.py::_embed_ipython_shell [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/console.py]
def _embed_ipython_shell(
    namespace: dict[str, Any] | None = None, banner: str = ""
) -> EmbedFuncT:
    """Start an IPython Shell"""
    try:
        from IPython.terminal.embed import InteractiveShellEmbed  # noqa: T100,PLC0415
        from IPython.terminal.ipapp import load_default_config  # noqa: PLC0415
    except ImportError:
        from IPython.frontend.terminal.embed import (  # type: ignore[import-not-found,no-redef]  # noqa: T100,PLC0415
            InteractiveShellEmbed,
        )
        from IPython.frontend.terminal.ipapp import (  # type: ignore[import-not-found,no-redef]  # noqa: PLC0415
            load_default_config,
        )

    @wraps(_embed_ipython_shell)
    def wrapper(namespace: dict[str, Any] = namespace or {}, banner: str = "") -> None:
        config = load_default_config()  # type: ignore[no-untyped-call]
        # Always use .instance() to ensure _instance propagation to all parents
        # this is needed for <TAB> completion works well for new imports
        # and clear the instance to always have the fresh env
        # on repeated breaks like with inspect_response()
        InteractiveShellEmbed.clear_instance()
        shell = InteractiveShellEmbed.instance(
            banner1=banner, user_ns=namespace, config=config
        )
        shell()

    return wrapper

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py]
    def _extract_links(
        self,
        selector: Selector,
        response_url: str,
        response_encoding: str,
        base_url: str,
    ) -> list[Link]:
        links: list[Link] = []
        # hacky way to get the underlying lxml parsed document
        for el, _, attr_val in self._iter_links(selector.root):
            # pseudo lxml.html.HtmlElement.make_links_absolute(base_url)
            try:
                if self.strip:
                    attr_val = strip_html5_whitespace(attr_val)  # noqa: PLW2901 this is intended
                attr_val = urljoin(base_url, attr_val)  # noqa: PLW2901
            except ValueError:
                continue  # skipping bogus links
            else:
                url = self.process_attr(attr_val)
                if url is None:
                    continue
            try:
                url = safe_url_string(url, encoding=response_encoding)
            except ValueError:
                logger.debug(f"Skipping extraction of link with bad URL {url!r}")
                continue

            # to fix relative links after process_value
            url = urljoin(response_url, url)
            link = Link(
                url,
                _collect_string_content(el) or "",
                nofollow=rel_has_nofollow(el.get("rel")),
            )
            links.append(link)
        return self._deduplicate_if_needed(links)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def __init__(self, *a: Any, **kw: Any):
        super().__init__(*a, **kw)
        self._cbs: list[tuple[re.Pattern[str], CallbackT]] = []
        for r, c in self.sitemap_rules:
            if isinstance(c, str):
                c = cast("CallbackT", getattr(self, c))  # noqa: PLW2901
            self._cbs.append((regex(r), c))
        self._follow: list[re.Pattern[str]] = [regex(x) for x in self.sitemap_follow]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineCloseSpider.cb [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py]
        async def cb(_):
            raise ValueError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapydocs.py::make_setting_element [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapydocs.py]
def make_setting_element(
    setting_data: SettingData, app: Sphinx, fromdocname: str
) -> Any:
    refnode = make_refnode(
        app.builder,
        fromdocname,
        todocname=setting_data["docname"],
        targetid=setting_data["refid"],
        child=nodes.Text(setting_data["setting_name"]),
    )
    p = nodes.paragraph()
    p += refnode

    item = nodes.list_item()
    item += p
    return item

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_python.py::Callable.__call__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_python.py]
        def __call__(self, a, b, c):
            pass
```

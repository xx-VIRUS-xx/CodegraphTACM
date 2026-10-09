# scrapy-8 :: hybrid

query: BUG: Fix __classcell__ propagation.

## selected nodes

- rank=1 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=2 layer=FUNCTION tokens=1243 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::create_deprecated_class file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=3 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::ItemMeta.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py
- rank=4 layer=FUNCTION tokens=399 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=5 layer=FUNCTION tokens=289 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py::DownloadHandlers._close file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py
- rank=6 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/contextfactory.py::_AcceptableProtocolsContextFactory.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/contextfactory.py
- rank=7 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapyfixautodoc.py::maybe_skip_member file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapyfixautodoc.py
- rank=8 layer=FUNCTION tokens=424 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::warn_on_generator_with_return_value file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py
- rank=9 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.__copy__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=10 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.__copy__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=11 layer=FUNCTION tokens=370 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/console.py::_embed_ipython_shell file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/console.py
- rank=12 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/version.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/version.py
- rank=13 layer=FUNCTION tokens=237 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.enqueue_scrape file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=14 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestProcessSpiderException._test_asyncgen_nodowngrade file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py
- rank=15 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::Item.copy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py]
            def __init__(self, *args, **kwargs):  # pylint: disable=useless-parent-delegation
                # This call to super() trigger the __classcell__ propagation
                # requirement. When not done properly raises an error:
                # TypeError: __class__ set to <class '__main__.MyItem'>
                # defining 'MyItem' as <class '__main__.MyItem'>
                super().__init__(*args, **kwargs)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py::DownloadHandlers._close [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py]
    async def _close(self) -> None:
        for dh in self._handlers.values():
            if not hasattr(dh, "close"):  # pragma: no cover
                warnings.warn(
                    f"{global_object_name(dh)} doesn't define a close() method."
                    f" This is deprecated, please add an empty 'async def close()' method.",
                    category=ScrapyDeprecationWarning,
                    stacklevel=1,
                )
                continue

            if inspect.iscoroutinefunction(dh.close):
                await dh.close()
            else:  # pragma: no cover
                warnings.warn(
                    f"{global_object_name(dh.close)} is not a coroutine function."
                    f" This is deprecated, please rewrite it to return a coroutine.",
                    category=ScrapyDeprecationWarning,
                    stacklevel=1,
                )
                await ensure_awaitable(dh.close())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/contextfactory.py::_AcceptableProtocolsContextFactory.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/contextfactory.py]
    def __init__(self, context_factory: Any, acceptable_protocols: list[bytes]):
        verifyObject(IPolicyForHTTPS, context_factory)
        self._wrapped_context_factory: Any = context_factory
        self._acceptable_protocols: list[bytes] = acceptable_protocols

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapyfixautodoc.py::maybe_skip_member [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/_ext/scrapyfixautodoc.py]
def maybe_skip_member(app: Sphinx, what, name: str, obj, skip: bool, options) -> bool:
    if not skip:
        # autodocs was generating a text "alias of" for the following members
        return name in {"default_item_class", "default_selector_class"}
    return skip

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::warn_on_generator_with_return_value [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py]
def warn_on_generator_with_return_value(
    spider: Spider,
    callable: Callable[..., Any],  # noqa: A002
) -> None:
    """
    Logs a warning if a callable is a generator function and includes
    a 'return' statement with a value different than None
    """
    if not spider.settings.getbool("WARN_ON_GENERATOR_RETURN_VALUE"):
        return
    try:
        if is_generator_with_return_value(callable):
            warnings.warn(
                f'The "{spider.__class__.__name__}.{callable.__name__}" method is '
                'a generator and includes a "return" statement with a value '
                "different than None. This could lead to unexpected behaviour. Please see "
                "https://docs.python.org/3/reference/simple_stmts.html#the-return-statement "
                'for details about the semantics of the "return" statement within generators',
                stacklevel=2,
            )
    except IndentationError:
        callable_name = spider.__class__.__name__ + "." + callable.__name__
        warnings.warn(
            f'Unable to determine whether or not "{callable_name}" is a generator with a return value. '
            "This will not prevent your code from working, but it prevents Scrapy from detecting "
            f'potential issues in your implementation of "{callable_name}". Please, report this in the '
            "Scrapy issue tracker (https://github.com/scrapy/scrapy/issues), "
            f'including the code of "{callable_name}"',
            stacklevel=2,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.__copy__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def __copy__(self) -> Self:
        return self.__class__(self)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.__copy__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def __copy__(self) -> Self:
        return self.__class__(self)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestProcessSpiderException._test_asyncgen_nodowngrade [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py]
    async def _test_asyncgen_nodowngrade(self, *mw_classes: type[Any]) -> None:
        with pytest.raises(
            _InvalidOutput,
            match=r"Async iterable returned from .+ cannot be downgraded",
        ):
            await self._get_middleware_result(*mw_classes)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::Item.copy [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py]
    def copy(self) -> Self:
        return self.__class__(self)
```

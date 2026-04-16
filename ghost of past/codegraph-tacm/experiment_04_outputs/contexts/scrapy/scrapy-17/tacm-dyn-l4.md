# scrapy-17 :: tacm-dyn-l4

query: response_status_message should not fail on non-standard HTTP codes

## selected nodes

- rank=1 layer=FILE tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=2 layer=CLASS tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestScrapyHTTPPageGetter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=3 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::response_status_message file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=4 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=5 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=6 layer=CLASS tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=7 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_fail file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=8 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::Status file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=9 layer=CLASS tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=10 layer=CLASS tokens=255 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpBase file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py
- rank=11 layer=CLASS tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_deprecate.py::TestWarnWhenSubclassed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_deprecate.py
- rank=12 layer=CLASS tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::DummyPolicyTestMixin file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py
- rank=13 layer=CLASS tokens=776 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request_form.py::TestFormRequest file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request_form.py
- rank=14 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory.gotStatus file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=15 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=16 layer=CLASS tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipelines.py::TestCustomPipelineManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipelines.py
- rank=17 layer=FUNCTION tokens=359 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=18 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=19 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=20 layer=CLASS tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawl.py::TestCrawl file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawl.py
- rank=21 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=22 layer=CLASS tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=23 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_succeed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=24 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_response.py::TestResponse.CustomResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_response.py
- rank=25 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=26 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/html.py::HtmlResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/html.py
- rank=27 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::_InvalidSelector file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=28 layer=FILE tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/html.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/html.py
- rank=29 layer=FILE tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/xml.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/xml.py
- rank=30 layer=CLASS tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/xml.py::XmlResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/xml.py
- rank=31 layer=FILE tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/json.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/json.py
- rank=32 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/json.py::JsonResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/json.py
- rank=33 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=34 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=35 layer=CLASS tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py::TestBaseSettings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py
- rank=36 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=37 layer=FILE tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py
- rank=38 layer=CLASS tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py::TestRedirectMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py
- rank=39 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py::TestRedirectMiddleware.get_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py
- rank=40 layer=CLASS tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::TestDefaults file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py

## context

```text
file scrapy/utils/response.py
imports: __future__, os, re, tempfile, webbrowser, typing, weakref, twisted
defines: get_base_url, get_meta_refresh, response_status_message, _remove_html_comments, open_in_browser

class TestScrapyHTTPPageGetter:  [scrapy/tests/test_webclient.py:59]
methods: _test, test_earlyHeaders, test_non_standard_line_endings

def response_status_message(status: bytes | float | str) -> str:
    """Return status code plus status text descriptive message"""
    status_int = int(status)
    message = http.RESPONSES.get(status_int, "Unknown Status")
    return f"{status_int} {to_unicode(message)}"

    def should_cache_response(self, response: Response, request: Request) -> bool:
        return response.status not in self.ignore_http_codes

class DummyPolicy:  [scrapy/extensions/httpcache.py:35]
methods: is_cached_response_fresh, is_cached_response_valid
         should_cache_request, should_cache_response
         __init__

class TestContractsManager:  [scrapy/tests/test_contracts.py:249]
methods: setup_method, should_error, should_fail, should_succeed
         test_cb_kwargs, test_contracts
         test_custom_contracts, test_errback
         test_form_contract, test_inherited_contracts
         test_meta, test_regex, test_returns
         test_returns_async, test_same_url, test_scrapes

    def should_fail(self):
        assert self.results.failures
        assert not self.results.errors

class Status(LeafResource):  [tests/mockserver/http_resources.py:163]
methods: render_GET

class RFC2616Policy:  [scrapy/extensions/httpcache.py:59]
methods: _compute_current_age, _compute_freshness_lifetime
         _get_max_age, _parse_cachecontrol
         _set_conditional_validators
         is_cached_response_fresh
         is_cached_response_valid, should_cache_request
         should_cache_response, __init__

class TestHttpBase(ABC):  [scrapy/tests/test_downloader_handlers_http_base.py:56]
methods: download_handler_cls, get_dh
         test_content_length_zero_bodyless_post_only_one
         test_content_length_zero_bodyless_post_request_headers
         test_download
         test_download_has_correct_http_status_code
         test_download_has_correct_response_headers
         test_download_head
         test_download_is_not_automatically_gzip_decoded
         test_get_duplicate_header, test_host_header
         test_no_cookie_processing_or_persistence
         test_payload, test_redirect_status
         test_redirect_status_head
         test_request_header_duplicate
         test_request_header_none, test_response_class
         test_response_header_content_length
         test_server_receives_correct_request_body
         test_server_receives_correct_request_headers
         test_timeout_download_from_spider_nodata_rcvd
         test_timeout_download_from_spider_server_hangs
         test_unsupported_scheme

class TestWarnWhenSubclassed:  [scrapy/tests/test_utils_deprecate.py:24]
methods: _mywarnings, test_clsdict, test_custom_class_paths
         test_deprecate_a_class_with_custom_metaclass
         test_deprecate_subclass_of_deprecated_class
         test_inspect_stack, test_isinstance
         test_issubclass, test_no_warning_on_definition
         test_subclassing_warning_message
         test_subclassing_warns_once_by_default
         test_subclassing_warns_only_on_direct_children
         test_warning_auto_message, test_warning_on_instance

class DummyPolicyTestMixin(PolicyTestMixin):  [scrapy/tests/test_downloadermiddleware_httpcache.py:151]
methods: test_different_request_response_urls, test_middleware
         test_middleware_ignore_http_codes
         test_middleware_ignore_missing
         test_middleware_ignore_schemes

class TestFormRequest(TestRequest):  [scrapy/tests/test_http_request_form.py:29]
methods: assertQueryEqual, test_custom_encoding_bytes
         test_custom_encoding_textual_data
         test_default_encoding_bytes
         test_default_encoding_mixed_data
         test_default_encoding_textual_data
         test_empty_formdata
         test_form_response_with_custom_invalid_formdata_value_error
         test_form_response_with_invalid_formdata_type_error
         test_formdata_overrides_querystring
         test_from_response_ambiguous_clickdata
         test_from_response_button_notype
         test_from_response_button_novalue
         test_from_response_button_submit
         test_from_response_case_insensitive
         test_from_response_checkbox
         test_from_response_clickdata_does_not_ignore_image
         test_from_response_css
         test_from_response_descendants
         test_from_response_dont_click
         test_from_response_dont_submit_image_as_input
         test_from_response_dont_submit_reset_as_input
         test_from_response_drop_params
         test_from_response_duplicate_form_key
         test_from_response_errors_formnumber
         test_from_response_errors_noform
         test_from_response_extra_headers
         test_from_response_formid_errors_formnumber
         test_from_response_formid_exists
         test_from_response_formid_nonexistent
         test_from_response_formname_errors_formnumber
         test_from_response_formname_exists
         test_from_response_formname_nonexistent
         test_from_response_formname_nonexistent_fallback_formid
         test_from_response_get
         test_from_response_input_hidden
         test_from_response_input_text
         test_from_response_input_textarea
         test_from_response_invalid_html5
         test_from_response_invalid_nr_index_clickdata
         test_from_response_multiple_clickdata
         test_from_response_multiple_forms_clickdata
         test_from_response_noformname
         test_from_response_non_matching_clickdata
         test_from_response_nr_index_clickdata
         test_from_response_override_clickable
         test_from_response_override_duplicate_form_key
         test_from_response_override_method
         test_from_response_override_params
         test_from_response_override_url
         test_from_response_post
         test_from_response_post_nonascii_bytes_latin1
         test_from_response_post_nonascii_bytes_utf8
         test_from_response_post_nonascii_unicode
         test_from_response_radio
         test_from_response_select
         test_from_response_submit_first_clickable
         test_from_response_submit_not_first_clickable
         test_from_response_submit_novalue
         test_from_response_unicode_clickdata
         test_from_response_unicode_clickdata_latin1
         test_from_response_unicode_xpath
         test_from_response_valid_form_methods
         test_from_response_xpath
         test_get_form_with_xpath_no_form_parent
         test_html_base_form_action, test_multi_key_values
         test_spaces_in_action

    def gotStatus(self, version, status, message):
        """
        Set the status of the request on us.
        @param version: The HTTP version.
        @type version: L{bytes}
        @param status: The HTTP status code, an integer represented as a
        bytestring.
        @type status: L{bytes}
        @param message: The HTTP status message.
        @type message: L{bytes}
        """
        self.version, self.status, self.message = version, status, message

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

class TestCustomPipelineManager:  [scrapy/tests/test_pipelines.py:250]
methods: _on_item_scraped, _on_item_scraped, _on_item_scraped
         test_deprecated_process_item_spider_arg
         test_integration_no_async_not_subclass
         test_integration_no_async_subclass
         test_integration_recommended

    def should_cache_response(self, response: Response, request: Request) -> bool:
        # What is cacheable - https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9.1
        # Response cacheability - https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.4
        # Status code 206 is not included because cache can not deal with partial contents
        cc = self._parse_cachecontrol(response)
        # obey directive "Cache-Control: no-store"
        if b"no-store" in cc:
            return False
        # Never cache 304 (Not Modified) responses
        if response.status == 304:
            return False
        # Cache unconditionally if configured to do so
        if self.always_store:
            return True
        # Any hint on response expiration is good
        if b"max-age" in cc or b"Expires" in response.headers:
            return True
        # Firefox fallbacks this statuses to one year expiration if none is set
        if response.status in {300, 301, 308}:
            return True
        # Other statuses without expiration requires at least one validator
        if response.status in {200, 203, 401}:
            return b"Last-Modified" in response.headers or b"ETag" in response.headers
        # Any other is probably not eligible for caching
        # Makes no sense to cache responses that does not contain expiration
        # info and can not be revalidated
        return False

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

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

class TestCrawl:  [scrapy/tests/test_crawl.py:64]
methods: _assert_retried, _on_item_scraped, _on_item_scraped
         _test_delay, cb, cb, setup_class, teardown_class
         test_crawl_multiple
         test_crawlerrunner_accepts_crawler
         test_engine_status, test_fixed_delay
         test_follow_all, test_format_engine_status
         test_open_spider_error_on_faulty_pipeline
         test_randomized_delay, test_referer_header
         test_retry_503, test_retry_conn_aborted
         test_retry_conn_failed, test_retry_conn_lost
         test_retry_dns_error, test_start_bug_before_yield
         test_start_bug_yielding, test_start_dupes
         test_start_items, test_start_unsupported_output
         test_timeout_failure, test_timeout_success
         test_unbounded_response, test_unknown_url_scheme

file http/response/__init__.py
imports: __future__, typing, urllib, scrapy, collections, ipaddress, twisted, typing_extensions
defines: Response

class Response(object_ref):  [http/response/__init__.py:36]
methods: _set_body, _set_url, body, cb_kwargs, copy, css, flags
         flags, follow, follow_all, headers, headers
         jmespath, meta, replace, replace, replace, text
         url, urljoin, xpath, __init__, __repr__

    def should_succeed(self):
        assert not self.results.failures
        assert not self.results.errors

class CustomResponse(self.response_class):  [scrapy/tests/test_http_response.py:114]
methods: —

    def __init__(self, settings: BaseSettings):
        self.ignore_schemes: list[str] = settings.getlist("HTTPCACHE_IGNORE_SCHEMES")
        self.ignore_http_codes: list[int] = [
            int(x) for x in settings.getlist("HTTPCACHE_IGNORE_HTTP_CODES")
        ]

class HtmlResponse(TextResponse):  [http/response/html.py:11]
methods: —

class _InvalidSelector(ValueError):  [http/response/text.py:295]
methods: —

file http/response/html.py
imports: scrapy
defines: HtmlResponse

file http/response/xml.py
imports: scrapy
defines: XmlResponse

class XmlResponse(TextResponse):  [http/response/xml.py:11]
methods: —

file http/response/json.py
imports: scrapy
defines: JsonResponse

class JsonResponse(TextResponse):  [http/response/json.py:11]
methods: —

    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

class TestBaseSettings:  [tests/test_settings/__init__.py:78]
methods: setup_method, test_copy, test_copy_to_dict, test_delete
         test_freeze, test_frozencopy, test_get
         test_getpriority, test_getwithbase
         test_getwithbase_for_non_component_priority_dicts
         test_getwithbase_invalid_setting_name
         test_getwithbase_override_none_by_type
         test_getwithbase_override_value_by_type
         test_getwithbase_warns_on_duplicate_import_paths
         test_getwithbase_warns_on_duplicate_mixed_type_and_path
         test_maxpriority
         test_set_calls_settings_attributes_methods_on_update
         test_set_instance_identity_on_update
         test_set_new_attribute
         test_set_settingsattribute
         test_setdefault_existing_value
         test_setdefault_not_existing_value
         test_setdict_alias, test_setitem
         test_setmodule_alias, test_setmodule_by_path
         test_setmodule_only_load_uppercase_vars
         test_update, test_update_iterable
         test_update_jsonstring, test_update_kwargs

class FormRequest(Request):  [http/request/form.py:39]
methods: from_response, __init__

def parse_item(response):
    pass

# --- Layer 04: Variable context ---
# call-chain context
  called by: process_response [retry.py]

# call-chain context
  called by: _cache_response [httpcache.py]

# call-chain context
  called by: handleStatus [webclient.py]

# call-chain context
  called by: _test_cookie_redirect [test_downloadermiddleware_cookies.py]
  called by: _test_cookie_header_redirect [test_downloadermiddleware_cookies.py]

# call-chain context
  called by: _cache_response [httpcache.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: parse_node [feed.py]

```

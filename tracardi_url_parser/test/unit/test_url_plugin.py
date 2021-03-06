from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from tracardi_url_parser.plugin import ParseURLParameters
from tracardi.domain.session import Session


def test_url_plugin_fail():
    init = {
        "url": 'session@context.page.url'
    }
    payload = {}
    session = Session(
        id='1',
        context={
            'page': {
                'none': "http://test.url/path/?param=1#hash"
            }
        }
    )
    try:
        run_plugin(ParseURLParameters, init, payload, session=session)
        assert False
    except KeyError:
        assert True


def test_url_parser_plugin_ok():
    init = {
        "url": 'session@context.page.url'
    }
    payload = {}
    session = Session(
        id='1',
        context={
            'page': {
                'url': "http://test.url/path/?param=1#hash"
            }
        }
    )
    result = run_plugin(ParseURLParameters, init, payload, session=session)
    assert result.output.value == {'url': 'http://test.url/path/?param=1#hash', 'scheme': 'http',
                                   'hostname': 'test.url', 'path': '/path/', 'query': 'param=1',
                                   'params': {'param': '1'}, 'fragment': 'hash'}

import asyncio

from tracardi_url_parser.plugin import ParseURLParameters
from tracardi.domain.session import Session


async def main():
    init = {}

    payload = {}

    plugin = ParseURLParameters(**init)
    plugin.session = Session(context={
        'page': {
            'url': "http://test.url/path/?param=1"
        }
    })

    result = await plugin.run(void=payload)
    print(result)


asyncio.run(main())

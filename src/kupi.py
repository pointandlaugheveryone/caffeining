import asyncio
from pykupi import KupiParser
############# TEST ONLY
async def task():
    parser = KupiParser()
    result = await parser.get_prices("limonada-pepsi")
    cheapest = result.offers[0]
    print(
        f'The cheapest drink now in {cheapest.offered_by} for {cheapest.price} {cheapest.price_currency} '
        f'until {cheapest.valid_until.strftime("%d.%m.%Y")}'
    )
    # The cheapest bananas now in Kaufland for 24.9 CZK until 08.03.2022
    await parser.session.close()


asyncio.run(task())
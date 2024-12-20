import asyncio
from pykupi import KupiParser
############# TEST ONLY
async def task():
    parser = KupiParser()
    '''
    result = await parser.get_prices("limonada-pepsi")
    cheapest = result.offers[0]
    print(
        f'The cheapest drink now in {cheapest.offered_by} for {cheapest.price} {cheapest.price_currency} '
        f'until {cheapest.valid_until.strftime("%d.%m.%Y")}'
    )
    '''

    text = await parser.get_prices("coca-cola-zero")
    mod = text.split(',')
    
    print(mod)
    await parser.session.close()

asyncio.run(task())
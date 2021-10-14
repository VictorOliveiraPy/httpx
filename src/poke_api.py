import asyncio
import httpx


async def main():
    async with httpx.AsyncClient() as client:
        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'

            resp = await client.get(pokemon_url)
            pokemon = resp.json()
            print(pokemon['name'])


if __name__ == '__main__':
    asyncio.run(main())

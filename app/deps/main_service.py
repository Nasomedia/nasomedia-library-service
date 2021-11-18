from fastapi.exceptions import HTTPException

from app.core.config import settings
from app import schemas

import aiohttp


class MainService():
    @classmethod
    async def get_episode(cls, episode_id: int) -> schemas.Episode:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{settings.MAIN_SERVICE_BASE_URL}/api/v1/episodes/{episode_id}") as resp:
                if resp.status != 200:
                    raise HTTPException(status_code=resp.status, detail=await resp.text())
                episode_data = await resp.json()
                return schemas.Episode(**episode_data)

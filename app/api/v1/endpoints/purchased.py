from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from pydantic import main
from sqlalchemy.orm import Session


from app import crud, schemas, models, deps
from app.crud import purchased

router = APIRouter()


@router.get("/{episode_id}", response_model=schemas.Episode)
async def read_purchased(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_serivce: deps.MainService = Depends(deps.MainService),
    *,
    episode_id: int
):
    """
    Retrieve purchased episode
    """
    purchased = crud.purchased.get_with_user(db, episode_id=episode_id, user_id=user.id)
    if not purchased:
        raise HTTPException(status_code=404, detail="Purchased episode not found")
    episode = await main_serivce.get_episode(episode_id=purchased.episode_id)

    return episode


@router.get("", response_model=List[schemas.Episode])
async def read_purchased_list(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_serivce: deps.MainService = Depends(deps.MainService)
):
    """
    Retrieve purchased episode
    """
    response: List[schemas.Episode] = []
    purchased_list = crud.purchased.get_multi_with_user(db, user_id=user.id)
    for purchased in purchased_list:
        episode = await main_serivce.get_episode(episode_id=purchased.episode_id)
        response.append(episode)

    return response


@router.post("/{episode_id}", response_model=schemas.Episode)
async def create_purchased(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_service: deps.MainService = Depends(deps.MainService),
    *,
    episode_id: int
):
    """
    Create new purchased episode
    """
    purchased = crud.purchased.get_with_user_and_episode(db, user_id=user.id, episode_id=episode_id)
    if not purchased:
        raise HTTPException(status_code=400, detail="Episode is already purchased")
    crud.purchased.create_with_user_and_episode(
        db, 
        user_id=user.id, 
        episode_id=episode_id
    )
    episode = await main_service.get_episode(episode_id=episode_id)
    return episode


@router.delete("/{episode_id}", response_model=schemas.Episode)
async def delete_purchased(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_service: deps.MainService = Depends(deps.MainService),
    *,
    episode_id: int,
):
    "Delete purchased episode"
    purchased = crud.purchased.get_with_user_and_episode(
        db, 
        user_id=user.id,
        episode_id=episode_id
    )
    if not purchased:
        raise HTTPException(status_code=404, detail="Purchased episode not found")
    crud.purchased.delete(db, id=purchased.id)
    episode = await main_service.get_episode(episode_id=episode_id)
    return episode

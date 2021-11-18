from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from pydantic import main
from sqlalchemy.orm import Session


from app import crud, schemas, models, deps
from app.crud import purchased

router = APIRouter()


@router.get("", response_model=List[schemas.Purchased])
async def read_purchased_list(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_serivce: deps.MainService = Depends(deps.MainService)
):
    """
    Retrieve purchased episode
    """
    response: List[schemas.Purchased] = []
    purchased_list = crud.purchased.get_multi_with_user(db, user_id=user.id)
    for purchased in purchased_list:
        episode = await main_serivce.get_episode(episode_id=purchased.episode_id)
        response.append(schemas.Liked(episode=episode))

    return response


@router.post("/{episode_id}", response_model=schemas.Purchased)
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
    crud.purchased.create_with_user_episode(
        db, 
        user_id=user.id, 
        episode_id=episode_id
    )
    episode = await main_service.get_episode(episode_id=episode_id)
    response = schemas.Purchased(episode=episode)
    return response


@router.delete("/{episode_id}", response_model=schemas.Purchased)
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
    response = schemas.Purchased(episode=episode)
    return response

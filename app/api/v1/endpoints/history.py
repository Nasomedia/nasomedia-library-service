from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from sqlalchemy.orm import Session

from app import crud, schemas, models, deps
from app.core.config import settings

from app.schemas import Episode

router = APIRouter()


@router.get("", response_model=List[schemas.History])
async def read_histories(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_service: deps.MainService = Depends(deps.MainService)
):
    """
    Retrieve user's read histories
    """
    response: List[schemas.History] = []
    histories = crud.history.get_multi_with_user(db, user_id=user.id)
    for history in histories:
        print(history.latest_date)
        episode = await main_service.get_episode(history.episode_id)
        response.append(schemas.History(
            latest_read=history.latest_date,
            progress=history.progress,
            episode=episode)
        )
    return response


@router.put("/{episode_id}", response_model=schemas.History)
async def update_history(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_service: deps.MainService = Depends(deps.MainService),
    *,
    episode_id: int,
    history_in: schemas.HistoryUpdate
):
    """
    Update user's read history
    """
    history = crud.history.get_with_user_and_episode(db, user_id=user.id, episode_id=episode_id)
    if not history:
        history = crud.history.create_with_user_and_episode(
            db, 
            obj_in=schemas.HistoryCreate(progress=history_in.progress), 
            user_id=user.id, 
            episode_id=episode_id
        )
    else:
        history = crud.history.update(
            db, db_obj=history, obj_in=history_in)
            
    episode = await main_service.get_episode(history.episode_id)
    response = schemas.History(
        latest_date=history.latest_date,
        progress=history.progress,
        episode=episode
    )
    return response


@router.delete("/{episode_id}", response_model=schemas.History)
async def delete_history(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_service: deps.MainService = Depends(deps.MainService),
    *,
    episode_id: int,
):
    "Delete user's read history"
    history = crud.history.get_with_user_and_episode(db, user_id=user.id, episode_id=episode_id)
    if not history:
        raise HTTPException(status_code=404, detail="History not found")
    crud.history.delete(db, id=history.id)
    episode = await main_service.get_episode(episode_id=history.episode_id)
    response = schemas.History(
        latest_date=history.latest_date,
        progress=history.progress,
        episode=episode
    )
    return response

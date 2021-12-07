from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from pydantic import main
from sqlalchemy.orm import Session


from app import crud, schemas, models, deps

router = APIRouter()


@router.get("", response_model=List[schemas.Liked])
async def read_liked(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_service: deps.MainService = Depends(deps.MainService)
):
    """
    Retrieve liked series
    """
    response: List[schemas.Liked] = []
    liked_list = crud.liked.get_multi_with_user(db, user_id=user.id)
    for liked in liked_list:
        series = await main_service.get_series(series_id=liked.series_id)
        response.append(schemas.Liked(series=series))

    return response


@router.post("/{series_id}", response_model=schemas.Liked)
async def create_liked(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_service: deps.MainService = Depends(deps.MainService),
    *,
    series_id: int,
):
    """
    Create new liked series
    """
    liked = crud.liked.get_with_user_and_series(
        db, 
        user_id=user.id, 
        series_id=series_id
    )
    if liked:
        raise HTTPException(status_code=400, detail="It is already liked")
    liked = crud.liked.create_with_user_and_series(
        db, 
        user_id=user.id, 
        series_id=series_id
    )
    # series = await main_service.get_series(series_id=series_id)
    # response = schemas.Liked(series=series)
    response = schemas.Liked()
    return response


@router.delete("/{series_id}", response_model=schemas.Liked)
async def delete_liked(
    db: Session = Depends(deps.get_db),
    user: schemas.User = Depends(deps.get_current_active_user),
    main_service: deps.MainService = Depends(deps.MainService),
    *,
    series_id: int,
):
    "Delete liked series"
    liked = crud.liked.get_with_user_and_series(db, user_id=user.id, series_id=series_id)
    if not liked:
        raise HTTPException(status_code=404, detail="Liked series not found")
    crud.liked.delete(db, id=liked.id)
    series = await main_service.get_series(series_id=series_id)
    response = schemas.Liked(series=series)
    return response

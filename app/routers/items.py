from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud

from ..dependency import get_db
import time
import psycopg2


router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.post("/", response_model=schemas.Item)
def create_item_for_user(
    item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item)


@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@router.put("/{item_id}", response_model=schemas.Item)
def update_product(
    item_id, new_item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    # Add lock in selected row
    try:
        item = db.query(models.Item).filter_by(id=item_id).with_for_update(nowait=True).first()
        
        # simulate the long process time
        time.sleep(3)

        item.owner_id = new_item.owner_id
        db.commit()
        
        return item
    except:
        raise HTTPException(status_code=403, detail="Data is locked")





    
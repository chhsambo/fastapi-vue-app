from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import select, asc, desc
from app.db import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

router = APIRouter()


@router.get("/products")
def index(page: int = 1, size: int = 10, order = "id", direction = "asc", db: Session = Depends(get_db)):
    sort_direction = asc if direction == "asc" else desc 
    products = (
        db.query(Product)
        .order_by(sort_direction(getattr(Product, order)))
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )
    return products
    # return db.query(Product).all()


@router.get("/products/{id}")
def get(id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == id).first()


@router.post("/products")
def create(payload: ProductCreate, db: Session = Depends(get_db)):
    product = Product(**payload.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.put("/products/{id}")
def update(id: int, payload: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    product.name = payload.name
    product.price = payload.price
    db.commit()
    db.refresh(product)
    return product


@router.delete("/products/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Product).filter(Product.id == id).delete()
    db.commit()

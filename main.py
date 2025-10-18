from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from . import models, schemas, utils
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="URL Shortener Service")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(request: schemas.URLCreate, db: Session = Depends(get_db)):
    short_url = utils.generate_short_url()
    db_url = models.URL(original_url=request.original_url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

@app.get("/{short_url}")
def redirect_to_original(short_url: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.short_url == short_url).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(db_url.original_url)

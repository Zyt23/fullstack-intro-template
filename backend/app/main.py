from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select

from app.db import SessionLocal, Profile, init_db

app = FastAPI(title="Fullstack Intro API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 教学阶段先放开；正式可改成你的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def _startup():
    init_db()
    # 插入一条默认数据（如果没有）
    with SessionLocal() as db:
        existing = db.scalar(select(Profile).where(Profile.id == 1))
        if not existing:
            db.add(
                Profile(
                    id=1,
                    name="Ada Lovelace",
                    title="Full-stack Learner",
                    bio="Hello! This is a demo profile powered by FastAPI + SQLite."
                )
            )
            db.commit()


@app.get("/api/profile")
def get_profile():
    with SessionLocal() as db:
        p = db.scalar(select(Profile).where(Profile.id == 1))
        return {"name": p.name, "title": p.title, "bio": p.bio}


@app.put("/api/profile")
def update_profile(payload: dict):
    with SessionLocal() as db:
        p = db.scalar(select(Profile).where(Profile.id == 1))
        p.name = payload.get("name", p.name)
        p.title = payload.get("title", p.title)
        p.bio = payload.get("bio", p.bio)
        db.commit()
        return {"ok": True}

from fastapi import APIRouter, File, UploadFile
from app.services.articles import ArticleServices, TypeArticle
from app.schemas.articles import ResponsePopRecSchema, ResponseArticleByDomaine, ResponseContenuArticleByDomaine
from app.core.gestion_image import save_image_local


article_router = APIRouter(prefix="/articles",tags=["Articles"])

@article_router.get("/pop_rec", response_model=ResponsePopRecSchema)
async def pop_rec():
    return await ArticleServices.pop_rec()

@article_router.get("/{domaine}/liste", response_model=ResponseArticleByDomaine)
async def liste_article_domaine(domaine:TypeArticle):
    return await ArticleServices.liste_article_domaine(domaine)

@article_router.get("/{id}/contenu", response_model=ResponseContenuArticleByDomaine)
async def liste_article_domaine(id:int):
    return await ArticleServices.lire_un_article(id)

@article_router.post("/uploadFile")
async def file(image:UploadFile = File(...)):
    return await save_image_local(image)

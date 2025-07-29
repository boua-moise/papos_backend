from fastapi import APIRouter, UploadFile, Depends
from app.services.administration import AdminService
from app.schemas.administration import AddSchema, ResponseListeArticleSchema, ResponseSimpleSchema, Contenu
from app.core.security import get_current_user

admin_router = APIRouter(prefix="/admin", tags=["Admintration"], dependencies=[Depends(get_current_user)])


@admin_router.get("/liste_article", response_model=ResponseListeArticleSchema)
async def liste_article():
    return await AdminService.articles()

@admin_router.post("/add_article", response_model=ResponseSimpleSchema)
async def add_article(article:AddSchema):
    return await AdminService.add_article(article)

@admin_router.post("/image_article/{id}", response_model=ResponseSimpleSchema)
async def upload_files(image:UploadFile, id:int):
    return await AdminService.add_picture_of_article(image, id)


@admin_router.delete("/delete_article/{id}", response_model=ResponseSimpleSchema)
async def delete_article(id:int):
    return await AdminService.delete_article(id)

@admin_router.put("/update_article/{id}", response_model=ResponseSimpleSchema)
async def update_article(contenu:Contenu, id:int):
    return await AdminService.update_article(id, contenu)
from prisma.models import Article
from fastapi import UploadFile
from app.schemas.administration import AddSchema, Contenu
from app.core.gestion_image import save_image_local


class AdminService:
    @staticmethod
    async def articles():
        articles = await Article.prisma().find_many()
        return {"article": articles}
    
    @staticmethod
    async def add_article(article:AddSchema):
        art = await Article.prisma().create(data={
            "authorId": article.authorId,
            "titre": article.titre,
            "contenu": article.contenu,
            "description": article.description,
            "categorie": article.categorie,
            "view": 0
        })
        
        return  {"response": f"{art.id}", "valide": True}
        
    @staticmethod
    async def add_picture_of_article(image:UploadFile, id):
        url = await save_image_local(image)
        print("url", url)
        await Article.prisma().update(data={"image": url.get("file").get("url")}, where={"id":id})
        return {"response": str(url), "valide": True}

    @staticmethod
    async def delete_article(id:int):
        await Article.prisma().delete(where={"id":id})
        return {"response": "Article supprimé avec succès", "valide": True}

    @staticmethod
    async def update_article(id:int, contenu:Contenu):
        article = await Article.prisma().find_unique(where={"id": id})
        await Article.prisma().update(where={"id":id}, data={
            "contenu":contenu.contenu,
            "titre": contenu.titre,
            "description": contenu.description,
            "categorie": contenu.categorie
            }
        )
        return {"response": "Article mis à jour avec succès", "valide": True}

from prisma.models import Article
from app.schemas.administration import TypeArticle

class ArticleServices:
    @staticmethod
    async def pop_rec():
        rec = await Article.prisma().find_many(order={"creatAt": "desc"}, take=2)
        pop = await Article.prisma().find_many(order={"view": "desc"}, take=5)
        return {"populaires": pop, "reccents": rec}
    
    @staticmethod
    async def liste_article_domaine(domaine:TypeArticle):
        articles = await Article.prisma().find_many(where={"categorie": domaine})

        return {"articles": articles}
    
    @staticmethod
    async def lire_un_article(id:int):
        contenu = await Article.prisma().find_first(where={"id": id})
        return {"response": contenu}
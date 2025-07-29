from pydantic import BaseModel
from app.schemas.administration import TypeArticle

class PopRec(BaseModel):
    id:int
    categorie:TypeArticle
    titre:str
    description:str
    image:str
    view:int

class Contenu(BaseModel):
    id:int
    categorie:TypeArticle
    titre:str
    contenu:str
    description:str
    image:str
    view:int

class ResponsePopRecSchema(BaseModel):
    populaires:list[PopRec]
    reccents:list[PopRec]

class ResponseArticleByDomaine(BaseModel):
    articles:list[PopRec]

class ResponseContenuArticleByDomaine(BaseModel):
    response:Contenu
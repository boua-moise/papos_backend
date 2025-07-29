from pydantic import BaseModel
from enum import Enum

class TypeArticle(str, Enum):
    Reseau = "reseau"
    Systeme = "systeme"
    Programmation = "programmation"
    cybersecurity = "cybersecurity"
    IA = "ia"

class AddSchema(BaseModel):
    authorId:int
    titre: str
    contenu:str
    description:str
    categorie:TypeArticle
    view:int

class ArticleSchema(BaseModel):
    id:int
    titre: str
    categorie:TypeArticle
    description:str
    image:str
    view:int

class ResponseListeArticleSchema(BaseModel):
    article:list[ArticleSchema]

class ResponseSimpleSchema(BaseModel):
    response:str
    valide:bool

class Contenu(BaseModel):
    titre: str
    contenu:str
    description:str
    categorie:TypeArticle

-- CreateEnum
CREATE TYPE "TypeArticle" AS ENUM ('systeme', 'reseau', 'programmation', 'cybersecurity', 'ia');

-- CreateTable
CREATE TABLE "Creator" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "firstname" TEXT NOT NULL,
    "mail" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "creatAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updateAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Creator_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Article" (
    "id" SERIAL NOT NULL,
    "authorId" INTEGER NOT NULL,
    "categorie" "TypeArticle" NOT NULL,
    "titre" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "image" TEXT,
    "contenu" TEXT NOT NULL,
    "view" INTEGER,
    "creatAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updateAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Article_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Creator_mail_key" ON "Creator"("mail");

-- AddForeignKey
ALTER TABLE "Article" ADD CONSTRAINT "Article_authorId_fkey" FOREIGN KEY ("authorId") REFERENCES "Creator"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

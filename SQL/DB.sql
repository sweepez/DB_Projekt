\set ON_ERROR_STOP

create database ah7515_ah7370;

\c ah7515_ah7370

create table Author (
    pID varchar(10) primary key,
    name varchar(255)
    ); 

create table Article (
    aID serial,
    title varchar(255),
    content text,
    published date,
    primary key(aID)
);

create table Image(
    ImID serial primary key,
    path varchar(255)
);

create table WrittenBy(
    AuthorID varchar(10),
    ArticleID int,
    foreign key (AuthorID) references Author(pID),
    foreign key (articleID) references Article(aID),
    primary key (AuthorID, ArticleID) 
);

create table ImageInArticle(
    ImageID int,
    ArticleID int,
    ImageText text,
    foreign key(ImageID) references Image(ImID),
    foreign key(ArticleID) references Article(aID),
    primary key(ImageID, ArticleID)
);

create table Comment(
    ArticleID int,
    comName varchar(255),
    comContent text,
    comPublished date,
    foreign key(ArticleID) references Article(aID),
    primary key(ArticleID, comName, comPublished)
);

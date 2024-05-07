 Create table livro (
    id int auto_increment primary key,
    titulo varchar(255) not null,
    autor varchar(100) not null,
    editora varchar(100) not null,
    ano_publicacao date not null,
    genero varchar(50) not null,
    quantidade int not null,
    disponivel boolean not null default true,
    data_cadastro date not null default current_date
 );
CREATE TABLE nome_da_tabela (
    coluna1 tipo_de_dado,
    coluna2 tipo_de_dado,
    coluna3 tipo_de_dado
);
/* banco de dados não relacionais 
#banco de dados não relacionais/NoSQL
orientado a objetos
hierarquicos

scgb - sistema de controle de gestão de biblioteca

funcionalidade (CRUDE) LEITURA, ESCRITA, ATUALIZAÇÃO, DELEÇÃO, EXIBIÇÃO
 chaves primarias 
 chaves estrangeiras
 *caracteristicas
 relacionamento entre tabelas
 linguagem de cojnsulta estruturada
 integridade referencial
 normalixação de dados 
 segurança
 flexibilidade e ext6ensibilidade
 suporte e tranções

 ** ACID 
 Atoimicidade:é a propriedade que garante que uma transação é executada por completo ou não é executada de forma alguma.
    Consistência: Garante  
    Isolamento: cada transição é executada de forma isolada 
    Durabilidade:


$$$ Linguagem de consulta padronizada
permite que o usuário acesse e manipule os dados de um banco de dados
SQL - Structured Query Language
DDL - Data Definition Language
DML - Data Manipulation Language(Manipulação de Dados )
DCL - Data Control Language  (Definição de Dados Estruitura como serão as tabelas )
TCL - Transaction Control Language
Dql - Data Query Language

*Sintaxe e Nomenclatura 
Nomes em geral iniciam com a Letra ou com um caractere de sublinhado
Sensibilidade a maiusculas e minusculas
*** Os nomes podem conter nomes e caracteres especiais

$$ MER - Modelo Entidade Relacionamento e DER - Diagrama Entidade Relacionamento

*Modelo Entidade Relacionamento  sendo este um modelo conceitual de dados que descreve as coisas do mundo real que são importantes para um sistema de informação
*Diagrama Entidade Relacionamento é uma representação gráfica do modelo entidade relacionamento
Cardinalidade - é a quantidade de ocorrências que um registro de uma tabela pode ter em relação a outra tabela

¨¨¨elementos conditod no DER -
Entidades - são objetos do mundo real que possuem atributos e que são armazenados no banco de dados
Atributos - são as caracteristicas das entidades

 cardinalidade  relacionamento 1 para 1 
    cardinalidade  relacionamento 1 para N um para MUITOS
    cardinalidade  relacionamento N para N MUITOS para MUITOS



create table nome_da_tabela (
    coluna1 tipo_de_dado,
    coluna2 tipo_de_dado,
    coluna3 tipo_de_dado
);

Tabelas são estruturas que armazenam dados de forma organizada LINHA E COLUNAS 
colunas  são os campos da tabela
registro é uma linha da tabela pode ser uma tupla 
 creat é a instancia da tabela , a coluna o tipo de coluna e pode adicionar comentarios 
    insert into nome_da_tabela (coluna1, coluna2, coluna3) values (valor1, valor2, valor3);
    tipos de dados  
    int - inteiro
    varchar - texto
    date - data
    time - hora
    boolean - verdadeiro ou falso
    float - numero decimal
    double - numero decimal
    char - caractere
    text - texto longo 
    blob - binario
    enum - enumerado

    Comandos :

    restrições do valor 
    Not Null 
    unique
   default
    check
 Chaves primarias e estrangeiras 
 Auto incremento ,Importante para chave primaria , serve para qualquer tipo de informação incremental 


 create table usuario (
    id int auto_increment primary key,
    nome varchar(255) not null, "nome do usuario"
    email varchar(100) not null unique,"email do usuario UNIQUE PARA RESTRIÇÃO DE EMAILS IGUAIS"
    senha varchar(50) not null, "le deve ser orbrigatorios"
    data_cadastro date not null default current_date "data de cadastro do usuario"


 )



 Teblas de resgitro e de Destinos 
 

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
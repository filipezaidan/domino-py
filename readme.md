## Integrantes da Equipe: 
- Filipe Zaidan Ferreira da Silva
- Lucas Matheus Vieira Lúcio

## Conteúdo de consultado para realização do projeto
- https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/listas-encadeadas/
- https://drive.google.com/file/d/1JuA8F_79TBt2_n6V2Br76BUsfxFb2ZZB/view?pli=1

## Comentário da equipe sobre se conseguiu ou não realizar tudo o que foi proposto:
### Sobre os requisitos funcionais:
Todos os requisitos (Criação de Peças de Dominó, Embaralhamento das Peças, Distribuição de Peças aos Jogadores, Jogada de Peças e Verificação de Estado do Jogo) foram cumpridos

### Sobre as Restrições
Todas foram respeitadas

### Sobre as Atividades a serem Realizadas
Todas as atividades foram realizadas

## Comentário destacando possíveis problemas identificados no código
Algo que seria um problema e nós notamos é que por não ser possível escolher em qual lado do jogo queremos inserir a peça, quando há a possibilidade de inserir em qualquer um dos dois lados o jogador não tem a liberdade de escolher estrategicamente em qual lado jogar.

### Relatório Técnico 
Para representar cada peça do jogo nós usamos duas classes, uma para a peça em si e outra para termos o "nó" da lista encadeada. Para representar as peças geradas, as mãos do jogadores, e o jogo em si, nós utilizamos listas encadeadas. A estrutura do nó e da lista encadeada nós pegamos do material passado no classroom e adaptamos conforme a necessidade do jogo. Segue algumas imagens de anotações/mapeamentos feitos no papel para facilitar a implementação do código:

![Alt text](https://media.discordapp.net/attachments/423569295272837130/1153045425000026162/3267533e-ab49-4048-9176-e538f4956053.png?width=372&height=662 "Anotação/Mapeamento parte 1")

![Alt text](https://media.discordapp.net/attachments/423569295272837130/1153045456297934848/a67edbd2-5888-4835-8e2b-c0ff88f8c2bb.png?width=372&height=662 "Anotação/Mapeamento parte 2")

A maior dificuldade foi na questão de inserir peças, principalmente por que uma peça não possui "lado certo" e foi preciso inverter ela para poder inserir de forma não pareça "gato por lebre". A lógica do projeto como um todo é bem interessante e deu pra praticar muito a ideia de "lista encadeada" e "nós". (Agora ***nós*** entendemos melhor essas estruturas kkkkk)
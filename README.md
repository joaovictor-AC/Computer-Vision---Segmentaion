# Atividade (Segmentação 1)
### Considerações
Essa é a primeira entrega/traballho/projetinho previsto no Plano de Ensino:

No livro do Peter Corke, você estudou sobre classificação a nível de tons de cinza utilizando limiarização. Você pode testar alguns dos diversos algoritmos, alguns implementados e acessíveis diretamente via Python/OpenCV.

O resultado é idealmente uma segmentacão binária com dois tons de cinza, geralmente um preto e o outro branco. Em ambiente controlado e com luz controlada, tais algoritmos podem ser suficientes, leves e muito fáceis de embarcar em hardware de baixo custo. São de fato, muito utilizados na indústria para inspeção visual automatizada há muitos anos.

Aqui começa a primeira Atividade em Segmentação para entregar:


1. A sementação de cenas complexas reais e em condições não ideais é algo bem complicado e você já deve ter observado isso na tarefa anterior sobre classificação a nível de tons de cinza usando limiarização. Isso ocorre devido ao ruído, variação na iluminação, etc. Primeiro os algoritmos usavam um único limiar global e isso levou ao desenvolvimento de alternativas. Leia sobre particionamento (Gonzalez, p. 498) e reproduza os resultados da Figura 10.46 e histogramas da Figura 10.47 (Exemplo 10.20).
>Faça e submeta uma apresentação estilo PowerPoint explicando a Limiarização Variável e o estudo reproduzido (salve em .pptx para apresentar se sorteado). Submeta também o Jupyter Notebook com os códigos usados para fazer o estudo.

2. Um processo de classificação utilizando as cores em uma cena é discutido na Seção 13.1.1.2 (Color Classification) do livro do Peter Corke. Leiam o tutorial elaborado por ele e tentem reproduzir os resultados utilizando algoritmo de clusterização k-means (sklearn, por exemplo). A rotulação das classes pode ser automática ou manual.
<br>Color space - o espaço de cromaticidade pode ser melhor compreendido estudando a Seção 10.2.4 do livro do Peter Corke e equação 10.11, por exemplo. As componentes R, G e B podem ser obtidas para um mesmo pixel e utilizadas na equação para mapear as cores. Existem diferentes espaços propostos. Na foto da Fig. 13.7, p. 422, muito boa, os tomates vermelhos possuem reflexo e um deles está por traz da folhagem verde. Isso traz problemas para o processo e resultados.
<br>Leia sobre segmentação de regiões usando clustering nos livros novos do Gonzalez (R. Gonzalez, R. Woods, S. Eddins Digital Image Processing Using Matlab, 3rd Ed., Gatesmark, 2020, nas páginas 680-684, por exemplo). O livro em português não aborda o tema. Estude o tema e o algoritmo proposto.
>Faça e submeta uma apresentação estilo PowerPoint explicando o algoritmo. Implemente-o em Python. Reproduza os resultados da Figura 11.24 (pág. 683) do livro novo citado acima. Submeta também o Jupyter Notebook com os códigos usados para fazer o estudo com os respectivos resultados.
# Sudoku
O primeiro objetivo deste projeto é gerar uma matriz de sudoku completamente preenchida. [**concluído**]</br>
Posteriormente serão adicionadas funcionalidades como geração de um sudoku para o jogador completar. [**em andamento**].

##Funcionamento atual
###geração do jogo:
As linhas geradas em getInitRow são escolhidas aleatóriamente e inseridas na tabela do jogo. A inserção só é realizada se não houver duplicatas na verificação de colunas e/ou quadrados.
###resolução do jogo:
Primeiro são contabilizadas todas as coordenadas que devem ser preenchidas. Em seguida, o programa verifica quais números são possíveis de inserir na coordenada em branco; se apenas um número é possível, ele então é inserido. Este processo se repete até o jogo estar resolvido.

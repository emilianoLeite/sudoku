# sudoku
O primeiro objetivo deste projeto é gerar uma matriz de sudoku completamente preenchida.
Posteriormente serão adicionadas funcionalidades como geração de um sudoku para o jogador completar.

###funcionamento atual (não funcional)

  A tabela é populada linha a linha, da coordenada 0,0 até a coordenada 8,8
  então sempre que um valor é válido a função vai printar o valor, populá-lo na tabela e ir pro próximo;
  Quando acabar a linha, a função irá printar a tabela toda e começar a popular a próxima linha.
  
  Exemplo:<br/>
  1 <br/>
  7 <br/>
  6 <br/>
  3 <br/>
  8 <br/>
  5<br/>
  9<br/>
  2<br/>
  4<br/>
  176385924<br/>
  
  000000000 <br/>
  
  000000000<br/>
  
  000000000<br/>
  
  000000000<br/>
  
  000000000<br/>
  
  000000000<br/>
  
  000000000<br/>
  
  000000000<br/>
  
  9<br/>
  8<br/>
  5<br/>
  4<br/>
  6<br/>
  7<br/>
  1<br/>
  3<br/>
  A função trava aqui, pois o único valor restante para a linha é o 2, porém o quadrado 3 já possui um 2.

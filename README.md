# sudoku
O primeiro objetivo deste projeto é gerar uma matriz de sudoku completamente preenchida.
Posteriormente serão adicionadas funcionalidades como geração de um sudoku para o jogador completar.

###funcionamento atual(main.py)
Cada linha é gerada randomicamente e inserida inteira(em contraste com inserção item a item). Inserção só é realizada se item não está duplicado na coluna ou quadrado.

###funcionamento sequencial(sequential.py)(não funcional)
Popular a tabela sequencialmente (inserir todos os '1', depois todos os '2', etc) <br/>
Exemplo: <br/>
1 5 2 |0 4 3 |6 0 7  <br/>

3 0 4 |5 6 7 |2 0 1 <br/>

7 6 0 |2 0 1 |4 3 5 <br/>
____________________<br/>
2 7 6 |4 3 0 |1 5 0 <br/>
	
0 4 3 |1 5 6 |7 2 0 <br/>
	
0 1 5 |7 0 2 |3 4 6 <br/>
____________________<br/>
4 0 1 |3 7 0 |5 6 2 <br/>
	
5 2 0 |6 1 4 |0 7 3 <br/>
	
6 3 7 |0 2 5 |0 1 4 <br/>

###funcionamento item a item (item_main.py)(não funcional)

  A tabela é populada linha a linha, da coordenada 0,0 até a coordenada 8,8
  então sempre que um valor é válido a função vai printar o valor, populá-lo na tabela e ir pro próximo;
  Quando acabar a linha, a função irá printar a tabela toda e começar a popular a próxima linha.
  
  Exemplo:<br/>
  1 7 6 |3 8 5 |9 2 4<br/>
  
  9 8 5 |4 6 7 |1 3 0 <br/>
  
  0 0 0 |0 0 0 |0 0 0<br/>
____________________<br/>  
  0 0 0 |0 0 0 |0 0 0<br/>
  
  0 0 0 |0 0 0 |0 0 0<br/>
  
  0 0 0 |0 0 0 |0 0 0<br/>
____________________<br/>  
  0 0 0 |0 0 0 |0 0 0<br/>
  
  0 0 0 |0 0 0 |0 0 0<br/>
  
  0 0 0 |0 0 0 |0 0 0<br/>
  
  A função trava aqui, pois o único valor restante para a linha é o 2, porém o quadrado 3 já possui um 2.
  
###funcionamento quadrado(square_main.py)(não funcional)
Mesmo método do item a item, porém preenche de quadrado em quadrado, em vez de linha a linha.

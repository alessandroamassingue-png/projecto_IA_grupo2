# P9 — Travessia de Ferry com Cargas Incompatíveis

## 1. Identificação do Projecto

**Disciplina:** Inteligência Artificial I  
**Instituição:** Universidade Eduardo Mondlane (UEM)  
**Faculdade:** Faculdade de Engenharia  
**Curso:** Engenharia Informática  
**Grupo:** 02 — Pós-Laboral  
**Ano:** 2026

## 2. Descrição do Problema

O projecto consiste na implementação de um sistema de procura para resolver o problema da travessia de um ferry entre Maputo e Katembe, considerando pessoas, animais e cargas com restrições de segurança.

O ferry deve transportar todos os elementos de uma margem para a outra, respeitando as seguintes condições:

- Capacidade máxima de 150 kg por travessia;
- Transporte de, no máximo, três elementos por travessia;
- Cada travessia deve incluir pelo menos um adulto;
- Determinados elementos não podem permanecer juntos numa margem sem a presença de um adulto;
- Gás e combustível não podem ser transportados juntos na mesma travessia.

O objectivo é encontrar uma sequência válida de acções que permita transportar todos os elementos para Katembe, respeitando as restrições estabelecidas.

### 2.1. Representação dos Estados

```markdown
Cada estado é representado por uma tupla:


(mascara, barco)

Onde:

- mascara representa a localização dos elementos através de uma representação binária;
- barco indica a localização do ferry:
  - 0 — Maputo;
  - 1 — Katembe.

Na máscara, cada bit representa a localização de um elemento:

- 0 — elemento em Maputo;
- 1 — elemento em Katembe.

O estado inicial original é:

(0, 0)
```

O estado objectivo é:

```python
(511, 1)
```

O domínio também permite criar problemas com estados iniciais personalizados, mantendo o estado objectivo fixo.

### 2.2. Custo das Travessias

O custo de cada travessia é calculado através da seguinte fórmula:

\[
Custo = 10 + \frac{P}{10}
\]

Onde `P` representa o peso total, em quilogramas, dos elementos transportados nessa travessia.

## 3. Objectivos do Projecto

O projecto tem como principais objectivos:

- Modelar o problema através de uma representação formal de estados, acções, transições e custos;
- Implementar diferentes algoritmos de procura;
- Desenvolver e utilizar heurísticas;
- Gerar instâncias com diferentes níveis de dificuldade;
- Verificar o funcionamento dos algoritmos através de testes automatizados;
- Validar propriedades das heurísticas;
- Comparar o desempenho dos algoritmos através de experiências computacionais.

As experiências analisam principalmente:

- Número de nós expandidos;
- Número de nós gerados;
- Número de travessias;
- Custo total da solução;
- Tempo de execução;
- Consumo de memória.

## 4. Estrutura do Projecto

A organização actual do projecto é a seguinte:

```text
projecto_ia_grupo02/
│
├── problema.py
├── dominio.py
├── buscas.py
├── heuristicas.py
├── main.py
├── gerador.py
├── experiencias.py
├── pytest.ini
├── README.md
│
├── instancias/
│   ├── pequenas/
│   │   ├── pequena_01.json
│   │   ├── pequena_02.json
│   │   ├── pequena_03.json
│   │   ├── pequena_04.json
│   │   └── pequena_05.json
│   │
│   ├── medias/
│   │   ├── media_01.json
│   │   ├── media_02.json
│   │   ├── media_03.json
│   │   ├── media_04.json
│   │   └── media_05.json
│   │
│   └── grandes/
│       ├── grande_01.json
│       ├── grande_02.json
│       ├── grande_03.json
│       ├── grande_04.json
│       └── grande_05.json
│
├── resultados/
│   ├── resultados_experiencias.csv
│   ├── nos_expandidos.png
│   ├── tempo_execucao.png
│   └── custo_vs_optimo.png
│
├── tests/
│   ├── test_a_estrela.py
│   ├── test_bfs.py
│   ├── test_bidireccional.py
│   ├── test_dfs.py
│   ├── test_dominio.py
│   ├── test_greedy.py
│   ├── test_heuristicas.py
│   ├── test_ids.py
│   └── test_ucs.py
│
└── validacoes/
    ├── teste_admissibilidade.py
    ├── teste_heuristicas.py
    ├── teste_IDA_Estrela.py
    ├── teste_instancia.py
    └── teste_predecessores.py
```

## 5. Descrição dos Principais Ficheiros

| Ficheiro | Responsabilidade |
|---|---|
| `problema.py` | Define a classe abstracta `Problema`, a estrutura dos nós através da classe `No` e a função `caminho()` para reconstruir percursos. |
| `dominio.py` | Implementa o problema do ferry, incluindo os estados, as acções possíveis, as restrições, as transições, os custos e os predecessores. |
| `buscas.py` | Implementa os algoritmos de procura utilizados no projecto. |
| `heuristicas.py` | Contém as funções das heurísticas h1 e h2. |
| `main.py` | Apresenta o menu interactivo para seleccionar e executar os algoritmos. |
| `gerador.py` | Gera automaticamente instâncias pequenas, médias e grandes. |
| `experiencias.py` | Executa experiências, monitoriza limites de tempo e memória, guarda resultados e produz gráficos. |
| `pytest.ini` | Configura a descoberta dos ficheiros e funções de teste pelo pytest. |
| `README.md` | Apresenta a documentação e as instruções de utilização do projecto. |

### 5.1. Pasta `tests/`

Contém os testes automatizados desenvolvidos com pytest.

Os testes verificam:

- Funcionamento do domínio;
- Validade dos estados e das acções;
- Funcionamento dos algoritmos de procura;
- Reconstrução dos percursos;
- Validade das soluções encontradas;
- Admissibilidade e consistência das heurísticas;
- Optimalidade dos custos em algoritmos que garantem essa propriedade.

### 5.2. Pasta `validacoes/`

Contém programas auxiliares utilizados para demonstrar e verificar propriedades específicas do projecto.

| Ficheiro | Finalidade |
|---|---|
| `teste_admissibilidade.py` | Verifica admissibilidade, consistência, dominância das heurísticas e reversibilidade das transições. |
| `teste_heuristicas.py` | Apresenta os valores de h0, h1 e h2 para o estado inicial e compara as heurísticas. |
| `teste_IDA_Estrela.py` | Executa IDA* com h2 e apresenta a solução e as métricas. |
| `teste_instancia.py` | Demonstra a criação de instâncias com diferentes estados iniciais. |
| `teste_predecessores.py` | Demonstra a obtenção dos estados predecessores e a reversibilidade das transições. |

## 6. Algoritmos Implementados

O projecto disponibiliza doze configurações de algoritmos de procura:

1. Procura em Largura (BFS);
2. Procura em Profundidade (DFS);
3. Aprofundamento Iterativo (IDS);
4. Procura de Custo Uniforme (UCS);
5. Procura Gulosa com heurística h1;
6. Procura Gulosa com heurística h2;
7. A* com heurística h1;
8. A* com heurística h2;
9. IDA* com heurística h1;
10. IDA* com heurística h2;
11. Procura Bidireccional em Largura;
12. Procura Bidireccional de Custo Uniforme.

Os algoritmos estão implementados de forma genérica no módulo `buscas.py`, permitindo separar a lógica de procura das regras específicas do problema.

## 7. Heurísticas

Foram implementadas duas heurísticas principais:

### 7.1. Heurística h1

Estima o custo restante considerando o número de elementos que ainda estão em Maputo e a capacidade máxima de transporte do ferry.

### 7.2. Heurística h2

Considera o número total de elementos restantes e o número de elementos que não são adultos, tendo em conta a obrigação de transportar pelo menos um adulto por travessia.

A heurística h2 procura fornecer uma estimativa mais informativa do custo restante.

As duas heurísticas são utilizadas nos algoritmos Guloso, A* e IDA*.

A validação das suas propriedades encontra-se nos testes automatizados e nos programas auxiliares da pasta `validacoes/`.

## 8. Geração de Instâncias

O ficheiro `gerador.py` permite criar automaticamente quinze instâncias, distribuídas por três níveis de dificuldade.

| Nível | Distância mínima | Quantidade |
|---|---:|---:|
| Pequenas | 2 a 3 travessias | 5 |
| Médias | 4 a 6 travessias | 5 |
| Grandes | 7 a 8 travessias | 5 |
| **Total** | | **15** |

O gerador utiliza a semente fixa `202652`, permitindo reproduzir a geração das instâncias.

O processo começa no estado objectivo e utiliza transições inversas para obter estados iniciais. Posteriormente, a Procura em Largura (BFS) calcula a distância mínima de cada estado até ao objectivo.

A instância só é guardada quando a distância mínima calculada corresponde ao nível de dificuldade pretendido.

Cada instância é guardada num ficheiro JSON na pasta correspondente ao seu nível.

## 9. Execução do Projecto

### 9.1. Requisitos

- Python;
- PyCharm ou outro editor de código Python;
- pytest;
- matplotlib;
- psutil.

### 9.2. Instalação das dependências

No terminal do PyCharm, executar:

```bash
pip install pytest matplotlib psutil
```

### 9.3. Executar o programa principal

Para iniciar o menu interactivo:

```bash
python main.py
```

O menu apresenta doze opções de algoritmos de procura e uma opção para terminar o programa.

Depois de seleccionar um algoritmo, são apresentados:

- Número de travessias;
- Custo total;
- Nós expandidos;
- Nós gerados;
- Percurso encontrado;
- Estados visitados e acções realizadas.

No caso do IDS, também são apresentados o número de nós reexpandidos e o número de iterações.

O menu principal utiliza a instância inicial predefinida no domínio.

### 9.4. Gerar instâncias

Para gerar as quinze instâncias:

```bash
python gerador.py
```

As instâncias são guardadas automaticamente na pasta `instancias/`, separadas por nível de dificuldade.

### 9.5. Executar as experiências

Para executar as experiências com as instâncias geradas:

```bash
python experiencias.py
```

O programa carrega automaticamente os ficheiros JSON existentes na pasta `instancias/` e executa as doze configurações de algoritmos em cada instância.

Os resultados são guardados na pasta `resultados/`.

## 10. Execução dos Testes Automatizados

O projecto utiliza pytest para executar os testes automatizados.

Para executar todos os testes, utilizar:

```bash
pytest
```

Para executar apenas os testes de um módulo específico, pode ser utilizado, por exemplo:

```bash
pytest tests/test_dominio.py
```

A configuração de descoberta está definida em `pytest.ini`:

```ini
[pytest]
python_files = test_*.py
python_functions = test_*
```

Assim, o pytest identifica os ficheiros e as funções que seguem os padrões configurados.

## 11. Execução das Validações

Os programas da pasta `validacoes/` podem ser executados individualmente a partir da raiz do projecto.

### 11.1. Verificar admissibilidade e consistência

```bash
python -m validacoes.teste_admissibilidade
```

### 11.2. Apresentar os valores das heurísticas

```bash
python -m validacoes.teste_heuristicas
```

### 11.3. Executar IDA* com h2

```bash
python -m validacoes.teste_IDA_Estrela
```

### 11.4. Testar instâncias personalizadas

```bash
python -m validacoes.teste_instancia
```

### 11.5. Verificar predecessores

```bash
python -m validacoes.teste_predecessores
```

Estes programas são auxiliares de demonstração e validação. Não substituem os testes automatizados da pasta `tests/`.

## 12. Experiências e Limites de Execução

O ficheiro `experiencias.py` executa as experiências em processos independentes, permitindo monitorizar o tempo e a memória utilizados por cada algoritmo.

Foram definidos os seguintes limites:

- **Tempo máximo por execução:** 60 segundos;
- **Memória máxima monitorizada por processo:** 2 GB.

A memória é monitorizada através do RSS do processo, enquanto o `tracemalloc` regista a memória Python monitorizada durante a execução.

Quando um limite é ultrapassado, o processo é interrompido e o estado da execução é registado.

Os estados possíveis incluem:

- `ok` — execução concluída;
- `sem_solucao` — não foi encontrada uma solução;
- `tempo_limite` — foi atingido o limite de tempo;
- `memoria_limite` — foi ultrapassado o limite de memória;
- `erro` — ocorreu um erro durante a execução.

## 13. Resultados Experimentais

Os resultados das experiências são guardados na pasta `resultados/`.

### 13.1. Ficheiro CSV

O ficheiro:

```text
resultados/resultados_experiencias.csv
```

Contém os dados recolhidos durante as experiências, incluindo:

- Nome e nível da instância;
- Distância mínima;
- Algoritmo executado;
- Estado da execução;
- Custo da solução;
- Profundidade;
- Nós expandidos;
- Nós gerados;
- Tempo de execução;
- Memória observada;
- Nós reexpandidos;
- Número de iterações.

### 13.2. Gráficos

O programa produz três gráficos:

**1. `nos_expandidos.png`**

Compara a média de nós expandidos pelos algoritmos em função da distância mínima das instâncias.

**2. `tempo_execucao.png`**

Compara o tempo médio de execução dos algoritmos em função da distância mínima.

**3. `custo_vs_optimo.png`**

Compara os custos encontrados pelos algoritmos com os custos encontrados pelo UCS na mesma instância, utilizando o UCS como referência.

As médias dos gráficos consideram apenas as execuções concluídas com estado `ok`.

## 14. Observações Finais

O projecto está organizado em módulos independentes, permitindo separar a definição abstracta dos problemas, a implementação do domínio, os algoritmos de procura, as heurísticas, os testes e as experiências.

A pasta `tests/` contém os testes automatizados, enquanto a pasta `validacoes/` contém programas auxiliares para demonstração e verificação de propriedades específicas.

O ficheiro `main.py` permite executar os algoritmos individualmente sobre a instância original. O ficheiro `experiencias.py` permite comparar os algoritmos utilizando as instâncias pequenas, médias e grandes.

---

**Projecto P9 — Inteligência Artificial I**  
**Grupo 02 — Pós-Laboral | 2026**
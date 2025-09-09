# 🧬 Algoritmo Genético - Resolução de Equações Lineares

## 📋 Descrição

Este projeto implementa um **Algoritmo Genético** em Python para resolver equações lineares da forma `ax + by + cz = d`, onde `a`, `b`, `c` e `d` são constantes conhecidas, e o objetivo é encontrar valores inteiros para `x`, `y` e `z` que satisfaçam a equação.

O algoritmo utiliza os princípios da evolução biológica (seleção natural, cruzamento e mutação) para evoluir uma população de soluções candidatas até encontrar a solução ótima ou uma aproximação satisfatória.

## 🎯 Objetivo

Demonstrar a aplicação prática de algoritmos genéticos na resolução de problemas matemáticos, fornecendo:
- Implementação completa e modular
- Visualização da evolução do algoritmo
- Análise estatística dos resultados
- Interface intuitiva e educativa

## 🚀 Funcionalidades

### Operadores Genéticos Implementados:
- **Seleção por Torneio**: Seleciona os melhores indivíduos para reprodução
- **Cruzamento Uniforme**: Combina genes de dois pais para gerar descendentes
- **Mutação Adaptativa**: Introduz variações aleatórias para manter diversidade
- **Elitismo**: Preserva os melhores indivíduos entre gerações

### Características Avançadas:
- ✅ Parâmetros configuráveis (população, taxas de operadores, etc.)
- ✅ Múltiplos critérios de parada
- ✅ Coleta de estatísticas de evolução
- ✅ Visualização gráfica da convergência
- ✅ Validação automática de soluções
- ✅ Tratamento de múltiplos exemplos

## 📦 Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos para instalação:

1. **Clone ou baixe o repositório:**
```bash
git clone <url-do-repositorio>
cd algoritmo-genetico-equacoes
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv

# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## 🖥️ Como Usar

### Execução Básica:
```bash
python algoritmo_genetico.py
```

### Uso Programático:

```python
from algoritmo_genetico import AlgoritmoGenetico

# Criar instância para resolver: 3x + 5y + 2z = 14
ag = AlgoritmoGenetico(
    a=3, b=5, c=2, d=14,
    tamanho_populacao=100,
    taxa_cruzamento=0.8,
    taxa_mutacao=0.1,
    max_geracoes=500
)

# Executar o algoritmo
melhor_solucao, melhor_fitness = ag.executar()

# Exibir resultados
ag.exibir_resultados()

# Plotar evolução
ag.plotar_evolucao()
```

## ⚙️ Parâmetros Configuráveis

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|---------|-----------|
| `a, b, c, d` | int | - | Coeficientes da equação ax + by + cz = d |
| `tamanho_populacao` | int | 100 | Número de indivíduos na população |
| `taxa_cruzamento` | float | 0.8 | Probabilidade de cruzamento (0.0 a 1.0) |
| `taxa_mutacao` | float | 0.1 | Probabilidade de mutação (0.0 a 1.0) |
| `max_geracoes` | int | 1000 | Número máximo de gerações |
| `range_valores` | tuple | (-100, 100) | Faixa de valores para x, y, z |

## 📊 Exemplos de Uso

### Exemplo 1: Equação Simples
```python
# Resolver: 3x + 5y + 2z = 14
ag1 = AlgoritmoGenetico(a=3, b=5, c=2, d=14)
melhor_solucao, fitness = ag1.executar()
```

**Possível saída:**
```
Melhor solução: x = 2, y = 0, z = 4
Resultado: 3×2 + 5×0 + 2×4 = 14
✅ SOLUÇÃO EXATA ENCONTRADA!
```

### Exemplo 2: Equação Mais Complexa
```python
# Resolver: 7x + 4y + 3z = 25
ag2 = AlgoritmoGenetico(a=7, b=4, c=3, d=25, max_geracoes=600)
melhor_solucao, fitness = ag2.executar()
```

## 📈 Interpretação dos Resultados

### Fitness (Função Objetivo):
- **Fitness = 0**: Solução perfeita (satisfaz exatamente a equação)
- **Fitness > 0**: Diferença entre o resultado da equação e o valor esperado

### Gráfico de Evolução:
- **Linha azul**: Melhor fitness por geração
- **Linha vermelha tracejada**: Fitness médio da população
- **Escala logarítmica**: Facilita visualização da convergência

## 🔧 Estrutura do Código

```
algoritmo_genetico.py
├── Classe AlgoritmoGenetico
│   ├── __init__()              # Inicialização de parâmetros
│   ├── criar_populacao_inicial() # Geração da população
│   ├── calcular_fitness()       # Avaliação de indivíduos
│   ├── selecao_torneio()       # Seleção de pais
│   ├── cruzamento_uniforme()   # Geração de descendentes
│   ├── mutacao()               # Introdução de variabilidade
│   ├── executar()              # Loop principal do AG
│   ├── exibir_resultados()     # Apresentação de resultados
│   └── plotar_evolucao()       # Visualização gráfica
└── main()                      # Função de demonstração
```

## 🎓 Conceitos Educacionais

### Algoritmos Genéticos - Fundamentos:
1. **População**: Conjunto de soluções candidatas
2. **Indivíduo**: Uma solução específica representada por genes
3. **Fitness**: Medida de qualidade de uma solução
4. **Seleção**: Escolha de indivíduos para reprodução
5. **Cruzamento**: Combinação de características parentais
6. **Mutação**: Introdução de variações aleatórias
7. **Elitismo**: Preservação das melhores soluções

### Vantagens dos Algoritmos Genéticos:
- ✅ Não requerem derivadas ou gradientes
- ✅ Adequados para problemas discretos
- ✅ Exploram múltiplas regiões do espaço de busca
- ✅ Robustos a ruído e funções multimodais
- ✅ Paralelizáveis naturalmente

## 🛠️ Personalização e Extensões

### Modificar a Função de Fitness:
```python
def calcular_fitness_customizado(self, individuo):
    x, y, z = individuo
    # Exemplo: penalizar soluções com valores muito grandes
    resultado = abs(self.a * x + self.b * y + self.c * z - self.d)
    penalizacao = sum(abs(val) for val in individuo) * 0.01
    return resultado + penalizacao
```

### Adicionar Novos Operadores:
```python
def cruzamento_dois_pontos(self, pai1, pai2):
    """Implementação de cruzamento de dois pontos"""
    # Sua implementação aqui
    pass
```

## 📚 Dependências

- **numpy**: Operações matemáticas e arrays
- **matplotlib**: Visualização de gráficos
- **typing**: Anotações de tipo (Python 3.7+)

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é disponibilizado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas, sugestões ou problemas:

- Abra uma [issue](../../issues) no GitHub
- Consulte a documentação inline no código
- Verifique os exemplos fornecidos

## 🔍 Troubleshooting

### Problemas Comuns:

1. **Convergência lenta:**
   - Aumente o tamanho da população
   - Ajuste as taxas de cruzamento e mutação
   - Verifique se a faixa de valores é adequada

2. **Não encontra solução exata:**
   - Aumente o número máximo de gerações
   - Reduza a taxa de mutação
   - Verifique se a equação tem solução inteira

3. **Erro de importação:**
   - Verifique se todas as dependências estão instaladas
   - Confirme a versão do Python (3.7+)

---

**Desenvolvido com 💙 para fins educacionais e demonstração de algoritmos genéticos**
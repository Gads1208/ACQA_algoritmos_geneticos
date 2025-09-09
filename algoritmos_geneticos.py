import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
import copy

class AlgoritmoGenetico:
    """
    Implementação de um Algoritmo Genético para resolver equações lineares da forma ax + by + cz = d
    """
    
    def __init__(self, a: int, b: int, c: int, d: int, 
                 tamanho_populacao: int = 100, 
                 taxa_cruzamento: float = 0.8,
                 taxa_mutacao: float = 0.1,
                 max_geracoes: int = 1000,
                 range_valores: Tuple[int, int] = (-100, 100)):
        """
        Inicializa o Algoritmo Genético
        
        Args:
            a, b, c, d: Coeficientes da equação ax + by + cz = d
            tamanho_populacao: Número de indivíduos na população
            taxa_cruzamento: Probabilidade de cruzamento
            taxa_mutacao: Probabilidade de mutação
            max_geracoes: Número máximo de gerações
            range_valores: Faixa de valores para x, y, z
        """
        self.a, self.b, self.c, self.d = a, b, c, d
        self.tamanho_populacao = tamanho_populacao
        self.taxa_cruzamento = taxa_cruzamento
        self.taxa_mutacao = taxa_mutacao
        self.max_geracoes = max_geracoes
        self.range_min, self.range_max = range_valores
        
        # Para armazenar estatísticas da evolução
        self.historico_fitness = []
        self.melhor_individuo = None
        self.melhor_fitness = float('inf')
        
    def criar_individuo(self) -> List[int]:
        """
        Cria um indivíduo aleatório representado por [x, y, z]
        
        Returns:
            Lista com três valores inteiros aleatórios
        """
        return [random.randint(self.range_min, self.range_max) for _ in range(3)]
    
    def criar_populacao_inicial(self) -> List[List[int]]:
        """
        Gera a população inicial com indivíduos aleatórios
        
        Returns:
            Lista de indivíduos (população)
        """
        print("🔄 Gerando população inicial...")
        populacao = [self.criar_individuo() for _ in range(self.tamanho_populacao)]
        print(f"✅ População inicial criada com {len(populacao)} indivíduos")
        return populacao
    
    def calcular_fitness(self, individuo: List[int]) -> float:
        """
        Calcula o fitness de um indivíduo baseado na diferença da equação
        Fitness = |ax + by + cz - d| (quanto menor, melhor)
        
        Args:
            individuo: Lista [x, y, z]
            
        Returns:
            Valor do fitness (0 = solução perfeita)
        """
        x, y, z = individuo
        resultado_equacao = self.a * x + self.b * y + self.c * z
        fitness = abs(resultado_equacao - self.d)
        return fitness
    
    def avaliar_populacao(self, populacao: List[List[int]]) -> List[Tuple[List[int], float]]:
        """
        Avalia toda a população e retorna indivíduos com seus fitness
        
        Args:
            populacao: Lista de indivíduos
            
        Returns:
            Lista de tuplas (indivíduo, fitness) ordenada por fitness
        """
        avaliacao = [(individuo, self.calcular_fitness(individuo)) for individuo in populacao]
        # Ordena por fitness (menor é melhor)
        avaliacao.sort(key=lambda x: x[1])
        return avaliacao
    
    def selecao_torneio(self, populacao_avaliada: List[Tuple[List[int], float]], 
                       tamanho_torneio: int = 3) -> List[int]:
        """
        Seleciona um indivíduo através do método de torneio
        
        Args:
            populacao_avaliada: População com fitness calculado
            tamanho_torneio: Número de indivíduos no torneio
            
        Returns:
            Indivíduo selecionado
        """
        # Seleciona aleatoriamente indivíduos para o torneio
        candidatos = random.sample(populacao_avaliada, tamanho_torneio)
        # Retorna o melhor do torneio (menor fitness)
        vencedor = min(candidatos, key=lambda x: x[1])
        return copy.deepcopy(vencedor[0])
    
    def cruzamento_uniforme(self, pai1: List[int], pai2: List[int]) -> Tuple[List[int], List[int]]:
        """
        Realiza cruzamento uniforme entre dois pais
        
        Args:
            pai1, pai2: Indivíduos pais
            
        Returns:
            Dois filhos resultantes do cruzamento
        """
        if random.random() > self.taxa_cruzamento:
            return copy.deepcopy(pai1), copy.deepcopy(pai2)
        
        filho1, filho2 = copy.deepcopy(pai1), copy.deepcopy(pai2)
        
        # Para cada gene, decide aleatoriamente de qual pai herdar
        for i in range(len(pai1)):
            if random.random() < 0.5:
                filho1[i], filho2[i] = filho2[i], filho1[i]
        
        return filho1, filho2
    
    def mutacao(self, individuo: List[int]) -> List[int]:
        """
        Aplica mutação em um indivíduo
        
        Args:
            individuo: Indivíduo a ser mutado
            
        Returns:
            Indivíduo mutado
        """
        individuo_mutado = copy.deepcopy(individuo)
        
        for i in range(len(individuo_mutado)):
            if random.random() < self.taxa_mutacao:
                # Mutação: adiciona um valor aleatório pequeno
                mutacao_valor = random.randint(-10, 10)
                individuo_mutado[i] = max(self.range_min, 
                                        min(self.range_max, 
                                            individuo_mutado[i] + mutacao_valor))
        
        return individuo_mutado
    
    def executar(self) -> Tuple[List[int], float]:
        """
        Executa o algoritmo genético completo
        
        Returns:
            Melhor indivíduo encontrado e seu fitness
        """
        print(f"🎯 Resolvendo equação: {self.a}x + {self.b}y + {self.c}z = {self.d}")
        print(f"📊 Parâmetros: Pop={self.tamanho_populacao}, Cruzamento={self.taxa_cruzamento}, Mutação={self.taxa_mutacao}")
        print("-" * 60)
        
        # Criar população inicial
        populacao = self.criar_populacao_inicial()
        
        for geracao in range(self.max_geracoes):
            # Avaliar população
            populacao_avaliada = self.avaliar_populacao(populacao)
            
            # Atualizar melhor indivíduo
            melhor_atual = populacao_avaliada[0]
            if melhor_atual[1] < self.melhor_fitness:
                self.melhor_individuo = copy.deepcopy(melhor_atual[0])
                self.melhor_fitness = melhor_atual[1]
            
            # Armazenar estatísticas
            fitness_medio = sum(ind[1] for ind in populacao_avaliada) / len(populacao_avaliada)
            self.historico_fitness.append({
                'geracao': geracao,
                'melhor_fitness': melhor_atual[1],
                'fitness_medio': fitness_medio,
                'melhor_individuo': copy.deepcopy(melhor_atual[0])
            })
            
            # Verificar critério de parada
            if melhor_atual[1] == 0:
                print(f"🎉 SOLUÇÃO ENCONTRADA na geração {geracao}!")
                print(f"💡 Solução: x={melhor_atual[0][0]}, y={melhor_atual[0][1]}, z={melhor_atual[0][2]}")
                break
            
            # Mostrar progresso a cada 50 gerações
            if geracao % 50 == 0:
                print(f"Geração {geracao:4d}: Melhor fitness = {melhor_atual[1]:6.2f}, "
                      f"Fitness médio = {fitness_medio:6.2f}")
            
            # Criar nova população
            nova_populacao = []
            
            # Elitismo: manter os 2 melhores
            nova_populacao.extend([copy.deepcopy(ind[0]) for ind in populacao_avaliada[:2]])
            
            # Gerar resto da população por cruzamento e mutação
            while len(nova_populacao) < self.tamanho_populacao:
                pai1 = self.selecao_torneio(populacao_avaliada)
                pai2 = self.selecao_torneio(populacao_avaliada)
                
                filho1, filho2 = self.cruzamento_uniforme(pai1, pai2)
                
                filho1 = self.mutacao(filho1)
                filho2 = self.mutacao(filho2)
                
                nova_populacao.extend([filho1, filho2])
            
            # Ajustar tamanho da população
            populacao = nova_populacao[:self.tamanho_populacao]
        
        print("-" * 60)
        print(f"🏁 Algoritmo finalizado após {geracao + 1} gerações")
        return self.melhor_individuo, self.melhor_fitness
    
    def verificar_solucao(self, individuo: List[int]) -> bool:
        """
        Verifica se um indivíduo é uma solução válida
        
        Args:
            individuo: Lista [x, y, z]
            
        Returns:
            True se for uma solução válida
        """
        x, y, z = individuo
        return (self.a * x + self.b * y + self.c * z) == self.d
    
    def exibir_resultados(self):
        """
        Exibe os resultados finais do algoritmo
        """
        if self.melhor_individuo:
            x, y, z = self.melhor_individuo
            resultado = self.a * x + self.b * y + self.c * z
            
            print("\n" + "="*60)
            print("📈 RESULTADOS FINAIS")
            print("="*60)
            print(f"Equação original: {self.a}x + {self.b}y + {self.c}z = {self.d}")
            print(f"Melhor solução encontrada: x = {x}, y = {y}, z = {z}")
            print(f"Resultado da equação: {self.a}×{x} + {self.b}×{y} + {self.c}×{z} = {resultado}")
            print(f"Fitness (diferença): {self.melhor_fitness}")
            
            if self.verificar_solucao(self.melhor_individuo):
                print("✅ SOLUÇÃO EXATA ENCONTRADA!")
            else:
                print(f"⚠️  Solução aproximada (erro de {self.melhor_fitness})")
            
            print("="*60)
    
    def plotar_evolucao(self):
        """
        Plota gráfico da evolução do fitness ao longo das gerações
        """
        if not self.historico_fitness:
            print("❌ Nenhum dado de evolução disponível para plotar.")
            return
        
        geracoes = [h['geracao'] for h in self.historico_fitness]
        melhor_fitness = [h['melhor_fitness'] for h in self.historico_fitness]
        fitness_medio = [h['fitness_medio'] for h in self.historico_fitness]
        
        plt.figure(figsize=(12, 6))
        plt.plot(geracoes, melhor_fitness, 'b-', label='Melhor Fitness', linewidth=2)
        plt.plot(geracoes, fitness_medio, 'r--', label='Fitness Médio', alpha=0.7)
        plt.xlabel('Geração')
        plt.ylabel('Fitness (Erro)')
        plt.title('Evolução do Algoritmo Genético')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.yscale('log')  # Escala logarítmica para melhor visualização
        plt.show()


def main():
    """
    Função principal para demonstrar o uso do Algoritmo Genético
    """
    print("🧬 ALGORITMO GENÉTICO - RESOLUÇÃO DE EQUAÇÕES LINEARES")
    print("=" * 60)
    
    # Exemplo 1: 3x + 5y + 2z = 14
    print("\n🔍 EXEMPLO 1: 3x + 5y + 2z = 14")
    ag1 = AlgoritmoGenetico(a=3, b=5, c=2, d=14, 
                           tamanho_populacao=150, 
                           taxa_cruzamento=0.8, 
                           taxa_mutacao=0.1,
                           max_geracoes=500)
    
    melhor_solucao1, melhor_fitness1 = ag1.executar()
    ag1.exibir_resultados()
    
    # Exemplo 2: 2x + 3y + z = 10
    print("\n🔍 EXEMPLO 2: 2x + 3y + z = 10")
    ag2 = AlgoritmoGenetico(a=2, b=3, c=1, d=10,
                           tamanho_populacao=100,
                           taxa_cruzamento=0.9,
                           taxa_mutacao=0.05,
                           max_geracoes=300)
    
    melhor_solucao2, melhor_fitness2 = ag2.executar()
    ag2.exibir_resultados()
    
    # Exemplo 3: Equação mais complexa
    print("\n🔍 EXEMPLO 3: 7x + 4y + 3z = 25")
    ag3 = AlgoritmoGenetico(a=7, b=4, c=3, d=25,
                           tamanho_populacao=200,
                           taxa_cruzamento=0.85,
                           taxa_mutacao=0.15,
                           max_geracoes=600)
    
    melhor_solucao3, melhor_fitness3 = ag3.executar()
    ag3.exibir_resultados()
    
    # Plotar evolução do primeiro exemplo
    print("\n📊 Plotando evolução do Exemplo 1...")
    ag1.plotar_evolucao()
    
    print("\n🎯 Demonstração concluída!")


if __name__ == "__main__":
    main()
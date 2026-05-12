def salvar_avaliacoes(filmes, notas):
    "Salva as avaliações em um arquivo de texto"
    try:
        with open('avaliacoes_de_filmes.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('=== Avaliação dos Filmes ===\n\n')
            
            for i in range(len(filmes)):
                arquivo.write(f'Filme: {filmes[i]}\n')
                arquivo.write(f'Nota: {notas[i]:.1f}\n')
                
                # Classificação
                if notas[i] > 8:
                    classificacao = 'Excelente'
                elif notas[i] >= 7:
                    classificacao = 'Muito Bom'
                elif notas[i] >= 5:
                    classificacao = 'Regular'
                else:
                    classificacao = 'Ruim'
                
                arquivo.write(f'Classificação: {classificacao}\n')
                arquivo.write('-' * 40 + '\n\n')
            
            # Estatísticas
            if len(notas) > 0:
                media = sum(notas) / len(notas)
                arquivo.write(f'\n=== Estatísticas ===\n')
                arquivo.write(f'Total de filmes avaliados: {len(filmes)}\n')
                arquivo.write(f'Média das notas: {media:.2f}\n')
                arquivo.write(f'Melhor nota: {max(notas):.1f}\n')
                arquivo.write(f'Pior nota: {min(notas):.1f}\n')
        
        print('Avaliações salvas com sucesso em "avaliacoes_de_filmes.txt".')
    except Exception as e:
        print(f'Erro ao salvar avaliações: {e}')


def main():
    """Função principal do avaliador de filmes"""
    print('=== Avaliador de Filmes ===\n')
    
    filmes = []
    notas = []
    
    avaliar_novamente = 's'
    
    while avaliar_novamente == 's':
        nome_do_filme = input('Qual o nome do filme? ')
        
        # Validação da nota
        while True:
            try:
                nota_filme = float(input('De 0 a 10, qual a nota que você dá para este filme? '))
                
                if nota_filme < 0 or nota_filme > 10:
                    print('Nota inválida! Digite uma nota entre 0 e 10.')
                    continue
                
                break  # Nota válida, sair do loop
            except ValueError:
                print('Nota inválida! Digite apenas números.')
        
        # Adicionar filme e nota às listas
        filmes.append(nome_do_filme)
        notas.append(nota_filme)
        
        # Classificar o filme
        if nota_filme > 8:
            print(f'O filme "{nome_do_filme}" foi classificado como Excelente!')
        elif nota_filme >= 7:
            print(f'O filme "{nome_do_filme}" foi classificado como Muito Bom.')
        elif nota_filme >= 5:
            print(f'O filme "{nome_do_filme}" foi classificado como Regular.')
        else:
            print(f'O filme "{nome_do_filme}" foi classificado como Ruim.')
        
        print()
        avaliar_novamente = input('Deseja avaliar outro filme? (s/n): ').lower()
        print()
    
    # Exibir estatísticas
    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print('\n=== Resumo das Avaliações ===')
        print(f'Filmes avaliados: {", ".join(filmes)}')
        print(f'Notas registradas: {[f"{nota:.1f}" for nota in notas]}')
        print(f'Média das notas: {media:.2f}')
        print(f'Total de filmes avaliados: {len(filmes)}')
        
        # Perguntar se deseja salvar as avaliações 
        print()
        salvar = input('Deseja salvar as avaliações em um arquivo de texto? (s/n): ').lower()
        if salvar == 's':
            salvar_avaliacoes(filmes, notas)
    else:
        print('Nenhum filme foi avaliado.')


    print('\nObrigado(a) por utilizar o avaliador de filmes!')

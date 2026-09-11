# Scholarship Eligibility Evaluator - Testes e Análise de Mutação

Este repositório contém a suíte de testes automatizados e as instruções para execução da análise de mutação do sistema Scholarship Eligibility Evaluator.

## Como Executar os Testes

Para rodar a suíte de testes funcionais e estruturais, abra o terminal na pasta raiz do projeto e execute o comando principal:

`bash
pytest
`

Para executar os testes e visualizar o relatório de cobertura estrutural, detalhando as linhas executadas, utilize:

`bash
pytest --cov=ScholarshipEligibilityEvaluator --cov-report=term-missing
`

## Como Executar a Análise de Mutação

O processo de análise de mutação com o Cosmic Ray foi dividido em duas etapas para avaliar a evolução da suíte de testes. Os relatórios gerados com o sufixo **_1** correspondem à primeira rodada de mutação (score inicial), e os arquivos com o sufixo **_2** referem-se à segunda rodada (score final após a implementação de testes adicionais para cobrir lacunas).

Execute a seguinte sequência de comandos no terminal para reproduzir a análise:

**1. Inicializar a sessão**
Cria o banco de dados da sessão de mutação com base no arquivo de configuração existente:
`bash
cosmic-ray init cosmic-ray.toml session.sqlite
`

**2. Executar o baseline**
Garante que a suíte de testes atual passa integralmente no código original, sem mutações:
`bash
cosmic-ray baseline cosmic-ray.toml
`

**3. Executar a mutação**
Injeta as mutações e roda a suíte de testes contra cada mutante gerado:
`bash
cosmic-ray exec cosmic-ray.toml session.sqlite
`

**4. Gerar os Relatórios**
Para extrair o log da primeira rodada (suíte inicial):
`bash
cr-report session.sqlite > relatorio_mutacao_1.txt
`

Para reproduzir a segunda rodada, exclua o banco de dados da sessão atual (`del session.sqlite`), adicione os testes complementares à suíte, repita os passos de 1 a 3, e extraia o novo relatório final:
`bash
cr-report session.sqlite > relatorio_mutacao_2.txt
`
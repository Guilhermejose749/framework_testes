# Scholarship Eligibility Evaluator - Testes e Análise de Mutação

Este repositório contém a suíte de testes automatizados e as instruções para execução da análise de mutação do sistema **Scholarship Eligibility Evaluator**.

## Pré-requisitos

Certifique-se de ter as ferramentas instaladas no seu ambiente Python antes de executar os comandos:
```bash
pip install pytest pytest-cov cosmic-ray
```

## Como Executar os Testes

Para rodar a suíte de testes funcionais e estruturais, abra o terminal na pasta raiz do projeto e execute o comando principal:
```bash
pytest
```

Para executar os testes e visualizar o relatório de cobertura estrutural (detalhando exatamente quais linhas foram ou não executadas), utilize:
```bash
pytest --cov=ScholarshipEligibilityEvaluator --cov-report=term-missing
```

## Como Executar a Análise de Mutação

O processo de análise com o **Cosmic Ray** foi dividido em duas etapas para documentar a evolução da suíte de testes:
* **Arquivos `_1`:** Correspondem à primeira rodada de mutação (score inicial).
* **Arquivos `_2`:** Referem-se à segunda rodada (score final após a implementação de testes adicionais para cobrir lacunas).

Execute a sequência abaixo no terminal para reproduzir a análise completa:

**1. Inicializar a sessão**
Cria o banco de dados da sessão de mutação com base no arquivo de configuração existente:
```bash
cosmic-ray init cosmic-ray.toml session.sqlite
```

**2. Executar o baseline**
Garante que a suíte de testes atual passa integralmente no código original, sem mutações:
```bash
cosmic-ray baseline cosmic-ray.toml
```

**3. Executar a mutação**
Injeta as mutações e roda a suíte de testes contra cada mutante gerado:
```bash
cosmic-ray exec cosmic-ray.toml session.sqlite
```

**4. Gerar os Relatórios**
Para extrair o log da primeira rodada (suíte inicial), exporte a saída para um arquivo de texto:
```bash
cr-report session.sqlite > relatorio_mutacao_1.txt
```

**5. Executar a Segunda Rodada**
Para reproduzir o score final, exclua o banco de dados da sessão atual, adicione os testes complementares à suíte, repita os passos de 1 a 3, e extraia o novo relatório:
```bash
del session.sqlite
# Repita os passos 1, 2 e 3
cr-report session.sqlite > relatorio_mutacao_2.txt
```
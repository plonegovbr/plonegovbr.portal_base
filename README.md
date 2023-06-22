<div align="center"><img alt="logo" src="https://raw.githubusercontent.com/plonegovbr/plonegovbr.portal_base/main/docs/logo.svg" width="100" /></div>

<h1 align="center">Portal Brasil: Configurações Base</h1>

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/plonegovbr.portal_base)](https://pypi.org/project/plonegovbr.portal_base/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/plonegovbr.portal_base)](https://pypi.org/project/plonegovbr.portal_base/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/plonegovbr.portal_base)](https://pypi.org/project/plonegovbr.portal_base/)
[![PyPI - License](https://img.shields.io/pypi/l/plonegovbr.portal_base)](https://pypi.org/project/plonegovbr.portal_base/)
[![PyPI - Status](https://img.shields.io/pypi/status/plonegovbr.portal_base)](https://pypi.org/project/plonegovbr.portal_base/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/plonegovbr.portal_base)](https://pypi.org/project/plonegovbr.portal_base/)

[![Meta](https://github.com/plonegovbr/plonegovbr.portal_base/actions/workflows/meta.yml/badge.svg)](https://github.com/plonegovbr/plonegovbr.portal_base/actions/workflows/meta.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/plonegovbr/plonegovbr.portal_base)](https://github.com/plonegovbr/plonegovbr.portal_base)
[![GitHub Repo stars](https://img.shields.io/github/stars/plonegovbr/plonegovbr.portal_base?style=social)](https://github.com/plonegovbr/plonegovbr.portal_base)

</div>

## Sumário

`plonegovbr.portal_base` é a base de código compartilhada pelas várias distribuições do [Portal Brasil](https://plone.org.br/projetos/portal-brasil).

## Funcionalidades
### Tipos de conteúdo

#### Campus

Representa um Campus de uma instituição de ensino superior.

#### Curso

Representa um Curso de uma instituição de ensino superior.

### Comportamentos

#### plonegovbr.portal_base.campi

Adiciona o atributo `campi` que permite que um conteúdo tenha relacionamento com 1 ou mais objetos do tipo `Campus`.

### Vocabulários

| id | descrição |
| -- | -- |
| plonegovbr.portal_base.vocab.campi | Lista de todos os objetos do tipo Campus presentes no Portal |

### Catálogo

Esse pacote adiciona os seguintes índices e metadados ao `Portal Catalog`.

| Atributo | Tipo do Índice | Metadado | Comentário |
| -- | -- | -- | -- |
| campi | KeywordIndex | ✅ | Utilizado quando o comportamento `plonegovbr.portal_base.campi` está habilitado |

## Documentação

### Instalação em seu site

Esse pacote é parte do `Portal Brasil`.

## Desenvolvimento

- [Código fonte](https://github.com/plonegovbr/plonegovbr.portal_base/)
- [Tickets](https://github.com/plonegovbr/plonegovbr.portal/issues)

### Configuração do ambiente

**Você precisa ter o Python (versão 3.8 ou superior) instalado em seu computador.**

Para instalação do ambiente de desenvolvimento, rode:

```bash
make install
```

Utilizamos a versão mais atual do Plone 6.x para o desenvolvimento deste produto.

### Atualizar traduções

```bash
make i18n
```
### Formatar a base de código

```bash
make format
```
### Rodar os testes

```bash
make test
```

## License

The project is licensed under GPLv2.

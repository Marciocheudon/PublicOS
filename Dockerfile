# Use uma imagem oficial do Python como imagem base
FROM python:3.8-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos para o container
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do diretório local para o container
COPY . .

# Defina a variável de ambiente para informar ao Flask como executar
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Informe o Docker de que o container irá escutar na porta 8080 no tempo de execução
EXPOSE 8080

# Defina o comando padrão para o container
CMD ["flask", "run"]

# Titulo do projeto
Attendance System

# Sobre o projeto
#### A fim de automatizar o processo de chamdas na sala de aula, esse projeto utiliza conceitos de deep learning como reconhecimento facial para tornar essa atividade algo simples e sem necessidade de trabalho humano.

# Objetivo do projeto
#### O objetivo do projeto é realizar chamadas em uma sala de aula de maneira automatizada através do reconhecimento facial dos alunos.

# Como funciona
#### Utilizando um script python que processa imagens através de uma webcam é populado um arquivo csv contendo o nome da pessoa e horario em que ela foi encontrada. Sempre que esse csv é atualizado essa informação é enviada a um servidor que está rodando em segundo plano que guarda todas as informações que estão sendo logadas. Depois dessa fase de processamento e envio ao servidor existe uma pagina web que consome essas informações no servidor e gera uma visão mais limpa e clara sobre essas informações.

# Tecnologias utilizadas
- Python
- JavaScript
- Java

# Como executar o projeto
1. Fazer cadastros dos rostos utilizando o script `register` na pasta processing.
2. Deixar o script `attendance` rodando de fundo para realizar o log da chamada.
3. Levantar o servidor java na pasta backend, arquivo `backend\attendance\src\main\java\com\attendance\attendance\AttendanceApplication.java`
4. Para interface mais amigavel utilizar o que foi construido na pasta frontend rodando o liveserver, tendo acesso a pagina web dentro do servidor local.

# Referencias
[Face Recognition Docs](https://face-recognition.readthedocs.io/en/latest/index.html)  
[Artigo Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)  
[Qt Designer Docs](https://doc.qt.io/qtforpython/)

# Professor
### Vandeir

# Autores
### Nícollas De Oliveira
### Gabriel Victor Reggiani Viaro

# Titulo do projeto
Attendance System

# Sobre o projeto
#### A fim de automatizar o processo de chamdas na sala de aula, esse projeto utiliza conceitos de deep learning como reconhecimento facial para tornar essa atividade algo simples e sem necessidade de trabalho humano.

# Objetivo do projeto
#### O objetivo do projeto é realizar chamadas em uma sala de aula de maneira automatizada através do reconhecimento facial dos alunos.

# Como funciona
#### Utilizando um script python que processa imagens através de uma webcam é populado um arquivo csv contendo o nome da pessoa e horario em que ela foi encontrada. Sempre que esse csv é atualizado essa informação é enviada a um servidor que está rodando em segundo plano que guarda todas as informações que estão sendo logadas. Depois dessa fase de processamento e envio ao servidor existe uma pagina web que consome essas informações no servidor e gera uma visão mais limpa e clara sobre essas informações.

# Algumas tecnologias utilizadas
- Python
- JavaScript
- Java

# Como 'levantar' a aplicacao 
0.  - Instalar [VSCode](https://code.visualstudio.com/download)
    - Instalar extensao *Live Server*
      - Nas configuracoes do vscode, `settings.json`, adicionar a seguinte linha para configurar a porta do Live Server: `"liveServer.settings.port": 8085`
1. Instalar [git](https://git-scm.com/downloads)
2.  - Instalar [Java JRE/JDK](https://www.oracle.com/java/technologies/downloads/)
    - Adicionar `JAVA_HOME` as variaveis de ambiente
3. Instalar [Python](https://www.python.org/downloads/)
4.  - Executar servidor Java
    - Abrir no browser `localhost:8081/h2` para configurar o BD
    - **JDBC URL**: `jdbc:h2:file:~/dump/dev/projects/attendance/database`
    - **user**: `attendance` /// **password**: `pass`
    - Depois de logado va ate `backend/attendance/src/main/resources/database` e execute os scripts `schema.sql` e `data.sql` (*mock data*)
5.  - Abra o arquivo `frontend/index.html`, botao direito ---> *open with liveserver*
    - Os arquivos mockados ja devem estar disponiveis na aplicacao web
6.  - Abra o terminal no diretorio do projeto e execute `pip install -r processing/requirements.txt`
    - Isso vai instalar quase todas as dependencias necessarias, infelizmente o dlib e o face_recognition nao deram muito certo instalando dessa maneira, entao as libs foram removidas do arquivo requirements.txt e iremos realizar a instalacao de outra forma (manual).
    - ***Windows***:
        - Realize o download desse [repositorio](https://github.com/RvTechiNNovate/face_recog_dlib_file) e extraia os arquivos em uma pasta
        - Abra a pasta extraida e novamente abra essa nova pasta no terminal
        - No terminal execute:
            - `pip install dlib-19.19.0-cp37-cp37m-win_amd64.whl` **OU** `pip install dlib-19.19.0-cp38-cp38-win_amd64.whl` de acordo com seu sistema operacional
            - Com o dlib instalado, execute novamente agora a instalacao do face_recognition: `pip install face_recognition==1.3.0`
    - ***Linux***:
        - Abra o terminal e execute nesta ordem:
            - `sudo apt-get install cmake`
            - `sudo pip3 install dlib==19.19.0`
            - `sudo pip3 install face_recognition==1.3.0`
7.  - A partir desse momento basta executar a partir da raiz do projeto: `python interface/main_menu.py` e utilizar o app.
    - No Linux pode ser que o PyQt5 nao funcione pela instalacao do pip, instale novamente utilizando o apt-get com o comando `sudo apt-get install python3-pyqt5`

# Como utilizar o app
1.  - Levantar o servidor java na pasta backend, executar o arquivo `backend\attendance\src\main\java\com\attendance\attendance\AttendanceApplication.java`.
    - Levantar o servidor liveserver na pasta frontend, rodar o servidor pelo arquivo `frontend\index.html`.
2. Executar o `main_menu.py` na pasta interface.
3. De acordo com a necessidade cadastrar novas faces ou simplesmente deixar executando a chamada.
4. Abrir a pagina web no terceiro botao da interface e analisar os registros inputados de acordo com o reconhecimento facial do script.

# Referencias
[Face Recognition Docs](https://face-recognition.readthedocs.io/en/latest/index.html)  
[Artigo Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)  
[Qt Designer Docs](https://doc.qt.io/qtforpython/)

# Professor
### Vandeir

# Autores
### Nícollas De Oliveira
### Gabriel Victor Reggiani Viaro

# 👁️ Contador de Piscadas com Python + OpenCV + Dlib

Este projeto realiza a **detecção de piscadas de olho em tempo real** usando a câmera do computador. Ele é baseado no cálculo do **Eye Aspect Ratio (EAR)** para identificar piscadas naturais, exibindo na tela um contador atualizado ao vivo.

## 📷 Demonstração

![preview](https://user-images.githubusercontent.com/SEU_USUARIO_GITHUB/preview.gif)  
*(adicione um GIF ou print da aplicação aqui, se quiser)*

---

## 🧠 Conceito

O projeto utiliza a técnica de **EAR (Eye Aspect Ratio)**, que calcula a razão entre distâncias verticais e horizontais dos olhos com base nos pontos faciais detectados pela biblioteca **dlib**. Quando o EAR cai abaixo de um determinado limiar, e por um certo número de frames consecutivos, é considerado uma piscada.

---

## 📦 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [Dlib](http://dlib.net/)
- [face_utils (imutils)](https://github.com/jrosebr1/imutils)
- [scipy](https://scipy.org/)

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO_GITHUB/face-blink-counter.git
cd face-blink-counter

2. Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate
3. Instale as dependências
pip install -r requirements.txt
4. Baixe o modelo de pontos faciais
Faça o download do arquivo:

📥 shape_predictor_68_face_landmarks.dat

Extraia com:

bunzip2 shape_predictor_68_face_landmarks.dat.bz2
Coloque o arquivo .dat dentro da pasta do projeto.

5. Execute a aplicação
python app.py
Pressione q para encerrar.

📁 Estrutura do Projeto

face-blink-counter/
│
├── app.py                      # Código principal
├── shape_predictor_68_face_landmarks.dat  # Modelo de pontos faciais (não incluído no Git)
├── .gitignore
└── README.md
🧪 Calibração

A detecção de piscadas pode ser ajustada pelos seguintes parâmetros no código:

EAR_THRESHOLD = 0.25           # Limiar para olho fechado
EAR_CONSEC_FRAMES = 1          # Frames consecutivos abaixo do limiar
Você pode visualizar o valor do EAR em tempo real no terminal e ajustar conforme necessário.

📄 Licença

Este projeto é open-source sob a licença MIT.
Sinta-se à vontade para usar, modificar e contribuir!

✍️ Autor

Fernando – makeandcoding.com
Apaixonado por tecnologia, visão computacional, automação e projetos maker.
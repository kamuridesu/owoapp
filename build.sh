curl https://gist.githubusercontent.com/kamuridesu/70391992baaf11a6655e5993cff182ec/raw/1c4df9081bddfdedfa41e695b8bbdbe44d1b3d84/app.py > app.py
curl https://gist.githubusercontent.com/kamuridesu/70391992baaf11a6655e5993cff182ec/raw/1c4df9081bddfdedfa41e695b8bbdbe44d1b3d84/Dockerfile > Dockerfile
curl https://gist.githubusercontent.com/kamuridesu/70391992baaf11a6655e5993cff182ec/raw/1c4df9081bddfdedfa41e695b8bbdbe44d1b3d84/read_env.py > read_env.py
docker build -t kamupplication .
docker run --rm -it --name kamupplication -p 9000:9000 kamupplication  # use -e para passar as variaveis de ambiente
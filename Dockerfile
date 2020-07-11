FROM python:3.6

RUN apt-get update && apt-get install -y python3-distutils && apt-get install -y python3-tk libxext-dev libxrender-dev libxtst-dev djvulibre-bin netpbm imagemagick
ADD start.sh .
RUN chmod +x start.sh
EXPOSE 5000
CMD ./start.sh
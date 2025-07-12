# 使用 Python 3.12 官方映像作為基礎映像
# 這個映像包含了 Python 3.12 運行環境和基本的系統工具
FROM python:3.12

# 將當前目錄（包含應用程式代碼）複製到容器的 /opt/app 目錄
# 這會將所有檔案從主機複製到容器內，包括 weather_code.py、requirements.txt 等
COPY . /opt/app

# 設定容器的工作目錄為 /opt/app
# 後續的 RUN、CMD 等指令都會在這個目錄下執行
WORKDIR /opt/app

# 安裝 Python 依賴套件
# --no-cache-dir: 不緩存下載的套件，減少映像大小
# -r requirements.txt: 從 requirements.txt 檔案讀取需要安裝的套件清單
RUN pip install --no-cache-dir -r requirements.txt

# 設定容器啟動時執行的命令
# 當容器啟動時，會執行 python weather_code.py
# 使用陣列格式可以避免 shell 解析問題，提高安全性
CMD ["python", "weather_code.py"]
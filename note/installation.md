<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) <br>
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) 
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Database-PostgreSQL-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Database-MongoDB-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED)

<br>

## *Airflow 安裝*

#### *I.　建立資料夾*
```bash
./dags - you can put your DAG files here.

./logs - contains logs from task execution and scheduler.

./config - you can add custom log parser or add airflow_local_settings.py to configure cluster policy.

./plugins - you can put your custom plugins here.
```

#### *II.　設定變數*
- 設定 AIRFLOW_UID 
    ```bash
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```
- 或手動建立 .env 填入
    ```bash
    AIRFLOW_UID=50000
    ```

#### *III.　初始化資料庫與建立帳號*
```bash
docker compose up airflow-init
```

#### *IV.　執行*
```bash
# 背景執行
docker compose up -d
```

![jpg](../sample/installation_00.jpg)

<br>

## *Airflow 其他常用操作*

#### *重啟服務 ( 更新檔案後的重整 )*
```bash
docker-compose restart airflow-webserver
```

#### *完全重啟服務*
```bash
docker-compose down
docker-compose up -d
```

#### *移除服務步驟*
```bash
docker-compose down -v
docker system prune --all --volumes
```
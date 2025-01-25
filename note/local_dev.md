<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) <br>
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) 
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Database-PostgreSQL-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Database-MongoDB-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED)

<br>

## *Airflow 依賴位置*

```bash
caed-airflow
  ├── .env
  ├── docker-compose.yml
  ├── confing
  ├── plugins
  ├── logs
  ├── disabled # 將不使用 dag 腳本遮蔽
  │    └── hello_world.py
  └── dags # 放置 dag 檔案
       │
       ├── logic # 放置 dag 引用的邏輯程式
       │   ├── crawler
       │   │    └── crawler_104.py
       │   └── other
       │        └── hello_world.py
       │
       ├── other_hello_world_dag.py
       └── crawler_104_dag.py
```

| 目錄 | 代表意義 | 主要功能 |
| :--: | :-- | :-- |
| config | 配置文件| 定義 Airflow 行為與設置 |
| dags | 工作流定義| 存放 DAG 腳本 (DAGs, Directed Acyclic Graphs) |
| log | 日誌文件| 存放 DAG 執行過程中的詳細日誌，便於問題排查與監控 |
| plugins |自定義功能與擴展| 用於添加自定義 Operator,Hook, Macro, Executor...etc. |

<br>

## *非 docker-compose 開發方式 (土法煉鋼 去你的...PyCharm pro)*
- #### 本地運行邏輯程式，若通過則註解 if __main__ == '__name__':
- #### 安裝本地開發必要套件
   ```commandline
   pip install -r requirements.txt
   ```

<br>

## *docker-compose 開發方式 ( Pycharm 設置 )*

1. 啟動本專案的 `caed-airflow/docker-compose.yaml` 服務 -> `docker compose up`
2. 在 Pycharm 中設置遠端執行環境
    - `File` -> `Settings` -> `Project: CAED` -> `Python Interpreter`
    - 點選右上角的齒輪 -> `Add` -> `On Docker Compose`
    - 在 Configuration file 中選擇 `caed-airflow/docker-compose.yaml`
    - `Service` 選擇 `airflow-python`，`Python Interpreter`
    - 按下 `Next` -> `OK`
    - ![jpg](https://airflow.apache.org/docs/apache-airflow/stable/_images/add_container_python_interpreter.png)
    - 回到預 Debug 的腳本, 點選右鍵開啟執行前設定黨
    - interpreter 選擇 airflow-python, 加入 exec 在 docker-compose/command
    - ![jpg](https://airflow.apache.org/docs/apache-airflow/stable/_images/docker-compose-pycharm.png)
    - 接下來對於 DAG 的開發就可以直接在 Pycharm 中進行了

<br>

## *Reference*
-  ### [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
<a href='https://github.com/dl-jack-123/CAED'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/dl-jack-123/CAED.svg'> <br> 
[![](https://img.shields.io/badge/Project-Apache_Airflow-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Docker-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/dl-jack-123/CAED) <br>
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) 
[![](https://img.shields.io/badge/Operating_System-Windows_10-blue.svg?style=plastic)](https://www.microsoft.com/zh-tw/software-download/windows10) <br>
[![](https://img.shields.io/badge/Database-PostgreSQL-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED) 
[![](https://img.shields.io/badge/Database-MongoDB-yellow.svg?style=plastic)](https://github.com/dl-jack-123/CAED)

<br>

# ⭐ CAED ⭐
## *Current progress*
| 項目 | 內容 | 負責人 | 完成時間 |
| :--: | -- | :--: |:--:|
| 爬蟲主題方向 | 人力銀行職缺相關內容 | - | 2025-01-14 |
| 架設 Airflow 服務 | - | PC / DL | 2025-01-16 |
| 爬蟲實作 | - | PC / DL | - |
| 資料表定義 | - | PC / DL | - |
| 資料庫底層撰寫 | - | DL | - |
| 資料存取設置 | - | DL | - |
| 資料表建立 | - | DL | - |
| 用 PostgreSQL 完成資料儲存 | - | - | - |
| 用 MongoDB 完成資料儲存 | - | - | - |
| Public Clouds | - | PC / DL | - |

<br>

## *Summary*
- ### *A.　Crawler + Airflow + ELK Stack + Docker*
  - #### *Crawler :* 撰寫爬蟲邏輯 ( 資料抓取 / 資料驗證 )
  - #### *Airflow :* 使用其管理工作流 ( 定時排程 / 通知 /...等 )
  - #### *ELK Stack*
    - #### 部署 ELK 監控 Airflow 的任務執行情況和爬蟲日誌
    - #### 配置 Logstash，將 Airflow 和爬蟲日誌導入 Elasticsearch
    - #### 使用 Kibana 可視化日誌，方便追蹤問題與錯誤
  - #### *Docker :* 將數個服務容器化，統一管理
- ### *B.　PostgreSQL / MongoDB*
  - #### 定義資料庫規範
  - #### 測試基本的資料寫入、查詢與驗證
- ### *C.　Deployed on 3 Major Public Clouds*
  - #### Amazon Web Services
  - #### Google Cloud Platform
  - #### Microsoft Azure

<br>

## *Showcase Results*
```commandline
# airflow:airflow
http://localhost:8080/
```
![00.jpg](sample/home_00.jpg)
![01.jpg](sample/home_01.jpg)
![02.jpg](sample/home_02.jpg)

<br>

## *Note Library*
-  ### [*⭐ Airflow Installation & Common Operations ⭐*](./note/installation.md)
-  ### [*⭐ Airflow Local Development ⭐*](./note/local_dev.md)
-  ### [*⭐ Airflow UI Operations ⭐*](./note/ui_operations.md)
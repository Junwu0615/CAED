from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# inside
from logic.crawler.crawler_104 import crawler, log

# DAG settings
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
"""
https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html
None: 不進行調度，僅用於「外部觸發」DAG
@once: 僅運行一次
@hourly: 每小時運行一次
@daily: 每天一次
@weekly: 每週週日早上午夜運行一次
@monthly: 每月第一天午夜運行一次
@yearly: 每年 1 月 1 日午夜運行一次
"""

with DAG(
        'crawler_104',
        default_args=default_args,
        schedule_interval='@daily',
        start_date=datetime(2025, 1, 1),
        catchup=False,
) as dag:
    task1 = PythonOperator(
        task_id='crawler',
        python_callable=crawler,
    )
    task2 = PythonOperator(
        task_id='log',
        python_callable=log,
    )

    task1 >> task2
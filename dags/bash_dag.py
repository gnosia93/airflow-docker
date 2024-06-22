from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'gnosia93',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
    
}


with DAG(
    dag_id='bash_dag',
    default_args=default_args,
    description='this is first dag',
    start_date=datetime(2024, 6, 22, 5),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command='echo hello world. '
    )
    
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command="echo I am second task, .. "
    )
    
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command="echo I am third task, .. "
    )
    
    
    task1 >> (task2, task3) 
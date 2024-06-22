from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'gnosia93',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
    
}

def greeting(name, age):
    print(f"python operator example of the airflow-11 .."
          f"My name is {name} "
          f"My age is {age} ")


with DAG (
    dag_id = 'python_dag',
    default_args=default_args,
    description='this example is python operator DAG',
    start_date=datetime(2024, 6, 22, 5),
    schedule_interval='@daily'

) as dag:
    
    task1 = PythonOperator(
        task_id = 'greeting',
        python_callable=greeting,
        op_kwargs={'name': 'soon', 'age': 50}
    )
    
    task1
    
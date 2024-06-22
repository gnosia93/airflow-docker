from datetime import datetime, timedelta
from airflow.decorators import dag, task


default_args = {
    'owner' : 'gnosia93',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=5)
}

@dag(
    dag_id = 'task_flow_dag',
    default_args=default_args,
    start_date=datetime(2024, 6, 22),
    schedule_interval='@daily'
)
def hello():
    
    @task()
    def get_name():
        return 'soon~~'
    
    @task()
    def get_age():
        return 30
    
    @task()
    def hello(name, age):
        print(f"Hello ETL !, My name is {name} "
              f"and I am {age} years old! ")
    
    name = get_name()
    age = get_age()
    hello(name=name, age=age)
 
hello_dag = hello()
 
 
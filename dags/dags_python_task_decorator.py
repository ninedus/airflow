from pprint import pprint

import pendulum
from airflow.decorators import task
from airflow import DAG
# from airflow.operators.python import (
#     ExternalPythonOperator,
#     PythonOperator,
#     PythonVirtualenvOperator,
#     is_venv_installed,
# )

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2024, 2, 2, tz="UTC"),
    catchup=False,
    tags=["example"],
):
    # [START howto_operator_python]
    @task(task_id="python_task_1")
    def print_context(some_input):
        """Print the Airflow context and ds variable from the context."""
        pprint(some_input)

    python_task_1 = print_context("task_decorator execution...")
    # [END howto_operator_python]



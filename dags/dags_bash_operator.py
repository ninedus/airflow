import datetime
import pendulum
from airflow.operators.bash import BashOperator
from airflow.models.dag import DAG

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 2, 3, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:

    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    # [END howto_operator_bash]

    # [START howto_operator_bash]
    bash_t2 = BashOperator(
        task_id="bash_t1",
        bash_command="echo $HOSTNAME",
    )
    # [END howto_operator_bash]

    bash_t1 >> bash_t2
    
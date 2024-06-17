from locust import User, task, between


class load(User):
    wait_time = between(1,2)

    @task
    def get_method(self):
        print("hellow")
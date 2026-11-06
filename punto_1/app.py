from locust import HttpUser, task, between


class UsuarioSimpsons(HttpUser):
    host = "https://thesimpsonsapi.com"
    wait_time = between(1, 3)

    @task(3)
    def listar_personajes(self):
        self.client.get("/api/characters")

    @task(1)
    def ver_homero(self):
        self.client.get("/api/characters/1")
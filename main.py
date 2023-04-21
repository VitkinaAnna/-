import threading


class Fork:
    def __init__(self):
        self.lock = threading.Lock()

    def pickUp(self):
        return self.lock.acquire(blocking=False)

    def putDown(self):
        self.lock.release()


class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            # Спроба взяти ліву виделку
            left_fork_pickup = self.left_fork.pickUp()
            # Спроба взяти праву виделку
            right_fork_pickup = self.right_fork.pickUp()

            # Якщо вдалося взяти обидві виделки, починаємо обід
            if left_fork_pickup and right_fork_pickup:
                print(f"{self.name} починає обід ")
                print(f"{self.name} закінчив обід ")

                # Покласти обидві виделки на стіл
                self.left_fork.putDown()
                self.right_fork.putDown()
            else:
                # Якщо не вдалося взяти обидві виделки, повернутися до початку циклу
                if left_fork_pickup:
                    self.left_fork.putDown()
                if right_fork_pickup:
                    self.right_fork.putDown()


forks = [Fork() for i in range(10)]
philosophers = [Philosopher(f"Філософ {i}", forks[i], forks[(i + 1) % 10]) for i in range(10)]

for philosopher in philosophers:
    philosopher.start()

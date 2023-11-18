import concurrent.futures
import threading
import time


class Hero:
    def __init__(self):
        self.health = 1000
        self.lock_obj = threading.Lock()

    def update(self, name, add_hp):
        print(f'start {name}.')
        # with self.lock_obj:
        new_health = self.health
        new_health += add_hp
        time.sleep(3)
        self.health = new_health
        print(f'ended {name}.')


if __name__ == '__main__':
    hero = Hero()
    print(f'Main started with {hero.health}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(hero.update, ('increase in health_1', 'increase in health_2'), (100, 200))
    print(f'Main ended with {hero.health}')


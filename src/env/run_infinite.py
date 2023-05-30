import minedojo
from datetime import datetime
import time


def run_infinite():
    start = time.time()
    print(f'run_infinite started: {datetime.now().strftime("%Y%m%d_%H%M%S_%f")} start={start}')
    env = minedojo.make(
        task_id="combat_spider_plains_leather_armors_diamond_sword_shield",
        image_size=(288, 512),
        world_seed=123,
        seed=42,
    )
    print(f"Finished to make an environment: now={time.time()-start}")

    env.reset()
    print(f"Finished to do restart: now={time.time() - start}")
    while True:
        obs, reward, done, info = env.step(env.action_space.no_op())


if __name__ == "__main__":
    run_infinite()

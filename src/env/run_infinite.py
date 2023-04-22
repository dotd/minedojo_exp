import minedojo


def run_infinite():
    env = minedojo.make(
        task_id="combat_spider_plains_leather_armors_diamond_sword_shield",
        image_size=(288, 512),
        world_seed=123,
        seed=42,
    )

    env.reset()
    while True:

        obs, reward, done, info = env.step(env.action_space.no_op())


if __name__ == "__main__":
    run_infinite()
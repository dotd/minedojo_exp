import os
import minedojo

os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/temurin-8.jdk/Contents/Home/"

#env = minedojo.make(
#    task_id="harvest_wool_with_shears_and_sheep",
#    image_size=(160, 256)
#)

env = minedojo.make(
    task_id="combat_spider_plains_leather_armors_diamond_sword_shield",
    image_size=(288, 512),
    world_seed=123,
    seed=42,
)

print("Before reset")
obs = env.reset()
for i in range(50):
    print(f"i={i}")
    act = env.action_space.no_op()
    act[0] = 1  # forward/backward
    if i % 10 == 0:
        act[2] = 1  # jump
    obs, reward, done, info = env.step(act)
env.close()

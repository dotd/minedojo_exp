import minedojo
import time
import _pickle as cPickle
from pathlib import Path
from definitions_minedojo import ROOT_DIR

t0 = time.time()
my_file = Path(f"{ROOT_DIR}/model/env.pk")
if my_file.is_file():
    print("Enter load")
    with open(my_file, 'rb') as file:
        env = cPickle.load(file)
    print(f"Finished load {(time.time() - t0) / 1000}")
else:
    print("Enter create and save")
    env = minedojo.make(
        task_id="harvest_wool_with_shears_and_sheep",
        image_size=(288, 512)
    )
    print(f"Env created {(time.time()-t0)/1000}")
    obs = env.reset()
    with open(my_file, 'wb') as file:
        cPickle.dump(env, file)
    print(f"Save {(time.time() - t0) / 1000}")

print("reset finish")

for i in range(60):
    print(i)
    act = env.action_space.no_op()
    act[0] = 1    # forward/backward
    if i % 50 == 0:
        act[2] = 1    # jump
    obs, rwd, done, info = env.step(act)
env.close()

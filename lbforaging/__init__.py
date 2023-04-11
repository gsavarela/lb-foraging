from gym.envs.registration import registry, register, make, spec
from itertools import product

sizes = range(5, 20)
players = range(2, 20)
foods = range(1, 10)
coop = [True, False]
partial_obs = [True, False]

for s, p, f, c, po in product(sizes, players, foods, coop, partial_obs):
    if s == 15 and p == 4 and f == 5 and po:
        # Register more partial observability scopes
        for i in (2, 5, 10, 12):
            register(
                id="Foraging{4}-{0}x{0}-{1}p-{2}f{3}-v1".format(s, p, f, "-coop" if c else "", f"-{i}s" if po else ""),
                entry_point="lbforaging.foraging:ForagingEnv",
                kwargs={
                    "players": p,
                    "max_player_level": 3,
                    "field_size": (s, s),
                    "max_food": f,
                    "sight": i if po else s,
                    "max_episode_steps": 50,
                    "force_coop": c,
                },
            )
    else:
        register(
            id="Foraging{4}-{0}x{0}-{1}p-{2}f{3}-v1".format(s, p, f, "-coop" if c else "", "-2s" if po else ""),
            entry_point="lbforaging.foraging:ForagingEnv",
            kwargs={
                "players": p,
                "max_player_level": 3,
                "field_size": (s, s),
                "max_food": f,
                "sight": 2 if po else s,
                "max_episode_steps": 50,
                "force_coop": c,
            },
        )

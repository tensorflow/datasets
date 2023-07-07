The Robomimic machine generated datasets were collected using a Soft Actor
Critic agent trained with a dense reward.
Each dataset consists of the agent's replay buffer.

Each task has two versions: one with low dimensional observations (`low_dim`),
and one with images (`image`).

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.

# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Open X-Embodiment datasets."""


from tensorflow_datasets.robotics import dataset_importer_builder


class Bridge(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `bridge` dataset."""

  def get_description(self):
    return 'WidowX interacting with toy kitchens'

  def get_citation(self):
    return """@inproceedings{walke2023bridgedata,
    title={BridgeData V2: A Dataset for Robot Learning at Scale},
    author={Walke, Homer and Black, Kevin and Lee, Abraham and Kim, Moo Jin and Du, Max and Zheng, Chongyi and Zhao, Tony and Hansen-Estruch, Philippe and Vuong, Quan and He, Andre and Myers, Vivek and Fang, Kuan and Finn, Chelsea and Levine, Sergey},
    booktitle={Conference on Robot Learning (CoRL)},
    year={2023}
}"""

  def get_homepage(self):
    return 'https://rail-berkeley.github.io/bridgedata/'

  def get_relative_dataset_location(self):
    return 'bridge_data_v2/0.0.1'


class TacoPlay(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `taco_play` dataset."""

  def get_description(self):
    return 'Franka arm interacting with kitchen'

  def get_citation(self):
    return """@inproceedings{rosete2022tacorl,
author = {Erick Rosete-Beas and Oier Mees and Gabriel Kalweit and Joschka Boedecker and Wolfram Burgard},
title = {Latent Plans for Task Agnostic Offline Reinforcement Learning},
journal = {Proceedings of the 6th Conference on Robot Learning (CoRL)},
year = {2022}
}
@inproceedings{mees23hulc2,
title={Grounding  Language  with  Visual  Affordances  over  Unstructured  Data},
author={Oier Mees and Jessica Borja-Diaz and Wolfram Burgard},
booktitle = {Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
year={2023},
address = {London, UK}
}"""

  def get_homepage(self):
    return 'https://www.kaggle.com/datasets/oiermees/taco-robot'

  def get_relative_dataset_location(self):
    return 'taco_play/0.1.0'


class JacoPlay(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `jaco_play` dataset."""

  def get_description(self):
    return 'Jaco 2 pick place on table top'

  def get_citation(self):
    return """@software{dass2023jacoplay,
  author = {Dass, Shivin and Yapeter, Jullian and Zhang, Jesse and Zhang, Jiahui
            and Pertsch, Karl and Nikolaidis, Stefanos and Lim, Joseph J.},
  title = {CLVR Jaco Play Dataset},
  url = {https://github.com/clvrai/clvr_jaco_play_dataset},
  version = {1.0.0},
  year = {2023}
}"""

  def get_homepage(self):
    return 'https://github.com/clvrai/clvr_jaco_play_dataset'

  def get_relative_dataset_location(self):
    return 'jaco_play/0.1.0'


class BerkeleyCableRouting(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `berkeley_cable_routing` dataset."""

  def get_description(self):
    return 'Routing cable into clamps on table top'

  def get_citation(self):
    return """@article{luo2023multistage,
  author    = {Jianlan Luo and Charles Xu and Xinyang Geng and Gilbert Feng and Kuan Fang and Liam Tan and Stefan Schaal and Sergey Levine},
  title     = {Multi-Stage Cable Routing through Hierarchical Imitation Learning},
  journal   = {arXiv pre-print},
  year      = {2023},
  url       = {https://arxiv.org/abs/2307.08927},
}"""

  def get_homepage(self):
    return 'https://sites.google.com/view/cablerouting/home'

  def get_relative_dataset_location(self):
    return 'berkeley_cable_routing/0.1.0'


class Roboturk(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `roboturk` dataset."""

  def get_description(self):
    return 'Cloth folding, bowl stacking'

  def get_citation(self):
    return """@inproceedings{mandlekar2019scaling,
          title={Scaling robot supervision to hundreds of hours with roboturk: Robotic manipulation dataset through human reasoning and dexterity},
          author={Mandlekar, Ajay and Booher, Jonathan and Spero, Max and Tung, Albert and Gupta, Anchit and Zhu, Yuke and Garg, Animesh and Savarese, Silvio and Fei-Fei, Li},
          booktitle={2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
          pages={1048--1055},
          year={2019},
          organization={IEEE}
        }"""

  def get_homepage(self):
    return 'https://roboturk.stanford.edu/dataset_real.html'

  def get_relative_dataset_location(self):
    return 'roboturk/0.1.0'


class NyuDoorOpeningSurprisingEffectiveness(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `nyu_door_opening_surprising_effectiveness` dataset."""

  def get_description(self):
    return 'Hello robot opening cabinets, microwaves etc'

  def get_citation(self):
    return """@misc{pari2021surprising,
    title={The Surprising Effectiveness of Representation Learning for Visual Imitation}, 
    author={Jyothish Pari and Nur Muhammad Shafiullah and Sridhar Pandian Arunachalam and Lerrel Pinto},
    year={2021},
    eprint={2112.01511},
    archivePrefix={arXiv},
    primaryClass={cs.RO}
}"""

  def get_homepage(self):
    return 'https://jyopari.github.io/VINN/'

  def get_relative_dataset_location(self):
    return 'nyu_door_opening_surprising_effectiveness/0.1.0'


class Viola(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `viola` dataset."""

  def get_description(self):
    return 'Franka robot interacting with stylized kitchen tasks'

  def get_citation(self):
    return """@article{zhu2022viola,
  title={VIOLA: Imitation Learning for Vision-Based Manipulation with Object Proposal Priors},
  author={Zhu, Yifeng and Joshi, Abhishek and Stone, Peter and Zhu, Yuke},
  journal={6th Annual Conference on Robot Learning (CoRL)},
  year={2022}
}"""

  def get_homepage(self):
    return 'https://ut-austin-rpl.github.io/VIOLA/'

  def get_relative_dataset_location(self):
    return 'viola/0.1.0'


class BerkeleyAutolabUr5(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `berkeley_autolab_ur5` dataset."""

  def get_description(self):
    return 'UR5 performing cloth manipulation, pick place etc tasks'

  def get_citation(self):
    return """@misc{BerkeleyUR5Website,
  title = {Berkeley {UR5} Demonstration Dataset},
  author = {Lawrence Yunliang Chen and Simeon Adebola and Ken Goldberg},
  howpublished = {https://sites.google.com/view/berkeley-ur5/home},
}"""

  def get_homepage(self):
    return 'https://sites.google.com/view/berkeley-ur5/home'

  def get_relative_dataset_location(self):
    return 'berkeley_autolab_ur5/0.1.0'


class Toto(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `toto` dataset."""

  def get_description(self):
    return 'Franka scooping and pouring tasks'

  def get_citation(self):
    return """@inproceedings{zhou2023train,
  author={Zhou, Gaoyue and Dean, Victoria and Srirama, Mohan Kumar and Rajeswaran, Aravind and Pari, Jyothish and Hatch, Kyle and Jain, Aryan and Yu, Tianhe and Abbeel, Pieter and Pinto, Lerrel and Finn, Chelsea and Gupta, Abhinav},
  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)}, 
  title={Train Offline, Test Online: A Real Robot Learning Benchmark}, 
  year={2023},
 }"""

  def get_homepage(self):
    return 'https://toto-benchmark.org/'

  def get_relative_dataset_location(self):
    return 'toto/0.1.0'


class UtokyoXarmBimanualConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `utokyo_xarm_bimanual_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'xArm bimanual setup folding towel'

  def get_citation(self):
    return """@misc{matsushima2023weblab,
  title={Weblab xArm Dataset},
  author={Tatsuya Matsushima and Hiroki Furuta and Yusuke Iwasawa and Yutaka Matsuo},
  year={2023},
}"""

  def get_homepage(self):
    return '--'

  def get_relative_dataset_location(self):
    return 'utokyo_xarm_bimanual_converted_externally_to_rlds/0.1.0'


class BerkeleyMvpConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `berkeley_mvp_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'xArm performing 6 manipulation tasks'

  def get_citation(self):
    return """@InProceedings{Radosavovic2022,
  title = {Real-World Robot Learning with Masked Visual Pre-training},
  author = {Ilija Radosavovic and Tete Xiao and Stephen James and Pieter Abbeel and Jitendra Malik and Trevor Darrell},
  booktitle = {CoRL},
  year = {2022}
}"""

  def get_homepage(self):
    return 'https://arxiv.org/abs/2203.06173'

  def get_relative_dataset_location(self):
    return 'berkeley_mvp_converted_externally_to_rlds/0.1.0'


class DlrSaraGridClampConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `dlr_sara_grid_clamp_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'place grid clamp onto grids on table'

  def get_citation(self):
    return r"""@article{padalkar2023guided,
  title={A guided reinforcement learning approach using shared control templates for learning manipulation skills in the real world},
  author={Padalkar, Abhishek and Quere, Gabriel and Raffin, Antonin and Silv{\'e}rio, Jo{\~a}o and Stulp, Freek},
  journal={Research square preprint rs-3289569/v1},
  year={2023}
}"""

  def get_homepage(self):
    return 'https://www.researchsquare.com/article/rs-3289569/v1'

  def get_relative_dataset_location(self):
    return 'dlr_sara_grid_clamp_converted_externally_to_rlds/0.1.0'


class NyuRotDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `nyu_rot_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'xArm short-horizon table-top tasks'

  def get_citation(self):
    return """@inproceedings{haldar2023watch,
  title={Watch and match: Supercharging imitation with regularized optimal transport},
  author={Haldar, Siddhant and Mathur, Vaibhav and Yarats, Denis and Pinto, Lerrel},
  booktitle={Conference on Robot Learning},
  pages={32--43},
  year={2023},
  organization={PMLR}
}"""

  def get_homepage(self):
    return 'https://rot-robot.github.io/'

  def get_relative_dataset_location(self):
    return 'nyu_rot_dataset_converted_externally_to_rlds/0.1.0'


class BerkeleyGnmSacSon(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `berkeley_gnm_sac_son` dataset."""

  def get_description(self):
    return 'office navigation'

  def get_citation(self):
    return """@article{hirose2023sacson,
  title={SACSoN: Scalable Autonomous Data Collection for Social Navigation},
  author={Hirose, Noriaki and Shah, Dhruv and Sridhar, Ajay and Levine, Sergey},
  journal={arXiv preprint arXiv:2306.01874},
  year={2023}
}"""

  def get_homepage(self):
    return 'https://sites.google.com/view/SACSoN-review'

  def get_relative_dataset_location(self):
    return 'berkeley_gnm_sac_son/0.1.0'


class ManiskillDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `maniskill_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Simulated Franka performing various manipulation tasks'

  def get_citation(self):
    return """@inproceedings{gu2023maniskill2,
  title={ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills},
  author={Gu, Jiayuan and Xiang, Fanbo and Li, Xuanlin and Ling, Zhan and Liu, Xiqiang and Mu, Tongzhou and Tang, Yihe and Tao, Stone and Wei, Xinyue and Yao, Yunchao and Yuan, Xiaodi and Xie, Pengwei and Huang, Zhiao and Chen, Rui and Su, Hao},
  booktitle={International Conference on Learning Representations},
  year={2023}
}"""

  def get_homepage(self):
    return 'https://github.com/haosulab/ManiSkill2'

  def get_relative_dataset_location(self):
    return 'maniskill_dataset_converted_externally_to_rlds/0.1.0'


class UtaustinMutex(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `utaustin_mutex` dataset."""

  def get_description(self):
    return 'Diverse household manipulation tasks'

  def get_citation(self):
    return r"""@inproceedings{
    shah2023mutex,
    title={{MUTEX}: Learning Unified Policies from Multimodal Task Specifications},
    author={Rutav Shah and Roberto Mart{\'\i}n-Mart{\'\i}n and Yuke Zhu},
    booktitle={7th Annual Conference on Robot Learning},
    year={2023},
    url={https://openreview.net/forum?id=PwqiqaaEzJ}
}"""

  def get_homepage(self):
    return 'https://ut-austin-rpl.github.io/MUTEX/'

  def get_relative_dataset_location(self):
    return 'utaustin_mutex/0.1.0'


class BcZ(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `bc_z` dataset."""

  def get_description(self):
    return 'Teleoped Google robot doing mostly pick-place from a table'

  def get_citation(self):
    return """@inproceedings{jang2021bc,
title={{BC}-Z: Zero-Shot Task Generalization with Robotic Imitation Learning},
author={Eric Jang and Alex Irpan and Mohi Khansari and Daniel Kappler and Frederik Ebert and Corey Lynch and Sergey Levine and Chelsea Finn},
booktitle={5th Annual Conference on Robot Learning},
year={2021},
url={https://openreview.net/forum?id=8kbp23tSGYv}}"""

  def get_homepage(self):
    return 'https://www.kaggle.com/datasets/google/bc-z-robot/discussion/309201'

  def get_relative_dataset_location(self):
    return 'bc_z/0.1.0'


class AustinBudsDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `austin_buds_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka stylized kitchen tasks'

  def get_citation(self):
    return """@article{zhu2022bottom,
  title={Bottom-Up Skill Discovery From Unsegmented Demonstrations for Long-Horizon Robot Manipulation},
  author={Zhu, Yifeng and Stone, Peter and Zhu, Yuke},
  journal={IEEE Robotics and Automation Letters},
  volume={7},
  number={2},
  pages={4126--4133},
  year={2022},
  publisher={IEEE}
}"""

  def get_homepage(self):
    return 'https://ut-austin-rpl.github.io/rpl-BUDS/'

  def get_relative_dataset_location(self):
    return 'austin_buds_dataset_converted_externally_to_rlds/0.1.0'


class UiucD3field(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `uiuc_d3field` dataset."""

  def get_description(self):
    return 'Organizing office desk, utensils etc'

  def get_citation(self):
    return """@article{wang2023d3field,
  title={D^3Field: Dynamic 3D Descriptor Fields for Generalizable Robotic Manipulation}, 
  author={Wang, Yixuan and Li, Zhuoran and Zhang, Mingtong and Driggs-Campbell, Katherine and Wu, Jiajun and Fei-Fei, Li and Li, Yunzhu},
  journal={arXiv preprint arXiv:},
  year={2023},
}"""

  def get_homepage(self):
    return 'https://robopil.github.io/d3fields/'

  def get_relative_dataset_location(self):
    return 'uiuc_d3field/0.1.0'


class UscClothSimConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `usc_cloth_sim_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka cloth interaction tasks'

  def get_citation(self):
    return """@article{salhotra2022dmfd,
    author={Salhotra, Gautam and Liu, I-Chun Arthur and Dominguez-Kuhne, Marcus and Sukhatme, Gaurav S.},
    journal={IEEE Robotics and Automation Letters},
    title={Learning Deformable Object Manipulation From Expert Demonstrations},
    year={2022},
    volume={7},
    number={4},
    pages={8775-8782},
    doi={10.1109/LRA.2022.3187843}
}"""

  def get_homepage(self):
    return 'https://uscresl.github.io/dmfd/'

  def get_relative_dataset_location(self):
    return 'usc_cloth_sim_converted_externally_to_rlds/0.1.0'


class AsuTableTopConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `asu_table_top_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'UR5 performing table-top pick/place/rotate tasks'

  def get_citation(self):
    return """@inproceedings{zhou2023modularity,
  title={Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies for Robot Manipulation},
  author={Zhou, Yifan and Sonawani, Shubham and Phielipp, Mariano and Stepputtis, Simon and Amor, Heni},
  booktitle={Conference on Robot Learning},
  pages={1684--1695},
  year={2023},
  organization={PMLR}
}
@article{zhou2023learning,
  title={Learning modular language-conditioned robot policies through attention},
  author={Zhou, Yifan and Sonawani, Shubham and Phielipp, Mariano and Ben Amor, Heni and Stepputtis, Simon},
  journal={Autonomous Robots},
  pages={1--21},
  year={2023},
  publisher={Springer}
}"""

  def get_homepage(self):
    return 'https://link.springer.com/article/10.1007/s10514-023-10129-1'

  def get_relative_dataset_location(self):
    return 'asu_table_top_converted_externally_to_rlds/0.1.0'


class CmuPlayFusion(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `cmu_play_fusion` dataset."""

  def get_description(self):
    return (
        'The robot plays with 3 complex scenes: a grill with many cooking'
        ' objects like toaster, pan, etc. It has to pick, open, place, close.'
        ' It  has to set a table, move plates, cups, utensils. And it has to'
        ' place dishes in the sink, dishwasher, hand cups etc. '
    )

  def get_citation(self):
    return """@inproceedings{chen2023playfusion,
  title={PlayFusion: Skill Acquisition via Diffusion from Language-Annotated Play},
  author={Chen, Lili and Bahl, Shikhar and Pathak, Deepak},
  booktitle={CoRL},
  year={2023}
}"""

  def get_homepage(self):
    return 'https://play-fusion.github.io/'

  def get_relative_dataset_location(self):
    return 'cmu_play_fusion/0.1.0'


class KaistNonprehensileConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `kaist_nonprehensile_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka manipulating ungraspable objects'

  def get_citation(self):
    return """@article{kimpre,
  title={Pre-and post-contact policy decomposition for non-prehensile manipulation with zero-shot sim-to-real transfer},
  author={Kim, Minchan and Han, Junhyek and Kim, Jaehyung and Kim, Beomjoon},
  booktitle={2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year={2023},
  organization={IEEE}
}"""

  def get_homepage(self):
    return '--'

  def get_relative_dataset_location(self):
    return 'kaist_nonprehensile_converted_externally_to_rlds/0.1.0'


class DlrSaraPourConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `dlr_sara_pour_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'pouring liquid from a bottle into a mug'

  def get_citation(self):
    return r"""@inproceedings{padalkar2023guiding,
  title={Guiding Reinforcement Learning with Shared Control Templates},
  author={Padalkar, Abhishek and Quere, Gabriel and Steinmetz, Franz and Raffin, Antonin and Nieuwenhuisen, Matthias and Silv{\'e}rio, Jo{\~a}o and Stulp, Freek},
  booktitle={40th IEEE International Conference on Robotics and Automation, ICRA 2023},
  year={2023},
  organization={IEEE}
}"""

  def get_homepage(self):
    return 'https://elib.dlr.de/193739/1/padalkar2023rlsct.pdf'

  def get_relative_dataset_location(self):
    return 'dlr_sara_pour_converted_externally_to_rlds/0.1.0'


class CmuStretch(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `cmu_stretch` dataset."""

  def get_description(self):
    return 'Hello stretch robot kitchen interactions'

  def get_citation(self):
    return """@inproceedings{bahl2023affordances,
  title={Affordances from Human Videos as a Versatile Representation for Robotics},
  author={Bahl, Shikhar and Mendonca, Russell and Chen, Lili and Jain, Unnat and Pathak, Deepak},
  booktitle={CVPR},
  year={2023}
}
@article{mendonca2023structured,
  title={Structured World Models from Human Videos},
  author={Mendonca, Russell and Bahl, Shikhar and Pathak, Deepak},
  journal={CoRL},
  year={2023}
}"""

  def get_homepage(self):
    return 'https://robo-affordances.github.io/'

  def get_relative_dataset_location(self):
    return 'cmu_stretch/0.1.0'


class UtokyoSaytapConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `utokyo_saytap_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'A1 walking, no RGB'

  def get_citation(self):
    return """@article{saytap2023,
  author = {Yujin Tang and Wenhao Yu and Jie Tan and Heiga Zen and Aleksandra Faust and
Tatsuya Harada},
  title  = {SayTap: Language to Quadrupedal Locomotion},
  eprint = {arXiv:2306.07580},
  url    = {https://saytap.github.io},
  note   = "{https://saytap.github.io}",
  year   = {2023}
}"""

  def get_homepage(self):
    return 'https://saytap.github.io/'

  def get_relative_dataset_location(self):
    return 'utokyo_saytap_converted_externally_to_rlds/0.1.0'


class UtokyoPr2TabletopManipulationConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'PR2 tabletop manipulation (folding cloth, picking)'

  def get_citation(self):
    return """@misc{oh2023pr2utokyodatasets,
  author={Jihoon Oh and Naoaki Kanazawa and Kento Kawaharazuka},
  title={X-Embodiment U-Tokyo PR2 Datasets},
  year={2023},
  url={https://github.com/ojh6404/rlds_dataset_builder},
}"""

  def get_homepage(self):
    return '--'

  def get_relative_dataset_location(self):
    return 'utokyo_pr2_tabletop_manipulation_converted_externally_to_rlds/0.1.0'


class BerkeleyRptConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `berkeley_rpt_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka performing tabletop pick place tasks'

  def get_citation(self):
    return """@article{Radosavovic2023,
  title={Robot Learning with Sensorimotor Pre-training},
  author={Ilija Radosavovic and Baifeng Shi and Letian Fu and Ken Goldberg and Trevor Darrell and Jitendra Malik},
  year={2023},
  journal={arXiv:2306.10007}
}
"""

  def get_homepage(self):
    return 'https://arxiv.org/abs/2306.10007'

  def get_relative_dataset_location(self):
    return 'berkeley_rpt_converted_externally_to_rlds/0.1.0'


class TokyoULsmoConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `tokyo_u_lsmo_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'motion planning trajectory of pick place tasks'

  def get_citation(self):
    return """@Article{Osa22,
  author  = {Takayuki Osa},
  journal = {The International Journal of Robotics Research},
  title   = {Motion Planning by Learning the Solution Manifold in Trajectory Optimization},
  year    = {2022},
  number  = {3},
  pages   = {291--311},
  volume  = {41},
}"""

  def get_homepage(self):
    return 'https://journals.sagepub.com/doi/full/10.1177/02783649211044405'

  def get_relative_dataset_location(self):
    return 'tokyo_u_lsmo_converted_externally_to_rlds/0.1.0'


class StanfordKukaMultimodalDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `stanford_kuka_multimodal_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Kuka iiwa peg insertion with force feedback'

  def get_citation(self):
    return """@inproceedings{lee2019icra,
  title={Making sense of vision and touch: Self-supervised learning of multimodal representations for contact-rich tasks},
  author={Lee, Michelle A and Zhu, Yuke and Srinivasan, Krishnan and Shah, Parth and Savarese, Silvio and Fei-Fei, Li and  Garg, Animesh and Bohg, Jeannette},
  booktitle={2019 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2019},
  url={https://arxiv.org/abs/1810.10191}
}"""

  def get_homepage(self):
    return 'https://sites.google.com/view/visionandtouch'

  def get_relative_dataset_location(self):
    return 'stanford_kuka_multimodal_dataset_converted_externally_to_rlds/0.1.0'


class BerkeleyFanucManipulation(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `berkeley_fanuc_manipulation` dataset."""

  def get_description(self):
    return 'Fanuc robot performing various manipulation tasks'

  def get_citation(self):
    return """@article{fanuc_manipulation2023,
  title={Fanuc Manipulation: A Dataset for Learning-based Manipulation with FANUC Mate 200iD Robot},
  author={Zhu, Xinghao and Tian, Ran and Xu, Chenfeng and Ding, Mingyu and Zhan, Wei and Tomizuka, Masayoshi},
  year={2023},
}"""

  def get_homepage(self):
    return 'https://sites.google.com/berkeley.edu/fanuc-manipulation'

  def get_relative_dataset_location(self):
    return 'berkeley_fanuc_manipulation/0.1.0'


class BerkeleyGnmCoryHall(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `berkeley_gnm_cory_hall` dataset."""

  def get_description(self):
    return 'hallway navigation'

  def get_citation(self):
    return """@inproceedings{kahn2018self,
  title={Self-supervised deep reinforcement learning with generalized computation graphs for robot navigation},
  author={Kahn, Gregory and Villaflor, Adam and Ding, Bosen and Abbeel, Pieter and Levine, Sergey},
  booktitle={2018 IEEE international conference on robotics and automation (ICRA)},
  pages={5129--5136},
  year={2018},
  organization={IEEE}
}"""

  def get_homepage(self):
    return 'https://arxiv.org/abs/1709.10489'

  def get_relative_dataset_location(self):
    return 'berkeley_gnm_cory_hall/0.1.0'


class Kuka(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `kuka` dataset."""

  def get_description(self):
    return 'Bin picking and rearrangement tasks'

  def get_citation(self):
    return """@article{kalashnikov2018qt,
  title={Qt-opt: Scalable deep reinforcement learning for vision-based robotic manipulation},
  author={Kalashnikov, Dmitry and Irpan, Alex and Pastor, Peter and Ibarz, Julian and Herzog, Alexander and Jang, Eric and Quillen, Deirdre and Holly, Ethan and Kalakrishnan, Mrinal and Vanhoucke, Vincent and others},
  journal={arXiv preprint arXiv:1806.10293},
  year={2018}
}"""

  def get_homepage(self):
    return 'https://arxiv.org/abs/1806.10293'

  def get_relative_dataset_location(self):
    return 'kuka/0.1.0'


class UtokyoXarmPickAndPlaceConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `utokyo_xarm_pick_and_place_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'xArm picking and placing objects'

  def get_citation(self):
    return """@misc{matsushima2023weblab,
  title={Weblab xArm Dataset},
  author={Tatsuya Matsushima and Hiroki Furuta and Yusuke Iwasawa and Yutaka Matsuo},
  year={2023},
}"""

  def get_homepage(self):
    return '--'

  def get_relative_dataset_location(self):
    return 'utokyo_xarm_pick_and_place_converted_externally_to_rlds/0.1.0'


class ColumbiaCairlabPushtReal(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `columbia_cairlab_pusht_real` dataset."""

  def get_description(self):
    return 'UR5 planar pushing tasks'

  def get_citation(self):
    return """@inproceedings{chi2023diffusionpolicy,
	title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
	author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
	booktitle={Proceedings of Robotics: Science and Systems (RSS)},
	year={2023}
}"""

  def get_homepage(self):
    return 'https://github.com/columbia-ai-robotics/diffusion_policy'

  def get_relative_dataset_location(self):
    return 'columbia_cairlab_pusht_real/0.1.0'


class CmuFrankaExplorationDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `cmu_franka_exploration_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka exploring toy kitchens'

  def get_citation(self):
    return """@inproceedings{mendonca2023structured,
              title={Structured World Models from Human Videos},
              author={Mendonca, Russell  and Bahl, Shikhar and Pathak, Deepak},
              journal={RSS},
              year={2023}
            }"""

  def get_homepage(self):
    return 'https://human-world-model.github.io/'

  def get_relative_dataset_location(self):
    return 'cmu_franka_exploration_dataset_converted_externally_to_rlds/0.1.0'


class BerkeleyGnmRecon(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `berkeley_gnm_recon` dataset."""

  def get_description(self):
    return 'off-road navigation'

  def get_citation(self):
    return """@inproceedings{
shah2021rapid,
title={{Rapid Exploration for Open-World Navigation with Latent Goal Models}},
author={Dhruv Shah and Benjamin Eysenbach and Nicholas Rhinehart and Sergey Levine},
booktitle={5th Annual Conference on Robot Learning },
year={2021},
url={https://openreview.net/forum?id=d_SWJhyKfVw}
}"""

  def get_homepage(self):
    return 'https://sites.google.com/view/recon-robot'

  def get_relative_dataset_location(self):
    return 'berkeley_gnm_recon/0.1.0'


class UtokyoPr2OpeningFridgeConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `utokyo_pr2_opening_fridge_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'PR2 opening fridge doors'

  def get_citation(self):
    return """@misc{oh2023pr2utokyodatasets,
  author={Jihoon Oh and Naoaki Kanazawa and Kento Kawaharazuka},
  title={X-Embodiment U-Tokyo PR2 Datasets},
  year={2023},
  url={https://github.com/ojh6404/rlds_dataset_builder},
}"""

  def get_homepage(self):
    return '--'

  def get_relative_dataset_location(self):
    return 'utokyo_pr2_opening_fridge_converted_externally_to_rlds/0.1.0'


class EthAgentAffordances(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `eth_agent_affordances` dataset."""

  def get_description(self):
    return 'Franka opening ovens -- point cloud + proprio only'

  def get_citation(self):
    return """@inproceedings{schiavi2023learning,
  title={Learning agent-aware affordances for closed-loop interaction with articulated objects},
  author={Schiavi, Giulio and Wulkop, Paula and Rizzi, Giuseppe and Ott, Lionel and Siegwart, Roland and Chung, Jen Jen},
  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)},
  pages={5916--5922},
  year={2023},
  organization={IEEE}
}"""

  def get_homepage(self):
    return 'https://ieeexplore.ieee.org/iel7/10160211/10160212/10160747.pdf'

  def get_relative_dataset_location(self):
    return 'eth_agent_affordances/0.1.0'


class AustinSiriusDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `austin_sirius_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka tabletop manipulation tasks'

  def get_citation(self):
    return """@inproceedings{liu2022robot,
    title = {Robot Learning on the Job: Human-in-the-Loop Autonomy and Learning During Deployment},
    author = {Huihan Liu and Soroush Nasiriany and Lance Zhang and Zhiyao Bao and Yuke Zhu},
    booktitle = {Robotics: Science and Systems (RSS)},
    year = {2023}
}"""

  def get_homepage(self):
    return 'https://ut-austin-rpl.github.io/sirius/'

  def get_relative_dataset_location(self):
    return 'austin_sirius_dataset_converted_externally_to_rlds/0.1.0'


class StanfordRobocookConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `stanford_robocook_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka preparing dumplings with various tools'

  def get_citation(self):
    return """@article{shi2023robocook,
  title={RoboCook: Long-Horizon Elasto-Plastic Object Manipulation with Diverse Tools},
  author={Shi, Haochen and Xu, Huazhe and Clarke, Samuel and Li, Yunzhu and Wu, Jiajun},
  journal={arXiv preprint arXiv:2306.14447},
  year={2023}
}"""

  def get_homepage(self):
    return 'https://hshi74.github.io/robocook/'

  def get_relative_dataset_location(self):
    return 'stanford_robocook_converted_externally_to_rlds/0.1.0'


class NyuFrankaPlayDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `nyu_franka_play_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka interacting with toy kitchens'

  def get_citation(self):
    return """@article{cui2022play,
  title   = {From Play to Policy: Conditional Behavior Generation from Uncurated Robot Data},
  author  = {Cui, Zichen Jeff and Wang, Yibin and Shafiullah, Nur Muhammad Mahi and Pinto, Lerrel},
  journal = {arXiv preprint arXiv:2210.10047},
  year    = {2022}
}"""

  def get_homepage(self):
    return 'https://play-to-policy.github.io/'

  def get_relative_dataset_location(self):
    return 'nyu_franka_play_dataset_converted_externally_to_rlds/0.1.0'


class StanfordMaskVitConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `stanford_mask_vit_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Sawyer pushing and picking objects in a bin'

  def get_citation(self):
    return """@inproceedings{gupta2022maskvit,
  title={MaskViT: Masked Visual Pre-Training for Video Prediction},
  author={Agrim Gupta and Stephen Tian and Yunzhi Zhang and Jiajun Wu and Roberto Martín-Martín and Li Fei-Fei},
  booktitle={International Conference on Learning Representations},
  year={2022}
}"""

  def get_homepage(self):
    return 'https://arxiv.org/abs/2206.11894'

  def get_relative_dataset_location(self):
    return 'stanford_mask_vit_converted_externally_to_rlds/0.1.0'


class DlrEdanSharedControlConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `dlr_edan_shared_control_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'wheelchair with arm performing shelf pick tasks'

  def get_citation(self):
    return """@inproceedings{vogel_edan_2020,
	title = {EDAN - an EMG-Controlled Daily Assistant to Help People with Physical Disabilities},
	language = {en},
	booktitle = {2020 {IEEE}/{RSJ} {International} {Conference} on {Intelligent} {Robots} and {Systems} ({IROS})},
	author = {Vogel, Jörn and Hagengruber, Annette and Iskandar, Maged and Quere, Gabriel and Leipscher, Ulrike and Bustamante, Samuel and Dietrich, Alexander and Hoeppner, Hannes and Leidner, Daniel and Albu-Schäffer, Alin},
	year = {2020}
}
@inproceedings{quere_shared_2020,
	address = {Paris, France},
	title = {Shared {Control} {Templates} for {Assistive} {Robotics}},
	language = {en},
	booktitle = {2020 {IEEE} {International} {Conference} on {Robotics} and {Automation} ({ICRA})},
	author = {Quere, Gabriel and Hagengruber, Annette and Iskandar, Maged and Bustamante, Samuel and Leidner, Daniel and Stulp, Freek and Vogel, Joern},
	year = {2020},
	pages = {7},
}"""

  def get_homepage(self):
    return 'https://ieeexplore.ieee.org/document/9341156'

  def get_relative_dataset_location(self):
    return 'dlr_edan_shared_control_converted_externally_to_rlds/0.1.0'


class UcsdKitchenDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `ucsd_kitchen_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'xArm interacting with different toy kitchens'

  def get_citation(self):
    return """@ARTICLE{ucsd_kitchens,
  author = {Ge Yan, Kris Wu, and Xiaolong Wang},
  title = {{ucsd kitchens Dataset}},
  year = {2023},
  month = {August}
}
"""

  def get_homepage(self):
    return ' '

  def get_relative_dataset_location(self):
    return 'ucsd_kitchen_dataset_converted_externally_to_rlds/0.1.0'


class IamlabCmuPickupInsertConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `iamlab_cmu_pickup_insert_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka picking objects and insertion tasks'

  def get_citation(self):
    return """@inproceedings{
saxena2023multiresolution,
title={Multi-Resolution Sensing for Real-Time Control with Vision-Language Models},
author={Saumya Saxena and Mohit Sharma and Oliver Kroemer},
booktitle={7th Annual Conference on Robot Learning},
year={2023},
url={https://openreview.net/forum?id=WuBv9-IGDUA}
}"""

  def get_homepage(self):
    return 'https://openreview.net/forum?id=WuBv9-IGDUA'

  def get_relative_dataset_location(self):
    return 'iamlab_cmu_pickup_insert_converted_externally_to_rlds/0.1.0'


class AustinSailorDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `austin_sailor_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka tablesetting tasks'

  def get_citation(self):
    return """@inproceedings{nasiriany2022sailor,
      title={Learning and Retrieval from Prior Data for Skill-based Imitation Learning},
      author={Soroush Nasiriany and Tian Gao and Ajay Mandlekar and Yuke Zhu},
      booktitle={Conference on Robot Learning (CoRL)},
      year={2022}
    }"""

  def get_homepage(self):
    return 'https://ut-austin-rpl.github.io/sailor/'

  def get_relative_dataset_location(self):
    return 'austin_sailor_dataset_converted_externally_to_rlds/0.1.0'


class UcsdPickAndPlaceDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `ucsd_pick_and_place_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'xArm picking and placing objects with distractors'

  def get_citation(self):
    return """@preprint{Feng2023Finetuning,
	title={Finetuning Offline World Models in the Real World},
	author={Yunhai Feng, Nicklas Hansen, Ziyan Xiong, Chandramouli Rajagopalan, Xiaolong Wang},
	year={2023}
}"""

  def get_homepage(self):
    return 'https://owmcorl.github.io'

  def get_relative_dataset_location(self):
    return 'ucsd_pick_and_place_dataset_converted_externally_to_rlds/0.1.0'


class StanfordHydraDatasetConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `stanford_hydra_dataset_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return 'Franka solving long-horizon tasks'

  def get_citation(self):
    return """@article{belkhale2023hydra,
 title={HYDRA: Hybrid Robot Actions for Imitation Learning},
 author={Belkhale, Suneel and Cui, Yuchen and Sadigh, Dorsa},
 journal={arxiv},
 year={2023}
}"""

  def get_homepage(self):
    return 'https://sites.google.com/view/hydra-il-2023'

  def get_relative_dataset_location(self):
    return 'stanford_hydra_dataset_converted_externally_to_rlds/0.1.0'


class ImperialcollegeSawyerWristCam(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `imperialcollege_sawyer_wrist_cam` dataset."""

  def get_description(self):
    return 'Sawyer performing table top manipulation'

  def get_citation(self):
    return """--"""

  def get_homepage(self):
    return '--'

  def get_relative_dataset_location(self):
    return 'imperialcollege_sawyer_wrist_cam/0.1.0'


class Fractal20220817Data(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `fractal_20220817_data` dataset."""

  def get_description(self):
    return 'Table-top manipulation with 17 objects'

  def get_citation(self):
    return r"""@article{brohan2022rt,
  title={Rt-1: Robotics transformer for real-world control at scale},
  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Dabis, Joseph and Finn, Chelsea and Gopalakrishnan, Keerthana and Hausman, Karol and Herzog, Alex and Hsu, Jasmine and others},
  journal={arXiv preprint arXiv:2212.06817},
  year={2022}
}"""

  def get_homepage(self):
    return 'https://ai.googleblog.com/2022/12/rt-1-robotics-transformer-for-real.html'

  def get_relative_dataset_location(self):
    return 'fractal20220817_data/0.1.0'


class ConqHoseManipulation(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `conq_hose_manipulation` dataset."""

  def get_description(self):
    return r"""Mobile manipulation dataset"""

  def get_citation(self):
    return r"""@misc{ConqHoseManipData,
author={Peter Mitrano and Dmitry Berenson},
title={Conq Hose Manipulation Dataset, v1.15.0},
year={2024},
howpublished={https://sites.google.com/view/conq-hose-manipulation-dataset}
}"""

  def get_homepage(self):
    return (
        'https://sites.google.com/corp/view/conq-hose-manipulation-dataset/home'
    )

  def get_relative_dataset_location(self):
    return 'conq_hose_manipulation/0.0.1'


class Dobbe(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `dobbe` dataset."""

  def get_description(self):
    return r""" """

  def get_citation(self):
    return r"""@misc{shafiullah2023dobbe, title={On Bringing Robots Home}, author={Nur Muhammad Mahi Shafiullah and Anant Rai and Haritheja Etukuru and Yiqian Liu and Ishan Misra and Soumith Chintala and Lerrel Pinto}, year={2023}, eprint={2311.16098}, archivePrefix={arXiv}, primaryClass={cs.RO} }"""

  def get_homepage(self):
    return 'https://github.com/notmahi/dobb-e'

  def get_relative_dataset_location(self):
    return 'dobbe/0.0.1'


class Fmb(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `fmb` dataset."""

  def get_description(self):
    return r"""Our dataset consists of objects in diverse appearance and geometry. It requires multi-stage and multi-modal fine motor skills to successfully assemble the pegs onto a unfixed board in a randomized scene. We collected a total of 22,550 trajectories across two different tasks on a Franka Panda arm. We record the trajectories from 2 global views and 2 wrist views. Each view contains both RGB and depth map."""

  def get_citation(self):
    return 'https://doi.org/10.48550/arXiv.2401.08553'

  def get_homepage(self):
    return 'https://functional-manipulation-benchmark.github.io/'

  def get_relative_dataset_location(self):
    return 'fmb/0.0.1'


class IoAiTech(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `io_ai_tech` dataset."""

  def get_description(self):
    return ''

  def get_citation(self):
    return ''

  def get_homepage(self):
    return 'https://github.com/ioai-tech/rlds_dataset_builder'

  def get_relative_dataset_location(self):
    return 'io_ai_tech/0.0.1'


class MimicPlay(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `mimic_play` dataset."""

  def get_description(self):
    return r"""Real dataset of 14 long horizon manipulation tasks. A mix of human play data and single robot arm data performing the same tasks. """

  def get_citation(self):
    return r"""@article{wang2023mimicplay,title={Mimicplay: Long-horizon imitation learning by watching human play},author={Wang, Chen and Fan, Linxi and Sun, Jiankai and Zhang, Ruohan and Fei-Fei, Li and Xu, Danfei and Zhu, Yuke and Anandkumar, Anima},journal={arXiv preprint arXiv:2302.12422},year={2023}}"""

  def get_homepage(self):
    return 'https://mimic-play.github.io/'

  def get_relative_dataset_location(self):
    return 'mimic_play/0.0.1'


class AlohaMobile(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `aloha_mobile` dataset."""

  def get_description(self):
    return r"""Real dataset. Imitating mobile manipulation tasks that are bimanual and require whole-body control.  50 demonstrations for each task."""

  def get_citation(self):
    return r"""@inproceedings{fu2024mobile,author = {Fu, Zipeng and Zhao, Tony Z. and Finn, Chelsea},title = {Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation},booktitle = {arXiv},year = {2024},}"""

  def get_homepage(self):
    return 'https://mobile-aloha.github.io'

  def get_relative_dataset_location(self):
    return 'aloha_mobile/0.0.1'


class RoboSet(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `robo_set` dataset."""

  def get_description(self):
    return r"""Real dataset of a single robot arm demonstrating 12 non-trivial manipulation skills across 38 tasks, 7500 trajectories."""

  def get_citation(self):
    return r"""@misc{bharadhwaj2023roboagent, title={RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking}, author={Homanga Bharadhwaj and Jay Vakil and Mohit Sharma and Abhinav Gupta and Shubham Tulsiani and Vikash Kumar},  year={2023}, eprint={2309.01918}, archivePrefix={arXiv}, primaryClass={cs.RO} }"""

  def get_homepage(self):
    return 'https://robopen.github.io/'

  def get_relative_dataset_location(self):
    return 'robo_set/0.0.1'


class Tidybot(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `tidybot` dataset."""

  def get_description(self):
    return ''

  def get_citation(self):
    return r"""@article{wu2023tidybot,title = {TidyBot: Personalized Robot Assistance with Large Language Models},author = {Wu, Jimmy and Antonova, Rika and Kan, Adam and Lepert, Marion and Zeng, Andy and Song, Shuran and Bohg, Jeannette and Rusinkiewicz, Szymon and Funkhouser, Thomas},journal = {Autonomous Robots},year = {2023}}"""

  def get_homepage(self):
    return 'https://github.com/jimmyyhwu/tidybot'

  def get_relative_dataset_location(self):
    return 'tidybot/0.0.1'


class VimaConvertedExternallyToRlds(
    dataset_importer_builder.DatasetImporterBuilder
):
  """DatasetBuilder for `vima_converted_externally_to_rlds` dataset."""

  def get_description(self):
    return r"""SIM dataset of a single robot arm performing procedurally-generated tabletop tasks with multimodal prompts, 600K+ trajectories"""

  def get_citation(self):
    return r"""@inproceedings{jiang2023vima,  title     = {VIMA: General Robot Manipulation with Multimodal Prompts},  author    = {Yunfan Jiang and Agrim Gupta and Zichen Zhang and Guanzhi Wang and Yongqiang Dou and Yanjun Chen and Li Fei-Fei and Anima Anandkumar and Yuke Zhu and Linxi Fan}, booktitle = {Fortieth International Conference on Machine Learning},  year      = {2023}. }"""

  def get_homepage(self):
    return r"""https://vimalabs.github.io/"""

  def get_relative_dataset_location(self):
    return 'vima_converted_externally_to_rlds/0.0.1'


class BridgeDataMsr(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `bridge_data_msr` dataset."""

  def get_description(self):
    return (
        'A set of object manipulation trajectories collected at Microsoft'
        ' Research on a WidowX-250 robot in a setup and format compatible with'
        " UC Berkeley's BridgeData V2"
        ' (https://rail-berkeley.github.io/bridgedata/)'
    )

  def get_citation(self):
    return ''

  def get_homepage(self):
    return 'https://www.microsoft.com/en-us/download/details.aspx?id=105937'

  def get_relative_dataset_location(self):
    return 'bridge_data_msr/0.0.1'


class PlexRobosuite(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `plex_robosuite` dataset."""

  def get_description(self):
    return (
        "A dataset of high-qualty demonstration trajectories for Robosuite's"
        ' Door, Stack, PickPlaceMilk, PickPlaceBread, PickPlaceCereal, and'
        ' NutAssemblyRound tasks, 75 demonstrations per each.'
    )

  def get_citation(self):
    return 'https://doi.org/10.48550/arXiv.2303.08789'

  def get_homepage(self):
    return 'https://microsoft.github.io/PLEX/'

  def get_relative_dataset_location(self):
    return 'plex_robosuite/0.0.1'


class SpocRobot(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for `spoc_robot` dataset."""

  def get_description(self):
    return ''

  def get_citation(self):
    return r"""@article{spoc2023,
    author    = {Kiana Ehsani, Tanmay Gupta, Rose Hendrix, Jordi Salvador, Luca Weihs, Kuo-Hao Zeng, Kunal Pratap Singh, Yejin Kim, Winson Han, Alvaro Herrasti, Ranjay Krishna, Dustin Schwenk, Eli VanderBilt, Aniruddha Kembhavi},
    title     = {Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World},
    journal   = {arXiv},
    year      = {2023},
    eprint    = {2312.02976},
}"""

  def get_homepage(self):
    return 'https://spoc-robot.github.io/'

  def get_relative_dataset_location(self):
    return 'spoc/0.0.1'

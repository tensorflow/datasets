<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="universal_dependencies" />
  <meta itemprop="description" content="Universal Dependencies (UD) is a framework for consistent annotation of grammar&#10;(parts of speech, morphological features, and syntactic dependencies) across&#10;different human languages. UD is an open community effort with over 300&#10;contributors producing more than 200 treebanks in over 100 languages. If you’re&#10;new to UD, you should start by reading the first part of the Short Introduction&#10;and then browsing the annotation guidelines.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;universal_dependencies&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/universal_dependencies" />
  <meta itemprop="sameAs" content="https://universaldependencies.org/" />
  <meta itemprop="citation" content="@misc{11234/1-4758,&#10; title = {Universal Dependencies 2.10},&#10; author = {Zeman, Daniel and Nivre, Joakim and Abrams, Mitchell and Ackermann,  Elia and Aepli, No{&quot;e}mi and Aghaei, Hamid and Agi{&#x27;c}, {v Z}eljko and  Ahmadi, Amir and Ahrenberg, Lars and Ajede, Chika Kennedy and  Aleksandravi{v c}i{=u}te, Gabriele and Alfina, Ika and Algom, Avner  and Andersen, Erik and Antonsen, Lene and Aplonova, Katya and Aquino,  Angelina and Aragon, Carolina and Aranes, Glyd and Aranzabe, Maria Jesus and  Arican, Bilge Nas and Arnard{&#x27;o}ttir, {     H}{&#x27;o}runn and Arutie, Gashaw  and Arwidarasti, Jessica Naraiswari and Asahara, Masayuki and Aslan, Deniz  Baran and Asmazoglu, Cengiz and Ateyah, Luma and Atmaca, Furkan and  Attia, Mohammed and Atutxa, Aitziber and Augustinus, Liesbeth and Badmaeva,  Elena and Balasubramani, Keerthana and Ballesteros, Miguel and Banerjee,  Esha and Bank, Sebastian and Barbu Mititelu, Verginica and Barkarson,  Starkaður and Basile, Rodolfo and Basmov, Victoria and Batchelor, Colin and  Bauer, John and Bedir, Seyyit Talha and Bengoetxea, Kepa and Ben Moshe, Yifat  and Berk, G{&quot;o}zde and Berzak, Yevgeni and Bhat, Irshad Ahmad and Bhat,  Riyaz Ahmad and Biagetti, Erica and Bick, Eckhard and Bielinskiene,  Agne and Bjarnad{&#x27;o}ttir, Krist{&#x27;i}n and Blokland, Rogier and  Bobicev, Victoria and Boizou, Lo{&quot;i}c and Borges V{&quot;o}lker, Emanuel  and B{&quot;o}rstell, Carl and Bosco, Cristina and Bouma, Gosse and Bowman, Sam  and Boyd, Adriane and Braggaar, Anouck and Brokaite, Kristina and  Burchardt, Aljoscha and Candito, Marie and Caron, Bernard and Caron, Gauthier  and Cassidy, Lauren and Cavalcanti, Tatiana and Cebiroglu Eryigit,  G{&quot;u}l{s}en and Cecchini, Flavio Massimiliano and Celano, Giuseppe G. A.  and {C}{&#x27;e}pl{&quot;o}, Slavom{&#x27;i}r and Cesur, Neslihan and Cetin, Savas  and {C}etinoglu, {&quot;O}zlem and Chalub, Fabricio and Chauhan, Shweta  and Chi, Ethan and Chika, Taishi and Cho, Yongseok and Choi, Jinho and Chun,  Jayeol and Chung, Juyeon and Cignarella, Alessandra T. and Cinkov{&#x27;a},  Silvie and Collomb, Aur{&#x27;e}lie and {C}{&quot;o}ltekin, {C}a{g}ri and  Connor, Miriam and Corbetta, Daniela and Courtin, Marine and Cristescu,  Mihaela and Daniel, Philemon and Davidson, Elizabeth and Dehouck, Mathieu  and de Laurentiis, Martina and de Marneffe, Marie-Catherine and de Paiva,  Valeria and Derin, Mehmet Oguz and de Souza, Elvis and Diaz de Ilarraza,  Arantza and Dickerson, Carly and Dinakaramani, Arawinda and Di Nuovo, Elisa  and Dione, Bamba and Dirix, Peter and Dobrovoljc, Kaja and Dozat, Timothy and  Droganova, Kira and Dwivedi, Puneet and Eckhoff, Hanne and Eiche, Sandra and  Eli, Marhaba and Elkahky, Ali and Ephrem, Binyam and Erina, Olga and Erjavec,  Toma{v z} and Etienne, Aline and Evelyn, Wograine and Facundes, Sidney and  Farkas, Rich{&#x27;a}rd and Favero, Federica and Ferdaousi, Jannatul and  Fernanda, Mar{&#x27;i}lia and Fernandez Alcalde, Hector and Foster, Jennifer  and Freitas, Cl{&#x27;a}udia and Fujita, Kazunori and Gajdo{v s}ov{&#x27;a},  Katar{&#x27;i}na and Galbraith, Daniel and Gamba, Federica and Garcia, Marcos  and G{&quot;a}rdenfors, Moa and Garza, Sebastian and Gerardi, Fabr{&#x27;i}cio  Ferraz and Gerdes, Kim and Ginter, Filip and Godoy, Gustavo and Goenaga,  Iakes and Gojenola, Koldo and G{&quot;o}kirmak, Memduh and Goldberg, Yoav and  G{&#x27;o}mez Guinovart, Xavier and Gonz{&#x27;a}lez Saavedra, Berta and  Griciute, Bernadeta and Grioni, Matias and Grobol, Lo{&quot;i}c and  Gruzitis, Normunds and Guillaume, Bruno and Guillot-Barbance,  C{&#x27;e}line and G{&quot;u}ng{&quot;o}r, Tunga and Habash, Nizar and Hafsteinsson,  Hinrik and Hajic, Jan and Hajic jr., Jan and  H{&quot;a}m{&quot;a}l{&quot;a}inen, Mika and Ha My, Linh and Han, Na-Rae and  Hanifmuti, Muhammad Yudistira and Harada, Takahiro and Hardwick, Sam and  Harris, Kim and Haug, Dag and Heinecke, Johannes and Hellwig, Oliver and  Hennig, Felix and Hladk{&#x27;a}, Barbora and Hlav{&#x27;a}{v c}ov{&#x27;a}, Jaroslava  and Hociung, Florinel and Hohle, Petter and Hwang, Jena and Ikeda, Takumi  and Ingason, Anton Karl and Ion, Radu and Irimia, Elena and Ishola,  {O}l{&#x27;a}j{&#x27;i}d{&#x27;e} and Ito, Kaoru and Jannat, Siratun and  Jel{&#x27;i}nek, Tom{&#x27;a}{v s} and Jha, Apoorva and Johannsen, Anders and  J{&#x27;o}nsd{&#x27;o}ttir, Hildur and Jorgensen, Fredrik and Juutinen, Markus  and K, Sarveswaran and Ka{c s}ikara, H{&quot;u}ner and Kaasen, Andre and  Kabaeva, Nadezhda and Kahane, Sylvain and Kanayama, Hiroshi and Kanerva,  Jenna and Kara, Neslihan and Karah{&#x27;o}ǧa, Ritv{&#x27;a}n and Katz, Boris and  Kayadelen, Tolga and Kenney, Jessica and Kettnerov{&#x27;a}, V{&#x27;a}clava and  Kirchner, Jesse and Klementieva, Elena and Klyachko, Elena and K{&quot;o}hn,  Arne and K{&quot;o}ksal, Abdullatif and Kopacewicz, Kamil and Korkiakangas, Timo  and K{&quot;o}se, Mehmet and Kotsyba, Natalia and Kovalevskaite, Jolanta and  Krek, Simon and Krishnamurthy, Parameswari and K{&quot;u}bler, Sandra and  Kuyruk{c c}u, O{g}uzhan and Kuzgun, Asli and Kwak, Sookyoung and  Laippala, Veronika and Lam, Lucia and Lambertino, Lorenzo and Lando, Tatiana  and Larasati, Septina Dian and Lavrentiev, Alexei and Lee, John and Le  H{o}ng, Phương and Lenci, Alessandro and Lertpradit, Saran and Leung,  Herman and Levina, Maria and Li, Cheuk Ying and Li, Josie and Li, Keying and  Li, Yuan and Lim, {KyungTae} and Lima Padovani, Bruna and Lind{&#x27;e}n, Krister  and Ljube{s}i{&#x27;c}, Nikola and Loginova, Olga and Lusito, Stefano and  Luthfi, Andry and Luukko, Mikko and Lyashevskaya, Olga and Lynn, Teresa and  Macketanz, Vivien and Mahamdi, Menel and Maillard, Jean and Makazhanov, Aibek  and Mandl, Michael and Manning, Christopher and Manurung, Ruli and  Mar{s}an, B{&quot;u}{s}ra and M{a}r{a}nduc, C{a}t{a}lina and  Mare{c}ek, David and Marheinecke, Katrin and Markantonatou, Stella and  Mart{&#x27;i}nez Alonso, H{&#x27;e}ctor and Mart{&#x27;i}n Rodr{&#x27;i}guez, Lorena  and Martins, Andr{&#x27;e} and Ma{s}ek, Jan and Matsuda, Hiroshi and  Matsumoto, Yuji and Mazzei, Alessandro and {McDonald}, Ryan and {McGuinness},  Sarah and Mendon{c}a, Gustavo and Merzhevich, Tatiana and Miekka, Niko and  Mischenkova, Karina and Misirpashayeva, Margarita and Missil{&quot;a}, Anna and  Mititelu, C{a}t{a}lin and Mitrofan, Maria and Miyao, Yusuke and Mojiri  Foroushani, {AmirHossein} and Moln{&#x27;a}r, Judit and Moloodi, Amirsaeid and  Montemagni, Simonetta and More, Amir and Moreno Romero, Laura and Moretti,  Giovanni and Mori, Keiko Sophie and Mori, Shinsuke and Morioka, Tomohiko and  Moro, Shigeki and Mortensen, Bjartur and Moskalevskyi, Bohdan and Muischnek,  Kadri and Munro, Robert and Murawaki, Yugo and M{&quot;u}{&quot;u}risep, Kaili and  Nainwani, Pinkey and Nakhl{&#x27;e}, Mariam and Navarro Horniacek, Juan  Ignacio and Nedoluzhko, Anna and Ne{v s}pore-Berzkalne, Gunta and  Nevaci, Manuela and Nguy{e}n Th{i}, Lương and Nguy{e}n  Th{i} Minh, Huy{e}n and Nikaido, Yoshihiro and Nikolaev, Vitaly  and Nitisaroj, Rattima and Nourian, Alireza and Nurmi, Hanna and Ojala,  Stina and Ojha, Atul Kr. and Ol{&#x27;u}{&#x27;o}kun, Ad{e}day{o}̀ and Omura,  Mai and Onwuegbuzia, Emeka and Ordan, Noam and Osenova, Petya and  {&quot;O}stling, Robert and {O}vrelid, Lilja and {&quot;O}zate{s},  {S}aziye Bet{&quot;u}l and {&quot;O}z{c}elik, Merve and {&quot;O}zg{&quot;u}r,  Arzucan and {&quot;O}zt{&quot;u}rk Ba{s}aran, Balkiz and Paccosi, Teresa  and Palmero Aprosio, Alessio and Park, Hyunji Hayley and Partanen, Niko  and Pascual, Elena and Passarotti, Marco and Patejuk, Agnieszka and  Paulino-Passos, Guilherme and Pedonese, Giulia and Peljak-{L}api{n}ska,  Angelika and Peng, Siyao and Perez, Cenel-Augusto and Perkova, Natalia and  Perrier, Guy and Petrov, Slav and Petrova, Daria and Peverelli, Andrea and  Phelan, Jason and Piitulainen, Jussi and Pirinen, Tommi A and Pitler, Emily  and Plank, Barbara and Poibeau, Thierry and Ponomareva, Larisa and Popel,  Martin and Pretkalni{n}a, Lauma and Pr{&#x27;e}vost, Sophie and Prokopidis,  Prokopis and Przepi{o}rkowski, Adam and Puolakainen, Tiina and Pyysalo,  Sampo and Qi, Peng and R{&quot;a}{&quot;a}bis, Andriela and Rademaker, Alexandre and  Rahoman, Mizanur and Rama, Taraka and Ramasamy, Loganathan and Ramisch,  Carlos and Rashel, Fam and Rasooli, Mohammad Sadegh and Ravishankar, Vinit  and Real, Livy and Rebeja, Petru and Reddy, Siva and Regnault, Mathilde and  Rehm, Georg and Riabov, Ivan and Rie{ss}ler, Michael and Rimkut{e}, Erika  and Rinaldi, Larissa and Rituma, Laura and Rizqiyah, Putri and Rocha, Luisa  and R{&quot;o}gnvaldsson, Eir{&#x27;i}kur and Romanenko, Mykhailo and Rosa, Rudolf  and Roșca, Valentin and Rovati, Davide and Rozonoyer, Ben and Rudina, Olga  and Rueter, Jack and R{&#x27;u}narsson, Kristj{&#x27;a}n and Sadde, Shoval and  Safari, Pegah and Sagot, Beno{i}t and Sahala, Aleksi and Saleh, Shadi  and Salomoni, Alessio and Samard{v z}i{&#x27;c}, Tanja and Samson, Stephanie and  Sanguinetti, Manuela and Saniyar, Ezgi and S{&quot;a}rg, Dage and  Saulite, Baiba and Sawanakunanon, Yanin and Saxena, Shefali and  Scannell, Kevin and Scarlata, Salvatore and Schneider, Nathan and Schuster,  Sebastian and Schwartz, Lane and Seddah, Djam{&#x27;e} and Seeker, Wolfgang and  Seraji, Mojgan and Shahzadi, Syeda and Shen, Mo and Shimada, Atsuko and  Shirasu, Hiroyuki and Shishkina, Yana and Shohibussirri, Muh and Sichinava,  Dmitry and Siewert, Janine and Sigurðsson, Einar Freyr and Silveira, Aline  and Silveira, Natalia and Simi, Maria and Simionescu, Radu and Simk{&#x27;o},  Katalin and {S}imkov{&#x27;a}, M{&#x27;a}ria and Simov, Kiril and Skachedubova,  Maria and Smith, Aaron and Soares-Bastos, Isabela and Sourov, Shafi and  Spadine, Carolyn and Sprugnoli, Rachele and Stamou, Vivian and  Steingr{&#x27;i}msson, Stein{h}{&#x27;o}r and Stella, Antonio and Straka,  Milan and Strickland, Emmett and Strnadov{&#x27;a}, Jana and Suhr, Alane and  Sulestio, Yogi Lesmana and Sulubacak, Umut and Suzuki, Shingo and Swanson,  Daniel and Sz{&#x27;a}nt{&#x27;o}, Zsolt and Taguchi, Chihiro and Taji, Dima and  Takahashi, Yuta and Tamburini, Fabio and Tan, Mary Ann C. and Tanaka, Takaaki  and Tanaya, Dipta and Tavoni, Mirko and Tella, Samson and Tellier, Isabelle  and Testori, Marinella and Thomas, Guillaume and Tonelli, Sara and Torga,  Liisi and Toska, Marsida and Trosterud, Trond and Trukhina, Anna and  Tsarfaty, Reut and T{&quot;u}rk, Utku and Tyers, Francis and Uematsu, Sumire  and Untilov, Roman and Ure{v s}ov{&#x27;a}, Zde{n}ka and Uria, Larraitz and  Uszkoreit, Hans and Utka, Andrius and Vagnoni, Elena and Vajjala, Sowmya and  van der Goot, Rob and Vanhove, Martine and van Niekerk, Daniel and van Noord,  Gertjan and Varga, Viktor and Vedenina, Uliana and Villemonte de la  Clergerie, Eric and Vincze, Veronika and Vlasova, Natalia and Wakasa,  Aya and Wallenberg, Joel C. and Wallin, Lars and Walsh, Abigail and Wang,  Jing Xian and Washington, Jonathan North and Wendt, Maximilan and Widmer,  Paul and Wigderson, Shira and Wijono, Sri Hartati and Williams, Seyi and  Wir{&#x27;e}n, Mats and Wittern, Christian and Woldemariam, Tsegay and Wong,  Tak-sum and Wr{&#x27;o}blewska, Alina and Yako, Mary and Yamashita, Kayo and  Yamazaki, Naoki and Yan, Chunxiao and Yasuoka, Koichi and Yavrumyan, Marat M.  and Yenice, Arife Bet{&quot;u}l and Yildiz, Olcay Taner and Yu, Zhuoran and  Yuliawati, Arlisa and {Z}abokrtsk{&#x27;y}, Zden{v e}k and Zahra, Shorouq and  Zeldes, Amir and Zhou, He and Zhu, Hanzhi and Zhuravleva, Anna and Ziane,  Rayan&#10; },&#10; url = {http://hdl.handle.net/11234/1-4758},&#10; note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal  and Applied Linguistics ({{&#x27;U}FAL}), Faculty of Mathematics and Physics,  Charles University},&#10; copyright = {Licence Universal Dependencies v2.10},&#10; year = {2022}&#10;}" />
</div>

# `universal_dependencies`


*   **Description**:

Universal Dependencies (UD) is a framework for consistent annotation of grammar
(parts of speech, morphological features, and syntactic dependencies) across
different human languages. UD is an open community effort with over 300
contributors producing more than 200 treebanks in over 100 languages. If you’re
new to UD, you should start by reading the first part of the Short Introduction
and then browsing the annotation guidelines.

*   **Homepage**:
    [https://universaldependencies.org/](https://universaldependencies.org/)

*   **Source code**:
    [`tfds.text.universal_dependencies.UniversalDependencies`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/universal_dependencies/universal_dependencies.py)

*   **Versions**:

    *   `1.0.0`: Initial release, which corresponds to Universal Dependencies
        2.10.
    *   **`1.0.1`** (default): Updated config names.

*   **Feature structure**:

```python
FeaturesDict({
    'deprel': Sequence(Text(shape=(), dtype=tf.string)),
    'deps': Sequence(Text(shape=(), dtype=tf.string)),
    'feats': Sequence(Text(shape=(), dtype=tf.string)),
    'head': Sequence(Text(shape=(), dtype=tf.string)),
    'idx': Text(shape=(), dtype=tf.string),
    'lemmas': Sequence(Text(shape=(), dtype=tf.string)),
    'misc': Sequence(Text(shape=(), dtype=tf.string)),
    'text': Text(shape=(), dtype=tf.string),
    'tokens': Sequence(Text(shape=(), dtype=tf.string)),
    'upos': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=18)),
    'xpos': Sequence(Text(shape=(), dtype=tf.string)),
})
```

*   **Feature documentation**:

Feature | Class                | Shape   | Dtype     | Description
:------ | :------------------- | :------ | :-------- | :----------
        | FeaturesDict         |         |           |
deprel  | Sequence(Text)       | (None,) | tf.string |
deps    | Sequence(Text)       | (None,) | tf.string |
feats   | Sequence(Text)       | (None,) | tf.string |
head    | Sequence(Text)       | (None,) | tf.string |
idx     | Text                 |         | tf.string |
lemmas  | Sequence(Text)       | (None,) | tf.string |
misc    | Sequence(Text)       | (None,) | tf.string |
text    | Text                 |         | tf.string |
tokens  | Sequence(Text)       | (None,) | tf.string |
upos    | Sequence(ClassLabel) | (None,) | tf.int64  |
xpos    | Sequence(Text)       | (None,) | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@misc{11234/1-4758,
 title = {Universal Dependencies 2.10},
 author = {Zeman, Daniel and Nivre, Joakim and Abrams, Mitchell and Ackermann,  Elia and Aepli, No{"e}mi and Aghaei, Hamid and Agi{'c}, {v Z}eljko and  Ahmadi, Amir and Ahrenberg, Lars and Ajede, Chika Kennedy and  Aleksandravi{v c}i{=u}te, Gabriele and Alfina, Ika and Algom, Avner  and Andersen, Erik and Antonsen, Lene and Aplonova, Katya and Aquino,  Angelina and Aragon, Carolina and Aranes, Glyd and Aranzabe, Maria Jesus and  Arican, Bilge Nas and Arnard{'o}ttir, {     H}{'o}runn and Arutie, Gashaw  and Arwidarasti, Jessica Naraiswari and Asahara, Masayuki and Aslan, Deniz  Baran and Asmazoglu, Cengiz and Ateyah, Luma and Atmaca, Furkan and  Attia, Mohammed and Atutxa, Aitziber and Augustinus, Liesbeth and Badmaeva,  Elena and Balasubramani, Keerthana and Ballesteros, Miguel and Banerjee,  Esha and Bank, Sebastian and Barbu Mititelu, Verginica and Barkarson,  Starkaður and Basile, Rodolfo and Basmov, Victoria and Batchelor, Colin and  Bauer, John and Bedir, Seyyit Talha and Bengoetxea, Kepa and Ben Moshe, Yifat  and Berk, G{"o}zde and Berzak, Yevgeni and Bhat, Irshad Ahmad and Bhat,  Riyaz Ahmad and Biagetti, Erica and Bick, Eckhard and Bielinskiene,  Agne and Bjarnad{'o}ttir, Krist{'i}n and Blokland, Rogier and  Bobicev, Victoria and Boizou, Lo{"i}c and Borges V{"o}lker, Emanuel  and B{"o}rstell, Carl and Bosco, Cristina and Bouma, Gosse and Bowman, Sam  and Boyd, Adriane and Braggaar, Anouck and Brokaite, Kristina and  Burchardt, Aljoscha and Candito, Marie and Caron, Bernard and Caron, Gauthier  and Cassidy, Lauren and Cavalcanti, Tatiana and Cebiroglu Eryigit,  G{"u}l{s}en and Cecchini, Flavio Massimiliano and Celano, Giuseppe G. A.  and {C}{'e}pl{"o}, Slavom{'i}r and Cesur, Neslihan and Cetin, Savas  and {C}etinoglu, {"O}zlem and Chalub, Fabricio and Chauhan, Shweta  and Chi, Ethan and Chika, Taishi and Cho, Yongseok and Choi, Jinho and Chun,  Jayeol and Chung, Juyeon and Cignarella, Alessandra T. and Cinkov{'a},  Silvie and Collomb, Aur{'e}lie and {C}{"o}ltekin, {C}a{g}ri and  Connor, Miriam and Corbetta, Daniela and Courtin, Marine and Cristescu,  Mihaela and Daniel, Philemon and Davidson, Elizabeth and Dehouck, Mathieu  and de Laurentiis, Martina and de Marneffe, Marie-Catherine and de Paiva,  Valeria and Derin, Mehmet Oguz and de Souza, Elvis and Diaz de Ilarraza,  Arantza and Dickerson, Carly and Dinakaramani, Arawinda and Di Nuovo, Elisa  and Dione, Bamba and Dirix, Peter and Dobrovoljc, Kaja and Dozat, Timothy and  Droganova, Kira and Dwivedi, Puneet and Eckhoff, Hanne and Eiche, Sandra and  Eli, Marhaba and Elkahky, Ali and Ephrem, Binyam and Erina, Olga and Erjavec,  Toma{v z} and Etienne, Aline and Evelyn, Wograine and Facundes, Sidney and  Farkas, Rich{'a}rd and Favero, Federica and Ferdaousi, Jannatul and  Fernanda, Mar{'i}lia and Fernandez Alcalde, Hector and Foster, Jennifer  and Freitas, Cl{'a}udia and Fujita, Kazunori and Gajdo{v s}ov{'a},  Katar{'i}na and Galbraith, Daniel and Gamba, Federica and Garcia, Marcos  and G{"a}rdenfors, Moa and Garza, Sebastian and Gerardi, Fabr{'i}cio  Ferraz and Gerdes, Kim and Ginter, Filip and Godoy, Gustavo and Goenaga,  Iakes and Gojenola, Koldo and G{"o}kirmak, Memduh and Goldberg, Yoav and  G{'o}mez Guinovart, Xavier and Gonz{'a}lez Saavedra, Berta and  Griciute, Bernadeta and Grioni, Matias and Grobol, Lo{"i}c and  Gruzitis, Normunds and Guillaume, Bruno and Guillot-Barbance,  C{'e}line and G{"u}ng{"o}r, Tunga and Habash, Nizar and Hafsteinsson,  Hinrik and Hajic, Jan and Hajic jr., Jan and  H{"a}m{"a}l{"a}inen, Mika and Ha My, Linh and Han, Na-Rae and  Hanifmuti, Muhammad Yudistira and Harada, Takahiro and Hardwick, Sam and  Harris, Kim and Haug, Dag and Heinecke, Johannes and Hellwig, Oliver and  Hennig, Felix and Hladk{'a}, Barbora and Hlav{'a}{v c}ov{'a}, Jaroslava  and Hociung, Florinel and Hohle, Petter and Hwang, Jena and Ikeda, Takumi  and Ingason, Anton Karl and Ion, Radu and Irimia, Elena and Ishola,  {O}l{'a}j{'i}d{'e} and Ito, Kaoru and Jannat, Siratun and  Jel{'i}nek, Tom{'a}{v s} and Jha, Apoorva and Johannsen, Anders and  J{'o}nsd{'o}ttir, Hildur and Jorgensen, Fredrik and Juutinen, Markus  and K, Sarveswaran and Ka{c s}ikara, H{"u}ner and Kaasen, Andre and  Kabaeva, Nadezhda and Kahane, Sylvain and Kanayama, Hiroshi and Kanerva,  Jenna and Kara, Neslihan and Karah{'o}ǧa, Ritv{'a}n and Katz, Boris and  Kayadelen, Tolga and Kenney, Jessica and Kettnerov{'a}, V{'a}clava and  Kirchner, Jesse and Klementieva, Elena and Klyachko, Elena and K{"o}hn,  Arne and K{"o}ksal, Abdullatif and Kopacewicz, Kamil and Korkiakangas, Timo  and K{"o}se, Mehmet and Kotsyba, Natalia and Kovalevskaite, Jolanta and  Krek, Simon and Krishnamurthy, Parameswari and K{"u}bler, Sandra and  Kuyruk{c c}u, O{g}uzhan and Kuzgun, Asli and Kwak, Sookyoung and  Laippala, Veronika and Lam, Lucia and Lambertino, Lorenzo and Lando, Tatiana  and Larasati, Septina Dian and Lavrentiev, Alexei and Lee, John and Le  H{o}ng, Phương and Lenci, Alessandro and Lertpradit, Saran and Leung,  Herman and Levina, Maria and Li, Cheuk Ying and Li, Josie and Li, Keying and  Li, Yuan and Lim, {KyungTae} and Lima Padovani, Bruna and Lind{'e}n, Krister  and Ljube{s}i{'c}, Nikola and Loginova, Olga and Lusito, Stefano and  Luthfi, Andry and Luukko, Mikko and Lyashevskaya, Olga and Lynn, Teresa and  Macketanz, Vivien and Mahamdi, Menel and Maillard, Jean and Makazhanov, Aibek  and Mandl, Michael and Manning, Christopher and Manurung, Ruli and  Mar{s}an, B{"u}{s}ra and M{a}r{a}nduc, C{a}t{a}lina and  Mare{c}ek, David and Marheinecke, Katrin and Markantonatou, Stella and  Mart{'i}nez Alonso, H{'e}ctor and Mart{'i}n Rodr{'i}guez, Lorena  and Martins, Andr{'e} and Ma{s}ek, Jan and Matsuda, Hiroshi and  Matsumoto, Yuji and Mazzei, Alessandro and {McDonald}, Ryan and {McGuinness},  Sarah and Mendon{c}a, Gustavo and Merzhevich, Tatiana and Miekka, Niko and  Mischenkova, Karina and Misirpashayeva, Margarita and Missil{"a}, Anna and  Mititelu, C{a}t{a}lin and Mitrofan, Maria and Miyao, Yusuke and Mojiri  Foroushani, {AmirHossein} and Moln{'a}r, Judit and Moloodi, Amirsaeid and  Montemagni, Simonetta and More, Amir and Moreno Romero, Laura and Moretti,  Giovanni and Mori, Keiko Sophie and Mori, Shinsuke and Morioka, Tomohiko and  Moro, Shigeki and Mortensen, Bjartur and Moskalevskyi, Bohdan and Muischnek,  Kadri and Munro, Robert and Murawaki, Yugo and M{"u}{"u}risep, Kaili and  Nainwani, Pinkey and Nakhl{'e}, Mariam and Navarro Horniacek, Juan  Ignacio and Nedoluzhko, Anna and Ne{v s}pore-Berzkalne, Gunta and  Nevaci, Manuela and Nguy{e}n Th{i}, Lương and Nguy{e}n  Th{i} Minh, Huy{e}n and Nikaido, Yoshihiro and Nikolaev, Vitaly  and Nitisaroj, Rattima and Nourian, Alireza and Nurmi, Hanna and Ojala,  Stina and Ojha, Atul Kr. and Ol{'u}{'o}kun, Ad{e}day{o}̀ and Omura,  Mai and Onwuegbuzia, Emeka and Ordan, Noam and Osenova, Petya and  {"O}stling, Robert and {O}vrelid, Lilja and {"O}zate{s},  {S}aziye Bet{"u}l and {"O}z{c}elik, Merve and {"O}zg{"u}r,  Arzucan and {"O}zt{"u}rk Ba{s}aran, Balkiz and Paccosi, Teresa  and Palmero Aprosio, Alessio and Park, Hyunji Hayley and Partanen, Niko  and Pascual, Elena and Passarotti, Marco and Patejuk, Agnieszka and  Paulino-Passos, Guilherme and Pedonese, Giulia and Peljak-{L}api{n}ska,  Angelika and Peng, Siyao and Perez, Cenel-Augusto and Perkova, Natalia and  Perrier, Guy and Petrov, Slav and Petrova, Daria and Peverelli, Andrea and  Phelan, Jason and Piitulainen, Jussi and Pirinen, Tommi A and Pitler, Emily  and Plank, Barbara and Poibeau, Thierry and Ponomareva, Larisa and Popel,  Martin and Pretkalni{n}a, Lauma and Pr{'e}vost, Sophie and Prokopidis,  Prokopis and Przepi{o}rkowski, Adam and Puolakainen, Tiina and Pyysalo,  Sampo and Qi, Peng and R{"a}{"a}bis, Andriela and Rademaker, Alexandre and  Rahoman, Mizanur and Rama, Taraka and Ramasamy, Loganathan and Ramisch,  Carlos and Rashel, Fam and Rasooli, Mohammad Sadegh and Ravishankar, Vinit  and Real, Livy and Rebeja, Petru and Reddy, Siva and Regnault, Mathilde and  Rehm, Georg and Riabov, Ivan and Rie{ss}ler, Michael and Rimkut{e}, Erika  and Rinaldi, Larissa and Rituma, Laura and Rizqiyah, Putri and Rocha, Luisa  and R{"o}gnvaldsson, Eir{'i}kur and Romanenko, Mykhailo and Rosa, Rudolf  and Roșca, Valentin and Rovati, Davide and Rozonoyer, Ben and Rudina, Olga  and Rueter, Jack and R{'u}narsson, Kristj{'a}n and Sadde, Shoval and  Safari, Pegah and Sagot, Beno{i}t and Sahala, Aleksi and Saleh, Shadi  and Salomoni, Alessio and Samard{v z}i{'c}, Tanja and Samson, Stephanie and  Sanguinetti, Manuela and Saniyar, Ezgi and S{"a}rg, Dage and  Saulite, Baiba and Sawanakunanon, Yanin and Saxena, Shefali and  Scannell, Kevin and Scarlata, Salvatore and Schneider, Nathan and Schuster,  Sebastian and Schwartz, Lane and Seddah, Djam{'e} and Seeker, Wolfgang and  Seraji, Mojgan and Shahzadi, Syeda and Shen, Mo and Shimada, Atsuko and  Shirasu, Hiroyuki and Shishkina, Yana and Shohibussirri, Muh and Sichinava,  Dmitry and Siewert, Janine and Sigurðsson, Einar Freyr and Silveira, Aline  and Silveira, Natalia and Simi, Maria and Simionescu, Radu and Simk{'o},  Katalin and {S}imkov{'a}, M{'a}ria and Simov, Kiril and Skachedubova,  Maria and Smith, Aaron and Soares-Bastos, Isabela and Sourov, Shafi and  Spadine, Carolyn and Sprugnoli, Rachele and Stamou, Vivian and  Steingr{'i}msson, Stein{h}{'o}r and Stella, Antonio and Straka,  Milan and Strickland, Emmett and Strnadov{'a}, Jana and Suhr, Alane and  Sulestio, Yogi Lesmana and Sulubacak, Umut and Suzuki, Shingo and Swanson,  Daniel and Sz{'a}nt{'o}, Zsolt and Taguchi, Chihiro and Taji, Dima and  Takahashi, Yuta and Tamburini, Fabio and Tan, Mary Ann C. and Tanaka, Takaaki  and Tanaya, Dipta and Tavoni, Mirko and Tella, Samson and Tellier, Isabelle  and Testori, Marinella and Thomas, Guillaume and Tonelli, Sara and Torga,  Liisi and Toska, Marsida and Trosterud, Trond and Trukhina, Anna and  Tsarfaty, Reut and T{"u}rk, Utku and Tyers, Francis and Uematsu, Sumire  and Untilov, Roman and Ure{v s}ov{'a}, Zde{n}ka and Uria, Larraitz and  Uszkoreit, Hans and Utka, Andrius and Vagnoni, Elena and Vajjala, Sowmya and  van der Goot, Rob and Vanhove, Martine and van Niekerk, Daniel and van Noord,  Gertjan and Varga, Viktor and Vedenina, Uliana and Villemonte de la  Clergerie, Eric and Vincze, Veronika and Vlasova, Natalia and Wakasa,  Aya and Wallenberg, Joel C. and Wallin, Lars and Walsh, Abigail and Wang,  Jing Xian and Washington, Jonathan North and Wendt, Maximilan and Widmer,  Paul and Wigderson, Shira and Wijono, Sri Hartati and Williams, Seyi and  Wir{'e}n, Mats and Wittern, Christian and Woldemariam, Tsegay and Wong,  Tak-sum and Wr{'o}blewska, Alina and Yako, Mary and Yamashita, Kayo and  Yamazaki, Naoki and Yan, Chunxiao and Yasuoka, Koichi and Yavrumyan, Marat M.  and Yenice, Arife Bet{"u}l and Yildiz, Olcay Taner and Yu, Zhuoran and  Yuliawati, Arlisa and {Z}abokrtsk{'y}, Zden{v e}k and Zahra, Shorouq and  Zeldes, Amir and Zhou, He and Zhu, Hanzhi and Zhuravleva, Anna and Ziane,  Rayan
 },
 url = {http://hdl.handle.net/11234/1-4758},
 note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal  and Applied Linguistics ({{'U}FAL}), Faculty of Mathematics and Physics,  Charles University},
 copyright = {Licence Universal Dependencies v2.10},
 year = {2022}
}
```


## universal_dependencies/af_afribooms (default config)

*   **Config description**: UD Afrikaans-AfriBooms is a conversion of the
    AfriBooms Dependency Treebank, originally annotated with a simplified PoS
    set and dependency relations according to a subset of the Stanford tag set.
    The corpus consists of public government documents. The dataset was proposed
    in 'AfriBooms: An Online Treebank for Afrikaans' by Augustinus et al.
    (2016); https://www.aclweb.org/anthology/L16-1107.pdf.

*   **Download size**: `2.95 MiB`

*   **Dataset size**: `4.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 194
`'test'`  | 425
`'train'` | 1,315

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-af_afribooms-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/akk_pisandub

*   **Config description**: A small set of sentences from Babylonian royal
    inscriptions.

*   **Download size**: `99.41 KiB`

*   **Dataset size**: `126.32 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 101

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-akk_pisandub-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/akk_riao

*   **Config description**: UD_Akkadian-RIAO is a small treebank which consists
    of 22 277 words and 1845 sentences. This represents an intact subset of a
    total of 2211 sentences from the early Neo-Assyrian royal inscriptions of
    the tenth and ninth centuries BCE. These royal inscriptions were extracted
    from Oracc (Open Richly Annotated Cuneiform Corpus;
    http://oracc.museum.upenn.edu/riao/), where all Neo-Assyrian royal
    inscriptions are lemmatized word-for-word. The language of the corpus is
    Standard Babylonian, with occasional Assyrianisms, whereas “Akkadian” is the
    umbrella term for both Assyrian and Babylonian. The treebank was manually
    annotated following the UD annotation guidelines.

*   **Download size**: `1.87 MiB`

*   **Dataset size**: `2.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,874

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-akk_riao-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/aqz_tudet

*   **Config description**: UD_Akuntsu-TuDeT is a collection of annotated texts
    in Akuntsú. Together with UD_Tupinamba-TuDeT and UD_Munduruku-TuDeT,
    UD_Akuntsu-TuDeT is part of the TuLaR project. The sentences are being
    annotated by Carolina Aragon and Fabrício Ferraz Gerardi.

*   **Download size**: `67.25 KiB`

*   **Dataset size**: `97.39 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 243

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-aqz_tudet-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/sq_tsa

*   **Config description**: The UD Treebank for Standard Albanian (TSA) is a
    small treebank that consists of 60 sentences corresponding to 922 tokens.
    The data was collected from different Wikipedia entries. This treebank was
    created mainly manually following the Universal Dependencies guidelines. The
    lemmatization was performed using the lemmatizer
    https://bitbucket.org/timarkh/uniparser-albanian-grammar/src/master/
    developed by the Albanian National Corpus team (Maria Morozova, Alexander
    Rusakov, Timofey Arkhangelskiy). Tagging and Morphological Analysis were
    semi-automated through python scripts and corrected manually, whereas
    Dependency relations were assigned fully manually. We encourage any
    initiatives to increase the size and/or improve the overall quality of the
    Treebank.

*   **Download size**: `62.00 KiB`

*   **Dataset size**: `93.65 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 60

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-sq_tsa-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/am_att

*   **Config description**: UD_Amharic-ATT is a manually annotated Treebanks. It
    is annotated for POS tag, morphological information and dependency
    relations. Since Amharic is a morphologically-rich, pro-drop, and languages
    having a feature of clitic doubling, clitics have been segmented manually.

*   **Download size**: `995.32 KiB`

*   **Dataset size**: `1.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,074

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-am_att-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/grc_perseus

*   **Config description**: This Universal Dependencies Ancient Greek Treebank
    consists of an automatic conversion of a selection of passages from the
    Ancient Greek and Latin Dependency Treebank 2.1

*   **Download size**: `18.02 MiB`

*   **Dataset size**: `24.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,137
`'test'`  | 1,306
`'train'` | 11,476

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-grc_perseus-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/grc_proiel

*   **Config description**: The Ancient Greek PROIEL treebank is based on the
    Ancient Greek data from the PROIEL treebank, which is maintained at the
    Department of Philosophy, Classics, History of Arts and Ideas at the
    University of Oslo. The conversion is based on the 20180408 release of the
    PROIEL treebank available from
    https://github.com/proiel/proiel-treebank/releases. The original annotators
    are acknowledged in the files available there. The conversion code is
    available in the Rubygem proiel-cli, https://github.com/proiel/proiel-cli.

*   **Download size**: `22.62 MiB`

*   **Dataset size**: `30.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,019
`'test'`  | 1,047
`'train'` | 15,014

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-grc_proiel-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/apu_ufpa

*   **Config description**: The initial release contains 70 annotated sentences.
    This is the first treebank in a language from the Arawak family. The
    original interlinear glosses are included in the tree bank, and their
    conversion into a full UD annotation is an ongoing process. The sent_id
    values (e.g.: FernandaM2017:Texto-6-19) are representative of the collector,
    year of publication, text identifier and the number of the sentence in order
    from the original text.

*   **Download size**: `95.51 KiB`

*   **Dataset size**: `98.49 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 115

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-apu_ufpa-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/hbo_ptnk

*   **Config description**: UD Ancient Hebrew PTNK contains portions of the
    Biblia Hebraic Stuttgartensia with morphological annotations from ETCBC.

*   **Download size**: `3.11 MiB`

*   **Dataset size**: `4.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 439
`'test'`  | 410
`'train'` | 730

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-hbo_ptnk-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/ar_nyuad

*   **Config description**: The treebank consists of 19,738 sentences (738889
    tokens), and its domain is mainly newswire. The annotation is licensed under
    the terms of CC BY-SA 4.0, and the original PATB can be obtained from the
    LDC’s official website.

*   **Download size**: `55.87 MiB`

*   **Dataset size**: `78.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,986
`'test'`  | 1,963
`'train'` | 15,789

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-ar_nyuad-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/ar_padt

*   **Config description**: The Arabic-PADT UD treebank is based on the Prague
    Arabic Dependency Treebank (PADT), created at the Charles University in
    Prague.

*   **Download size**: `48.84 MiB`

*   **Dataset size**: `64.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 909
`'test'`  | 680
`'train'` | 6,075

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-ar_padt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/ar_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.98 MiB`

*   **Dataset size**: `2.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-ar_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/aii_as

*   **Config description**: The Uppsala Assyrian Treebank is a small treebank
    for Modern Standard Assyrian. The corpus is collected and annotated
    manually. The data was randomly collected from different textbooks and a
    short translation of The Merchant of Venice.

*   **Download size**: `31.99 KiB`

*   **Dataset size**: `48.85 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 57

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-aii_as-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/bm_crb

*   **Config description**: The UD Bambara treebank is a section of the Corpus
    Référence du Bambara annotated natively with Universal Dependencies.

*   **Download size**: `873.37 KiB`

*   **Dataset size**: `1.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,026

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-bm_crb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/eu_bdt

*   **Config description**: The Basque UD treebank is based on a automatic
    conversion from part of the Basque Dependency Treebank (BDT), created at the
    University of of the Basque Country by the IXA NLP research group. The
    treebank consists of 8.993 sentences (121.443 tokens) and covers mainly
    literary and journalistic texts.

*   **Download size**: `7.83 MiB`

*   **Dataset size**: `11.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,798
`'test'`  | 1,799
`'train'` | 5,396

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-eu_bdt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/bej_nsc

*   **Config description**: A Universal Dependencies corpus for Beja,
    North-Cushitic branch of the Afro-Asiatic phylum mainly spoken in Sudan,
    Egypt and Eritrea.

*   **Download size**: `136.52 KiB`

*   **Dataset size**: `168.15 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 56

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-bej_nsc-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/be_hse

*   **Config description**: The Belarusian UD treebank is based on a sample of
    the news texts included in the Belarusian-Russian parallel subcorpus of the
    Russian National Corpus, online search available at:
    http://ruscorpora.ru/search-para-be.html.

*   **Download size**: `30.04 MiB`

*   **Dataset size**: `39.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,301
`'test'`  | 1,077
`'train'` | 22,853

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-be_hse-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/bn_bru

*   **Config description**: The BRU Bengali treebank has been created at Begum
    Rokeya University, Rangpur, by the members of Semantics Lab.

*   **Download size**: `38.41 KiB`

*   **Dataset size**: `51.42 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 56

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-bn_bru-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/bho_bhtb

*   **Config description**: The Bhojpuri UD Treebank (BHTB) v2.6 consists of
    6,664 tokens(357 sentences). This Treebank is a part of the Universal
    Dependency treebank project. Initially, it was initiated by me (Atul) at
    Jawaharlal Nehru University, New Delhi during the doctoral research work.
    BHTB data contains syntactic annotation according to dependency-constituency
    schema, as well as morphological tags and lemmas. In this data, XPOS is
    annotated according to Bureau of Indian Standards (BIS) Part Of Speech (POS)
    tagset.

*   **Download size**: `599.76 KiB`

*   **Dataset size**: `817.23 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 357

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-bho_bhtb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/br_keb

*   **Config description**: UD Breton-KEB is a treebank of Breton that has been
    manually annotated according to the Universal Dependencies guidelines. The
    tokenisation guidelines and morphological annotation comes from a
    finite-state morphological analyser of Breton released as part of the
    Apertium project.

*   **Download size**: `663.63 KiB`

*   **Dataset size**: `863.36 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 888

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-br_keb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/bg_btb

*   **Config description**: UD_Bulgarian-BTB is based on the HPSG-based
    BulTreeBank, created at the Institute of Information and Communication
    Technologies, Bulgarian Academy of Sciences. The original consists of
    215,000 tokens (over 15,000 sentences).

*   **Download size**: `14.22 MiB`

*   **Dataset size**: `20.01 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,115
`'test'`  | 1,116
`'train'` | 8,907

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-bg_btb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/bxr_bdt

*   **Config description**: The UD Buryat treebank was annotated manually
    natively in UD and contains grammar book sentences, along with news and some
    fiction.

*   **Download size**: `710.23 KiB`

*   **Dataset size**: `1018.12 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 908
`'train'` | 19

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-bxr_bdt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/yue_hk

*   **Config description**: A Cantonese treebank (in Traditional Chinese
    characters) of film subtitles and of legislative proceedings of Hong Kong,
    parallel with the Chinese-HK treebank.

*   **Download size**: `693.38 KiB`

*   **Dataset size**: `1.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,004

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-yue_hk-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/ca_ancora

*   **Config description**: Catalan data from the AnCora corpus.

*   **Download size**: `48.14 MiB`

*   **Dataset size**: `64.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,709
`'test'`  | 1,846
`'train'` | 13,123

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-ca_ancora-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/ceb_gja

*   **Config description**: UD_Cebuano_GJA is a collection of annotated Cebuano
    sample sentences randomly taken from three different sources:
    community-contributed samples from the website Tatoeba, a Cebuano grammar
    book by Bunye & Yap (1971) and Tanangkinsing's reference grammar on Cebuano
    (2011). This project is currently work in progress.

*   **Download size**: `99.30 KiB`

*   **Dataset size**: `136.74 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 188

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-ceb_gja-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/zh_cfl

*   **Config description**: The Chinese-CFL UD treebank is manually annotated by
    Keying Li with minor manual revisions by Herman Leung and John Lee at City
    University of Hong Kong, based on essays written by learners of Mandarin
    Chinese as a foreign language. The data is in Simplified Chinese.

*   **Download size**: `375.71 KiB`

*   **Dataset size**: `558.45 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 451

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-zh_cfl-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/zh_gsd

*   **Config description**: Traditional Chinese Universal Dependencies Treebank
    annotated and converted by Google.

*   **Download size**: `6.48 MiB`

*   **Dataset size**: `8.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 500
`'test'`  | 500
`'train'` | 3,997

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-zh_gsd-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/zh_gsdsimp

*   **Config description**: Simplified Chinese Universal Dependencies dataset
    converted from the GSD (traditional) dataset with manual corrections.

*   **Download size**: `6.48 MiB`

*   **Dataset size**: `8.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 500
`'test'`  | 500
`'train'` | 3,997

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-zh_gsdsimp-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/zh_hk

*   **Config description**: A Traditional Chinese treebank of film subtitles and
    of legislative proceedings of Hong Kong, parallel with the Cantonese-HK
    treebank.

*   **Download size**: `482.85 KiB`

*   **Dataset size**: `779.66 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,004

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-zh_hk-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/zh_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.53 MiB`

*   **Dataset size**: `1.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-zh_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/ckt_hse

*   **Config description**: This data is a manual annotation of the corpus from
    multimedia annotated corpus of the Chuklang project, a dialectal corpus of
    the Amguema variant of Chukchi.

*   **Download size**: `793.16 KiB`

*   **Dataset size**: `828.50 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,004

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-ckt_hse-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/lzh_kyoto

*   **Config description**: Classical Chinese Universal Dependencies Treebank
    annotated and converted by Institute for Research in Humanities, Kyoto
    University.

*   **Download size**: `26.86 MiB`

*   **Dataset size**: `39.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 5,687
`'test'`  | 4,932
`'train'` | 48,569

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-lzh_kyoto-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/cop_scriptorium

*   **Config description**: UD Coptic contains manually annotated Sahidic Coptic
    texts, including Biblical texts, sermons, letters, and hagiography.

*   **Download size**: `4.73 MiB`

*   **Dataset size**: `6.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 381
`'test'`  | 403
`'train'` | 1,227

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-cop_scriptorium-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/hr_set

*   **Config description**: The Croatian UD treebank is based on the extension
    of the SETimes-HR corpus, the hr500k corpus.

*   **Download size**: `14.41 MiB`

*   **Dataset size**: `20.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 960
`'test'`  | 1,136
`'train'` | 6,914

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-hr_set-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/cs_cac

*   **Config description**: The UD_Czech-CAC treebank is based on the Czech
    Academic Corpus 2.0 (CAC; Český akademický korpus; ČAK), created at Charles
    University in Prague.

*   **Download size**: `53.72 MiB`

*   **Dataset size**: `73.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 603
`'test'`  | 628
`'train'` | 23,478

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-cs_cac-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/cs_cltt

*   **Config description**: The UD_Czech-CLTT treebank is based on the Czech
    Legal Text Treebank 1.0, created at Charles University in Prague.

*   **Download size**: `3.57 MiB`

*   **Dataset size**: `4.73 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 129
`'test'`  | 136
`'train'` | 860

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-cs_cltt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/cs_fictree

*   **Config description**: FicTree is a treebank of Czech fiction,
    automatically converted into the UD format. The treebank was built at
    Charles University in Prague.

*   **Download size**: `16.65 MiB`

*   **Dataset size**: `23.29 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,309
`'test'`  | 1,291
`'train'` | 10,160

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-cs_fictree-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/cs_pdt

*   **Config description**: The Czech-PDT UD treebank is based on the Prague
    Dependency Treebank 3.0 (PDT), created at the Charles University in Prague.

*   **Download size**: `164.29 MiB`

*   **Dataset size**: `224.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (dev, test), Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 9,270
`'test'`  | 10,148
`'train'` | 68,495

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-cs_pdt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/cs_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `2.14 MiB`

*   **Dataset size**: `2.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-cs_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/da_ddt

*   **Config description**: The Danish UD treebank is a conversion of the Danish
    Dependency Treebank.

*   **Download size**: `6.13 MiB`

*   **Dataset size**: `9.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 564
`'test'`  | 565
`'train'` | 4,383

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-da_ddt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/nl_alpino

*   **Config description**: This corpus consists of samples from various
    treebanks annotated at the University of Groningen using the Alpino
    annotation tools and guidelines.

*   **Download size**: `15.98 MiB`

*   **Dataset size**: `21.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 718
`'test'`  | 596
`'train'` | 12,289

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-nl_alpino-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/nl_lassysmall

*   **Config description**: This corpus contains sentences from the Wikipedia
    section of the Lassy Small Treebank. Universal Dependency annotation was
    generated automatically from the original annotation in Lassy.

*   **Download size**: `7.61 MiB`

*   **Dataset size**: `9.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 676
`'test'`  | 876
`'train'` | 5,789

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-nl_lassysmall-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_esl

*   **Config description**: UD English-ESL / Treebank of Learner English (TLE)
    contains manual POS tag and dependency annotations for 5,124 English as a
    Second Language (ESL) sentences drawn from the Cambridge Learner Corpus
    First Certificate in English (FCE) dataset.

*   **Download size**: `3.20 MiB`

*   **Dataset size**: `4.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 500
`'test'`  | 500
`'train'` | 4,124

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_esl-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_ewt

*   **Config description**: A Gold Standard Universal Dependencies Corpus for
    English, built over the source material of the English Web Treebank
    LDC2012T13 (https://catalog.ldc.upenn.edu/LDC2012T13).

*   **Download size**: `16.37 MiB`

*   **Dataset size**: `23.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,001
`'test'`  | 2,077
`'train'` | 12,543

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_ewt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_gum

*   **Config description**: Universal Dependencies syntax annotations from the
    GUM corpus (https://corpling.uis.georgetown.edu/gum/).

*   **Download size**: `13.81 MiB`

*   **Dataset size**: `18.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,117
`'test'`  | 1,096
`'train'` | 6,917

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_gum-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_gumreddit

*   **Config description**: Universal Dependencies syntax annotations from the
    Reddit portion of the GUM corpus (https://corpling.uis.georgetown.edu/gum/)

*   **Download size**: `1.47 MiB`

*   **Dataset size**: `2.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 104
`'test'`  | 105
`'train'` | 686

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_gumreddit-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_lines

*   **Config description**: UD English_LinES is the English half of the LinES
    Parallel Treebank with the original dependency annotation first
    automatically converted into Universal Dependencies and then partially
    reviewed. Its contents cover literature, an online manual and Europarl data.

*   **Download size**: `5.27 MiB`

*   **Dataset size**: `7.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,032
`'test'`  | 1,035
`'train'` | 3,176

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_lines-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_atis

*   **Config description**: UD Atis Treebank is a manually annotated treebank
    consisting of the sentences in the Atis (Airline Travel Informations)
    dataset which includes the human speech transcriptions of people asking for
    flight information on the automated inquiry systems.

*   **Download size**: `3.06 MiB`

*   **Dataset size**: `4.76 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 572
`'test'`  | 586
`'train'` | 4,274

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_atis-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_partut

*   **Config description**: UD_English-ParTUT is a conversion of a multilingual
    parallel treebank developed at the University of Turin, and consisting of a
    variety of text genres, including talks, legal texts and Wikipedia articles,
    among others.

*   **Download size**: `2.59 MiB`

*   **Dataset size**: `3.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 156
`'test'`  | 153
`'train'` | 1,781

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_partut-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_pronouns

*   **Config description**: UD English-Pronouns is dataset created to make
    pronoun identification more accurate and with a more balanced distribution
    across genders. The dataset is initially targeting the Independent Genitive
    pronouns, 'hers', (independent) 'his', (singular) 'theirs', 'mine', and
    (singular) 'yours'.

*   **Download size**: `138.08 KiB`

*   **Dataset size**: `186.09 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 285

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_pronouns-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/en_pud

*   **Config description**: This is the English portion of the Parallel
    Universal Dependencies (PUD) treebanks created for the CoNLL 2017 shared
    task on Multilingual Parsing from Raw Text to Universal Dependencies
    (http://universaldependencies.org/conll17/).

*   **Download size**: `1.28 MiB`

*   **Dataset size**: `1.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-en_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/myv_jr

*   **Config description**: UD Erzya is the original annotation (CoNLL-U) for
    texts in the Erzya language, it originally consists of a sample from a
    number of fiction authors writing originals in Erzya.

*   **Download size**: `1.88 MiB`

*   **Dataset size**: `2.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,714

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-myv_jr-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/et_edt

*   **Config description**: UD Estonian is a converted version of the Estonian
    Dependency Treebank (EDT), originally annotated in the Constraint Grammar
    (CG) annotation scheme, and consisting of genres of fiction, newspaper texts
    and scientific texts. The treebank contains 30,972 trees, 437,769 tokens.

*   **Download size**: `31.09 MiB`

*   **Dataset size**: `45.98 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 3,127
`'test'`  | 3,214
`'train'` | 24,632

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-et_edt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/et_ewt

*   **Config description**: UD EWT treebank consists of different genres of new
    media. The treebank contains 4,493 trees, 56,399 tokens.

*   **Download size**: `5.35 MiB`

*   **Dataset size**: `8.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 833
`'test'`  | 913
`'train'` | 4,579

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-et_ewt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fo_farpahc

*   **Config description**: UD_Icelandic-FarPaHC is a conversion of the Faroese
    Parsed Historical Corpus (FarPaHC) to the Universal Dependencies scheme. The
    conversion was done using UDConverter.

*   **Download size**: `2.09 MiB`

*   **Dataset size**: `2.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 300
`'test'`  | 301
`'train'` | 1,020

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fo_farpahc-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fo_oft

*   **Config description**: This is a treebank of Faroese based on the Faroese
    Wikipedia.

*   **Download size**: `783.86 KiB`

*   **Dataset size**: `1.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,208

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fo_oft-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fi_ftb

*   **Config description**: FinnTreeBank 1 consists of manually annotated
    grammatical examples from VISK. The UD version of FinnTreeBank 1 was
    converted from a native annotation model with a script and later manually
    revised.

*   **Download size**: `12.52 MiB`

*   **Dataset size**: `18.45 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,875
`'test'`  | 1,867
`'train'` | 14,981

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fi_ftb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fi_ood

*   **Config description**: Finnish-OOD is an external out-of-domain test set
    for Finnish-TDT annotated natively into UD scheme.

*   **Download size**: `1.40 MiB`

*   **Dataset size**: `2.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,122

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fi_ood-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fi_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.34 MiB`

*   **Dataset size**: `1.80 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fi_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fi_tdt

*   **Config description**: UD_Finnish-TDT is based on the Turku Dependency
    Treebank (TDT), a broad-coverage dependency treebank of general Finnish
    covering numerous genres. The conversion to UD was followed by extensive
    manual checks and corrections, and the treebank closely adheres to the UD
    guidelines.

*   **Download size**: `15.84 MiB`

*   **Dataset size**: `23.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,364
`'test'`  | 1,555
`'train'` | 12,217

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fi_tdt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fr_fqb

*   **Config description**: The corpus **UD_French-FQB** is an automatic
    conversion of the French QuestionBank v1, a corpus entirely made of
    questions.

*   **Download size**: `1.47 MiB`

*   **Dataset size**: `2.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,289

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fr_fqb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fr_ftb

*   **Config description**: The Universal Dependency version of the French
    Treebank (Abeillé et al., 2003), hereafter UD_French-FTB, is a treebank of
    sentences from the newspaper Le Monde, initially manually annotated with
    morphological information and phrase-structure and then converted to the
    Universal Dependencies annotation scheme.

*   **Download size**: `29.49 MiB`

*   **Dataset size**: `44.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,235
`'test'`  | 2,541
`'train'` | 14,759

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fr_ftb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fr_gsd

*   **Config description**: The **UD_French-GSD** was converted in 2015 from the
    content head version of the universal dependency treebank v2.0
    (https://github.com/ryanmcd/uni-dep-tb). It is updated since 2015
    independently from the previous source.

*   **Download size**: `24.38 MiB`

*   **Dataset size**: `35.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,476
`'test'`  | 416
`'train'` | 14,449

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fr_gsd-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fr_partut

*   **Config description**: UD_French-ParTUT is a conversion of a multilingual
    parallel treebank developed at the University of Turin, and consisting of a
    variety of text genres, including talks, legal texts and Wikipedia articles,
    among others.

*   **Download size**: `1.74 MiB`

*   **Dataset size**: `2.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 107
`'test'`  | 110
`'train'` | 803

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fr_partut-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fr_rhapsodie

*   **Config description**: A Universal Dependencies corpus for spoken French.

*   **Download size**: `3.00 MiB`

*   **Dataset size**: `4.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,082
`'test'`  | 840
`'train'` | 1,288

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fr_rhapsodie-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fr_parisstories

*   **Config description**: Paris Stories is a corpus of oral French collected
    and transcribed by Linguistics students from Sorbonne Nouvelle and corrected
    by students from the Plurital Master's Degree of Computational Linguistics (
    Inalco, Paris Nanterre, Sorbonne Nouvelle) between 2017 and 2021. It
    contains monologues and dialogues from speakers living in the Parisian
    region.

*   **Download size**: `1.97 MiB`

*   **Dataset size**: `2.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 547
`'train'` | 1,216

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fr_parisstories-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fr_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.71 MiB`

*   **Dataset size**: `2.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fr_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/fr_sequoia

*   **Config description**: UD_French-Sequoia is an automatic conversion of the
    Sequoia Treebank corpus French Sequoia corpus.

*   **Download size**: `4.21 MiB`

*   **Dataset size**: `6.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 412
`'test'`  | 456
`'train'` | 2,231

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-fr_sequoia-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/gl_ctg

*   **Config description**: The Galician UD treebank is based on the automatic
    parsing of the Galician Technical Corpus (http://sli.uvigo.gal/CTG) created
    at the University of Vigo by the the TALG NLP research group.

*   **Download size**: `7.85 MiB`

*   **Dataset size**: `10.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 860
`'test'`  | 861
`'train'` | 2,272

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-gl_ctg-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/gl_treegal

*   **Config description**: The Galician-TreeGal is a treebank for Galician
    developed at LyS Group (Universidade da Coruña).

*   **Download size**: `1.66 MiB`

*   **Dataset size**: `2.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 400
`'train'` | 600

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-gl_treegal-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/de_gsd

*   **Config description**: The German UD is converted from the content head
    version of the universal dependency treebank v2.0 (legacy).

*   **Download size**: `20.69 MiB`

*   **Dataset size**: `29.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 799
`'test'`  | 977
`'train'` | 13,814

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-de_gsd-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/de_hdt

*   **Config description**: UD German-HDT is a conversion of the Hamburg
    Dependency Treebank, created at the University of Hamburg through manual
    annotation in conjunction with a standard for morphologically and
    syntactically annotating sentences as well as a constraint-based parser.

*   **Download size**: `242.97 MiB`

*   **Dataset size**: `347.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 18,434
`'test'`  | 18,459
`'train'` | 153,035

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-de_hdt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/de_lit

*   **Config description**: This treebank aims at gathering texts of the German
    literary history. Currently, it hosts Fragments of the early Romanticism,
    i.e. aphorism-like texts mainly dealing with philosophical issues concerning
    art, beauty and related topics.

*   **Download size**: `1.97 MiB`

*   **Dataset size**: `2.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,922

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-de_lit-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/de_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.65 MiB`

*   **Dataset size**: `2.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-de_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/got_proiel

*   **Config description**: The UD Gothic treebank is based on the Gothic data
    from the PROIEL treebank, and consists of Wulfila's Bible translation.

*   **Download size**: `4.98 MiB`

*   **Dataset size**: `7.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 985
`'test'`  | 1,029
`'train'` | 3,387

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-got_proiel-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/el_gdt

*   **Config description**: The Greek UD treebank (UD_Greek-GDT) is derived from
    the Greek Dependency Treebank (http://gdt.ilsp.gr), a resource developed and
    maintained by researchers at the Institute for Language and Speech
    Processing/Athena R.C. (http://www.ilsp.gr).

*   **Download size**: `5.52 MiB`

*   **Dataset size**: `7.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 403
`'test'`  | 456
`'train'` | 1,662

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-el_gdt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/gub_tudet

*   **Config description**: UD_Guajajara-TuDeT is a collection of annotated
    sentences in Guajajara. Sentences stem from multiple sources such as
    descriptions of the language, short stories, dictionaries and translations
    from the New Testament. Sentence annotation and documentation by Lorena
    Martín Rodríguez and Fabrício Ferraz Gerardi.

*   **Download size**: `683.38 KiB`

*   **Dataset size**: `738.09 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,126

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-gub_tudet-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/gn_oldtudet

*   **Config description**: UD_Guarani-OldTuDeT is a collection of annotated
    texts in Old Guaraní. All known sources in this language are being
    annotated: cathesisms, grammars (seventeenth and eighteenth century),
    sentences from dictionaries, and other texts. Sentence annotation and
    documentation by Fabrício Ferraz Gerardi and Lorena Martín Rodríguez.

*   **Download size**: `18.93 KiB`

*   **Dataset size**: `24.71 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 59

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-gn_oldtudet-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/he_htb

*   **Config description**: A Universal Dependencies Corpus for Hebrew.

*   **Download size**: `11.64 MiB`

*   **Dataset size**: `16.10 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 484
`'test'`  | 491
`'train'` | 5,241

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-he_htb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/he_iahltwiki

*   **Config description**: Publicly available subset of the IAHLT UD Hebrew
    Treebank's Wikipedia section (https://www.iahlt.org/)

*   **Download size**: `10.30 MiB`

*   **Dataset size**: `14.16 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 348
`'test'`  | 393
`'train'` | 4,298

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-he_iahltwiki-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/qfn_fame

*   **Config description**: UD_Frisian_Dutch-Fame is a selection of 400
    sentences from the FAME! speech corpus by Yilmaz et al. (2016a, 2016b). The
    treebank is manually annotated using the UD scheme.

*   **Download size**: `232.57 KiB`

*   **Dataset size**: `290.88 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 400

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-qfn_fame-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/qhe_hiencs

*   **Config description**: The Hindi-English Code-switching treebank is based
    on code-switching tweets of Hindi and English multilingual speakers (mostly
    Indian) on Twitter. The treebank is manually annotated using UD sceheme. The
    training and evaluations sets were seperately annotated by different
    annotators using UD v2 and v1 guidelines respectively. The evaluation sets
    are automatically converted from UD v1 to v2.

*   **Download size**: `893.15 KiB`

*   **Dataset size**: `1.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 225
`'test'`  | 225
`'train'` | 1,448

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-qhe_hiencs-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/hi_hdtb

*   **Config description**: The Hindi UD treebank is based on the Hindi
    Dependency Treebank (HDTB), created at IIIT Hyderabad, India.

*   **Download size**: `49.18 MiB`

*   **Dataset size**: `68.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,659
`'test'`  | 1,684
`'train'` | 13,304

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-hi_hdtb-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/hi_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `2.20 MiB`

*   **Dataset size**: `2.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-hi_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/hu_szeged

*   **Config description**: The Hungarian UD treebank is derived from the Szeged
    Dependency Treebank (Vincze et al. 2010).

*   **Download size**: `2.92 MiB`

*   **Dataset size**: `4.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 441
`'test'`  | 449
`'train'` | 910

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-hu_szeged-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/is_modern

*   **Config description**: UD_Icelandic-Modern is a conversion of the modern
    additions to the Icelandic Parsed Historical Corpus (IcePaHC) to the
    Universal Dependencies scheme.

*   **Download size**: `9.02 MiB`

*   **Dataset size**: `12.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 784
`'test'`  | 768
`'train'` | 5,376

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-is_modern-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/is_icepahc

*   **Config description**: UD_Icelandic-IcePaHC is a conversion of the
    Icelandic Parsed Historical Corpus (IcePaHC) to the Universal Dependencies
    scheme. The conversion was done using UDConverter.

*   **Download size**: `81.16 MiB`

*   **Dataset size**: `112.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 4,865
`'test'`  | 5,157
`'train'` | 34,007

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-is_icepahc-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/is_pud

*   **Config description**: Icelandic-PUD is the Icelandic part of the Parallel
    Universal Dependencies (PUD) treebanks.

*   **Download size**: `1.45 MiB`

*   **Dataset size**: `1.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-is_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/id_csui

*   **Config description**: UD Indonesian-CSUI is a conversion from an
    Indonesian constituency treebank in the Penn Treebank format named Kethu
    that was also a conversion from a constituency treebank built by
    Dinakaramani et al. (2015). We named this treebank Indonesian-CSUI, since
    all the three versions of the treebanks were built at Faculty of Computer
    Science, Universitas Indonesia.

*   **Download size**: `1.62 MiB`

*   **Dataset size**: `1.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 374
`'train'` | 656

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-id_csui-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/id_gsd

*   **Config description**: The Indonesian UD is converted from the content head
    version of the universal dependency treebank v2.0 (legacy).

*   **Download size**: `9.15 MiB`

*   **Dataset size**: `11.25 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 559
`'test'`  | 557
`'train'` | 4,482

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-id_gsd-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/id_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.10 MiB`

*   **Dataset size**: `1.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-id_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/ga_idt

*   **Config description**: A Universal Dependencies 4910-sentence treebank for
    modern Irish.

*   **Download size**: `7.62 MiB`

*   **Dataset size**: `10.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 451
`'test'`  | 454
`'train'` | 4,005

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-ga_idt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/ga_twittirish

*   **Config description**: A Universal Dependencies treebank of 866 tweets in
    modern Irish.

*   **Download size**: `782.30 KiB`

*   **Dataset size**: `1.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 866

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-ga_twittirish-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/it_isdt

*   **Config description**: The Italian corpus annotated according to the UD
    annotation scheme was obtained by conversion from ISDT (Italian Stanford
    Dependency Treebank), released for the dependency parsing shared task of
    Evalita-2014 (Bosco et al. 2014).

*   **Download size**: `20.03 MiB`

*   **Dataset size**: `29.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 564
`'test'`  | 482
`'train'` | 13,121

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-it_isdt-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/it_partut

*   **Config description**: UD_Italian-ParTUT is a conversion of a multilingual
    parallel treebank developed at the University of Turin, and consisting of a
    variety of text genres, including talks, legal texts and Wikipedia articles,
    among others.

*   **Download size**: `3.42 MiB`

*   **Dataset size**: `4.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 156
`'test'`  | 153
`'train'` | 1,781

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-it_partut-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/it_postwita

*   **Config description**: PoSTWITA-UD is a collection of Italian tweets
    annotated in Universal Dependencies that can be exploited for the training
    of NLP systems to enhance their performance on social media texts.

*   **Download size**: `7.27 MiB`

*   **Dataset size**: `10.47 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 670
`'test'`  | 674
`'train'` | 5,368

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-it_postwita-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/it_markit

*   **Config description**: It is MarkIT That is New: An Italian Treebank of
    Marked Constructions. Teresa Paccosi, Alessio Palmero Aprosio and Sara
    Tonelli, To appear in Proceedings of the Eighth Italian Conference on
    Computational Linguistics 2022 (CLIC-it 2021)

*   **Download size**: `2.48 MiB`

*   **Dataset size**: `3.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 341
`'test'`  | 341
`'train'` | 613

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-it_markit-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/it_valico

*   **Config description**: Manually corrected Treebank of Learner Italian drawn
    from the Valico corpus and correspondent corrected sentences.

*   **Download size**: `520.45 KiB`

*   **Dataset size**: `657.38 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 398

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-it_valico-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/it_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.56 MiB`

*   **Dataset size**: `2.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/universal_dependencies-it_pud-1.0.1.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## universal_dependencies/it_twittiro

*   **Config description**: TWITTIRÒ-UD is a collection of ironic Italian tweets
    annotated in Universal Dependencies. The treebank can be exploited for the
    training of NLP systems to enhance their performance on social media texts,
    and in particular, for irony detection purposes.

*   **Download size**: `1.81 MiB`

*   **Dataset size**: `2.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 144
`'test'`  | 142
`'train'` | 1,138

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/it_vit

*   **Config description**: The UD_Italian-VIT corpus was obtained by conversion
    from VIT (Venice Italian Treebank), developed at the Laboratory of
    Computational Linguistics of the Università Ca' Foscari in Venice (Delmonte
    et al. 2007; Delmonte 2009;
    http://rondelmo.it/resource/VIT/Browser-VIT/index.htm).

*   **Download size**: `16.77 MiB`

*   **Dataset size**: `23.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 743
`'test'`  | 1,067
`'train'` | 8,277

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ja_pudluw

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `4.37 MiB`

*   **Dataset size**: `5.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ja_bccwjluw

*   **Config description**: This Universal Dependencies (UD) Japanese treebank
    is based on the definition of UD Japanese convention described in the UD
    documentation. The original sentences are from `Balanced Corpus of
    Contemporary Written Japanese'(BCCWJ).

*   **Download size**: `59.20 MiB`

*   **Dataset size**: `100.36 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 8,427
`'test'`  | 7,881
`'train'` | 40,801

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ja_gsdluw

*   **Config description**: This Universal Dependencies (UD) Japanese treebank
    is based on the definition of UD Japanese convention described in the UD
    documentation. The original sentences are from Google UDT 2.0.

*   **Download size**: `28.31 MiB`

*   **Dataset size**: `33.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 507
`'test'`  | 543
`'train'` | 7,050

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ja_bccwj

*   **Config description**: This Universal Dependencies (UD) Japanese treebank
    is based on the definition of UD Japanese convention described in the UD
    documentation. The original sentences are from `Balanced Corpus of
    Contemporary Written Japanese'(BCCWJ).

*   **Download size**: `93.05 MiB`

*   **Dataset size**: `157.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 8,427
`'test'`  | 7,881
`'train'` | 40,801

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ja_gsd

*   **Config description**: This Universal Dependencies (UD) Japanese treebank
    is based on the definition of UD Japanese convention described in the UD
    documentation. The original sentences are from Google UDT 2.0.

*   **Download size**: `43.21 MiB`

*   **Dataset size**: `52.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 507
`'test'`  | 543
`'train'` | 7,050

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ja_modern

*   **Config description**: This Universal Dependencies (UD) Japanese treebank
    is based on the definition of UD Japanese convention described in the UD
    documentation. The original sentences are from `Corpus of Historical
    Japanese' (CHJ).

*   **Download size**: `2.06 MiB`

*   **Dataset size**: `2.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 822

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ja_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the [CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal
    Dependencies](http://universaldependencies.org/conll17/).

*   **Download size**: `6.48 MiB`

*   **Dataset size**: `7.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/jv_csui

*   **Config description**: UD Javanese-CSUI is a dependency treebank in
    Javanese, a regional language in Indonesia with more than 60 million users.
    The original sentences were taken from OPUS, especially from the WikiMatrix
    v1 corpus. We revised the sentences that contained more Indonesian words
    than Javanese words and manually annotated them.

*   **Download size**: `141.40 KiB`

*   **Dataset size**: `171.69 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 125

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/urb_tudet

*   **Config description**: UD_Kaapor-TuDeT is a collection of annotated
    sentences in Ka'apor. The project is a work in progress and the treebank is
    being updated on a regular basis.

*   **Download size**: `24.74 KiB`

*   **Dataset size**: `33.60 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 83

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/xnr_kdtb

*   **Config description**: The Kangri UD Treebank (KDTB) is a part of the
    Universal Dependency treebank project.

*   **Download size**: `132.92 KiB`

*   **Dataset size**: `196.42 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 288

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/krl_kkpp

*   **Config description**: UD Karelian-KKPP is a manually annotated new corpus
    of Karelian made in Universal dependencies annotation scheme. The data is
    collected from VepKar corpora and consists of mostly modern news texts but
    also some stories and educational texts.

*   **Download size**: `220.80 KiB`

*   **Dataset size**: `317.02 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 228

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/kk_ktb

*   **Config description**: The UD Kazakh treebank is a combination of text from
    various sources including Wikipedia, some folk tales, sentences from the
    UDHR, news and phrasebook sentences. Sentences IDs include partial document
    identifiers.

*   **Download size**: `833.88 KiB`

*   **Dataset size**: `1.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 1,047
`'train'` | 31

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/arr_tudet

*   **Config description**: UD_Karo-TuDeT is a collection of annotated sentences
    in Karo. The sentences stem from the only grammatical description of the
    language (Gabas, 1999) and from the sentences in the dictionary by the same
    author (Gabas, 2007). Sentence annotation and documentation by Fabrício
    Ferraz Gerardi.

*   **Download size**: `174.70 KiB`

*   **Dataset size**: `259.24 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 674

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/kfm_aha

*   **Config description**: The AHA Khunsari Treebank is a small treebank for
    contemporary Khunsari. Its corpus is collected and annotated manually. We
    have prepared this treebank based on interviews with Khunsari speakers.

*   **Download size**: `6.14 KiB`

*   **Dataset size**: `7.56 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 10

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/quc_iu

*   **Config description**: UD Kʼicheʼ-IU is a treebank consisting of sentences
    from a variety of text domains but principally dictionary example sentences
    and linguistic examples.

*   **Download size**: `823.85 KiB`

*   **Dataset size**: `1.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,435

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/koi_uh

*   **Config description**: This is a Komi-Permyak literary language treebank
    consisting of original and translated texts.

*   **Download size**: `99.43 KiB`

*   **Dataset size**: `118.77 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 100

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/kpv_ikdp

*   **Config description**: This treebank consists of dialectal transcriptions
    of spoken Komi-Zyrian. The current texts are short recorded segments from
    different areas where the Iźva dialect of Komi language is spoken.

*   **Download size**: `202.88 KiB`

*   **Dataset size**: `273.92 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 214

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/kpv_lattice

*   **Config description**: UD Komi-Zyrian Lattice is a treebank of written
    standard Komi-Zyrian.

*   **Download size**: `741.82 KiB`

*   **Dataset size**: `989.46 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 663

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ko_gsd

*   **Config description**: The Google Korean Universal Dependency Treebank is
    first converted from the Universal Dependency Treebank v2.0 (legacy), and
    then enhanced by Chun et al., 2018.

*   **Download size**: `4.66 MiB`

*   **Dataset size**: `6.31 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 950
`'test'`  | 989
`'train'` | 4,400

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ko_kaist

*   **Config description**: The KAIST Korean Universal Dependency Treebank is
    generated by Chun et al., 2018 from the constituency trees in the KAIST
    Tree-Tagging Corpus.

*   **Download size**: `20.84 MiB`

*   **Dataset size**: `27.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,066
`'test'`  | 2,287
`'train'` | 23,010

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ko_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.92 MiB`

*   **Dataset size**: `2.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/kmr_mg

*   **Config description**: The UD Kurmanji corpus is a corpus of Kurmanji
    Kurdish. It contains fiction and encyclopaedic texts in roughly equal
    measure. It has been annotated natively in accordance with the UD annotation
    scheme.

*   **Download size**: `747.04 KiB`

*   **Dataset size**: `1.07 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 734
`'train'` | 20

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/la_ittb

*   **Config description**: Latin data from the *Index Thomisticus* Treebank.
    Data are taken from the *Index Thomisticus* corpus by Roberto Busa SJ, which
    contains the complete work by Thomas Aquinas (1225–1274; Medieval Latin) and
    by 61 other authors related to Thomas.

*   **Download size**: `40.75 MiB`

*   **Dataset size**: `55.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,101
`'test'`  | 2,101
`'train'` | 22,775

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/la_udante

*   **Config description**: The UDante treebank is based on the Latin texts of
    Dante Alighieri, taken from the DanteSearch corpus, originally created at
    the University of Pisa, Italy. It is a treebank of Latin language, more
    precisely of literary Medieval Latin (XIVth century).

*   **Download size**: `4.87 MiB`

*   **Dataset size**: `6.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 376
`'test'`  | 419
`'train'` | 926

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/la_llct

*   **Config description**: This Universal Dependencies version of the LLCT
    (Late Latin Charter Treebank) consists of an automated conversion of the
    LLCT2 treebank from the Latin Dependency Treebank (LDT) format into the
    Universal Dependencies standard.

*   **Download size**: `20.99 MiB`

*   **Dataset size**: `27.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 850
`'test'`  | 884
`'train'` | 7,289

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/la_perseus

*   **Config description**: This Universal Dependencies Latin Treebank consists
    of an automatic conversion of a selection of passages from the Ancient Greek
    and Latin Dependency Treebank 2.1

*   **Download size**: `2.45 MiB`

*   **Dataset size**: `3.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 939
`'train'` | 1,334

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/la_proiel

*   **Config description**: The Latin PROIEL treebank is based on the Latin data
    from the PROIEL treebank, and contains most of the Vulgate New Testament
    translations plus selections from Caesar's Gallic War, Cicero's Letters to
    Atticus, Palladius' Opus Agriculturae and the first book of Cicero's De
    officiis.

*   **Download size**: `17.58 MiB`

*   **Dataset size**: `25.21 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,234
`'test'`  | 1,260
`'train'` | 15,917

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/lv_lvtb

*   **Config description**: Latvian UD Treebank is based on Latvian Treebank
    (LVTB), being created at University of Latvia, Institute of Mathematics and
    Computer Science, Artificial Intelligence Laboratory.

*   **Download size**: `30.93 MiB`

*   **Dataset size**: `42.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,957
`'test'`  | 2,325
`'train'` | 12,521

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/lij_glt

*   **Config description**: The Genoese Ligurian Treebank is a small, manually
    annotated collection of contemporary Ligurian prose. The focus of the
    treebank is written Genoese, the koiné variety of Ligurian which is
    associated with today's literary, journalistic and academic ligurophone
    sphere.

*   **Download size**: `426.33 KiB`

*   **Dataset size**: `636.88 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 296
`'train'` | 20

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/lt_alksnis

*   **Config description**: The Lithuanian dependency treebank ALKSNIS v3.0
    (Vytautas Magnus University).

*   **Download size**: `6.68 MiB`

*   **Dataset size**: `9.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 617
`'test'`  | 684
`'train'` | 2,341

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/lt_hse

*   **Config description**: Lithuanian treebank annotated manually
    (dependencies) using the Morphological Annotator by CCL, Vytautas Magnus
    University (http://tekstynas.vdu.lt/) and manual disambiguation. A pilot
    version which includes news and an essay by Tomas Venclova is available
    here.

*   **Download size**: `255.28 KiB`

*   **Dataset size**: `1.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 153
`'test'`  | 153
`'train'` | 153

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/olo_kkpp

*   **Config description**: UD Livvi-KKPP is a manually annotated new corpus of
    Livvi-Karelian made directly in the Universal dependencies annotation
    scheme. The data is collected from VepKar corpora and consists of mostly
    modern news texts but also some stories and educational texts.

*   **Download size**: `119.00 KiB`

*   **Dataset size**: `165.75 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 106
`'train'` | 19

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/nds_lsdc

*   **Config description**: The UD Low Saxon LSDC dataset consists of sentences
    in 18 Low Saxon dialects from both Germany and the Netherlands. These
    sentences are (or are to become) part of the LSDC dataset and represent the
    language from the 19th and early 20th century in genres such as short
    stories, novels, speeches, letters and fairytales.

*   **Download size**: `209.01 KiB`

*   **Dataset size**: `280.72 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 83

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/mt_mudt

*   **Config description**: MUDT (Maltese Universal Dependencies Treebank) is a
    manually annotated treebank of Maltese, a Semitic language of Malta
    descended from North African Arabic with a significant amount of
    Italo-Romance influence. MUDT was designed as a balanced corpus with four
    major genres (see Splitting below) represented roughly equally.

*   **Download size**: `1.92 MiB`

*   **Dataset size**: `2.67 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 433
`'test'`  | 518
`'train'` | 1,123

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/gv_cadhan

*   **Config description**: This is the Cadhan Aonair UD treebank for Manx
    Gaelic, created by Kevin Scannell.

*   **Download size**: `1.26 MiB`

*   **Dataset size**: `1.79 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,319

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/mr_ufal

*   **Config description**: UD Marathi is a manually annotated treebank
    consisting primarily of stories from Wikisource, and parts of an article on
    Wikipedia.

*   **Download size**: `330.87 KiB`

*   **Dataset size**: `496.00 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 46
`'test'`  | 47
`'train'` | 373

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/gun_dooley

*   **Config description**: UD Mbya_Guarani-Dooley is a corpus of narratives
    written in Mbyá Guaraní (Tupian) in Brazil, and collected by Robert Dooley.
    Due to copyright restrictions, the corpus that is distributed as part of UD
    only contains the annotation (tags, features, relations) while the FORM and
    LEMMA columns are empty.

*   **Download size**: `560.08 KiB`

*   **Dataset size**: `859.37 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,046

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/gun_thomas

*   **Config description**: UD Mbya_Guarani-Thomas is a corpus of Mbyá Guaraní
    (Tupian) texts collected by Guillaume Thomas. The current version of the
    corpus consists of three speeches by Paulina Kerechu Núñez Romero, a Mbyá
    Guaraní speaker from Ytu, Caazapá Department, Paraguay.

*   **Download size**: `90.88 KiB`

*   **Dataset size**: `120.86 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 98

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/mdf_jr

*   **Config description**: Erme Universal Dependencies annotated texts Moksha
    are the origin of UD_Moksha-JR with annotation (CoNLL-U) for texts in the
    Moksha language, it originally consists of a sample from a number of fiction
    authors writing originals in Moksha.

*   **Download size**: `343.96 KiB`

*   **Dataset size**: `451.57 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 342

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/myu_tudet

*   **Config description**: UD_Munduruku-TuDeT is a collection of annotated
    sentences in Mundurukú. Together with UD_Akuntsu-TuDeT and
    UD_Tupinamba-TuDeT, UD_Munduruku-TuDeT is part of the TuLaR project.

*   **Download size**: `67.85 KiB`

*   **Dataset size**: `83.48 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 158

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/pcm_nsc

*   **Config description**: A Universal Dependencies corpus for spoken Naija
    (Nigerian Pidgin).

*   **Download size**: `16.99 MiB`

*   **Dataset size**: `21.58 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 991
`'test'`  | 972
`'train'` | 7,278

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/nyq_aha

*   **Config description**: The AHA Nayini Treebank is a small treebank for
    contemporary Nayini. Its corpus is collected and annotated manually. We have
    prepared this treebank based on interviews with Nayini speakers.

*   **Download size**: `6.24 KiB`

*   **Dataset size**: `7.72 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 10

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sme_giella

*   **Config description**: This is a North Sámi treebank based on a manually
    disambiguated and function-labelled gold-standard corpus of North Sámi
    produced by the Giellatekno team at UiT Norgga árktalaš universitehta.

*   **Download size**: `1.78 MiB`

*   **Dataset size**: `2.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 865
`'train'` | 2,257

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/no_bokmaal

*   **Config description**: The Norwegian UD treebank is based on the Bokmål
    section of the Norwegian Dependency Treebank (NDT), which is a syntactic
    treebank of Norwegian. NDT has been automatically converted to the UD scheme
    by Lilja Øvrelid at the University of Oslo.

*   **Download size**: `18.29 MiB`

*   **Dataset size**: `27.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,409
`'test'`  | 1,939
`'train'` | 15,696

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/no_nynorsk

*   **Config description**: The Norwegian UD treebank is based on the Nynorsk
    section of the Norwegian Dependency Treebank (NDT), which is a syntactic
    treebank of Norwegian. NDT has been automatically converted to the UD scheme
    by Lilja Øvrelid at the University of Oslo.

*   **Download size**: `17.68 MiB`

*   **Dataset size**: `26.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,890
`'test'`  | 1,511
`'train'` | 14,174

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/no_nynorsklia

*   **Config description**: This Norwegian treebank is based on the LIA treebank
    of transcribed spoken Norwegian dialects. The treebank has been
    automatically converted to the UD scheme by Lilja Øvrelid at the University
    of Oslo.

*   **Download size**: `3.19 MiB`

*   **Dataset size**: `4.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 881
`'test'`  | 957
`'train'` | 3,412

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/cu_proiel

*   **Config description**: The Old Church Slavonic (OCS) UD treebank is based
    on the Old Church Slavonic data from the PROIEL treebank and contains the
    text of the Codex Marianus New Testament translation.

*   **Download size**: `5.92 MiB`

*   **Dataset size**: `8.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,073
`'test'`  | 1,141
`'train'` | 4,124

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/fro_srcmf

*   **Config description**: UD_Old_French-SRCMF is a conversion of (part of) the
    SRCMF corpus (Syntactic Reference Corpus of Medieval French srcmf.org).

*   **Download size**: `13.51 MiB`

*   **Dataset size**: `18.54 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,887
`'test'`  | 1,989
`'train'` | 14,153

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/orv_birchbark

*   **Config description**: UD Old_East_Slavic-Birchbark is based on the RNC
    Corpus of Birchbark Letters and includes documents written in 1025-1500 in
    an East Slavic vernacular (letters, household and business records, records
    for church services, spell against diseases, and other short inscriptions).
    The treebank is manually syntactically annotated in the UD 2.0 scheme,
    morphological and lexical annotation is a conversion of the original RNC
    annotation.

*   **Download size**: `4.04 MiB`

*   **Dataset size**: `4.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,054
`'test'`  | 1,006
`'train'` | 1,045

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/orv_rnc

*   **Config description**: `UD_Old_Russian-RNC` is a sample of the Middle
    Russian corpus (1300-1700), a part of the Russian National Corpus. The data
    were originally annotated according to the RNC and extended UD-Russian
    morphological schemas and UD 2.4 dependency schema.

*   **Download size**: `2.95 MiB`

*   **Dataset size**: `4.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 648
`'train'` | 422

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/orv_torot

*   **Config description**: UD_Old_Russian-TOROT is a conversion of a selection
    of the Old East Slavonic and Middle Russian data in the Tromsø Old Russian
    and OCS Treebank (TOROT), which was originally annotated in PROIEL
    dependency format.

*   **Download size**: `14.49 MiB`

*   **Dataset size**: `20.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,852
`'test'`  | 1,756
`'train'` | 13,336

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/otk_tonqq

*   **Config description**: `UD_Old_Turkish-Tonqq` is an Old Turkish treebank
    built upon Turkic script texts or sentences that are trivially convertible.

*   **Download size**: `10.44 KiB`

*   **Dataset size**: `14.01 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 20

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/fa_perdt

*   **Config description**: The Persian Universal Dependency Treebank (PerUDT)
    is the result of automatic coversion of Persian Dependency Treebank (PerDT)
    with extensive manual corrections. Please refer to the follwoing work, if
    you use this data: Mohammad Sadegh Rasooli, Pegah Safari, Amirsaeid Moloodi,
    and Alireza Nourian. 'The Persian Dependency Treebank Made Universal'. 2020
    (to appear).

*   **Download size**: `32.05 MiB`

*   **Dataset size**: `43.48 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,456
`'test'`  | 1,455
`'train'` | 26,196

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/fa_seraji

*   **Config description**: The Persian Universal Dependency Treebank (Persian
    UD) is based on Uppsala Persian Dependency Treebank (UPDT). The conversion
    of the UPDT to the Universal Dependencies was performed semi-automatically
    with extensive manual checks and corrections.

*   **Download size**: `9.43 MiB`

*   **Dataset size**: `12.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 599
`'test'`  | 600
`'train'` | 4,798

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/pl_lfg

*   **Config description**: The LFG Enhanced UD treebank of Polish is based on a
    corpus of LFG (Lexical Functional Grammar) syntactic structures generated by
    an LFG grammar of Polish, POLFIE, and manually disambiguated by human
    annotators.

*   **Download size**: `14.18 MiB`

*   **Dataset size**: `18.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,745
`'test'`  | 1,727
`'train'` | 13,774

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/pl_pdb

*   **Config description**: The Polish PDB-UD treebank is based on the Polish
    Dependency Bank 2.0 (PDB 2.0), created at the Institute of Computer Science,
    Polish Academy of Sciences in Warsaw. The PDB-UD treebank is an extended and
    corrected version of the Polish SZ-UD treebank (the release 1.2 to 2.3).

*   **Download size**: `34.66 MiB`

*   **Dataset size**: `47.62 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,215
`'test'`  | 2,215
`'train'` | 17,722

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/pl_pud

*   **Config description**: This is the Polish portion of the Parallel Universal
    Dependencies (PUD) treebanks, created at the Institute of Computer Science,
    Polish Academy of Sciences in Warsaw.Re

*   **Download size**: `1.91 MiB`

*   **Dataset size**: `2.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/pt_bosque

*   **Config description**: This Universal Dependencies (UD) Portuguese treebank
    is based on the Constraint Grammar converted version of the Bosque, which is
    part of the Floresta Sintá(c)tica treebank. It contains both European
    (CETEMPúblico) and Brazilian (CETENFolha) variants.

*   **Download size**: `14.29 MiB`

*   **Dataset size**: `20.41 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,172
`'test'`  | 1,167
`'train'` | 7,018

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/pt_gsd

*   **Config description**: The Brazilian Portuguese UD is converted from the
    Google Universal Dependency Treebank v2.0 (legacy).

*   **Download size**: `14.57 MiB`

*   **Dataset size**: `20.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,204
`'test'`  | 1,200
`'train'` | 9,615

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/pt_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.48 MiB`

*   **Dataset size**: `1.95 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ro_art

*   **Config description**: The UD treebank ArT is a treebank of the Aromanian
    dialect of the Romanian language in UD format.

*   **Download size**: `44.38 KiB`

*   **Dataset size**: `65.95 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 50

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ro_nonstandard

*   **Config description**: The Romanian Non-standard UD treebank (called
    UAIC-RoDia) is based on UAIC-RoDia Treebank. UAIC-RoDia = ISLRN
    156-635-615-024-0

*   **Download size**: `48.00 MiB`

*   **Dataset size**: `66.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,052
`'test'`  | 1,052
`'train'` | 24,121

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ro_rrt

*   **Config description**: The Romanian UD treebank (called RoRefTrees) (Barbu
    Mititelu et al., 2016) is the reference treebank in UD format for standard
    Romanian.

*   **Download size**: `16.38 MiB`

*   **Dataset size**: `22.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 752
`'test'`  | 729
`'train'` | 8,043

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ro_simonero

*   **Config description**: SiMoNERo is a medical corpus of contemporary
    Romanian.

*   **Download size**: `11.36 MiB`

*   **Dataset size**: `15.68 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 443
`'test'`  | 491
`'train'` | 3,747

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ru_gsd

*   **Config description**: Russian Universal Dependencies Treebank annotated
    and converted by Google.

*   **Download size**: `8.42 MiB`

*   **Dataset size**: `11.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 579
`'test'`  | 601
`'train'` | 3,850

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ru_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.78 MiB`

*   **Dataset size**: `2.26 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ru_syntagrus

*   **Config description**: Russian data from the SynTagRus corpus.

*   **Download size**: `97.99 MiB`

*   **Dataset size**: `139.66 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 6,584
`'test'`  | 6,491
`'train'` | 48,814

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ru_taiga

*   **Config description**: Universal Dependencies treebank is based on data
    samples extracted from Taiga Corpus and MorphoRuEval-2017 and GramEval-2020
    shared tasks collections.

*   **Download size**: `18.12 MiB`

*   **Dataset size**: `24.32 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 946
`'test'`  | 881
`'train'` | 16,045

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sa_ufal

*   **Config description**: A small Sanskrit treebank of sentences from
    Pañcatantra, an ancient Indian collection of interrelated fables by Vishnu
    Sharma.

*   **Download size**: `414.72 KiB`

*   **Dataset size**: `407.83 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 230

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sa_vedic

*   **Config description**: The Treebank of Vedic Sanskrit contains 4,000
    sentences with 27,000 words chosen from metrical and prose passages of the
    Ṛgveda (RV), the Śaunaka recension of the Atharvaveda (ŚS), the
    Maitrāyaṇīsaṃhitā (MS), and the Aitareya- (AB) and Śatapatha-Brāhmaṇas (ŚB).
    Lexical and morpho-syntactic information has been generated using a tagging
    software and manually validated. POS tags have been induced automatically
    from the morpho-sytactic information of each word.

*   **Download size**: `1.95 MiB`

*   **Dataset size**: `3.14 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 1,473
`'train'` | 2,524

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/gd_arcosg

*   **Config description**: A treebank of Scottish Gaelic based on the Annotated
    Reference Corpus Of Scottish Gaelic (ARCOSG).

*   **Download size**: `5.07 MiB`

*   **Dataset size**: `7.20 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 655
`'test'`  | 545
`'train'` | 3,539

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sr_set

*   **Config description**: The Serbian UD treebank is based on the
    [SETimes-SR](http://hdl.handle.net/11356/1200) corpus and additional news
    documents from the Serbian web.

*   **Download size**: `7.07 MiB`

*   **Dataset size**: `10.04 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 536
`'test'`  | 520
`'train'` | 3,328

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sms_giellagas

*   **Config description**: The UD Skolt Sami Giellagas treebank is based almost
    entirely on spoken Skolt Sami corpora.

*   **Download size**: `216.27 KiB`

*   **Dataset size**: `299.21 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 218

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sk_snk

*   **Config description**: The Slovak UD treebank is based on data originally
    annotated as part of the Slovak National Corpus, following the annotation
    style of the Prague Dependency Treebank.

*   **Download size**: `9.55 MiB`

*   **Dataset size**: `13.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,060
`'test'`  | 1,061
`'train'` | 8,483

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sl_ssj

*   **Config description**: The Slovenian UD Treebank is a rule-based conversion
    of the ssj500k treebank, the largest collection of manually syntactically
    annotated data in Slovenian, originally annotated in the JOS annotation
    scheme.

*   **Download size**: `19.82 MiB`

*   **Dataset size**: `28.72 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,250
`'test'`  | 1,282
`'train'` | 10,903

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sl_sst

*   **Config description**: The Spoken Slovenian UD Treebank (SST) is the first
    syntactically annotated corpus of spoken Slovenian, based on a sample of the
    reference GOS corpus, a collection of transcribed audio recordings of
    monologic, dialogic and multi-party spontaneous speech in different everyday
    situations.

*   **Download size**: `2.53 MiB`

*   **Dataset size**: `3.88 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 1,110
`'train'` | 2,078

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/soj_aha

*   **Config description**: The AHA Soi Treebank is a small treebank for
    contemporary Soi. Its corpus is collected and annotated manually. We have
    prepared this treebank based on interviews with Soi speakers.

*   **Download size**: `4.47 KiB`

*   **Dataset size**: `5.58 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 8

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ajp_madar

*   **Config description**: The South_Levantine_Arabic-MADAR treebank consists
    of 100 manually-annotated sentences taken from the
    [MADAR](https://camel.abudhabi.nyu.edu/madar/) (Multi-Arabic Dialect
    Applications and Resources) project.

*   **Download size**: `42.16 KiB`

*   **Dataset size**: `65.64 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 100

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/es_ancora

*   **Config description**: Spanish data from the AnCora corpus.

*   **Download size**: `50.23 MiB`

*   **Dataset size**: `66.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,654
`'test'`  | 1,721
`'train'` | 14,287

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/es_gsd

*   **Config description**: The Spanish UD is converted from the content head
    version of the universal dependency treebank v2.0 (legacy).

*   **Download size**: `24.86 MiB`

*   **Dataset size**: `36.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,400
`'test'`  | 426
`'train'` | 14,187

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/es_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the [CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal
    Dependencies](http://universaldependencies.org/conll17/).

*   **Download size**: `1.60 MiB`

*   **Dataset size**: `2.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/swl_sslc

*   **Config description**: The Universal Dependencies treebank for Swedish Sign
    Language (ISO 639-3: swl) is derived from the Swedish Sign Language Corpus
    (SSLC) from the department of linguistics, Stockholm University.

*   **Download size**: `79.78 KiB`

*   **Dataset size**: `122.04 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 82
`'test'`  | 34
`'train'` | 87

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sv_lines

*   **Config description**: UD Swedish_LinES is the Swedish half of the LinES
    Parallel Treebank with UD annotations. All segments are translations from
    English and the sources cover literary genres, online manuals and Europarl
    data.

*   **Download size**: `6.91 MiB`

*   **Dataset size**: `9.18 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,032
`'test'`  | 1,035
`'train'` | 3,176

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sv_pud

*   **Config description**: Swedish-PUD is the Swedish part of the Parallel
    Universal Dependencies (PUD) treebanks.

*   **Download size**: `1.64 MiB`

*   **Dataset size**: `2.13 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sv_talbanken

*   **Config description**: The Swedish-Talbanken treebank is based on
    Talbanken, a treebank developed at Lund University in the 1970s.

*   **Download size**: `8.08 MiB`

*   **Dataset size**: `11.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 504
`'test'`  | 1,219
`'train'` | 4,303

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/gsw_uzh

*   **Config description**: _UD_Swiss_German-UZH_ is a tiny manually annotated
    treebank of 100 sentences in different Swiss German dialects and a variety
    of text genres.

*   **Download size**: `58.28 KiB`

*   **Dataset size**: `86.61 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 100

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tl_trg

*   **Config description**: UD_Tagalog-TRG is a UD treebank manually annotated
    using sentences from a grammar book.

*   **Download size**: `59.91 KiB`

*   **Dataset size**: `84.14 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 128

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tl_ugnayan

*   **Config description**: Ugnayan is a manually annotated Tagalog treebank
    currently composed of educational fiction and nonfiction text. The treebank
    is under development at the University of the Philippines.

*   **Download size**: `53.91 KiB`

*   **Dataset size**: `76.16 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 94

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ta_mwtt

*   **Config description**: MWTT - Modern Written Tamil Treebank has sentences
    taken primarily from a text called 'A Grammar of Modern Tamil' by Thomas
    Lehmann (1993). This initial release has 536 sentences of various lengths,
    and all of these are added as the test set.

*   **Download size**: `394.18 KiB`

*   **Dataset size**: `499.94 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 534

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ta_ttb

*   **Config description**: The UD Tamil treebank is based on the Tamil
    Dependency Treebank created at the Charles University in Prague by
    Loganathan Ramasamy.

*   **Download size**: `1.68 MiB`

*   **Dataset size**: `2.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 80
`'test'`  | 120
`'train'` | 400

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/te_mtg

*   **Config description**: The Telugu UD treebank is created in UD based on
    manual annotations of sentences from a grammar book.

*   **Download size**: `628.67 KiB`

*   **Dataset size**: `866.20 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 131
`'test'`  | 146
`'train'` | 1,051

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/th_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.53 MiB`

*   **Dataset size**: `1.85 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tpn_tudet

*   **Config description**: UD_Tupinamba-TuDeT is a collection of annotated
    texts in Tupi(nambá). Together with UD_Akuntsu-TuDeT and UD_Munduruku-TuDeT,
    UD_Tupinamba-TuDeT is part of the TuLaR. The treebank is ongoing work and is
    constantly being updated.

*   **Download size**: `293.55 KiB`

*   **Dataset size**: `371.48 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 546

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/qtd_sagt

*   **Config description**: UD Turkish-German SAGT is a Turkish-German
    code-switching treebank that is developed as part of the SAGT project.

*   **Download size**: `2.78 MiB`

*   **Dataset size**: `4.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 801
`'test'`  | 805
`'train'` | 578

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_atis

*   **Config description**: This treebank is a translation of English ATIS
    (Airline Travel Information System) corpus (see References). It consists of
    5432 sentences.

*   **Download size**: `3.26 MiB`

*   **Dataset size**: `5.09 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 572
`'test'`  | 586
`'train'` | 4,274

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_tourism

*   **Config description**: Turkish Tourism is a domain specific treebank
    consisting of 19,750 manually annotated sentences and 92,200 tokens. These
    sentences were taken from the original customer reviews of a tourism
    company.

*   **Download size**: `6.48 MiB`

*   **Dataset size**: `11.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 2,166
`'test'`  | 2,191
`'train'` | 15,476

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_kenet

*   **Config description**: Turkish-Kenet UD Treebank is the biggest treebank of
    Turkish. It consists of 18,700 manually annotated sentences and 178,700
    tokens. Its corpus consists of dictionary examples.

*   **Download size**: `12.16 MiB`

*   **Dataset size**: `19.00 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 1,646
`'test'`  | 1,643
`'train'` | 15,398

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_penn

*   **Config description**: Turkish version of the Penn Treebank. It consists of
    a total of 9,560 manually annotated sentences and 87,367 tokens. (It only
    includes sentences up to 15 words long.)

*   **Download size**: `12.29 MiB`

*   **Dataset size**: `18.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 622
`'test'`  | 924
`'train'` | 14,850

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_framenet

*   **Config description**: Turkish FrameNet consists of 2,700 manually
    annotated example sentences and 19,221 tokens. Its data consists of the
    sentences taken from the Turkish FrameNet Project. The annotated sentences
    can be filtered according to the semantic frame category of the root of the
    sentence.

*   **Download size**: `1.43 MiB`

*   **Dataset size**: `2.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 205
`'test'`  | 205
`'train'` | 2,288

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_boun

*   **Config description**: The largest Turkish dependency treebank annotated in
    UD style. Created by the members of
    [TABILAB](http://http://tabilab.cmpe.boun.edu.tr/) from Boğaziçi University.

*   **Download size**: `9.07 MiB`

*   **Dataset size**: `13.24 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 979
`'test'`  | 979
`'train'` | 7,803

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_gb

*   **Config description**: This is a treebank annotating example sentences from
    a comprehensive grammar book of Turkish.

*   **Download size**: `1.41 MiB`

*   **Dataset size**: `2.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,880

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_imst

*   **Config description**: The UD Turkish Treebank, also called the IMST-UD
    Treebank, is a semi-automatic conversion of the IMST Treebank (Sulubacak et
    al., 2016).

*   **Download size**: `4.51 MiB`

*   **Dataset size**: `6.70 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 988
`'test'`  | 983
`'train'` | 3,664

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/tr_pud

*   **Config description**: This is a part of the Parallel Universal
    Dependencies (PUD) treebanks created for the CoNLL 2017 shared task on
    Multilingual Parsing from Raw Text to Universal Dependencies.

*   **Download size**: `1.29 MiB`

*   **Dataset size**: `1.65 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/uk_iu

*   **Config description**: Gold standard Universal Dependencies corpus for
    Ukrainian, developed for UD originally, by Institute for Ukrainian, NGO.
    [українською]

*   **Download size**: `16.54 MiB`

*   **Dataset size**: `21.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 672
`'test'`  | 892
`'train'` | 5,496

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/hsb_ufal

*   **Config description**: A small treebank of Upper Sorbian based mostly on
    Wikipedia.

*   **Download size**: `762.63 KiB`

*   **Dataset size**: `1.11 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 623
`'train'` | 23

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ur_udtb

*   **Config description**: The Urdu Universal Dependency Treebank was
    automatically converted from Urdu Dependency Treebank (UDTB) which is part
    of an ongoing effort of creating multi-layered treebanks for Hindi and Urdu.

*   **Download size**: `15.16 MiB`

*   **Dataset size**: `21.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 552
`'test'`  | 535
`'train'` | 4,043

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ug_udt

*   **Config description**: The Uyghur UD treebank is based on the Uyghur
    Dependency Treebank (UDT), created at the Xinjiang University in Ürümqi,
    China.

*   **Download size**: `3.30 MiB`

*   **Dataset size**: `4.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 900
`'test'`  | 900
`'train'` | 1,656

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/vi_vtb

*   **Config description**: The Vietnamese UD treebank is a conversion of the
    constituent treebank created in the VLSP project (https://vlsp.hpda.vn/).

*   **Download size**: `1.96 MiB`

*   **Dataset size**: `2.81 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 800
`'test'`  | 800
`'train'` | 1,400

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/wbp_ufal

*   **Config description**: A small treebank of grammatical examples in
    Warlpiri, taken from linguistic literature.

*   **Download size**: `37.58 KiB`

*   **Dataset size**: `47.36 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 55

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/cy_ccg

*   **Config description**: UD Welsh-CCG (Corpws Cystrawennol y Gymraeg) is a
    treebank of Welsh, annotated according to the Universal Dependencies
    guidelines.

*   **Download size**: `2.28 MiB`

*   **Dataset size**: `3.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 953
`'train'` | 976

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/hy_armtdp

*   **Config description**: A Universal Dependencies treebank for Eastern
    Armenian developed for UD originally by the ArmTDP team led by Marat M.
    Yavrumyan at the Yerevan State University.

*   **Download size**: `6.56 MiB`

*   **Dataset size**: `8.50 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 249
`'test'`  | 277
`'train'` | 1,974

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/wo_wtb

*   **Config description**: UD_Wolof-WTB is a natively manual developed treebank
    for Wolof. Sentences were collected from encyclopedic, fictional,
    biographical, religious texts and news.

*   **Download size**: `2.65 MiB`

*   **Dataset size**: `3.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'dev'`   | 449
`'test'`  | 470
`'train'` | 1,188

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sjo_xdt

*   **Config description**: The UD Xibe Treebank is a corpus of the Xibe
    language (ISO 639-3: sjo) containing manually annotated syntactic trees
    under the Universal Dependencies. Sentences come from three sources: grammar
    book examples, newspaper (Cabcal News) and Xibe textbooks.

*   **Download size**: `1.50 MiB`

*   **Dataset size**: `1.74 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 810

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/sah_yktdt

*   **Config description**: UD_Yakut-YKTDT is a collection Yakut ([Sakha])
    sentences (https://glottolog.org/resource/languoid/id/yaku1245). The project
    is work-in-progress and the treebank is being updated on a regular basis

*   **Download size**: `51.76 KiB`

*   **Dataset size**: `61.70 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 96

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/yo_ytb

*   **Config description**: Parts of the Yoruba Bible and of the Yoruba edition
    of Wikipedia, hand-annotated natively in Universal Dependencies.

*   **Download size**: `554.64 KiB`

*   **Dataset size**: `767.54 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 318

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

## universal_dependencies/ess_sli

*   **Config description**: UD_Yupik-SLI is a treebank of St. Lawrence Island
    Yupik (ISO 639-3: ess) that has been manually annotated at the morpheme
    level, based on a finite-state morphological analyzer by Chen et al., 2020.
    The word-level annotation, merging multiword expressions, is provided in
    not-to-release/ess_sli-ud-test.merged.conllu. More information about the
    treebank can be found in our publication (AmericasNLP, 2021).

*   **Download size**: `302.87 KiB`

*   **Dataset size**: `410.25 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 309

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Only shown for the first 100 configs.

<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikipedia" />
  <meta itemprop="description" content="Wikipedia dataset containing cleaned articles of all languages.&#10;The datasets are built from the Wikipedia dump&#10;(https://dumps.wikimedia.org/) with one split per language. Each example&#10;contains the content of one full Wikipedia article with cleaning to strip&#10;markdown and unwanted sections (references, etc.).&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;wikipedia&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikipedia" />
  <meta itemprop="sameAs" content="https://dumps.wikimedia.org" />
  <meta itemprop="citation" content="@ONLINE {wikidump,&#10;    author = &quot;Wikimedia Foundation&quot;,&#10;    title  = &quot;Wikimedia Downloads&quot;,&#10;    url    = &quot;https://dumps.wikimedia.org&quot;&#10;}&#10;" />
</div>
# `wikipedia`

Wikipedia dataset containing cleaned articles of all languages. The datasets are
built from the Wikipedia dump (https://dumps.wikimedia.org/) with one split per
language. Each example contains the content of one full Wikipedia article with
cleaning to strip markdown and unwanted sections (references, etc.).

*   URL: [https://dumps.wikimedia.org](https://dumps.wikimedia.org)
*   `DatasetBuilder`:
    [`tfds.text.wikipedia.Wikipedia`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wikipedia.py)

`wikipedia` is configured with `tfds.text.wikipedia.WikipediaConfig` and has the
following configurations predefined (defaults to the first one):

*   `20190301.aa` (`v1.0.0`) (`Size: 44.09 KiB`): Wikipedia dataset for aa,
    parsed from 20190301 dump.

*   `20190301.ab` (`v1.0.0`) (`Size: 1.31 MiB`): Wikipedia dataset for ab,
    parsed from 20190301 dump.

*   `20190301.ace` (`v1.0.0`) (`Size: 2.66 MiB`): Wikipedia dataset for ace,
    parsed from 20190301 dump.

*   `20190301.ady` (`v1.0.0`) (`Size: 349.43 KiB`): Wikipedia dataset for ady,
    parsed from 20190301 dump.

*   `20190301.af` (`v1.0.0`) (`Size: 84.13 MiB`): Wikipedia dataset for af,
    parsed from 20190301 dump.

*   `20190301.ak` (`v1.0.0`) (`Size: 377.84 KiB`): Wikipedia dataset for ak,
    parsed from 20190301 dump.

*   `20190301.als` (`v1.0.0`) (`Size: 46.90 MiB`): Wikipedia dataset for als,
    parsed from 20190301 dump.

*   `20190301.am` (`v1.0.0`) (`Size: 6.54 MiB`): Wikipedia dataset for am,
    parsed from 20190301 dump.

*   `20190301.an` (`v1.0.0`) (`Size: 31.39 MiB`): Wikipedia dataset for an,
    parsed from 20190301 dump.

*   `20190301.ang` (`v1.0.0`) (`Size: 3.77 MiB`): Wikipedia dataset for ang,
    parsed from 20190301 dump.

*   `20190301.ar` (`v1.0.0`) (`Size: 805.82 MiB`): Wikipedia dataset for ar,
    parsed from 20190301 dump.

*   `20190301.arc` (`v1.0.0`) (`Size: 952.49 KiB`): Wikipedia dataset for arc,
    parsed from 20190301 dump.

*   `20190301.arz` (`v1.0.0`) (`Size: 20.32 MiB`): Wikipedia dataset for arz,
    parsed from 20190301 dump.

*   `20190301.as` (`v1.0.0`) (`Size: 19.06 MiB`): Wikipedia dataset for as,
    parsed from 20190301 dump.

*   `20190301.ast` (`v1.0.0`) (`Size: 216.68 MiB`): Wikipedia dataset for ast,
    parsed from 20190301 dump.

*   `20190301.atj` (`v1.0.0`) (`Size: 467.05 KiB`): Wikipedia dataset for atj,
    parsed from 20190301 dump.

*   `20190301.av` (`v1.0.0`) (`Size: 3.61 MiB`): Wikipedia dataset for av,
    parsed from 20190301 dump.

*   `20190301.ay` (`v1.0.0`) (`Size: 2.06 MiB`): Wikipedia dataset for ay,
    parsed from 20190301 dump.

*   `20190301.az` (`v1.0.0`) (`Size: 163.04 MiB`): Wikipedia dataset for az,
    parsed from 20190301 dump.

*   `20190301.azb` (`v1.0.0`) (`Size: 50.59 MiB`): Wikipedia dataset for azb,
    parsed from 20190301 dump.

*   `20190301.ba` (`v1.0.0`) (`Size: 55.04 MiB`): Wikipedia dataset for ba,
    parsed from 20190301 dump.

*   `20190301.bar` (`v1.0.0`) (`Size: 30.14 MiB`): Wikipedia dataset for bar,
    parsed from 20190301 dump.

*   `20190301.bat-smg` (`v1.0.0`) (`Size: 4.61 MiB`): Wikipedia dataset for
    bat-smg, parsed from 20190301 dump.

*   `20190301.bcl` (`v1.0.0`) (`Size: 6.18 MiB`): Wikipedia dataset for bcl,
    parsed from 20190301 dump.

*   `20190301.be` (`v1.0.0`) (`Size: 192.23 MiB`): Wikipedia dataset for be,
    parsed from 20190301 dump.

*   `20190301.be-x-old` (`v1.0.0`) (`Size: 74.77 MiB`): Wikipedia dataset for
    be-x-old, parsed from 20190301 dump.

*   `20190301.bg` (`v1.0.0`) (`Size: 326.20 MiB`): Wikipedia dataset for bg,
    parsed from 20190301 dump.

*   `20190301.bh` (`v1.0.0`) (`Size: 13.28 MiB`): Wikipedia dataset for bh,
    parsed from 20190301 dump.

*   `20190301.bi` (`v1.0.0`) (`Size: 424.88 KiB`): Wikipedia dataset for bi,
    parsed from 20190301 dump.

*   `20190301.bjn` (`v1.0.0`) (`Size: 2.09 MiB`): Wikipedia dataset for bjn,
    parsed from 20190301 dump.

*   `20190301.bm` (`v1.0.0`) (`Size: 447.98 KiB`): Wikipedia dataset for bm,
    parsed from 20190301 dump.

*   `20190301.bn` (`v1.0.0`) (`Size: 145.04 MiB`): Wikipedia dataset for bn,
    parsed from 20190301 dump.

*   `20190301.bo` (`v1.0.0`) (`Size: 12.41 MiB`): Wikipedia dataset for bo,
    parsed from 20190301 dump.

*   `20190301.bpy` (`v1.0.0`) (`Size: 5.05 MiB`): Wikipedia dataset for bpy,
    parsed from 20190301 dump.

*   `20190301.br` (`v1.0.0`) (`Size: 49.14 MiB`): Wikipedia dataset for br,
    parsed from 20190301 dump.

*   `20190301.bs` (`v1.0.0`) (`Size: 103.26 MiB`): Wikipedia dataset for bs,
    parsed from 20190301 dump.

*   `20190301.bug` (`v1.0.0`) (`Size: 1.76 MiB`): Wikipedia dataset for bug,
    parsed from 20190301 dump.

*   `20190301.bxr` (`v1.0.0`) (`Size: 3.21 MiB`): Wikipedia dataset for bxr,
    parsed from 20190301 dump.

*   `20190301.ca` (`v1.0.0`) (`Size: 849.65 MiB`): Wikipedia dataset for ca,
    parsed from 20190301 dump.

*   `20190301.cbk-zam` (`v1.0.0`) (`Size: 1.84 MiB`): Wikipedia dataset for
    cbk-zam, parsed from 20190301 dump.

*   `20190301.cdo` (`v1.0.0`) (`Size: 3.22 MiB`): Wikipedia dataset for cdo,
    parsed from 20190301 dump.

*   `20190301.ce` (`v1.0.0`) (`Size: 43.89 MiB`): Wikipedia dataset for ce,
    parsed from 20190301 dump.

*   `20190301.ceb` (`v1.0.0`) (`Size: 1.79 GiB`): Wikipedia dataset for ceb,
    parsed from 20190301 dump.

*   `20190301.ch` (`v1.0.0`) (`Size: 684.97 KiB`): Wikipedia dataset for ch,
    parsed from 20190301 dump.

*   `20190301.cho` (`v1.0.0`) (`Size: 25.99 KiB`): Wikipedia dataset for cho,
    parsed from 20190301 dump.

*   `20190301.chr` (`v1.0.0`) (`Size: 651.25 KiB`): Wikipedia dataset for chr,
    parsed from 20190301 dump.

*   `20190301.chy` (`v1.0.0`) (`Size: 325.90 KiB`): Wikipedia dataset for chy,
    parsed from 20190301 dump.

*   `20190301.ckb` (`v1.0.0`) (`Size: 22.16 MiB`): Wikipedia dataset for ckb,
    parsed from 20190301 dump.

*   `20190301.co` (`v1.0.0`) (`Size: 3.38 MiB`): Wikipedia dataset for co,
    parsed from 20190301 dump.

*   `20190301.cr` (`v1.0.0`) (`Size: 259.71 KiB`): Wikipedia dataset for cr,
    parsed from 20190301 dump.

*   `20190301.crh` (`v1.0.0`) (`Size: 4.01 MiB`): Wikipedia dataset for crh,
    parsed from 20190301 dump.

*   `20190301.cs` (`v1.0.0`) (`Size: 759.21 MiB`): Wikipedia dataset for cs,
    parsed from 20190301 dump.

*   `20190301.csb` (`v1.0.0`) (`Size: 2.03 MiB`): Wikipedia dataset for csb,
    parsed from 20190301 dump.

*   `20190301.cu` (`v1.0.0`) (`Size: 631.49 KiB`): Wikipedia dataset for cu,
    parsed from 20190301 dump.

*   `20190301.cv` (`v1.0.0`) (`Size: 22.23 MiB`): Wikipedia dataset for cv,
    parsed from 20190301 dump.

*   `20190301.cy` (`v1.0.0`) (`Size: 64.37 MiB`): Wikipedia dataset for cy,
    parsed from 20190301 dump.

*   `20190301.da` (`v1.0.0`) (`Size: 323.53 MiB`): Wikipedia dataset for da,
    parsed from 20190301 dump.

*   `20190301.de` (`v1.0.0`) (`Size: 4.97 GiB`): Wikipedia dataset for de,
    parsed from 20190301 dump.

*   `20190301.din` (`v1.0.0`) (`Size: 457.06 KiB`): Wikipedia dataset for din,
    parsed from 20190301 dump.

*   `20190301.diq` (`v1.0.0`) (`Size: 7.24 MiB`): Wikipedia dataset for diq,
    parsed from 20190301 dump.

*   `20190301.dsb` (`v1.0.0`) (`Size: 3.54 MiB`): Wikipedia dataset for dsb,
    parsed from 20190301 dump.

*   `20190301.dty` (`v1.0.0`) (`Size: 4.95 MiB`): Wikipedia dataset for dty,
    parsed from 20190301 dump.

*   `20190301.dv` (`v1.0.0`) (`Size: 4.24 MiB`): Wikipedia dataset for dv,
    parsed from 20190301 dump.

*   `20190301.dz` (`v1.0.0`) (`Size: 360.01 KiB`): Wikipedia dataset for dz,
    parsed from 20190301 dump.

*   `20190301.ee` (`v1.0.0`) (`Size: 434.14 KiB`): Wikipedia dataset for ee,
    parsed from 20190301 dump.

*   `20190301.el` (`v1.0.0`) (`Size: 324.40 MiB`): Wikipedia dataset for el,
    parsed from 20190301 dump.

*   `20190301.eml` (`v1.0.0`) (`Size: 7.72 MiB`): Wikipedia dataset for eml,
    parsed from 20190301 dump.

*   `20190301.en` (`v1.0.0`) (`Size: 15.72 GiB`): Wikipedia dataset for en,
    parsed from 20190301 dump.

*   `20190301.eo` (`v1.0.0`) (`Size: 245.73 MiB`): Wikipedia dataset for eo,
    parsed from 20190301 dump.

*   `20190301.es` (`v1.0.0`) (`Size: 2.93 GiB`): Wikipedia dataset for es,
    parsed from 20190301 dump.

*   `20190301.et` (`v1.0.0`) (`Size: 196.03 MiB`): Wikipedia dataset for et,
    parsed from 20190301 dump.

*   `20190301.eu` (`v1.0.0`) (`Size: 180.35 MiB`): Wikipedia dataset for eu,
    parsed from 20190301 dump.

*   `20190301.ext` (`v1.0.0`) (`Size: 2.40 MiB`): Wikipedia dataset for ext,
    parsed from 20190301 dump.

*   `20190301.fa` (`v1.0.0`) (`Size: 693.84 MiB`): Wikipedia dataset for fa,
    parsed from 20190301 dump.

*   `20190301.ff` (`v1.0.0`) (`Size: 387.75 KiB`): Wikipedia dataset for ff,
    parsed from 20190301 dump.

*   `20190301.fi` (`v1.0.0`) (`Size: 656.44 MiB`): Wikipedia dataset for fi,
    parsed from 20190301 dump.

*   `20190301.fiu-vro` (`v1.0.0`) (`Size: 2.00 MiB`): Wikipedia dataset for
    fiu-vro, parsed from 20190301 dump.

*   `20190301.fj` (`v1.0.0`) (`Size: 262.98 KiB`): Wikipedia dataset for fj,
    parsed from 20190301 dump.

*   `20190301.fo` (`v1.0.0`) (`Size: 13.67 MiB`): Wikipedia dataset for fo,
    parsed from 20190301 dump.

*   `20190301.fr` (`v1.0.0`) (`Size: 4.14 GiB`): Wikipedia dataset for fr,
    parsed from 20190301 dump.

*   `20190301.frp` (`v1.0.0`) (`Size: 2.03 MiB`): Wikipedia dataset for frp,
    parsed from 20190301 dump.

*   `20190301.frr` (`v1.0.0`) (`Size: 7.88 MiB`): Wikipedia dataset for frr,
    parsed from 20190301 dump.

*   `20190301.fur` (`v1.0.0`) (`Size: 2.29 MiB`): Wikipedia dataset for fur,
    parsed from 20190301 dump.

*   `20190301.fy` (`v1.0.0`) (`Size: 45.52 MiB`): Wikipedia dataset for fy,
    parsed from 20190301 dump.

*   `20190301.ga` (`v1.0.0`) (`Size: 24.78 MiB`): Wikipedia dataset for ga,
    parsed from 20190301 dump.

*   `20190301.gag` (`v1.0.0`) (`Size: 2.04 MiB`): Wikipedia dataset for gag,
    parsed from 20190301 dump.

*   `20190301.gan` (`v1.0.0`) (`Size: 3.82 MiB`): Wikipedia dataset for gan,
    parsed from 20190301 dump.

*   `20190301.gd` (`v1.0.0`) (`Size: 8.51 MiB`): Wikipedia dataset for gd,
    parsed from 20190301 dump.

*   `20190301.gl` (`v1.0.0`) (`Size: 235.07 MiB`): Wikipedia dataset for gl,
    parsed from 20190301 dump.

*   `20190301.glk` (`v1.0.0`) (`Size: 1.91 MiB`): Wikipedia dataset for glk,
    parsed from 20190301 dump.

*   `20190301.gn` (`v1.0.0`) (`Size: 3.37 MiB`): Wikipedia dataset for gn,
    parsed from 20190301 dump.

*   `20190301.gom` (`v1.0.0`) (`Size: 6.07 MiB`): Wikipedia dataset for gom,
    parsed from 20190301 dump.

*   `20190301.gor` (`v1.0.0`) (`Size: 1.28 MiB`): Wikipedia dataset for gor,
    parsed from 20190301 dump.

*   `20190301.got` (`v1.0.0`) (`Size: 604.10 KiB`): Wikipedia dataset for got,
    parsed from 20190301 dump.

*   `20190301.gu` (`v1.0.0`) (`Size: 27.23 MiB`): Wikipedia dataset for gu,
    parsed from 20190301 dump.

*   `20190301.gv` (`v1.0.0`) (`Size: 5.32 MiB`): Wikipedia dataset for gv,
    parsed from 20190301 dump.

*   `20190301.ha` (`v1.0.0`) (`Size: 1.62 MiB`): Wikipedia dataset for ha,
    parsed from 20190301 dump.

*   `20190301.hak` (`v1.0.0`) (`Size: 3.28 MiB`): Wikipedia dataset for hak,
    parsed from 20190301 dump.

*   `20190301.haw` (`v1.0.0`) (`Size: 1017.76 KiB`): Wikipedia dataset for haw,
    parsed from 20190301 dump.

*   `20190301.he` (`v1.0.0`) (`Size: 572.30 MiB`): Wikipedia dataset for he,
    parsed from 20190301 dump.

*   `20190301.hi` (`v1.0.0`) (`Size: 137.86 MiB`): Wikipedia dataset for hi,
    parsed from 20190301 dump.

*   `20190301.hif` (`v1.0.0`) (`Size: 4.57 MiB`): Wikipedia dataset for hif,
    parsed from 20190301 dump.

*   `20190301.ho` (`v1.0.0`) (`Size: 18.37 KiB`): Wikipedia dataset for ho,
    parsed from 20190301 dump.

*   `20190301.hr` (`v1.0.0`) (`Size: 246.05 MiB`): Wikipedia dataset for hr,
    parsed from 20190301 dump.

*   `20190301.hsb` (`v1.0.0`) (`Size: 10.38 MiB`): Wikipedia dataset for hsb,
    parsed from 20190301 dump.

*   `20190301.ht` (`v1.0.0`) (`Size: 10.23 MiB`): Wikipedia dataset for ht,
    parsed from 20190301 dump.

*   `20190301.hu` (`v1.0.0`) (`Size: 810.17 MiB`): Wikipedia dataset for hu,
    parsed from 20190301 dump.

*   `20190301.hy` (`v1.0.0`) (`Size: 277.53 MiB`): Wikipedia dataset for hy,
    parsed from 20190301 dump.

*   `20190301.ia` (`v1.0.0`) (`Size: 7.85 MiB`): Wikipedia dataset for ia,
    parsed from 20190301 dump.

*   `20190301.id` (`v1.0.0`) (`Size: 523.94 MiB`): Wikipedia dataset for id,
    parsed from 20190301 dump.

*   `20190301.ie` (`v1.0.0`) (`Size: 1.70 MiB`): Wikipedia dataset for ie,
    parsed from 20190301 dump.

*   `20190301.ig` (`v1.0.0`) (`Size: 1.00 MiB`): Wikipedia dataset for ig,
    parsed from 20190301 dump.

*   `20190301.ii` (`v1.0.0`) (`Size: 30.88 KiB`): Wikipedia dataset for ii,
    parsed from 20190301 dump.

*   `20190301.ik` (`v1.0.0`) (`Size: 238.12 KiB`): Wikipedia dataset for ik,
    parsed from 20190301 dump.

*   `20190301.ilo` (`v1.0.0`) (`Size: 15.22 MiB`): Wikipedia dataset for ilo,
    parsed from 20190301 dump.

*   `20190301.inh` (`v1.0.0`) (`Size: 1.26 MiB`): Wikipedia dataset for inh,
    parsed from 20190301 dump.

*   `20190301.io` (`v1.0.0`) (`Size: 12.56 MiB`): Wikipedia dataset for io,
    parsed from 20190301 dump.

*   `20190301.is` (`v1.0.0`) (`Size: 41.86 MiB`): Wikipedia dataset for is,
    parsed from 20190301 dump.

*   `20190301.it` (`v1.0.0`) (`Size: 2.66 GiB`): Wikipedia dataset for it,
    parsed from 20190301 dump.

*   `20190301.iu` (`v1.0.0`) (`Size: 284.06 KiB`): Wikipedia dataset for iu,
    parsed from 20190301 dump.

*   `20190301.ja` (`v1.0.0`) (`Size: 2.74 GiB`): Wikipedia dataset for ja,
    parsed from 20190301 dump.

*   `20190301.jam` (`v1.0.0`) (`Size: 895.29 KiB`): Wikipedia dataset for jam,
    parsed from 20190301 dump.

*   `20190301.jbo` (`v1.0.0`) (`Size: 1.06 MiB`): Wikipedia dataset for jbo,
    parsed from 20190301 dump.

*   `20190301.jv` (`v1.0.0`) (`Size: 39.32 MiB`): Wikipedia dataset for jv,
    parsed from 20190301 dump.

*   `20190301.ka` (`v1.0.0`) (`Size: 131.78 MiB`): Wikipedia dataset for ka,
    parsed from 20190301 dump.

*   `20190301.kaa` (`v1.0.0`) (`Size: 1.35 MiB`): Wikipedia dataset for kaa,
    parsed from 20190301 dump.

*   `20190301.kab` (`v1.0.0`) (`Size: 3.62 MiB`): Wikipedia dataset for kab,
    parsed from 20190301 dump.

*   `20190301.kbd` (`v1.0.0`) (`Size: 1.65 MiB`): Wikipedia dataset for kbd,
    parsed from 20190301 dump.

*   `20190301.kbp` (`v1.0.0`) (`Size: 1.24 MiB`): Wikipedia dataset for kbp,
    parsed from 20190301 dump.

*   `20190301.kg` (`v1.0.0`) (`Size: 439.26 KiB`): Wikipedia dataset for kg,
    parsed from 20190301 dump.

*   `20190301.ki` (`v1.0.0`) (`Size: 370.78 KiB`): Wikipedia dataset for ki,
    parsed from 20190301 dump.

*   `20190301.kj` (`v1.0.0`) (`Size: 16.58 KiB`): Wikipedia dataset for kj,
    parsed from 20190301 dump.

*   `20190301.kk` (`v1.0.0`) (`Size: 113.46 MiB`): Wikipedia dataset for kk,
    parsed from 20190301 dump.

*   `20190301.kl` (`v1.0.0`) (`Size: 862.51 KiB`): Wikipedia dataset for kl,
    parsed from 20190301 dump.

*   `20190301.km` (`v1.0.0`) (`Size: 21.92 MiB`): Wikipedia dataset for km,
    parsed from 20190301 dump.

*   `20190301.kn` (`v1.0.0`) (`Size: 69.62 MiB`): Wikipedia dataset for kn,
    parsed from 20190301 dump.

*   `20190301.ko` (`v1.0.0`) (`Size: 625.16 MiB`): Wikipedia dataset for ko,
    parsed from 20190301 dump.

*   `20190301.koi` (`v1.0.0`) (`Size: 2.12 MiB`): Wikipedia dataset for koi,
    parsed from 20190301 dump.

*   `20190301.krc` (`v1.0.0`) (`Size: 3.16 MiB`): Wikipedia dataset for krc,
    parsed from 20190301 dump.

*   `20190301.ks` (`v1.0.0`) (`Size: 309.15 KiB`): Wikipedia dataset for ks,
    parsed from 20190301 dump.

*   `20190301.ksh` (`v1.0.0`) (`Size: 3.07 MiB`): Wikipedia dataset for ksh,
    parsed from 20190301 dump.

*   `20190301.ku` (`v1.0.0`) (`Size: 17.09 MiB`): Wikipedia dataset for ku,
    parsed from 20190301 dump.

*   `20190301.kv` (`v1.0.0`) (`Size: 3.36 MiB`): Wikipedia dataset for kv,
    parsed from 20190301 dump.

*   `20190301.kw` (`v1.0.0`) (`Size: 1.71 MiB`): Wikipedia dataset for kw,
    parsed from 20190301 dump.

*   `20190301.ky` (`v1.0.0`) (`Size: 33.13 MiB`): Wikipedia dataset for ky,
    parsed from 20190301 dump.

*   `20190301.la` (`v1.0.0`) (`Size: 82.72 MiB`): Wikipedia dataset for la,
    parsed from 20190301 dump.

*   `20190301.lad` (`v1.0.0`) (`Size: 3.39 MiB`): Wikipedia dataset for lad,
    parsed from 20190301 dump.

*   `20190301.lb` (`v1.0.0`) (`Size: 45.70 MiB`): Wikipedia dataset for lb,
    parsed from 20190301 dump.

*   `20190301.lbe` (`v1.0.0`) (`Size: 1.22 MiB`): Wikipedia dataset for lbe,
    parsed from 20190301 dump.

*   `20190301.lez` (`v1.0.0`) (`Size: 4.16 MiB`): Wikipedia dataset for lez,
    parsed from 20190301 dump.

*   `20190301.lfn` (`v1.0.0`) (`Size: 2.81 MiB`): Wikipedia dataset for lfn,
    parsed from 20190301 dump.

*   `20190301.lg` (`v1.0.0`) (`Size: 1.58 MiB`): Wikipedia dataset for lg,
    parsed from 20190301 dump.

*   `20190301.li` (`v1.0.0`) (`Size: 13.86 MiB`): Wikipedia dataset for li,
    parsed from 20190301 dump.

*   `20190301.lij` (`v1.0.0`) (`Size: 2.73 MiB`): Wikipedia dataset for lij,
    parsed from 20190301 dump.

*   `20190301.lmo` (`v1.0.0`) (`Size: 21.34 MiB`): Wikipedia dataset for lmo,
    parsed from 20190301 dump.

*   `20190301.ln` (`v1.0.0`) (`Size: 1.83 MiB`): Wikipedia dataset for ln,
    parsed from 20190301 dump.

*   `20190301.lo` (`v1.0.0`) (`Size: 3.44 MiB`): Wikipedia dataset for lo,
    parsed from 20190301 dump.

*   `20190301.lrc` (`v1.0.0`) (`Size: 4.71 MiB`): Wikipedia dataset for lrc,
    parsed from 20190301 dump.

*   `20190301.lt` (`v1.0.0`) (`Size: 174.73 MiB`): Wikipedia dataset for lt,
    parsed from 20190301 dump.

*   `20190301.ltg` (`v1.0.0`) (`Size: 798.18 KiB`): Wikipedia dataset for ltg,
    parsed from 20190301 dump.

*   `20190301.lv` (`v1.0.0`) (`Size: 127.47 MiB`): Wikipedia dataset for lv,
    parsed from 20190301 dump.

*   `20190301.mai` (`v1.0.0`) (`Size: 10.80 MiB`): Wikipedia dataset for mai,
    parsed from 20190301 dump.

*   `20190301.map-bms` (`v1.0.0`) (`Size: 4.49 MiB`): Wikipedia dataset for
    map-bms, parsed from 20190301 dump.

*   `20190301.mdf` (`v1.0.0`) (`Size: 1.04 MiB`): Wikipedia dataset for mdf,
    parsed from 20190301 dump.

*   `20190301.mg` (`v1.0.0`) (`Size: 25.64 MiB`): Wikipedia dataset for mg,
    parsed from 20190301 dump.

*   `20190301.mh` (`v1.0.0`) (`Size: 27.71 KiB`): Wikipedia dataset for mh,
    parsed from 20190301 dump.

*   `20190301.mhr` (`v1.0.0`) (`Size: 5.69 MiB`): Wikipedia dataset for mhr,
    parsed from 20190301 dump.

*   `20190301.mi` (`v1.0.0`) (`Size: 1.96 MiB`): Wikipedia dataset for mi,
    parsed from 20190301 dump.

*   `20190301.min` (`v1.0.0`) (`Size: 25.05 MiB`): Wikipedia dataset for min,
    parsed from 20190301 dump.

*   `20190301.mk` (`v1.0.0`) (`Size: 140.69 MiB`): Wikipedia dataset for mk,
    parsed from 20190301 dump.

*   `20190301.ml` (`v1.0.0`) (`Size: 117.24 MiB`): Wikipedia dataset for ml,
    parsed from 20190301 dump.

*   `20190301.mn` (`v1.0.0`) (`Size: 28.23 MiB`): Wikipedia dataset for mn,
    parsed from 20190301 dump.

*   `20190301.mr` (`v1.0.0`) (`Size: 49.58 MiB`): Wikipedia dataset for mr,
    parsed from 20190301 dump.

*   `20190301.mrj` (`v1.0.0`) (`Size: 3.01 MiB`): Wikipedia dataset for mrj,
    parsed from 20190301 dump.

*   `20190301.ms` (`v1.0.0`) (`Size: 205.79 MiB`): Wikipedia dataset for ms,
    parsed from 20190301 dump.

*   `20190301.mt` (`v1.0.0`) (`Size: 8.21 MiB`): Wikipedia dataset for mt,
    parsed from 20190301 dump.

*   `20190301.mus` (`v1.0.0`) (`Size: 14.20 KiB`): Wikipedia dataset for mus,
    parsed from 20190301 dump.

*   `20190301.mwl` (`v1.0.0`) (`Size: 8.95 MiB`): Wikipedia dataset for mwl,
    parsed from 20190301 dump.

*   `20190301.my` (`v1.0.0`) (`Size: 34.60 MiB`): Wikipedia dataset for my,
    parsed from 20190301 dump.

*   `20190301.myv` (`v1.0.0`) (`Size: 7.79 MiB`): Wikipedia dataset for myv,
    parsed from 20190301 dump.

*   `20190301.mzn` (`v1.0.0`) (`Size: 6.47 MiB`): Wikipedia dataset for mzn,
    parsed from 20190301 dump.

*   `20190301.na` (`v1.0.0`) (`Size: 480.57 KiB`): Wikipedia dataset for na,
    parsed from 20190301 dump.

*   `20190301.nah` (`v1.0.0`) (`Size: 4.30 MiB`): Wikipedia dataset for nah,
    parsed from 20190301 dump.

*   `20190301.nap` (`v1.0.0`) (`Size: 5.55 MiB`): Wikipedia dataset for nap,
    parsed from 20190301 dump.

*   `20190301.nds` (`v1.0.0`) (`Size: 33.28 MiB`): Wikipedia dataset for nds,
    parsed from 20190301 dump.

*   `20190301.nds-nl` (`v1.0.0`) (`Size: 6.67 MiB`): Wikipedia dataset for
    nds-nl, parsed from 20190301 dump.

*   `20190301.ne` (`v1.0.0`) (`Size: 29.26 MiB`): Wikipedia dataset for ne,
    parsed from 20190301 dump.

*   `20190301.new` (`v1.0.0`) (`Size: 16.91 MiB`): Wikipedia dataset for new,
    parsed from 20190301 dump.

*   `20190301.ng` (`v1.0.0`) (`Size: 91.11 KiB`): Wikipedia dataset for ng,
    parsed from 20190301 dump.

*   `20190301.nl` (`v1.0.0`) (`Size: 1.38 GiB`): Wikipedia dataset for nl,
    parsed from 20190301 dump.

*   `20190301.nn` (`v1.0.0`) (`Size: 126.01 MiB`): Wikipedia dataset for nn,
    parsed from 20190301 dump.

*   `20190301.no` (`v1.0.0`) (`Size: 610.74 MiB`): Wikipedia dataset for no,
    parsed from 20190301 dump.

*   `20190301.nov` (`v1.0.0`) (`Size: 1.12 MiB`): Wikipedia dataset for nov,
    parsed from 20190301 dump.

*   `20190301.nrm` (`v1.0.0`) (`Size: 1.56 MiB`): Wikipedia dataset for nrm,
    parsed from 20190301 dump.

*   `20190301.nso` (`v1.0.0`) (`Size: 2.20 MiB`): Wikipedia dataset for nso,
    parsed from 20190301 dump.

*   `20190301.nv` (`v1.0.0`) (`Size: 2.52 MiB`): Wikipedia dataset for nv,
    parsed from 20190301 dump.

*   `20190301.ny` (`v1.0.0`) (`Size: 1.18 MiB`): Wikipedia dataset for ny,
    parsed from 20190301 dump.

*   `20190301.oc` (`v1.0.0`) (`Size: 70.97 MiB`): Wikipedia dataset for oc,
    parsed from 20190301 dump.

*   `20190301.olo` (`v1.0.0`) (`Size: 1.55 MiB`): Wikipedia dataset for olo,
    parsed from 20190301 dump.

*   `20190301.om` (`v1.0.0`) (`Size: 1.06 MiB`): Wikipedia dataset for om,
    parsed from 20190301 dump.

*   `20190301.or` (`v1.0.0`) (`Size: 24.90 MiB`): Wikipedia dataset for or,
    parsed from 20190301 dump.

*   `20190301.os` (`v1.0.0`) (`Size: 7.31 MiB`): Wikipedia dataset for os,
    parsed from 20190301 dump.

*   `20190301.pa` (`v1.0.0`) (`Size: 40.39 MiB`): Wikipedia dataset for pa,
    parsed from 20190301 dump.

*   `20190301.pag` (`v1.0.0`) (`Size: 1.29 MiB`): Wikipedia dataset for pag,
    parsed from 20190301 dump.

*   `20190301.pam` (`v1.0.0`) (`Size: 8.17 MiB`): Wikipedia dataset for pam,
    parsed from 20190301 dump.

*   `20190301.pap` (`v1.0.0`) (`Size: 1.33 MiB`): Wikipedia dataset for pap,
    parsed from 20190301 dump.

*   `20190301.pcd` (`v1.0.0`) (`Size: 4.14 MiB`): Wikipedia dataset for pcd,
    parsed from 20190301 dump.

*   `20190301.pdc` (`v1.0.0`) (`Size: 1.10 MiB`): Wikipedia dataset for pdc,
    parsed from 20190301 dump.

*   `20190301.pfl` (`v1.0.0`) (`Size: 3.22 MiB`): Wikipedia dataset for pfl,
    parsed from 20190301 dump.

*   `20190301.pi` (`v1.0.0`) (`Size: 586.77 KiB`): Wikipedia dataset for pi,
    parsed from 20190301 dump.

*   `20190301.pih` (`v1.0.0`) (`Size: 654.11 KiB`): Wikipedia dataset for pih,
    parsed from 20190301 dump.

*   `20190301.pl` (`v1.0.0`) (`Size: 1.76 GiB`): Wikipedia dataset for pl,
    parsed from 20190301 dump.

*   `20190301.pms` (`v1.0.0`) (`Size: 13.42 MiB`): Wikipedia dataset for pms,
    parsed from 20190301 dump.

*   `20190301.pnb` (`v1.0.0`) (`Size: 24.31 MiB`): Wikipedia dataset for pnb,
    parsed from 20190301 dump.

*   `20190301.pnt` (`v1.0.0`) (`Size: 533.84 KiB`): Wikipedia dataset for pnt,
    parsed from 20190301 dump.

*   `20190301.ps` (`v1.0.0`) (`Size: 14.09 MiB`): Wikipedia dataset for ps,
    parsed from 20190301 dump.

*   `20190301.pt` (`v1.0.0`) (`Size: 1.58 GiB`): Wikipedia dataset for pt,
    parsed from 20190301 dump.

*   `20190301.qu` (`v1.0.0`) (`Size: 11.42 MiB`): Wikipedia dataset for qu,
    parsed from 20190301 dump.

*   `20190301.rm` (`v1.0.0`) (`Size: 5.85 MiB`): Wikipedia dataset for rm,
    parsed from 20190301 dump.

*   `20190301.rmy` (`v1.0.0`) (`Size: 509.61 KiB`): Wikipedia dataset for rmy,
    parsed from 20190301 dump.

*   `20190301.rn` (`v1.0.0`) (`Size: 779.25 KiB`): Wikipedia dataset for rn,
    parsed from 20190301 dump.

*   `20190301.ro` (`v1.0.0`) (`Size: 449.49 MiB`): Wikipedia dataset for ro,
    parsed from 20190301 dump.

*   `20190301.roa-rup` (`v1.0.0`) (`Size: 931.23 KiB`): Wikipedia dataset for
    roa-rup, parsed from 20190301 dump.

*   `20190301.roa-tara` (`v1.0.0`) (`Size: 5.98 MiB`): Wikipedia dataset for
    roa-tara, parsed from 20190301 dump.

*   `20190301.ru` (`v1.0.0`) (`Size: 3.51 GiB`): Wikipedia dataset for ru,
    parsed from 20190301 dump.

*   `20190301.rue` (`v1.0.0`) (`Size: 4.11 MiB`): Wikipedia dataset for rue,
    parsed from 20190301 dump.

*   `20190301.rw` (`v1.0.0`) (`Size: 904.81 KiB`): Wikipedia dataset for rw,
    parsed from 20190301 dump.

*   `20190301.sa` (`v1.0.0`) (`Size: 14.29 MiB`): Wikipedia dataset for sa,
    parsed from 20190301 dump.

*   `20190301.sah` (`v1.0.0`) (`Size: 11.88 MiB`): Wikipedia dataset for sah,
    parsed from 20190301 dump.

*   `20190301.sat` (`v1.0.0`) (`Size: 2.36 MiB`): Wikipedia dataset for sat,
    parsed from 20190301 dump.

*   `20190301.sc` (`v1.0.0`) (`Size: 4.39 MiB`): Wikipedia dataset for sc,
    parsed from 20190301 dump.

*   `20190301.scn` (`v1.0.0`) (`Size: 11.83 MiB`): Wikipedia dataset for scn,
    parsed from 20190301 dump.

*   `20190301.sco` (`v1.0.0`) (`Size: 57.80 MiB`): Wikipedia dataset for sco,
    parsed from 20190301 dump.

*   `20190301.sd` (`v1.0.0`) (`Size: 12.62 MiB`): Wikipedia dataset for sd,
    parsed from 20190301 dump.

*   `20190301.se` (`v1.0.0`) (`Size: 3.30 MiB`): Wikipedia dataset for se,
    parsed from 20190301 dump.

*   `20190301.sg` (`v1.0.0`) (`Size: 286.02 KiB`): Wikipedia dataset for sg,
    parsed from 20190301 dump.

*   `20190301.sh` (`v1.0.0`) (`Size: 406.72 MiB`): Wikipedia dataset for sh,
    parsed from 20190301 dump.

*   `20190301.si` (`v1.0.0`) (`Size: 36.84 MiB`): Wikipedia dataset for si,
    parsed from 20190301 dump.

*   `20190301.simple` (`v1.0.0`) (`Size: 156.11 MiB`): Wikipedia dataset for
    simple, parsed from 20190301 dump.

*   `20190301.sk` (`v1.0.0`) (`Size: 254.37 MiB`): Wikipedia dataset for sk,
    parsed from 20190301 dump.

*   `20190301.sl` (`v1.0.0`) (`Size: 201.41 MiB`): Wikipedia dataset for sl,
    parsed from 20190301 dump.

*   `20190301.sm` (`v1.0.0`) (`Size: 678.46 KiB`): Wikipedia dataset for sm,
    parsed from 20190301 dump.

*   `20190301.sn` (`v1.0.0`) (`Size: 2.02 MiB`): Wikipedia dataset for sn,
    parsed from 20190301 dump.

*   `20190301.so` (`v1.0.0`) (`Size: 8.17 MiB`): Wikipedia dataset for so,
    parsed from 20190301 dump.

*   `20190301.sq` (`v1.0.0`) (`Size: 77.55 MiB`): Wikipedia dataset for sq,
    parsed from 20190301 dump.

*   `20190301.sr` (`v1.0.0`) (`Size: 725.30 MiB`): Wikipedia dataset for sr,
    parsed from 20190301 dump.

*   `20190301.srn` (`v1.0.0`) (`Size: 634.21 KiB`): Wikipedia dataset for srn,
    parsed from 20190301 dump.

*   `20190301.ss` (`v1.0.0`) (`Size: 737.58 KiB`): Wikipedia dataset for ss,
    parsed from 20190301 dump.

*   `20190301.st` (`v1.0.0`) (`Size: 482.27 KiB`): Wikipedia dataset for st,
    parsed from 20190301 dump.

*   `20190301.stq` (`v1.0.0`) (`Size: 3.26 MiB`): Wikipedia dataset for stq,
    parsed from 20190301 dump.

*   `20190301.su` (`v1.0.0`) (`Size: 20.52 MiB`): Wikipedia dataset for su,
    parsed from 20190301 dump.

*   `20190301.sv` (`v1.0.0`) (`Size: 1.64 GiB`): Wikipedia dataset for sv,
    parsed from 20190301 dump.

*   `20190301.sw` (`v1.0.0`) (`Size: 27.60 MiB`): Wikipedia dataset for sw,
    parsed from 20190301 dump.

*   `20190301.szl` (`v1.0.0`) (`Size: 4.06 MiB`): Wikipedia dataset for szl,
    parsed from 20190301 dump.

*   `20190301.ta` (`v1.0.0`) (`Size: 141.07 MiB`): Wikipedia dataset for ta,
    parsed from 20190301 dump.

*   `20190301.tcy` (`v1.0.0`) (`Size: 2.33 MiB`): Wikipedia dataset for tcy,
    parsed from 20190301 dump.

*   `20190301.te` (`v1.0.0`) (`Size: 113.16 MiB`): Wikipedia dataset for te,
    parsed from 20190301 dump.

*   `20190301.tet` (`v1.0.0`) (`Size: 1.06 MiB`): Wikipedia dataset for tet,
    parsed from 20190301 dump.

*   `20190301.tg` (`v1.0.0`) (`Size: 36.95 MiB`): Wikipedia dataset for tg,
    parsed from 20190301 dump.

*   `20190301.th` (`v1.0.0`) (`Size: 254.00 MiB`): Wikipedia dataset for th,
    parsed from 20190301 dump.

*   `20190301.ti` (`v1.0.0`) (`Size: 309.72 KiB`): Wikipedia dataset for ti,
    parsed from 20190301 dump.

*   `20190301.tk` (`v1.0.0`) (`Size: 4.50 MiB`): Wikipedia dataset for tk,
    parsed from 20190301 dump.

*   `20190301.tl` (`v1.0.0`) (`Size: 50.85 MiB`): Wikipedia dataset for tl,
    parsed from 20190301 dump.

*   `20190301.tn` (`v1.0.0`) (`Size: 1.21 MiB`): Wikipedia dataset for tn,
    parsed from 20190301 dump.

*   `20190301.to` (`v1.0.0`) (`Size: 775.10 KiB`): Wikipedia dataset for to,
    parsed from 20190301 dump.

*   `20190301.tpi` (`v1.0.0`) (`Size: 1.39 MiB`): Wikipedia dataset for tpi,
    parsed from 20190301 dump.

*   `20190301.tr` (`v1.0.0`) (`Size: 497.19 MiB`): Wikipedia dataset for tr,
    parsed from 20190301 dump.

*   `20190301.ts` (`v1.0.0`) (`Size: 1.39 MiB`): Wikipedia dataset for ts,
    parsed from 20190301 dump.

*   `20190301.tt` (`v1.0.0`) (`Size: 53.23 MiB`): Wikipedia dataset for tt,
    parsed from 20190301 dump.

*   `20190301.tum` (`v1.0.0`) (`Size: 309.58 KiB`): Wikipedia dataset for tum,
    parsed from 20190301 dump.

*   `20190301.tw` (`v1.0.0`) (`Size: 345.96 KiB`): Wikipedia dataset for tw,
    parsed from 20190301 dump.

*   `20190301.ty` (`v1.0.0`) (`Size: 485.56 KiB`): Wikipedia dataset for ty,
    parsed from 20190301 dump.

*   `20190301.tyv` (`v1.0.0`) (`Size: 2.60 MiB`): Wikipedia dataset for tyv,
    parsed from 20190301 dump.

*   `20190301.udm` (`v1.0.0`) (`Size: 2.94 MiB`): Wikipedia dataset for udm,
    parsed from 20190301 dump.

*   `20190301.ug` (`v1.0.0`) (`Size: 5.64 MiB`): Wikipedia dataset for ug,
    parsed from 20190301 dump.

*   `20190301.uk` (`v1.0.0`) (`Size: 1.28 GiB`): Wikipedia dataset for uk,
    parsed from 20190301 dump.

*   `20190301.ur` (`v1.0.0`) (`Size: 129.57 MiB`): Wikipedia dataset for ur,
    parsed from 20190301 dump.

*   `20190301.uz` (`v1.0.0`) (`Size: 60.85 MiB`): Wikipedia dataset for uz,
    parsed from 20190301 dump.

*   `20190301.ve` (`v1.0.0`) (`Size: 257.59 KiB`): Wikipedia dataset for ve,
    parsed from 20190301 dump.

*   `20190301.vec` (`v1.0.0`) (`Size: 10.65 MiB`): Wikipedia dataset for vec,
    parsed from 20190301 dump.

*   `20190301.vep` (`v1.0.0`) (`Size: 4.59 MiB`): Wikipedia dataset for vep,
    parsed from 20190301 dump.

*   `20190301.vi` (`v1.0.0`) (`Size: 623.74 MiB`): Wikipedia dataset for vi,
    parsed from 20190301 dump.

*   `20190301.vls` (`v1.0.0`) (`Size: 6.58 MiB`): Wikipedia dataset for vls,
    parsed from 20190301 dump.

*   `20190301.vo` (`v1.0.0`) (`Size: 23.80 MiB`): Wikipedia dataset for vo,
    parsed from 20190301 dump.

*   `20190301.wa` (`v1.0.0`) (`Size: 8.75 MiB`): Wikipedia dataset for wa,
    parsed from 20190301 dump.

*   `20190301.war` (`v1.0.0`) (`Size: 256.72 MiB`): Wikipedia dataset for war,
    parsed from 20190301 dump.

*   `20190301.wo` (`v1.0.0`) (`Size: 1.54 MiB`): Wikipedia dataset for wo,
    parsed from 20190301 dump.

*   `20190301.wuu` (`v1.0.0`) (`Size: 9.08 MiB`): Wikipedia dataset for wuu,
    parsed from 20190301 dump.

*   `20190301.xal` (`v1.0.0`) (`Size: 1.64 MiB`): Wikipedia dataset for xal,
    parsed from 20190301 dump.

*   `20190301.xh` (`v1.0.0`) (`Size: 1.26 MiB`): Wikipedia dataset for xh,
    parsed from 20190301 dump.

*   `20190301.xmf` (`v1.0.0`) (`Size: 9.40 MiB`): Wikipedia dataset for xmf,
    parsed from 20190301 dump.

*   `20190301.yi` (`v1.0.0`) (`Size: 11.56 MiB`): Wikipedia dataset for yi,
    parsed from 20190301 dump.

*   `20190301.yo` (`v1.0.0`) (`Size: 11.55 MiB`): Wikipedia dataset for yo,
    parsed from 20190301 dump.

*   `20190301.za` (`v1.0.0`) (`Size: 735.93 KiB`): Wikipedia dataset for za,
    parsed from 20190301 dump.

*   `20190301.zea` (`v1.0.0`) (`Size: 2.47 MiB`): Wikipedia dataset for zea,
    parsed from 20190301 dump.

*   `20190301.zh` (`v1.0.0`) (`Size: 1.71 GiB`): Wikipedia dataset for zh,
    parsed from 20190301 dump.

*   `20190301.zh-classical` (`v1.0.0`) (`Size: 13.37 MiB`): Wikipedia dataset
    for zh-classical, parsed from 20190301 dump.

*   `20190301.zh-min-nan` (`v1.0.0`) (`Size: 50.30 MiB`): Wikipedia dataset for
    zh-min-nan, parsed from 20190301 dump.

*   `20190301.zh-yue` (`v1.0.0`) (`Size: 52.41 MiB`): Wikipedia dataset for
    zh-yue, parsed from 20190301 dump.

*   `20190301.zu` (`v1.0.0`) (`Size: 1.50 MiB`): Wikipedia dataset for zu,
    parsed from 20190301 dump.

## `wikipedia/20190301.aa`
Wikipedia dataset for aa, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1
TRAIN | 1

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ab`
Wikipedia dataset for ab, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,053
TRAIN | 4,053

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ace`
Wikipedia dataset for ace, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 9,264
TRAIN | 9,264

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ady`
Wikipedia dataset for ady, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 547
TRAIN | 547

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.af`
Wikipedia dataset for af, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 92,366
TRAIN | 92,366

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ak`
Wikipedia dataset for ak, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 628
TRAIN | 628

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.als`
Wikipedia dataset for als, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 27,705
TRAIN | 27,705

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.am`
Wikipedia dataset for am, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 13,231
TRAIN | 13,231

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.an`
Wikipedia dataset for an, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 47,536
TRAIN | 47,536

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ang`
Wikipedia dataset for ang, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,135
TRAIN | 3,135

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ar`
Wikipedia dataset for ar, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,272,226
TRAIN | 1,272,226

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.arc`
Wikipedia dataset for arc, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,272
TRAIN | 3,272

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.arz`
Wikipedia dataset for arz, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 28,136
TRAIN | 28,136

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.as`
Wikipedia dataset for as, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5,435
TRAIN | 5,435

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ast`
Wikipedia dataset for ast, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 106,275
TRAIN | 106,275

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.atj`
Wikipedia dataset for atj, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,005
TRAIN | 1,005

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.av`
Wikipedia dataset for av, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,918
TRAIN | 2,918

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ay`
Wikipedia dataset for ay, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,773
TRAIN | 4,773

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.az`
Wikipedia dataset for az, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 161,901
TRAIN | 161,901

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.azb`
Wikipedia dataset for azb, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 159,459
TRAIN | 159,459

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ba`
Wikipedia dataset for ba, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 51,934
TRAIN | 51,934

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bar`
Wikipedia dataset for bar, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 42,237
TRAIN | 42,237

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bat-smg`
Wikipedia dataset for bat-smg, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 19,344
TRAIN | 19,344

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bcl`
Wikipedia dataset for bcl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 9,025
TRAIN | 9,025

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.be`
Wikipedia dataset for be, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 164,589
TRAIN | 164,589

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.be-x-old`
Wikipedia dataset for be-x-old, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 93,527
TRAIN | 93,527

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bg`
Wikipedia dataset for bg, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 362,723
TRAIN | 362,723

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bh`
Wikipedia dataset for bh, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,725
TRAIN | 6,725

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bi`
Wikipedia dataset for bi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,352
TRAIN | 1,352

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bjn`
Wikipedia dataset for bjn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,476
TRAIN | 2,476

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bm`
Wikipedia dataset for bm, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 729
TRAIN | 729

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bn`
Wikipedia dataset for bn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 87,566
TRAIN | 87,566

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bo`
Wikipedia dataset for bo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 11,301
TRAIN | 11,301

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bpy`
Wikipedia dataset for bpy, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 25,360
TRAIN | 25,360

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.br`
Wikipedia dataset for br, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 76,055
TRAIN | 76,055

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bs`
Wikipedia dataset for bs, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 181,802
TRAIN | 181,802

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bug`
Wikipedia dataset for bug, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 14,378
TRAIN | 14,378

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.bxr`
Wikipedia dataset for bxr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,594
TRAIN | 2,594

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ca`
Wikipedia dataset for ca, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 650,189
TRAIN | 650,189

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.cbk-zam`
Wikipedia dataset for cbk-zam, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,289
TRAIN | 3,289

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.cdo`
Wikipedia dataset for cdo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 15,422
TRAIN | 15,422

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ce`
Wikipedia dataset for ce, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 213,978
TRAIN | 213,978

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ceb`
Wikipedia dataset for ceb, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,379,484
TRAIN | 5,379,484

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ch`
Wikipedia dataset for ch, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 496
TRAIN | 496

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.cho`
Wikipedia dataset for cho, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 14
TRAIN | 14

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.chr`
Wikipedia dataset for chr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 947
TRAIN | 947

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.chy`
Wikipedia dataset for chy, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 773
TRAIN | 773

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ckb`
Wikipedia dataset for ckb, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 23,099
TRAIN | 23,099

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.co`
Wikipedia dataset for co, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,232
TRAIN | 6,232

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.cr`
Wikipedia dataset for cr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 118
TRAIN | 118

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.crh`
Wikipedia dataset for crh, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,341
TRAIN | 6,341

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.cs`
Wikipedia dataset for cs, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 539,754
TRAIN | 539,754

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.csb`
Wikipedia dataset for csb, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5,620
TRAIN | 5,620

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.cu`
Wikipedia dataset for cu, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,463
TRAIN | 1,463

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.cv`
Wikipedia dataset for cv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 44,865
TRAIN | 44,865

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.cy`
Wikipedia dataset for cy, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 142,397
TRAIN | 142,397

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.da`
Wikipedia dataset for da, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 244,767
TRAIN | 244,767

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.de`
Wikipedia dataset for de, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,925,588
TRAIN | 2,925,588

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.din`
Wikipedia dataset for din, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 228
TRAIN | 228

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.diq`
Wikipedia dataset for diq, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 11,948
TRAIN | 11,948

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.dsb`
Wikipedia dataset for dsb, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,438
TRAIN | 3,438

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.dty`
Wikipedia dataset for dty, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,323
TRAIN | 3,323

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.dv`
Wikipedia dataset for dv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,156
TRAIN | 4,156

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.dz`
Wikipedia dataset for dz, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 286
TRAIN | 286

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ee`
Wikipedia dataset for ee, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 368
TRAIN | 368

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.el`
Wikipedia dataset for el, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 224,159
TRAIN | 224,159

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.eml`
Wikipedia dataset for eml, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 13,957
TRAIN | 13,957

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.en`
Wikipedia dataset for en, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,824,596
TRAIN | 5,824,596

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.eo`
Wikipedia dataset for eo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 353,663
TRAIN | 353,663

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.es`
Wikipedia dataset for es, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,728,167
TRAIN | 2,728,167

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.et`
Wikipedia dataset for et, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 288,641
TRAIN | 288,641

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.eu`
Wikipedia dataset for eu, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 400,162
TRAIN | 400,162

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ext`
Wikipedia dataset for ext, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,278
TRAIN | 3,278

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.fa`
Wikipedia dataset for fa, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,201,990
TRAIN | 2,201,990

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ff`
Wikipedia dataset for ff, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 298
TRAIN | 298

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.fi`
Wikipedia dataset for fi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 619,207
TRAIN | 619,207

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.fiu-vro`
Wikipedia dataset for fiu-vro, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,050
TRAIN | 6,050

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.fj`
Wikipedia dataset for fj, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 507
TRAIN | 507

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.fo`
Wikipedia dataset for fo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 12,935
TRAIN | 12,935

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.fr`
Wikipedia dataset for fr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,087,215
TRAIN | 2,087,215

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.frp`
Wikipedia dataset for frp, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,262
TRAIN | 4,262

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.frr`
Wikipedia dataset for frr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 9,706
TRAIN | 9,706

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.fur`
Wikipedia dataset for fur, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,508
TRAIN | 3,508

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.fy`
Wikipedia dataset for fy, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 41,573
TRAIN | 41,573

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ga`
Wikipedia dataset for ga, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 56,252
TRAIN | 56,252

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gag`
Wikipedia dataset for gag, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,034
TRAIN | 3,034

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gan`
Wikipedia dataset for gan, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,503
TRAIN | 6,503

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gd`
Wikipedia dataset for gd, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 14,891
TRAIN | 14,891

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gl`
Wikipedia dataset for gl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 203,961
TRAIN | 203,961

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.glk`
Wikipedia dataset for glk, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,432
TRAIN | 6,432

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gn`
Wikipedia dataset for gn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,337
TRAIN | 4,337

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gom`
Wikipedia dataset for gom, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,259
TRAIN | 4,259

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gor`
Wikipedia dataset for gor, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,467
TRAIN | 3,467

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.got`
Wikipedia dataset for got, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 715
TRAIN | 715

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gu`
Wikipedia dataset for gu, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 28,607
TRAIN | 28,607

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.gv`
Wikipedia dataset for gv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,996
TRAIN | 4,996

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ha`
Wikipedia dataset for ha, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,795
TRAIN | 3,795

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.hak`
Wikipedia dataset for hak, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 11,445
TRAIN | 11,445

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.haw`
Wikipedia dataset for haw, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,935
TRAIN | 3,935

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.he`
Wikipedia dataset for he, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 393,436
TRAIN | 393,436

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.hi`
Wikipedia dataset for hi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 156,142
TRAIN | 156,142

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.hif`
Wikipedia dataset for hif, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 10,036
TRAIN | 10,036

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ho`
Wikipedia dataset for ho, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3
TRAIN | 3

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.hr`
Wikipedia dataset for hr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 228,044
TRAIN | 228,044

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.hsb`
Wikipedia dataset for hsb, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 14,693
TRAIN | 14,693

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ht`
Wikipedia dataset for ht, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 56,093
TRAIN | 56,093

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.hu`
Wikipedia dataset for hu, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 625,614
TRAIN | 625,614

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.hy`
Wikipedia dataset for hy, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 575,357
TRAIN | 575,357

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ia`
Wikipedia dataset for ia, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 18,780
TRAIN | 18,780

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.id`
Wikipedia dataset for id, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 947,627
TRAIN | 947,627

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ie`
Wikipedia dataset for ie, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,403
TRAIN | 4,403

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ig`
Wikipedia dataset for ig, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,710
TRAIN | 2,710

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ii`
Wikipedia dataset for ii, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 14
TRAIN | 14

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ik`
Wikipedia dataset for ik, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 647
TRAIN | 647

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ilo`
Wikipedia dataset for ilo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 11,808
TRAIN | 11,808

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.inh`
Wikipedia dataset for inh, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 932
TRAIN | 932

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.io`
Wikipedia dataset for io, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 29,629
TRAIN | 29,629

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.is`
Wikipedia dataset for is, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 66,219
TRAIN | 66,219

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.it`
Wikipedia dataset for it, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,800,218
TRAIN | 1,800,218

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.iu`
Wikipedia dataset for iu, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 510
TRAIN | 510

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ja`
Wikipedia dataset for ja, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,382,683
TRAIN | 1,382,683

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.jam`
Wikipedia dataset for jam, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,692
TRAIN | 1,692

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.jbo`
Wikipedia dataset for jbo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,301
TRAIN | 1,301

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.jv`
Wikipedia dataset for jv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 72,893
TRAIN | 72,893

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ka`
Wikipedia dataset for ka, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 161,290
TRAIN | 161,290

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kaa`
Wikipedia dataset for kaa, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,192
TRAIN | 2,192

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kab`
Wikipedia dataset for kab, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,415
TRAIN | 3,415

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kbd`
Wikipedia dataset for kbd, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,608
TRAIN | 1,608

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kbp`
Wikipedia dataset for kbp, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,706
TRAIN | 1,706

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kg`
Wikipedia dataset for kg, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,240
TRAIN | 1,240

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ki`
Wikipedia dataset for ki, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,482
TRAIN | 1,482

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kj`
Wikipedia dataset for kj, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5
TRAIN | 5

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kk`
Wikipedia dataset for kk, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 266,609
TRAIN | 266,609

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kl`
Wikipedia dataset for kl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,713
TRAIN | 1,713

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.km`
Wikipedia dataset for km, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 10,889
TRAIN | 10,889

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kn`
Wikipedia dataset for kn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 24,679
TRAIN | 24,679

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ko`
Wikipedia dataset for ko, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 980,493
TRAIN | 980,493

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.koi`
Wikipedia dataset for koi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,964
TRAIN | 3,964

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.krc`
Wikipedia dataset for krc, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,317
TRAIN | 2,317

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ks`
Wikipedia dataset for ks, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 399
TRAIN | 399

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ksh`
Wikipedia dataset for ksh, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,356
TRAIN | 3,356

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ku`
Wikipedia dataset for ku, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 30,811
TRAIN | 30,811

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kv`
Wikipedia dataset for kv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,733
TRAIN | 6,733

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kw`
Wikipedia dataset for kw, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,913
TRAIN | 3,913

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ky`
Wikipedia dataset for ky, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 79,311
TRAIN | 79,311

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.la`
Wikipedia dataset for la, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 130,161
TRAIN | 130,161

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lad`
Wikipedia dataset for lad, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5,261
TRAIN | 5,261

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lb`
Wikipedia dataset for lb, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 61,607
TRAIN | 61,607

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lbe`
Wikipedia dataset for lbe, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,545
TRAIN | 1,545

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lez`
Wikipedia dataset for lez, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,348
TRAIN | 4,348

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lfn`
Wikipedia dataset for lfn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,741
TRAIN | 3,741

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lg`
Wikipedia dataset for lg, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,359
TRAIN | 2,359

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.li`
Wikipedia dataset for li, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 14,155
TRAIN | 14,155

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lij`
Wikipedia dataset for lij, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,281
TRAIN | 4,281

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lmo`
Wikipedia dataset for lmo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 43,911
TRAIN | 43,911

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ln`
Wikipedia dataset for ln, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,192
TRAIN | 3,192

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lo`
Wikipedia dataset for lo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,074
TRAIN | 4,074

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lrc`
Wikipedia dataset for lrc, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5,774
TRAIN | 5,774

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lt`
Wikipedia dataset for lt, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 217,121
TRAIN | 217,121

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ltg`
Wikipedia dataset for ltg, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 920
TRAIN | 920

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.lv`
Wikipedia dataset for lv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 91,567
TRAIN | 91,567

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mai`
Wikipedia dataset for mai, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 14,523
TRAIN | 14,523

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.map-bms`
Wikipedia dataset for map-bms, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 13,710
TRAIN | 13,710

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mdf`
Wikipedia dataset for mdf, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,344
TRAIN | 1,344

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mg`
Wikipedia dataset for mg, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 126,066
TRAIN | 126,066

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mh`
Wikipedia dataset for mh, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 8
TRAIN | 8

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mhr`
Wikipedia dataset for mhr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 12,204
TRAIN | 12,204

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mi`
Wikipedia dataset for mi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 7,174
TRAIN | 7,174

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.min`
Wikipedia dataset for min, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 226,002
TRAIN | 226,002

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mk`
Wikipedia dataset for mk, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 138,779
TRAIN | 138,779

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ml`
Wikipedia dataset for ml, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 112,979
TRAIN | 112,979

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mn`
Wikipedia dataset for mn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 23,195
TRAIN | 23,195

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mr`
Wikipedia dataset for mr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 95,825
TRAIN | 95,825

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mrj`
Wikipedia dataset for mrj, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 10,826
TRAIN | 10,826

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ms`
Wikipedia dataset for ms, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 357,957
TRAIN | 357,957

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mt`
Wikipedia dataset for mt, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,610
TRAIN | 4,610

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mus`
Wikipedia dataset for mus, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2
TRAIN | 2

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mwl`
Wikipedia dataset for mwl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,279
TRAIN | 4,279

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.my`
Wikipedia dataset for my, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 46,348
TRAIN | 46,348

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.myv`
Wikipedia dataset for myv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,077
TRAIN | 6,077

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.mzn`
Wikipedia dataset for mzn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 18,184
TRAIN | 18,184

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.na`
Wikipedia dataset for na, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,316
TRAIN | 1,316

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nah`
Wikipedia dataset for nah, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 10,613
TRAIN | 10,613

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nap`
Wikipedia dataset for nap, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 15,167
TRAIN | 15,167

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nds`
Wikipedia dataset for nds, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 45,754
TRAIN | 45,754

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nds-nl`
Wikipedia dataset for nds-nl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 8,644
TRAIN | 8,644

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ne`
Wikipedia dataset for ne, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 33,465
TRAIN | 33,465

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.new`
Wikipedia dataset for new, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 72,872
TRAIN | 72,872

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ng`
Wikipedia dataset for ng, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 21
TRAIN | 21

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nl`
Wikipedia dataset for nl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,409,491
TRAIN | 2,409,491

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nn`
Wikipedia dataset for nn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 213,859
TRAIN | 213,859

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.no`
Wikipedia dataset for no, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 783,420
TRAIN | 783,420

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nov`
Wikipedia dataset for nov, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,780
TRAIN | 1,780

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nrm`
Wikipedia dataset for nrm, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,048
TRAIN | 4,048

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nso`
Wikipedia dataset for nso, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 8,075
TRAIN | 8,075

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.nv`
Wikipedia dataset for nv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 7,105
TRAIN | 7,105

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ny`
Wikipedia dataset for ny, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 566
TRAIN | 566

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.oc`
Wikipedia dataset for oc, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 91,840
TRAIN | 91,840

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.olo`
Wikipedia dataset for olo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,348
TRAIN | 3,348

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.om`
Wikipedia dataset for om, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,054
TRAIN | 1,054

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.or`
Wikipedia dataset for or, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 28,368
TRAIN | 28,368

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.os`
Wikipedia dataset for os, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 13,490
TRAIN | 13,490

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pa`
Wikipedia dataset for pa, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 40,578
TRAIN | 40,578

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pag`
Wikipedia dataset for pag, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5,042
TRAIN | 5,042

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pam`
Wikipedia dataset for pam, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 8,721
TRAIN | 8,721

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pap`
Wikipedia dataset for pap, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,126
TRAIN | 2,126

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pcd`
Wikipedia dataset for pcd, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,485
TRAIN | 4,485

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pdc`
Wikipedia dataset for pdc, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,331
TRAIN | 2,331

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pfl`
Wikipedia dataset for pfl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,744
TRAIN | 3,744

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pi`
Wikipedia dataset for pi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,057
TRAIN | 3,057

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pih`
Wikipedia dataset for pih, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 748
TRAIN | 748

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pl`
Wikipedia dataset for pl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,610,189
TRAIN | 1,610,189

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pms`
Wikipedia dataset for pms, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 65,551
TRAIN | 65,551

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pnb`
Wikipedia dataset for pnb, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 50,764
TRAIN | 50,764

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pnt`
Wikipedia dataset for pnt, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 521
TRAIN | 521

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ps`
Wikipedia dataset for ps, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 10,554
TRAIN | 10,554

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.pt`
Wikipedia dataset for pt, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,393,069
TRAIN | 1,393,069

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.qu`
Wikipedia dataset for qu, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 29,495
TRAIN | 29,495

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.rm`
Wikipedia dataset for rm, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 3,710
TRAIN | 3,710

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.rmy`
Wikipedia dataset for rmy, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 693
TRAIN | 693

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.rn`
Wikipedia dataset for rn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 696
TRAIN | 696

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ro`
Wikipedia dataset for ro, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 393,012
TRAIN | 393,012

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.roa-rup`
Wikipedia dataset for roa-rup, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,245
TRAIN | 1,245

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.roa-tara`
Wikipedia dataset for roa-tara, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 9,288
TRAIN | 9,288

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ru`
Wikipedia dataset for ru, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 2,449,364
TRAIN | 2,449,364

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.rue`
Wikipedia dataset for rue, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 7,526
TRAIN | 7,526

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.rw`
Wikipedia dataset for rw, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,950
TRAIN | 1,950

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sa`
Wikipedia dataset for sa, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 21,846
TRAIN | 21,846

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sah`
Wikipedia dataset for sah, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 15,504
TRAIN | 15,504

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sat`
Wikipedia dataset for sat, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,036
TRAIN | 1,036

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sc`
Wikipedia dataset for sc, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,214
TRAIN | 6,214

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.scn`
Wikipedia dataset for scn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 31,330
TRAIN | 31,330

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sco`
Wikipedia dataset for sco, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 53,525
TRAIN | 53,525

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sd`
Wikipedia dataset for sd, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 16,930
TRAIN | 16,930

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.se`
Wikipedia dataset for se, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 8,127
TRAIN | 8,127

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sg`
Wikipedia dataset for sg, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 281
TRAIN | 281

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sh`
Wikipedia dataset for sh, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 3,923,606
TRAIN | 3,923,606

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.si`
Wikipedia dataset for si, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 25,922
TRAIN | 25,922

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.simple`
Wikipedia dataset for simple, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 143,427
TRAIN | 143,427

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sk`
Wikipedia dataset for sk, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 244,877
TRAIN | 244,877

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sl`
Wikipedia dataset for sl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 191,938
TRAIN | 191,938

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sm`
Wikipedia dataset for sm, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 957
TRAIN | 957

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sn`
Wikipedia dataset for sn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,656
TRAIN | 4,656

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.so`
Wikipedia dataset for so, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,587
TRAIN | 6,587

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sq`
Wikipedia dataset for sq, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 102,156
TRAIN | 102,156

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sr`
Wikipedia dataset for sr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 3,043,191
TRAIN | 3,043,191

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.srn`
Wikipedia dataset for srn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,234
TRAIN | 1,234

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ss`
Wikipedia dataset for ss, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 495
TRAIN | 495

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.st`
Wikipedia dataset for st, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 605
TRAIN | 605

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.stq`
Wikipedia dataset for stq, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 4,477
TRAIN | 4,477

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.su`
Wikipedia dataset for su, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 43,393
TRAIN | 43,393

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sv`
Wikipedia dataset for sv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 5,950,503
TRAIN | 5,950,503

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.sw`
Wikipedia dataset for sw, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 48,434
TRAIN | 48,434

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.szl`
Wikipedia dataset for szl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 8,603
TRAIN | 8,603

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ta`
Wikipedia dataset for ta, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 154,505
TRAIN | 154,505

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tcy`
Wikipedia dataset for tcy, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,267
TRAIN | 1,267

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.te`
Wikipedia dataset for te, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 91,857
TRAIN | 91,857

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tet`
Wikipedia dataset for tet, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,556
TRAIN | 1,556

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tg`
Wikipedia dataset for tg, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 96,808
TRAIN | 96,808

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.th`
Wikipedia dataset for th, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 224,144
TRAIN | 224,144

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ti`
Wikipedia dataset for ti, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 304
TRAIN | 304

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tk`
Wikipedia dataset for tk, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 6,743
TRAIN | 6,743

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tl`
Wikipedia dataset for tl, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 76,905
TRAIN | 76,905

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tn`
Wikipedia dataset for tn, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 751
TRAIN | 751

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.to`
Wikipedia dataset for to, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,577
TRAIN | 1,577

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tpi`
Wikipedia dataset for tpi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,523
TRAIN | 1,523

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tr`
Wikipedia dataset for tr, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 548,768
TRAIN | 548,768

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ts`
Wikipedia dataset for ts, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 665
TRAIN | 665

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tt`
Wikipedia dataset for tt, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 120,720
TRAIN | 120,720

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tum`
Wikipedia dataset for tum, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 638
TRAIN | 638

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tw`
Wikipedia dataset for tw, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 697
TRAIN | 697

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ty`
Wikipedia dataset for ty, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,279
TRAIN | 1,279

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.tyv`
Wikipedia dataset for tyv, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,563
TRAIN | 2,563

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.udm`
Wikipedia dataset for udm, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5,768
TRAIN | 5,768

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ug`
Wikipedia dataset for ug, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5,908
TRAIN | 5,908

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.uk`
Wikipedia dataset for uk, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,131,279
TRAIN | 1,131,279

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ur`
Wikipedia dataset for ur, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 330,776
TRAIN | 330,776

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.uz`
Wikipedia dataset for uz, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 149,537
TRAIN | 149,537

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.ve`
Wikipedia dataset for ve, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 337
TRAIN | 337

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.vec`
Wikipedia dataset for vec, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 13,433
TRAIN | 13,433

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.vep`
Wikipedia dataset for vep, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 7,230
TRAIN | 7,230

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.vi`
Wikipedia dataset for vi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,377,623
TRAIN | 1,377,623

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.vls`
Wikipedia dataset for vls, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 7,233
TRAIN | 7,233

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.vo`
Wikipedia dataset for vo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 122,640
TRAIN | 122,640

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.wa`
Wikipedia dataset for wa, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 15,283
TRAIN | 15,283

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.war`
Wikipedia dataset for war, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,263,705
TRAIN | 1,263,705

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.wo`
Wikipedia dataset for wo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,336
TRAIN | 1,336

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.wuu`
Wikipedia dataset for wuu, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 19,269
TRAIN | 19,269

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.xal`
Wikipedia dataset for xal, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,794
TRAIN | 2,794

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.xh`
Wikipedia dataset for xh, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,004
TRAIN | 1,004

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.xmf`
Wikipedia dataset for xmf, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 14,297
TRAIN | 14,297

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.yi`
Wikipedia dataset for yi, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 23,430
TRAIN | 23,430

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.yo`
Wikipedia dataset for yo, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 31,968
TRAIN | 31,968

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.za`
Wikipedia dataset for za, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 2,404
TRAIN | 2,404

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.zea`
Wikipedia dataset for zea, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 5,408
TRAIN | 5,408

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.zh`
Wikipedia dataset for zh, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | --------:
ALL   | 1,482,100
TRAIN | 1,482,100

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.zh-classical`
Wikipedia dataset for zh-classical, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 10,173
TRAIN | 10,173

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.zh-min-nan`
Wikipedia dataset for zh-min-nan, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 233,720
TRAIN | 233,720

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.zh-yue`
Wikipedia dataset for zh-yue, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 70,666
TRAIN | 70,666

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.zu`
Wikipedia dataset for zu, parsed from 20190301 dump.

Versions:

*   **`1.0.0`** (default): New split API
    (https://tensorflow.org/datasets/splits)
*   `0.0.4`: None
*   `0.0.3`: None

### Statistics

Split | Examples
:---- | -------:
ALL   | 1,184
TRAIN | 1,184

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## Citation
```
@ONLINE {wikidump,
    author = "Wikimedia Foundation",
    title  = "Wikimedia Downloads",
    url    = "https://dumps.wikimedia.org"
}
```

--------------------------------------------------------------------------------

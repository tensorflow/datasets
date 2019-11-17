<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikipedia" />
  <meta itemprop="description" content="Wikipedia dataset containing cleaned articles of all languages.&#10;The datasets are built from the Wikipedia dump&#10;(https://dumps.wikimedia.org/) with one split per language. Each example&#10;contains the content of one full Wikipedia article with cleaning to strip&#10;markdown and unwanted sections (references, etc.).&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wikipedia', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
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

*   `20190301.aa` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for aa, parsed
    from 20190301 dump.

*   `20190301.ab` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ab, parsed
    from 20190301 dump.

*   `20190301.ace` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ace,
    parsed from 20190301 dump.

*   `20190301.ady` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ady,
    parsed from 20190301 dump.

*   `20190301.af` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for af, parsed
    from 20190301 dump.

*   `20190301.ak` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ak, parsed
    from 20190301 dump.

*   `20190301.als` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for als,
    parsed from 20190301 dump.

*   `20190301.am` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for am, parsed
    from 20190301 dump.

*   `20190301.an` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for an, parsed
    from 20190301 dump.

*   `20190301.ang` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ang,
    parsed from 20190301 dump.

*   `20190301.ar` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ar, parsed
    from 20190301 dump.

*   `20190301.arc` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for arc,
    parsed from 20190301 dump.

*   `20190301.arz` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for arz,
    parsed from 20190301 dump.

*   `20190301.as` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for as, parsed
    from 20190301 dump.

*   `20190301.ast` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ast,
    parsed from 20190301 dump.

*   `20190301.atj` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for atj,
    parsed from 20190301 dump.

*   `20190301.av` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for av, parsed
    from 20190301 dump.

*   `20190301.ay` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ay, parsed
    from 20190301 dump.

*   `20190301.az` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for az, parsed
    from 20190301 dump.

*   `20190301.azb` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for azb,
    parsed from 20190301 dump.

*   `20190301.ba` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ba, parsed
    from 20190301 dump.

*   `20190301.bar` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bar,
    parsed from 20190301 dump.

*   `20190301.bat-smg` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    bat-smg, parsed from 20190301 dump.

*   `20190301.bcl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bcl,
    parsed from 20190301 dump.

*   `20190301.be` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for be, parsed
    from 20190301 dump.

*   `20190301.be-x-old` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    be-x-old, parsed from 20190301 dump.

*   `20190301.bg` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bg, parsed
    from 20190301 dump.

*   `20190301.bh` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bh, parsed
    from 20190301 dump.

*   `20190301.bi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bi, parsed
    from 20190301 dump.

*   `20190301.bjn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bjn,
    parsed from 20190301 dump.

*   `20190301.bm` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bm, parsed
    from 20190301 dump.

*   `20190301.bn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bn, parsed
    from 20190301 dump.

*   `20190301.bo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bo, parsed
    from 20190301 dump.

*   `20190301.bpy` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bpy,
    parsed from 20190301 dump.

*   `20190301.br` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for br, parsed
    from 20190301 dump.

*   `20190301.bs` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bs, parsed
    from 20190301 dump.

*   `20190301.bug` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bug,
    parsed from 20190301 dump.

*   `20190301.bxr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for bxr,
    parsed from 20190301 dump.

*   `20190301.ca` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ca, parsed
    from 20190301 dump.

*   `20190301.cbk-zam` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    cbk-zam, parsed from 20190301 dump.

*   `20190301.cdo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for cdo,
    parsed from 20190301 dump.

*   `20190301.ce` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ce, parsed
    from 20190301 dump.

*   `20190301.ceb` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ceb,
    parsed from 20190301 dump.

*   `20190301.ch` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ch, parsed
    from 20190301 dump.

*   `20190301.cho` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for cho,
    parsed from 20190301 dump.

*   `20190301.chr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for chr,
    parsed from 20190301 dump.

*   `20190301.chy` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for chy,
    parsed from 20190301 dump.

*   `20190301.ckb` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ckb,
    parsed from 20190301 dump.

*   `20190301.co` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for co, parsed
    from 20190301 dump.

*   `20190301.cr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for cr, parsed
    from 20190301 dump.

*   `20190301.crh` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for crh,
    parsed from 20190301 dump.

*   `20190301.cs` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for cs, parsed
    from 20190301 dump.

*   `20190301.csb` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for csb,
    parsed from 20190301 dump.

*   `20190301.cu` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for cu, parsed
    from 20190301 dump.

*   `20190301.cv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for cv, parsed
    from 20190301 dump.

*   `20190301.cy` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for cy, parsed
    from 20190301 dump.

*   `20190301.da` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for da, parsed
    from 20190301 dump.

*   `20190301.de` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for de, parsed
    from 20190301 dump.

*   `20190301.din` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for din,
    parsed from 20190301 dump.

*   `20190301.diq` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for diq,
    parsed from 20190301 dump.

*   `20190301.dsb` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for dsb,
    parsed from 20190301 dump.

*   `20190301.dty` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for dty,
    parsed from 20190301 dump.

*   `20190301.dv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for dv, parsed
    from 20190301 dump.

*   `20190301.dz` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for dz, parsed
    from 20190301 dump.

*   `20190301.ee` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ee, parsed
    from 20190301 dump.

*   `20190301.el` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for el, parsed
    from 20190301 dump.

*   `20190301.eml` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for eml,
    parsed from 20190301 dump.

*   `20190301.en` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for en, parsed
    from 20190301 dump.

*   `20190301.eo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for eo, parsed
    from 20190301 dump.

*   `20190301.es` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for es, parsed
    from 20190301 dump.

*   `20190301.et` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for et, parsed
    from 20190301 dump.

*   `20190301.eu` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for eu, parsed
    from 20190301 dump.

*   `20190301.ext` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ext,
    parsed from 20190301 dump.

*   `20190301.fa` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for fa, parsed
    from 20190301 dump.

*   `20190301.ff` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ff, parsed
    from 20190301 dump.

*   `20190301.fi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for fi, parsed
    from 20190301 dump.

*   `20190301.fiu-vro` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    fiu-vro, parsed from 20190301 dump.

*   `20190301.fj` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for fj, parsed
    from 20190301 dump.

*   `20190301.fo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for fo, parsed
    from 20190301 dump.

*   `20190301.fr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for fr, parsed
    from 20190301 dump.

*   `20190301.frp` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for frp,
    parsed from 20190301 dump.

*   `20190301.frr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for frr,
    parsed from 20190301 dump.

*   `20190301.fur` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for fur,
    parsed from 20190301 dump.

*   `20190301.fy` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for fy, parsed
    from 20190301 dump.

*   `20190301.ga` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ga, parsed
    from 20190301 dump.

*   `20190301.gag` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gag,
    parsed from 20190301 dump.

*   `20190301.gan` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gan,
    parsed from 20190301 dump.

*   `20190301.gd` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gd, parsed
    from 20190301 dump.

*   `20190301.gl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gl, parsed
    from 20190301 dump.

*   `20190301.glk` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for glk,
    parsed from 20190301 dump.

*   `20190301.gn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gn, parsed
    from 20190301 dump.

*   `20190301.gom` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gom,
    parsed from 20190301 dump.

*   `20190301.gor` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gor,
    parsed from 20190301 dump.

*   `20190301.got` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for got,
    parsed from 20190301 dump.

*   `20190301.gu` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gu, parsed
    from 20190301 dump.

*   `20190301.gv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for gv, parsed
    from 20190301 dump.

*   `20190301.ha` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ha, parsed
    from 20190301 dump.

*   `20190301.hak` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for hak,
    parsed from 20190301 dump.

*   `20190301.haw` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for haw,
    parsed from 20190301 dump.

*   `20190301.he` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for he, parsed
    from 20190301 dump.

*   `20190301.hi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for hi, parsed
    from 20190301 dump.

*   `20190301.hif` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for hif,
    parsed from 20190301 dump.

*   `20190301.ho` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ho, parsed
    from 20190301 dump.

*   `20190301.hr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for hr, parsed
    from 20190301 dump.

*   `20190301.hsb` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for hsb,
    parsed from 20190301 dump.

*   `20190301.ht` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ht, parsed
    from 20190301 dump.

*   `20190301.hu` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for hu, parsed
    from 20190301 dump.

*   `20190301.hy` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for hy, parsed
    from 20190301 dump.

*   `20190301.hz` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for hz, parsed
    from 20190301 dump.

*   `20190301.ia` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ia, parsed
    from 20190301 dump.

*   `20190301.id` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for id, parsed
    from 20190301 dump.

*   `20190301.ie` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ie, parsed
    from 20190301 dump.

*   `20190301.ig` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ig, parsed
    from 20190301 dump.

*   `20190301.ii` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ii, parsed
    from 20190301 dump.

*   `20190301.ik` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ik, parsed
    from 20190301 dump.

*   `20190301.ilo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ilo,
    parsed from 20190301 dump.

*   `20190301.inh` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for inh,
    parsed from 20190301 dump.

*   `20190301.io` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for io, parsed
    from 20190301 dump.

*   `20190301.is` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for is, parsed
    from 20190301 dump.

*   `20190301.it` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for it, parsed
    from 20190301 dump.

*   `20190301.iu` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for iu, parsed
    from 20190301 dump.

*   `20190301.ja` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ja, parsed
    from 20190301 dump.

*   `20190301.jam` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for jam,
    parsed from 20190301 dump.

*   `20190301.jbo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for jbo,
    parsed from 20190301 dump.

*   `20190301.jv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for jv, parsed
    from 20190301 dump.

*   `20190301.ka` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ka, parsed
    from 20190301 dump.

*   `20190301.kaa` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kaa,
    parsed from 20190301 dump.

*   `20190301.kab` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kab,
    parsed from 20190301 dump.

*   `20190301.kbd` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kbd,
    parsed from 20190301 dump.

*   `20190301.kbp` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kbp,
    parsed from 20190301 dump.

*   `20190301.kg` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kg, parsed
    from 20190301 dump.

*   `20190301.ki` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ki, parsed
    from 20190301 dump.

*   `20190301.kj` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kj, parsed
    from 20190301 dump.

*   `20190301.kk` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kk, parsed
    from 20190301 dump.

*   `20190301.kl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kl, parsed
    from 20190301 dump.

*   `20190301.km` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for km, parsed
    from 20190301 dump.

*   `20190301.kn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kn, parsed
    from 20190301 dump.

*   `20190301.ko` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ko, parsed
    from 20190301 dump.

*   `20190301.koi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for koi,
    parsed from 20190301 dump.

*   `20190301.kr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kr, parsed
    from 20190301 dump.

*   `20190301.krc` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for krc,
    parsed from 20190301 dump.

*   `20190301.ks` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ks, parsed
    from 20190301 dump.

*   `20190301.ksh` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ksh,
    parsed from 20190301 dump.

*   `20190301.ku` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ku, parsed
    from 20190301 dump.

*   `20190301.kv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kv, parsed
    from 20190301 dump.

*   `20190301.kw` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for kw, parsed
    from 20190301 dump.

*   `20190301.ky` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ky, parsed
    from 20190301 dump.

*   `20190301.la` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for la, parsed
    from 20190301 dump.

*   `20190301.lad` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lad,
    parsed from 20190301 dump.

*   `20190301.lb` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lb, parsed
    from 20190301 dump.

*   `20190301.lbe` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lbe,
    parsed from 20190301 dump.

*   `20190301.lez` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lez,
    parsed from 20190301 dump.

*   `20190301.lfn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lfn,
    parsed from 20190301 dump.

*   `20190301.lg` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lg, parsed
    from 20190301 dump.

*   `20190301.li` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for li, parsed
    from 20190301 dump.

*   `20190301.lij` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lij,
    parsed from 20190301 dump.

*   `20190301.lmo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lmo,
    parsed from 20190301 dump.

*   `20190301.ln` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ln, parsed
    from 20190301 dump.

*   `20190301.lo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lo, parsed
    from 20190301 dump.

*   `20190301.lrc` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lrc,
    parsed from 20190301 dump.

*   `20190301.lt` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lt, parsed
    from 20190301 dump.

*   `20190301.ltg` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ltg,
    parsed from 20190301 dump.

*   `20190301.lv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for lv, parsed
    from 20190301 dump.

*   `20190301.mai` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mai,
    parsed from 20190301 dump.

*   `20190301.map-bms` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    map-bms, parsed from 20190301 dump.

*   `20190301.mdf` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mdf,
    parsed from 20190301 dump.

*   `20190301.mg` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mg, parsed
    from 20190301 dump.

*   `20190301.mh` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mh, parsed
    from 20190301 dump.

*   `20190301.mhr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mhr,
    parsed from 20190301 dump.

*   `20190301.mi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mi, parsed
    from 20190301 dump.

*   `20190301.min` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for min,
    parsed from 20190301 dump.

*   `20190301.mk` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mk, parsed
    from 20190301 dump.

*   `20190301.ml` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ml, parsed
    from 20190301 dump.

*   `20190301.mn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mn, parsed
    from 20190301 dump.

*   `20190301.mr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mr, parsed
    from 20190301 dump.

*   `20190301.mrj` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mrj,
    parsed from 20190301 dump.

*   `20190301.ms` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ms, parsed
    from 20190301 dump.

*   `20190301.mt` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mt, parsed
    from 20190301 dump.

*   `20190301.mus` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mus,
    parsed from 20190301 dump.

*   `20190301.mwl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mwl,
    parsed from 20190301 dump.

*   `20190301.my` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for my, parsed
    from 20190301 dump.

*   `20190301.myv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for myv,
    parsed from 20190301 dump.

*   `20190301.mzn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for mzn,
    parsed from 20190301 dump.

*   `20190301.na` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for na, parsed
    from 20190301 dump.

*   `20190301.nah` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nah,
    parsed from 20190301 dump.

*   `20190301.nap` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nap,
    parsed from 20190301 dump.

*   `20190301.nds` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nds,
    parsed from 20190301 dump.

*   `20190301.nds-nl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nds-nl,
    parsed from 20190301 dump.

*   `20190301.ne` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ne, parsed
    from 20190301 dump.

*   `20190301.new` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for new,
    parsed from 20190301 dump.

*   `20190301.ng` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ng, parsed
    from 20190301 dump.

*   `20190301.nl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nl, parsed
    from 20190301 dump.

*   `20190301.nn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nn, parsed
    from 20190301 dump.

*   `20190301.no` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for no, parsed
    from 20190301 dump.

*   `20190301.nov` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nov,
    parsed from 20190301 dump.

*   `20190301.nrm` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nrm,
    parsed from 20190301 dump.

*   `20190301.nso` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nso,
    parsed from 20190301 dump.

*   `20190301.nv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for nv, parsed
    from 20190301 dump.

*   `20190301.ny` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ny, parsed
    from 20190301 dump.

*   `20190301.oc` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for oc, parsed
    from 20190301 dump.

*   `20190301.olo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for olo,
    parsed from 20190301 dump.

*   `20190301.om` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for om, parsed
    from 20190301 dump.

*   `20190301.or` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for or, parsed
    from 20190301 dump.

*   `20190301.os` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for os, parsed
    from 20190301 dump.

*   `20190301.pa` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pa, parsed
    from 20190301 dump.

*   `20190301.pag` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pag,
    parsed from 20190301 dump.

*   `20190301.pam` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pam,
    parsed from 20190301 dump.

*   `20190301.pap` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pap,
    parsed from 20190301 dump.

*   `20190301.pcd` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pcd,
    parsed from 20190301 dump.

*   `20190301.pdc` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pdc,
    parsed from 20190301 dump.

*   `20190301.pfl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pfl,
    parsed from 20190301 dump.

*   `20190301.pi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pi, parsed
    from 20190301 dump.

*   `20190301.pih` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pih,
    parsed from 20190301 dump.

*   `20190301.pl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pl, parsed
    from 20190301 dump.

*   `20190301.pms` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pms,
    parsed from 20190301 dump.

*   `20190301.pnb` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pnb,
    parsed from 20190301 dump.

*   `20190301.pnt` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pnt,
    parsed from 20190301 dump.

*   `20190301.ps` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ps, parsed
    from 20190301 dump.

*   `20190301.pt` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for pt, parsed
    from 20190301 dump.

*   `20190301.qu` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for qu, parsed
    from 20190301 dump.

*   `20190301.rm` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for rm, parsed
    from 20190301 dump.

*   `20190301.rmy` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for rmy,
    parsed from 20190301 dump.

*   `20190301.rn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for rn, parsed
    from 20190301 dump.

*   `20190301.ro` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ro, parsed
    from 20190301 dump.

*   `20190301.roa-rup` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    roa-rup, parsed from 20190301 dump.

*   `20190301.roa-tara` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    roa-tara, parsed from 20190301 dump.

*   `20190301.ru` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ru, parsed
    from 20190301 dump.

*   `20190301.rue` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for rue,
    parsed from 20190301 dump.

*   `20190301.rw` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for rw, parsed
    from 20190301 dump.

*   `20190301.sa` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sa, parsed
    from 20190301 dump.

*   `20190301.sah` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sah,
    parsed from 20190301 dump.

*   `20190301.sat` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sat,
    parsed from 20190301 dump.

*   `20190301.sc` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sc, parsed
    from 20190301 dump.

*   `20190301.scn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for scn,
    parsed from 20190301 dump.

*   `20190301.sco` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sco,
    parsed from 20190301 dump.

*   `20190301.sd` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sd, parsed
    from 20190301 dump.

*   `20190301.se` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for se, parsed
    from 20190301 dump.

*   `20190301.sg` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sg, parsed
    from 20190301 dump.

*   `20190301.sh` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sh, parsed
    from 20190301 dump.

*   `20190301.si` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for si, parsed
    from 20190301 dump.

*   `20190301.simple` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for simple,
    parsed from 20190301 dump.

*   `20190301.sk` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sk, parsed
    from 20190301 dump.

*   `20190301.sl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sl, parsed
    from 20190301 dump.

*   `20190301.sm` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sm, parsed
    from 20190301 dump.

*   `20190301.sn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sn, parsed
    from 20190301 dump.

*   `20190301.so` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for so, parsed
    from 20190301 dump.

*   `20190301.sq` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sq, parsed
    from 20190301 dump.

*   `20190301.sr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sr, parsed
    from 20190301 dump.

*   `20190301.srn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for srn,
    parsed from 20190301 dump.

*   `20190301.ss` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ss, parsed
    from 20190301 dump.

*   `20190301.st` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for st, parsed
    from 20190301 dump.

*   `20190301.stq` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for stq,
    parsed from 20190301 dump.

*   `20190301.su` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for su, parsed
    from 20190301 dump.

*   `20190301.sv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sv, parsed
    from 20190301 dump.

*   `20190301.sw` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for sw, parsed
    from 20190301 dump.

*   `20190301.szl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for szl,
    parsed from 20190301 dump.

*   `20190301.ta` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ta, parsed
    from 20190301 dump.

*   `20190301.tcy` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tcy,
    parsed from 20190301 dump.

*   `20190301.te` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for te, parsed
    from 20190301 dump.

*   `20190301.tet` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tet,
    parsed from 20190301 dump.

*   `20190301.tg` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tg, parsed
    from 20190301 dump.

*   `20190301.th` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for th, parsed
    from 20190301 dump.

*   `20190301.ti` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ti, parsed
    from 20190301 dump.

*   `20190301.tk` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tk, parsed
    from 20190301 dump.

*   `20190301.tl` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tl, parsed
    from 20190301 dump.

*   `20190301.tn` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tn, parsed
    from 20190301 dump.

*   `20190301.to` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for to, parsed
    from 20190301 dump.

*   `20190301.tpi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tpi,
    parsed from 20190301 dump.

*   `20190301.tr` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tr, parsed
    from 20190301 dump.

*   `20190301.ts` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ts, parsed
    from 20190301 dump.

*   `20190301.tt` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tt, parsed
    from 20190301 dump.

*   `20190301.tum` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tum,
    parsed from 20190301 dump.

*   `20190301.tw` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tw, parsed
    from 20190301 dump.

*   `20190301.ty` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ty, parsed
    from 20190301 dump.

*   `20190301.tyv` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for tyv,
    parsed from 20190301 dump.

*   `20190301.udm` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for udm,
    parsed from 20190301 dump.

*   `20190301.ug` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ug, parsed
    from 20190301 dump.

*   `20190301.uk` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for uk, parsed
    from 20190301 dump.

*   `20190301.ur` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ur, parsed
    from 20190301 dump.

*   `20190301.uz` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for uz, parsed
    from 20190301 dump.

*   `20190301.ve` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for ve, parsed
    from 20190301 dump.

*   `20190301.vec` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for vec,
    parsed from 20190301 dump.

*   `20190301.vep` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for vep,
    parsed from 20190301 dump.

*   `20190301.vi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for vi, parsed
    from 20190301 dump.

*   `20190301.vls` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for vls,
    parsed from 20190301 dump.

*   `20190301.vo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for vo, parsed
    from 20190301 dump.

*   `20190301.wa` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for wa, parsed
    from 20190301 dump.

*   `20190301.war` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for war,
    parsed from 20190301 dump.

*   `20190301.wo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for wo, parsed
    from 20190301 dump.

*   `20190301.wuu` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for wuu,
    parsed from 20190301 dump.

*   `20190301.xal` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for xal,
    parsed from 20190301 dump.

*   `20190301.xh` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for xh, parsed
    from 20190301 dump.

*   `20190301.xmf` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for xmf,
    parsed from 20190301 dump.

*   `20190301.yi` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for yi, parsed
    from 20190301 dump.

*   `20190301.yo` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for yo, parsed
    from 20190301 dump.

*   `20190301.za` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for za, parsed
    from 20190301 dump.

*   `20190301.zea` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for zea,
    parsed from 20190301 dump.

*   `20190301.zh` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for zh, parsed
    from 20190301 dump.

*   `20190301.zh-classical` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    zh-classical, parsed from 20190301 dump.

*   `20190301.zh-min-nan` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for
    zh-min-nan, parsed from 20190301 dump.

*   `20190301.zh-yue` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for zh-yue,
    parsed from 20190301 dump.

*   `20190301.zu` (`v0.0.4`) (`Size: ?? GiB`): Wikipedia dataset for zu, parsed
    from 20190301 dump.

## `wikipedia/20190301.aa`
Wikipedia dataset for aa, parsed from 20190301 dump.

Versions:

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.hz`
Wikipedia dataset for hz, parsed from 20190301 dump.

Versions:

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## `wikipedia/20190301.kr`
Wikipedia dataset for kr, parsed from 20190301 dump.

Versions:

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

*   **`0.0.4`** (default):

### Statistics
None computed

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

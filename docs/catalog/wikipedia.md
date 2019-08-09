<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="wikipedia" />
  <meta itemprop="description" content="Wikipedia dataset containing cleaned articles of all languages. The datasets are built from the Wikipedia dump (https://dumps.wikimedia.org/) with one split per language. Each example contains the content of one full Wikipedia article with cleaning to strip markdown and unwanted sections (references, etc.)." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wikipedia" />
  <meta itemprop="sameAs" content="https://dumps.wikimedia.org" />
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

*   `20190301.aa` (`v0.0.2`) (`Size: 44.09 KiB`): Wikipedia dataset for aa,
    parsed from 20190301 dump.

*   `20190301.ab` (`v0.0.2`) (`Size: 1.31 MiB`): Wikipedia dataset for ab,
    parsed from 20190301 dump.

*   `20190301.ace` (`v0.0.2`) (`Size: 2.66 MiB`): Wikipedia dataset for ace,
    parsed from 20190301 dump.

*   `20190301.ady` (`v0.0.2`) (`Size: 349.43 KiB`): Wikipedia dataset for ady,
    parsed from 20190301 dump.

*   `20190301.af` (`v0.0.2`) (`Size: 84.13 MiB`): Wikipedia dataset for af,
    parsed from 20190301 dump.

*   `20190301.ak` (`v0.0.2`) (`Size: 377.84 KiB`): Wikipedia dataset for ak,
    parsed from 20190301 dump.

*   `20190301.als` (`v0.0.2`) (`Size: 46.90 MiB`): Wikipedia dataset for als,
    parsed from 20190301 dump.

*   `20190301.am` (`v0.0.2`) (`Size: 6.54 MiB`): Wikipedia dataset for am,
    parsed from 20190301 dump.

*   `20190301.an` (`v0.0.2`) (`Size: 31.39 MiB`): Wikipedia dataset for an,
    parsed from 20190301 dump.

*   `20190301.ang` (`v0.0.2`) (`Size: 3.77 MiB`): Wikipedia dataset for ang,
    parsed from 20190301 dump.

*   `20190301.ar` (`v0.0.2`) (`Size: 805.82 MiB`): Wikipedia dataset for ar,
    parsed from 20190301 dump.

*   `20190301.arc` (`v0.0.2`) (`Size: 952.49 KiB`): Wikipedia dataset for arc,
    parsed from 20190301 dump.

*   `20190301.arz` (`v0.0.2`) (`Size: 20.32 MiB`): Wikipedia dataset for arz,
    parsed from 20190301 dump.

*   `20190301.as` (`v0.0.2`) (`Size: 19.06 MiB`): Wikipedia dataset for as,
    parsed from 20190301 dump.

*   `20190301.ast` (`v0.0.2`) (`Size: 216.68 MiB`): Wikipedia dataset for ast,
    parsed from 20190301 dump.

*   `20190301.atj` (`v0.0.2`) (`Size: 467.05 KiB`): Wikipedia dataset for atj,
    parsed from 20190301 dump.

*   `20190301.av` (`v0.0.2`) (`Size: 3.61 MiB`): Wikipedia dataset for av,
    parsed from 20190301 dump.

*   `20190301.ay` (`v0.0.2`) (`Size: 2.06 MiB`): Wikipedia dataset for ay,
    parsed from 20190301 dump.

*   `20190301.az` (`v0.0.2`) (`Size: 163.04 MiB`): Wikipedia dataset for az,
    parsed from 20190301 dump.

*   `20190301.azb` (`v0.0.2`) (`Size: 50.59 MiB`): Wikipedia dataset for azb,
    parsed from 20190301 dump.

*   `20190301.ba` (`v0.0.2`) (`Size: 55.04 MiB`): Wikipedia dataset for ba,
    parsed from 20190301 dump.

*   `20190301.bar` (`v0.0.2`) (`Size: 30.14 MiB`): Wikipedia dataset for bar,
    parsed from 20190301 dump.

*   `20190301.bat-smg` (`v0.0.2`) (`Size: 4.61 MiB`): Wikipedia dataset for
    bat-smg, parsed from 20190301 dump.

*   `20190301.bcl` (`v0.0.2`) (`Size: 6.18 MiB`): Wikipedia dataset for bcl,
    parsed from 20190301 dump.

*   `20190301.be` (`v0.0.2`) (`Size: 192.23 MiB`): Wikipedia dataset for be,
    parsed from 20190301 dump.

*   `20190301.be-x-old` (`v0.0.2`) (`Size: 74.77 MiB`): Wikipedia dataset for
    be-x-old, parsed from 20190301 dump.

*   `20190301.bg` (`v0.0.2`) (`Size: 326.20 MiB`): Wikipedia dataset for bg,
    parsed from 20190301 dump.

*   `20190301.bh` (`v0.0.2`) (`Size: 13.28 MiB`): Wikipedia dataset for bh,
    parsed from 20190301 dump.

*   `20190301.bi` (`v0.0.2`) (`Size: 424.88 KiB`): Wikipedia dataset for bi,
    parsed from 20190301 dump.

*   `20190301.bjn` (`v0.0.2`) (`Size: 2.09 MiB`): Wikipedia dataset for bjn,
    parsed from 20190301 dump.

*   `20190301.bm` (`v0.0.2`) (`Size: 447.98 KiB`): Wikipedia dataset for bm,
    parsed from 20190301 dump.

*   `20190301.bn` (`v0.0.2`) (`Size: 145.04 MiB`): Wikipedia dataset for bn,
    parsed from 20190301 dump.

*   `20190301.bo` (`v0.0.2`) (`Size: 12.41 MiB`): Wikipedia dataset for bo,
    parsed from 20190301 dump.

*   `20190301.bpy` (`v0.0.2`) (`Size: 5.05 MiB`): Wikipedia dataset for bpy,
    parsed from 20190301 dump.

*   `20190301.br` (`v0.0.2`) (`Size: 49.14 MiB`): Wikipedia dataset for br,
    parsed from 20190301 dump.

*   `20190301.bs` (`v0.0.2`) (`Size: 103.26 MiB`): Wikipedia dataset for bs,
    parsed from 20190301 dump.

*   `20190301.bug` (`v0.0.2`) (`Size: 1.76 MiB`): Wikipedia dataset for bug,
    parsed from 20190301 dump.

*   `20190301.bxr` (`v0.0.2`) (`Size: 3.21 MiB`): Wikipedia dataset for bxr,
    parsed from 20190301 dump.

*   `20190301.ca` (`v0.0.2`) (`Size: 849.65 MiB`): Wikipedia dataset for ca,
    parsed from 20190301 dump.

*   `20190301.cbk-zam` (`v0.0.2`) (`Size: 1.84 MiB`): Wikipedia dataset for
    cbk-zam, parsed from 20190301 dump.

*   `20190301.cdo` (`v0.0.2`) (`Size: 3.22 MiB`): Wikipedia dataset for cdo,
    parsed from 20190301 dump.

*   `20190301.ce` (`v0.0.2`) (`Size: 43.89 MiB`): Wikipedia dataset for ce,
    parsed from 20190301 dump.

*   `20190301.ceb` (`v0.0.2`) (`Size: 1.79 GiB`): Wikipedia dataset for ceb,
    parsed from 20190301 dump.

*   `20190301.ch` (`v0.0.2`) (`Size: 684.97 KiB`): Wikipedia dataset for ch,
    parsed from 20190301 dump.

*   `20190301.cho` (`v0.0.2`) (`Size: 25.99 KiB`): Wikipedia dataset for cho,
    parsed from 20190301 dump.

*   `20190301.chr` (`v0.0.2`) (`Size: 651.25 KiB`): Wikipedia dataset for chr,
    parsed from 20190301 dump.

*   `20190301.chy` (`v0.0.2`) (`Size: 325.90 KiB`): Wikipedia dataset for chy,
    parsed from 20190301 dump.

*   `20190301.ckb` (`v0.0.2`) (`Size: 22.16 MiB`): Wikipedia dataset for ckb,
    parsed from 20190301 dump.

*   `20190301.co` (`v0.0.2`) (`Size: 3.38 MiB`): Wikipedia dataset for co,
    parsed from 20190301 dump.

*   `20190301.cr` (`v0.0.2`) (`Size: 259.71 KiB`): Wikipedia dataset for cr,
    parsed from 20190301 dump.

*   `20190301.crh` (`v0.0.2`) (`Size: 4.01 MiB`): Wikipedia dataset for crh,
    parsed from 20190301 dump.

*   `20190301.cs` (`v0.0.2`) (`Size: 759.21 MiB`): Wikipedia dataset for cs,
    parsed from 20190301 dump.

*   `20190301.csb` (`v0.0.2`) (`Size: 2.03 MiB`): Wikipedia dataset for csb,
    parsed from 20190301 dump.

*   `20190301.cu` (`v0.0.2`) (`Size: 631.49 KiB`): Wikipedia dataset for cu,
    parsed from 20190301 dump.

*   `20190301.cv` (`v0.0.2`) (`Size: 22.23 MiB`): Wikipedia dataset for cv,
    parsed from 20190301 dump.

*   `20190301.cy` (`v0.0.2`) (`Size: 64.37 MiB`): Wikipedia dataset for cy,
    parsed from 20190301 dump.

*   `20190301.da` (`v0.0.2`) (`Size: 323.53 MiB`): Wikipedia dataset for da,
    parsed from 20190301 dump.

*   `20190301.de` (`v0.0.2`) (`Size: 4.97 GiB`): Wikipedia dataset for de,
    parsed from 20190301 dump.

*   `20190301.din` (`v0.0.2`) (`Size: 457.06 KiB`): Wikipedia dataset for din,
    parsed from 20190301 dump.

*   `20190301.diq` (`v0.0.2`) (`Size: 7.24 MiB`): Wikipedia dataset for diq,
    parsed from 20190301 dump.

*   `20190301.dsb` (`v0.0.2`) (`Size: 3.54 MiB`): Wikipedia dataset for dsb,
    parsed from 20190301 dump.

*   `20190301.dty` (`v0.0.2`) (`Size: 4.95 MiB`): Wikipedia dataset for dty,
    parsed from 20190301 dump.

*   `20190301.dv` (`v0.0.2`) (`Size: 4.24 MiB`): Wikipedia dataset for dv,
    parsed from 20190301 dump.

*   `20190301.dz` (`v0.0.2`) (`Size: 360.01 KiB`): Wikipedia dataset for dz,
    parsed from 20190301 dump.

*   `20190301.ee` (`v0.0.2`) (`Size: 434.14 KiB`): Wikipedia dataset for ee,
    parsed from 20190301 dump.

*   `20190301.el` (`v0.0.2`) (`Size: 324.40 MiB`): Wikipedia dataset for el,
    parsed from 20190301 dump.

*   `20190301.eml` (`v0.0.2`) (`Size: 7.72 MiB`): Wikipedia dataset for eml,
    parsed from 20190301 dump.

*   `20190301.en` (`v0.0.2`) (`Size: 15.72 GiB`): Wikipedia dataset for en,
    parsed from 20190301 dump.

*   `20190301.eo` (`v0.0.2`) (`Size: 245.73 MiB`): Wikipedia dataset for eo,
    parsed from 20190301 dump.

*   `20190301.es` (`v0.0.2`) (`Size: 2.93 GiB`): Wikipedia dataset for es,
    parsed from 20190301 dump.

*   `20190301.et` (`v0.0.2`) (`Size: 196.03 MiB`): Wikipedia dataset for et,
    parsed from 20190301 dump.

*   `20190301.eu` (`v0.0.2`) (`Size: 180.35 MiB`): Wikipedia dataset for eu,
    parsed from 20190301 dump.

*   `20190301.ext` (`v0.0.2`) (`Size: 2.40 MiB`): Wikipedia dataset for ext,
    parsed from 20190301 dump.

*   `20190301.fa` (`v0.0.2`) (`Size: 693.84 MiB`): Wikipedia dataset for fa,
    parsed from 20190301 dump.

*   `20190301.ff` (`v0.0.2`) (`Size: 387.75 KiB`): Wikipedia dataset for ff,
    parsed from 20190301 dump.

*   `20190301.fi` (`v0.0.2`) (`Size: 656.44 MiB`): Wikipedia dataset for fi,
    parsed from 20190301 dump.

*   `20190301.fiu-vro` (`v0.0.2`) (`Size: 2.00 MiB`): Wikipedia dataset for
    fiu-vro, parsed from 20190301 dump.

*   `20190301.fj` (`v0.0.2`) (`Size: 262.98 KiB`): Wikipedia dataset for fj,
    parsed from 20190301 dump.

*   `20190301.fo` (`v0.0.2`) (`Size: 13.67 MiB`): Wikipedia dataset for fo,
    parsed from 20190301 dump.

*   `20190301.fr` (`v0.0.2`) (`Size: 4.14 GiB`): Wikipedia dataset for fr,
    parsed from 20190301 dump.

*   `20190301.frp` (`v0.0.2`) (`Size: 2.03 MiB`): Wikipedia dataset for frp,
    parsed from 20190301 dump.

*   `20190301.frr` (`v0.0.2`) (`Size: 7.88 MiB`): Wikipedia dataset for frr,
    parsed from 20190301 dump.

*   `20190301.fur` (`v0.0.2`) (`Size: 2.29 MiB`): Wikipedia dataset for fur,
    parsed from 20190301 dump.

*   `20190301.fy` (`v0.0.2`) (`Size: 45.52 MiB`): Wikipedia dataset for fy,
    parsed from 20190301 dump.

*   `20190301.ga` (`v0.0.2`) (`Size: 24.78 MiB`): Wikipedia dataset for ga,
    parsed from 20190301 dump.

*   `20190301.gag` (`v0.0.2`) (`Size: 2.04 MiB`): Wikipedia dataset for gag,
    parsed from 20190301 dump.

*   `20190301.gan` (`v0.0.2`) (`Size: 3.82 MiB`): Wikipedia dataset for gan,
    parsed from 20190301 dump.

*   `20190301.gd` (`v0.0.2`) (`Size: 8.51 MiB`): Wikipedia dataset for gd,
    parsed from 20190301 dump.

*   `20190301.gl` (`v0.0.2`) (`Size: 235.07 MiB`): Wikipedia dataset for gl,
    parsed from 20190301 dump.

*   `20190301.glk` (`v0.0.2`) (`Size: 1.91 MiB`): Wikipedia dataset for glk,
    parsed from 20190301 dump.

*   `20190301.gn` (`v0.0.2`) (`Size: 3.37 MiB`): Wikipedia dataset for gn,
    parsed from 20190301 dump.

*   `20190301.gom` (`v0.0.2`) (`Size: 6.07 MiB`): Wikipedia dataset for gom,
    parsed from 20190301 dump.

*   `20190301.gor` (`v0.0.2`) (`Size: 1.28 MiB`): Wikipedia dataset for gor,
    parsed from 20190301 dump.

*   `20190301.got` (`v0.0.2`) (`Size: 604.10 KiB`): Wikipedia dataset for got,
    parsed from 20190301 dump.

*   `20190301.gu` (`v0.0.2`) (`Size: 27.23 MiB`): Wikipedia dataset for gu,
    parsed from 20190301 dump.

*   `20190301.gv` (`v0.0.2`) (`Size: 5.32 MiB`): Wikipedia dataset for gv,
    parsed from 20190301 dump.

*   `20190301.ha` (`v0.0.2`) (`Size: 1.62 MiB`): Wikipedia dataset for ha,
    parsed from 20190301 dump.

*   `20190301.hak` (`v0.0.2`) (`Size: 3.28 MiB`): Wikipedia dataset for hak,
    parsed from 20190301 dump.

*   `20190301.haw` (`v0.0.2`) (`Size: 1017.76 KiB`): Wikipedia dataset for haw,
    parsed from 20190301 dump.

*   `20190301.he` (`v0.0.2`) (`Size: 572.30 MiB`): Wikipedia dataset for he,
    parsed from 20190301 dump.

*   `20190301.hi` (`v0.0.2`) (`Size: 137.86 MiB`): Wikipedia dataset for hi,
    parsed from 20190301 dump.

*   `20190301.hif` (`v0.0.2`) (`Size: 4.57 MiB`): Wikipedia dataset for hif,
    parsed from 20190301 dump.

*   `20190301.ho` (`v0.0.2`) (`Size: 18.37 KiB`): Wikipedia dataset for ho,
    parsed from 20190301 dump.

*   `20190301.hr` (`v0.0.2`) (`Size: 246.05 MiB`): Wikipedia dataset for hr,
    parsed from 20190301 dump.

*   `20190301.hsb` (`v0.0.2`) (`Size: 10.38 MiB`): Wikipedia dataset for hsb,
    parsed from 20190301 dump.

*   `20190301.ht` (`v0.0.2`) (`Size: 10.23 MiB`): Wikipedia dataset for ht,
    parsed from 20190301 dump.

*   `20190301.hu` (`v0.0.2`) (`Size: 810.17 MiB`): Wikipedia dataset for hu,
    parsed from 20190301 dump.

*   `20190301.hy` (`v0.0.2`) (`Size: 277.53 MiB`): Wikipedia dataset for hy,
    parsed from 20190301 dump.

*   `20190301.hz` (`v0.0.2`) (`Size: 16.35 KiB`): Wikipedia dataset for hz,
    parsed from 20190301 dump.

*   `20190301.ia` (`v0.0.2`) (`Size: 7.85 MiB`): Wikipedia dataset for ia,
    parsed from 20190301 dump.

*   `20190301.id` (`v0.0.2`) (`Size: 523.94 MiB`): Wikipedia dataset for id,
    parsed from 20190301 dump.

*   `20190301.ie` (`v0.0.2`) (`Size: 1.70 MiB`): Wikipedia dataset for ie,
    parsed from 20190301 dump.

*   `20190301.ig` (`v0.0.2`) (`Size: 1.00 MiB`): Wikipedia dataset for ig,
    parsed from 20190301 dump.

*   `20190301.ii` (`v0.0.2`) (`Size: 30.88 KiB`): Wikipedia dataset for ii,
    parsed from 20190301 dump.

*   `20190301.ik` (`v0.0.2`) (`Size: 238.12 KiB`): Wikipedia dataset for ik,
    parsed from 20190301 dump.

*   `20190301.ilo` (`v0.0.2`) (`Size: 15.22 MiB`): Wikipedia dataset for ilo,
    parsed from 20190301 dump.

*   `20190301.inh` (`v0.0.2`) (`Size: 1.26 MiB`): Wikipedia dataset for inh,
    parsed from 20190301 dump.

*   `20190301.io` (`v0.0.2`) (`Size: 12.56 MiB`): Wikipedia dataset for io,
    parsed from 20190301 dump.

*   `20190301.is` (`v0.0.2`) (`Size: 41.86 MiB`): Wikipedia dataset for is,
    parsed from 20190301 dump.

*   `20190301.it` (`v0.0.2`) (`Size: 2.66 GiB`): Wikipedia dataset for it,
    parsed from 20190301 dump.

*   `20190301.iu` (`v0.0.2`) (`Size: 284.06 KiB`): Wikipedia dataset for iu,
    parsed from 20190301 dump.

*   `20190301.ja` (`v0.0.2`) (`Size: 2.74 GiB`): Wikipedia dataset for ja,
    parsed from 20190301 dump.

*   `20190301.jam` (`v0.0.2`) (`Size: 895.29 KiB`): Wikipedia dataset for jam,
    parsed from 20190301 dump.

*   `20190301.jbo` (`v0.0.2`) (`Size: 1.06 MiB`): Wikipedia dataset for jbo,
    parsed from 20190301 dump.

*   `20190301.jv` (`v0.0.2`) (`Size: 39.32 MiB`): Wikipedia dataset for jv,
    parsed from 20190301 dump.

*   `20190301.ka` (`v0.0.2`) (`Size: 131.78 MiB`): Wikipedia dataset for ka,
    parsed from 20190301 dump.

*   `20190301.kaa` (`v0.0.2`) (`Size: 1.35 MiB`): Wikipedia dataset for kaa,
    parsed from 20190301 dump.

*   `20190301.kab` (`v0.0.2`) (`Size: 3.62 MiB`): Wikipedia dataset for kab,
    parsed from 20190301 dump.

*   `20190301.kbd` (`v0.0.2`) (`Size: 1.65 MiB`): Wikipedia dataset for kbd,
    parsed from 20190301 dump.

*   `20190301.kbp` (`v0.0.2`) (`Size: 1.24 MiB`): Wikipedia dataset for kbp,
    parsed from 20190301 dump.

*   `20190301.kg` (`v0.0.2`) (`Size: 439.26 KiB`): Wikipedia dataset for kg,
    parsed from 20190301 dump.

*   `20190301.ki` (`v0.0.2`) (`Size: 370.78 KiB`): Wikipedia dataset for ki,
    parsed from 20190301 dump.

*   `20190301.kj` (`v0.0.2`) (`Size: 16.58 KiB`): Wikipedia dataset for kj,
    parsed from 20190301 dump.

*   `20190301.kk` (`v0.0.2`) (`Size: 113.46 MiB`): Wikipedia dataset for kk,
    parsed from 20190301 dump.

*   `20190301.kl` (`v0.0.2`) (`Size: 862.51 KiB`): Wikipedia dataset for kl,
    parsed from 20190301 dump.

*   `20190301.km` (`v0.0.2`) (`Size: 21.92 MiB`): Wikipedia dataset for km,
    parsed from 20190301 dump.

*   `20190301.kn` (`v0.0.2`) (`Size: 69.62 MiB`): Wikipedia dataset for kn,
    parsed from 20190301 dump.

*   `20190301.ko` (`v0.0.2`) (`Size: 625.16 MiB`): Wikipedia dataset for ko,
    parsed from 20190301 dump.

*   `20190301.koi` (`v0.0.2`) (`Size: 2.12 MiB`): Wikipedia dataset for koi,
    parsed from 20190301 dump.

*   `20190301.kr` (`v0.0.2`) (`Size: 13.89 KiB`): Wikipedia dataset for kr,
    parsed from 20190301 dump.

*   `20190301.krc` (`v0.0.2`) (`Size: 3.16 MiB`): Wikipedia dataset for krc,
    parsed from 20190301 dump.

*   `20190301.ks` (`v0.0.2`) (`Size: 309.15 KiB`): Wikipedia dataset for ks,
    parsed from 20190301 dump.

*   `20190301.ksh` (`v0.0.2`) (`Size: 3.07 MiB`): Wikipedia dataset for ksh,
    parsed from 20190301 dump.

*   `20190301.ku` (`v0.0.2`) (`Size: 17.09 MiB`): Wikipedia dataset for ku,
    parsed from 20190301 dump.

*   `20190301.kv` (`v0.0.2`) (`Size: 3.36 MiB`): Wikipedia dataset for kv,
    parsed from 20190301 dump.

*   `20190301.kw` (`v0.0.2`) (`Size: 1.71 MiB`): Wikipedia dataset for kw,
    parsed from 20190301 dump.

*   `20190301.ky` (`v0.0.2`) (`Size: 33.13 MiB`): Wikipedia dataset for ky,
    parsed from 20190301 dump.

*   `20190301.la` (`v0.0.2`) (`Size: 82.72 MiB`): Wikipedia dataset for la,
    parsed from 20190301 dump.

*   `20190301.lad` (`v0.0.2`) (`Size: 3.39 MiB`): Wikipedia dataset for lad,
    parsed from 20190301 dump.

*   `20190301.lb` (`v0.0.2`) (`Size: 45.70 MiB`): Wikipedia dataset for lb,
    parsed from 20190301 dump.

*   `20190301.lbe` (`v0.0.2`) (`Size: 1.22 MiB`): Wikipedia dataset for lbe,
    parsed from 20190301 dump.

*   `20190301.lez` (`v0.0.2`) (`Size: 4.16 MiB`): Wikipedia dataset for lez,
    parsed from 20190301 dump.

*   `20190301.lfn` (`v0.0.2`) (`Size: 2.81 MiB`): Wikipedia dataset for lfn,
    parsed from 20190301 dump.

*   `20190301.lg` (`v0.0.2`) (`Size: 1.58 MiB`): Wikipedia dataset for lg,
    parsed from 20190301 dump.

*   `20190301.li` (`v0.0.2`) (`Size: 13.86 MiB`): Wikipedia dataset for li,
    parsed from 20190301 dump.

*   `20190301.lij` (`v0.0.2`) (`Size: 2.73 MiB`): Wikipedia dataset for lij,
    parsed from 20190301 dump.

*   `20190301.lmo` (`v0.0.2`) (`Size: 21.34 MiB`): Wikipedia dataset for lmo,
    parsed from 20190301 dump.

*   `20190301.ln` (`v0.0.2`) (`Size: 1.83 MiB`): Wikipedia dataset for ln,
    parsed from 20190301 dump.

*   `20190301.lo` (`v0.0.2`) (`Size: 3.44 MiB`): Wikipedia dataset for lo,
    parsed from 20190301 dump.

*   `20190301.lrc` (`v0.0.2`) (`Size: 4.71 MiB`): Wikipedia dataset for lrc,
    parsed from 20190301 dump.

*   `20190301.lt` (`v0.0.2`) (`Size: 174.73 MiB`): Wikipedia dataset for lt,
    parsed from 20190301 dump.

*   `20190301.ltg` (`v0.0.2`) (`Size: 798.18 KiB`): Wikipedia dataset for ltg,
    parsed from 20190301 dump.

*   `20190301.lv` (`v0.0.2`) (`Size: 127.47 MiB`): Wikipedia dataset for lv,
    parsed from 20190301 dump.

*   `20190301.mai` (`v0.0.2`) (`Size: 10.80 MiB`): Wikipedia dataset for mai,
    parsed from 20190301 dump.

*   `20190301.map-bms` (`v0.0.2`) (`Size: 4.49 MiB`): Wikipedia dataset for
    map-bms, parsed from 20190301 dump.

*   `20190301.mdf` (`v0.0.2`) (`Size: 1.04 MiB`): Wikipedia dataset for mdf,
    parsed from 20190301 dump.

*   `20190301.mg` (`v0.0.2`) (`Size: 25.64 MiB`): Wikipedia dataset for mg,
    parsed from 20190301 dump.

*   `20190301.mh` (`v0.0.2`) (`Size: 27.71 KiB`): Wikipedia dataset for mh,
    parsed from 20190301 dump.

*   `20190301.mhr` (`v0.0.2`) (`Size: 5.69 MiB`): Wikipedia dataset for mhr,
    parsed from 20190301 dump.

*   `20190301.mi` (`v0.0.2`) (`Size: 1.96 MiB`): Wikipedia dataset for mi,
    parsed from 20190301 dump.

*   `20190301.min` (`v0.0.2`) (`Size: 25.05 MiB`): Wikipedia dataset for min,
    parsed from 20190301 dump.

*   `20190301.mk` (`v0.0.2`) (`Size: 140.69 MiB`): Wikipedia dataset for mk,
    parsed from 20190301 dump.

*   `20190301.ml` (`v0.0.2`) (`Size: 117.24 MiB`): Wikipedia dataset for ml,
    parsed from 20190301 dump.

*   `20190301.mn` (`v0.0.2`) (`Size: 28.23 MiB`): Wikipedia dataset for mn,
    parsed from 20190301 dump.

*   `20190301.mr` (`v0.0.2`) (`Size: 49.58 MiB`): Wikipedia dataset for mr,
    parsed from 20190301 dump.

*   `20190301.mrj` (`v0.0.2`) (`Size: 3.01 MiB`): Wikipedia dataset for mrj,
    parsed from 20190301 dump.

*   `20190301.ms` (`v0.0.2`) (`Size: 205.79 MiB`): Wikipedia dataset for ms,
    parsed from 20190301 dump.

*   `20190301.mt` (`v0.0.2`) (`Size: 8.21 MiB`): Wikipedia dataset for mt,
    parsed from 20190301 dump.

*   `20190301.mus` (`v0.0.2`) (`Size: 14.20 KiB`): Wikipedia dataset for mus,
    parsed from 20190301 dump.

*   `20190301.mwl` (`v0.0.2`) (`Size: 8.95 MiB`): Wikipedia dataset for mwl,
    parsed from 20190301 dump.

*   `20190301.my` (`v0.0.2`) (`Size: 34.60 MiB`): Wikipedia dataset for my,
    parsed from 20190301 dump.

*   `20190301.myv` (`v0.0.2`) (`Size: 7.79 MiB`): Wikipedia dataset for myv,
    parsed from 20190301 dump.

*   `20190301.mzn` (`v0.0.2`) (`Size: 6.47 MiB`): Wikipedia dataset for mzn,
    parsed from 20190301 dump.

*   `20190301.na` (`v0.0.2`) (`Size: 480.57 KiB`): Wikipedia dataset for na,
    parsed from 20190301 dump.

*   `20190301.nah` (`v0.0.2`) (`Size: 4.30 MiB`): Wikipedia dataset for nah,
    parsed from 20190301 dump.

*   `20190301.nap` (`v0.0.2`) (`Size: 5.55 MiB`): Wikipedia dataset for nap,
    parsed from 20190301 dump.

*   `20190301.nds` (`v0.0.2`) (`Size: 33.28 MiB`): Wikipedia dataset for nds,
    parsed from 20190301 dump.

*   `20190301.nds-nl` (`v0.0.2`) (`Size: 6.67 MiB`): Wikipedia dataset for
    nds-nl, parsed from 20190301 dump.

*   `20190301.ne` (`v0.0.2`) (`Size: 29.26 MiB`): Wikipedia dataset for ne,
    parsed from 20190301 dump.

*   `20190301.new` (`v0.0.2`) (`Size: 16.91 MiB`): Wikipedia dataset for new,
    parsed from 20190301 dump.

*   `20190301.ng` (`v0.0.2`) (`Size: 91.11 KiB`): Wikipedia dataset for ng,
    parsed from 20190301 dump.

*   `20190301.nl` (`v0.0.2`) (`Size: 1.38 GiB`): Wikipedia dataset for nl,
    parsed from 20190301 dump.

*   `20190301.nn` (`v0.0.2`) (`Size: 126.01 MiB`): Wikipedia dataset for nn,
    parsed from 20190301 dump.

*   `20190301.no` (`v0.0.2`) (`Size: 610.74 MiB`): Wikipedia dataset for no,
    parsed from 20190301 dump.

*   `20190301.nov` (`v0.0.2`) (`Size: 1.12 MiB`): Wikipedia dataset for nov,
    parsed from 20190301 dump.

*   `20190301.nrm` (`v0.0.2`) (`Size: 1.56 MiB`): Wikipedia dataset for nrm,
    parsed from 20190301 dump.

*   `20190301.nso` (`v0.0.2`) (`Size: 2.20 MiB`): Wikipedia dataset for nso,
    parsed from 20190301 dump.

*   `20190301.nv` (`v0.0.2`) (`Size: 2.52 MiB`): Wikipedia dataset for nv,
    parsed from 20190301 dump.

*   `20190301.ny` (`v0.0.2`) (`Size: 1.18 MiB`): Wikipedia dataset for ny,
    parsed from 20190301 dump.

*   `20190301.oc` (`v0.0.2`) (`Size: 70.97 MiB`): Wikipedia dataset for oc,
    parsed from 20190301 dump.

*   `20190301.olo` (`v0.0.2`) (`Size: 1.55 MiB`): Wikipedia dataset for olo,
    parsed from 20190301 dump.

*   `20190301.om` (`v0.0.2`) (`Size: 1.06 MiB`): Wikipedia dataset for om,
    parsed from 20190301 dump.

*   `20190301.or` (`v0.0.2`) (`Size: 24.90 MiB`): Wikipedia dataset for or,
    parsed from 20190301 dump.

*   `20190301.os` (`v0.0.2`) (`Size: 7.31 MiB`): Wikipedia dataset for os,
    parsed from 20190301 dump.

*   `20190301.pa` (`v0.0.2`) (`Size: 40.39 MiB`): Wikipedia dataset for pa,
    parsed from 20190301 dump.

*   `20190301.pag` (`v0.0.2`) (`Size: 1.29 MiB`): Wikipedia dataset for pag,
    parsed from 20190301 dump.

*   `20190301.pam` (`v0.0.2`) (`Size: 8.17 MiB`): Wikipedia dataset for pam,
    parsed from 20190301 dump.

*   `20190301.pap` (`v0.0.2`) (`Size: 1.33 MiB`): Wikipedia dataset for pap,
    parsed from 20190301 dump.

*   `20190301.pcd` (`v0.0.2`) (`Size: 4.14 MiB`): Wikipedia dataset for pcd,
    parsed from 20190301 dump.

*   `20190301.pdc` (`v0.0.2`) (`Size: 1.10 MiB`): Wikipedia dataset for pdc,
    parsed from 20190301 dump.

*   `20190301.pfl` (`v0.0.2`) (`Size: 3.22 MiB`): Wikipedia dataset for pfl,
    parsed from 20190301 dump.

*   `20190301.pi` (`v0.0.2`) (`Size: 586.77 KiB`): Wikipedia dataset for pi,
    parsed from 20190301 dump.

*   `20190301.pih` (`v0.0.2`) (`Size: 654.11 KiB`): Wikipedia dataset for pih,
    parsed from 20190301 dump.

*   `20190301.pl` (`v0.0.2`) (`Size: 1.76 GiB`): Wikipedia dataset for pl,
    parsed from 20190301 dump.

*   `20190301.pms` (`v0.0.2`) (`Size: 13.42 MiB`): Wikipedia dataset for pms,
    parsed from 20190301 dump.

*   `20190301.pnb` (`v0.0.2`) (`Size: 24.31 MiB`): Wikipedia dataset for pnb,
    parsed from 20190301 dump.

*   `20190301.pnt` (`v0.0.2`) (`Size: 533.84 KiB`): Wikipedia dataset for pnt,
    parsed from 20190301 dump.

*   `20190301.ps` (`v0.0.2`) (`Size: 14.09 MiB`): Wikipedia dataset for ps,
    parsed from 20190301 dump.

*   `20190301.pt` (`v0.0.2`) (`Size: 1.58 GiB`): Wikipedia dataset for pt,
    parsed from 20190301 dump.

*   `20190301.qu` (`v0.0.2`) (`Size: 11.42 MiB`): Wikipedia dataset for qu,
    parsed from 20190301 dump.

*   `20190301.rm` (`v0.0.2`) (`Size: 5.85 MiB`): Wikipedia dataset for rm,
    parsed from 20190301 dump.

*   `20190301.rmy` (`v0.0.2`) (`Size: 509.61 KiB`): Wikipedia dataset for rmy,
    parsed from 20190301 dump.

*   `20190301.rn` (`v0.0.2`) (`Size: 779.25 KiB`): Wikipedia dataset for rn,
    parsed from 20190301 dump.

*   `20190301.ro` (`v0.0.2`) (`Size: 449.49 MiB`): Wikipedia dataset for ro,
    parsed from 20190301 dump.

*   `20190301.roa-rup` (`v0.0.2`) (`Size: 931.23 KiB`): Wikipedia dataset for
    roa-rup, parsed from 20190301 dump.

*   `20190301.roa-tara` (`v0.0.2`) (`Size: 5.98 MiB`): Wikipedia dataset for
    roa-tara, parsed from 20190301 dump.

*   `20190301.ru` (`v0.0.2`) (`Size: 3.51 GiB`): Wikipedia dataset for ru,
    parsed from 20190301 dump.

*   `20190301.rue` (`v0.0.2`) (`Size: 4.11 MiB`): Wikipedia dataset for rue,
    parsed from 20190301 dump.

*   `20190301.rw` (`v0.0.2`) (`Size: 904.81 KiB`): Wikipedia dataset for rw,
    parsed from 20190301 dump.

*   `20190301.sa` (`v0.0.2`) (`Size: 14.29 MiB`): Wikipedia dataset for sa,
    parsed from 20190301 dump.

*   `20190301.sah` (`v0.0.2`) (`Size: 11.88 MiB`): Wikipedia dataset for sah,
    parsed from 20190301 dump.

*   `20190301.sat` (`v0.0.2`) (`Size: 2.36 MiB`): Wikipedia dataset for sat,
    parsed from 20190301 dump.

*   `20190301.sc` (`v0.0.2`) (`Size: 4.39 MiB`): Wikipedia dataset for sc,
    parsed from 20190301 dump.

*   `20190301.scn` (`v0.0.2`) (`Size: 11.83 MiB`): Wikipedia dataset for scn,
    parsed from 20190301 dump.

*   `20190301.sco` (`v0.0.2`) (`Size: 57.80 MiB`): Wikipedia dataset for sco,
    parsed from 20190301 dump.

*   `20190301.sd` (`v0.0.2`) (`Size: 12.62 MiB`): Wikipedia dataset for sd,
    parsed from 20190301 dump.

*   `20190301.se` (`v0.0.2`) (`Size: 3.30 MiB`): Wikipedia dataset for se,
    parsed from 20190301 dump.

*   `20190301.sg` (`v0.0.2`) (`Size: 286.02 KiB`): Wikipedia dataset for sg,
    parsed from 20190301 dump.

*   `20190301.sh` (`v0.0.2`) (`Size: 406.72 MiB`): Wikipedia dataset for sh,
    parsed from 20190301 dump.

*   `20190301.si` (`v0.0.2`) (`Size: 36.84 MiB`): Wikipedia dataset for si,
    parsed from 20190301 dump.

*   `20190301.simple` (`v0.0.2`) (`Size: 156.11 MiB`): Wikipedia dataset for
    simple, parsed from 20190301 dump.

*   `20190301.sk` (`v0.0.2`) (`Size: 254.37 MiB`): Wikipedia dataset for sk,
    parsed from 20190301 dump.

*   `20190301.sl` (`v0.0.2`) (`Size: 201.41 MiB`): Wikipedia dataset for sl,
    parsed from 20190301 dump.

*   `20190301.sm` (`v0.0.2`) (`Size: 678.46 KiB`): Wikipedia dataset for sm,
    parsed from 20190301 dump.

*   `20190301.sn` (`v0.0.2`) (`Size: 2.02 MiB`): Wikipedia dataset for sn,
    parsed from 20190301 dump.

*   `20190301.so` (`v0.0.2`) (`Size: 8.17 MiB`): Wikipedia dataset for so,
    parsed from 20190301 dump.

*   `20190301.sq` (`v0.0.2`) (`Size: 77.55 MiB`): Wikipedia dataset for sq,
    parsed from 20190301 dump.

*   `20190301.sr` (`v0.0.2`) (`Size: 725.30 MiB`): Wikipedia dataset for sr,
    parsed from 20190301 dump.

*   `20190301.srn` (`v0.0.2`) (`Size: 634.21 KiB`): Wikipedia dataset for srn,
    parsed from 20190301 dump.

*   `20190301.ss` (`v0.0.2`) (`Size: 737.58 KiB`): Wikipedia dataset for ss,
    parsed from 20190301 dump.

*   `20190301.st` (`v0.0.2`) (`Size: 482.27 KiB`): Wikipedia dataset for st,
    parsed from 20190301 dump.

*   `20190301.stq` (`v0.0.2`) (`Size: 3.26 MiB`): Wikipedia dataset for stq,
    parsed from 20190301 dump.

*   `20190301.su` (`v0.0.2`) (`Size: 20.52 MiB`): Wikipedia dataset for su,
    parsed from 20190301 dump.

*   `20190301.sv` (`v0.0.2`) (`Size: 1.64 GiB`): Wikipedia dataset for sv,
    parsed from 20190301 dump.

*   `20190301.sw` (`v0.0.2`) (`Size: 27.60 MiB`): Wikipedia dataset for sw,
    parsed from 20190301 dump.

*   `20190301.szl` (`v0.0.2`) (`Size: 4.06 MiB`): Wikipedia dataset for szl,
    parsed from 20190301 dump.

*   `20190301.ta` (`v0.0.2`) (`Size: 141.07 MiB`): Wikipedia dataset for ta,
    parsed from 20190301 dump.

*   `20190301.tcy` (`v0.0.2`) (`Size: 2.33 MiB`): Wikipedia dataset for tcy,
    parsed from 20190301 dump.

*   `20190301.te` (`v0.0.2`) (`Size: 113.16 MiB`): Wikipedia dataset for te,
    parsed from 20190301 dump.

*   `20190301.tet` (`v0.0.2`) (`Size: 1.06 MiB`): Wikipedia dataset for tet,
    parsed from 20190301 dump.

*   `20190301.tg` (`v0.0.2`) (`Size: 36.95 MiB`): Wikipedia dataset for tg,
    parsed from 20190301 dump.

*   `20190301.th` (`v0.0.2`) (`Size: 254.00 MiB`): Wikipedia dataset for th,
    parsed from 20190301 dump.

*   `20190301.ti` (`v0.0.2`) (`Size: 309.72 KiB`): Wikipedia dataset for ti,
    parsed from 20190301 dump.

*   `20190301.tk` (`v0.0.2`) (`Size: 4.50 MiB`): Wikipedia dataset for tk,
    parsed from 20190301 dump.

*   `20190301.tl` (`v0.0.2`) (`Size: 50.85 MiB`): Wikipedia dataset for tl,
    parsed from 20190301 dump.

*   `20190301.tn` (`v0.0.2`) (`Size: 1.21 MiB`): Wikipedia dataset for tn,
    parsed from 20190301 dump.

*   `20190301.to` (`v0.0.2`) (`Size: 775.10 KiB`): Wikipedia dataset for to,
    parsed from 20190301 dump.

*   `20190301.tpi` (`v0.0.2`) (`Size: 1.39 MiB`): Wikipedia dataset for tpi,
    parsed from 20190301 dump.

*   `20190301.tr` (`v0.0.2`) (`Size: 497.19 MiB`): Wikipedia dataset for tr,
    parsed from 20190301 dump.

*   `20190301.ts` (`v0.0.2`) (`Size: 1.39 MiB`): Wikipedia dataset for ts,
    parsed from 20190301 dump.

*   `20190301.tt` (`v0.0.2`) (`Size: 53.23 MiB`): Wikipedia dataset for tt,
    parsed from 20190301 dump.

*   `20190301.tum` (`v0.0.2`) (`Size: 309.58 KiB`): Wikipedia dataset for tum,
    parsed from 20190301 dump.

*   `20190301.tw` (`v0.0.2`) (`Size: 345.96 KiB`): Wikipedia dataset for tw,
    parsed from 20190301 dump.

*   `20190301.ty` (`v0.0.2`) (`Size: 485.56 KiB`): Wikipedia dataset for ty,
    parsed from 20190301 dump.

*   `20190301.tyv` (`v0.0.2`) (`Size: 2.60 MiB`): Wikipedia dataset for tyv,
    parsed from 20190301 dump.

*   `20190301.udm` (`v0.0.2`) (`Size: 2.94 MiB`): Wikipedia dataset for udm,
    parsed from 20190301 dump.

*   `20190301.ug` (`v0.0.2`) (`Size: 5.64 MiB`): Wikipedia dataset for ug,
    parsed from 20190301 dump.

*   `20190301.uk` (`v0.0.2`) (`Size: 1.28 GiB`): Wikipedia dataset for uk,
    parsed from 20190301 dump.

*   `20190301.ur` (`v0.0.2`) (`Size: 129.57 MiB`): Wikipedia dataset for ur,
    parsed from 20190301 dump.

*   `20190301.uz` (`v0.0.2`) (`Size: 60.85 MiB`): Wikipedia dataset for uz,
    parsed from 20190301 dump.

*   `20190301.ve` (`v0.0.2`) (`Size: 257.59 KiB`): Wikipedia dataset for ve,
    parsed from 20190301 dump.

*   `20190301.vec` (`v0.0.2`) (`Size: 10.65 MiB`): Wikipedia dataset for vec,
    parsed from 20190301 dump.

*   `20190301.vep` (`v0.0.2`) (`Size: 4.59 MiB`): Wikipedia dataset for vep,
    parsed from 20190301 dump.

*   `20190301.vi` (`v0.0.2`) (`Size: 623.74 MiB`): Wikipedia dataset for vi,
    parsed from 20190301 dump.

*   `20190301.vls` (`v0.0.2`) (`Size: 6.58 MiB`): Wikipedia dataset for vls,
    parsed from 20190301 dump.

*   `20190301.vo` (`v0.0.2`) (`Size: 23.80 MiB`): Wikipedia dataset for vo,
    parsed from 20190301 dump.

*   `20190301.wa` (`v0.0.2`) (`Size: 8.75 MiB`): Wikipedia dataset for wa,
    parsed from 20190301 dump.

*   `20190301.war` (`v0.0.2`) (`Size: 256.72 MiB`): Wikipedia dataset for war,
    parsed from 20190301 dump.

*   `20190301.wo` (`v0.0.2`) (`Size: 1.54 MiB`): Wikipedia dataset for wo,
    parsed from 20190301 dump.

*   `20190301.wuu` (`v0.0.2`) (`Size: 9.08 MiB`): Wikipedia dataset for wuu,
    parsed from 20190301 dump.

*   `20190301.xal` (`v0.0.2`) (`Size: 1.64 MiB`): Wikipedia dataset for xal,
    parsed from 20190301 dump.

*   `20190301.xh` (`v0.0.2`) (`Size: 1.26 MiB`): Wikipedia dataset for xh,
    parsed from 20190301 dump.

*   `20190301.xmf` (`v0.0.2`) (`Size: 9.40 MiB`): Wikipedia dataset for xmf,
    parsed from 20190301 dump.

*   `20190301.yi` (`v0.0.2`) (`Size: 11.56 MiB`): Wikipedia dataset for yi,
    parsed from 20190301 dump.

*   `20190301.yo` (`v0.0.2`) (`Size: 11.55 MiB`): Wikipedia dataset for yo,
    parsed from 20190301 dump.

*   `20190301.za` (`v0.0.2`) (`Size: 735.93 KiB`): Wikipedia dataset for za,
    parsed from 20190301 dump.

*   `20190301.zea` (`v0.0.2`) (`Size: 2.47 MiB`): Wikipedia dataset for zea,
    parsed from 20190301 dump.

*   `20190301.zh` (`v0.0.2`) (`Size: 1.71 GiB`): Wikipedia dataset for zh,
    parsed from 20190301 dump.

*   `20190301.zh-classical` (`v0.0.2`) (`Size: 13.37 MiB`): Wikipedia dataset
    for zh-classical, parsed from 20190301 dump.

*   `20190301.zh-min-nan` (`v0.0.2`) (`Size: 50.30 MiB`): Wikipedia dataset for
    zh-min-nan, parsed from 20190301 dump.

*   `20190301.zh-yue` (`v0.0.2`) (`Size: 52.41 MiB`): Wikipedia dataset for
    zh-yue, parsed from 20190301 dump.

*   `20190301.zu` (`v0.0.2`) (`Size: 1.50 MiB`): Wikipedia dataset for zu,
    parsed from 20190301 dump.

## `wikipedia/20190301.aa`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ab`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ace`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ady`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.af`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ak`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.als`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.am`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.an`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ang`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ar`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.arc`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.arz`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.as`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ast`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.atj`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.av`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ay`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.az`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.azb`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ba`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bar`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bat-smg`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bcl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.be`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.be-x-old`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bg`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bh`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bjn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bm`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bpy`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.br`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bs`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bug`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.bxr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ca`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.cbk-zam`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.cdo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ce`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ceb`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ch`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.cho`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.chr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.chy`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ckb`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.co`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.cr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.crh`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.cs`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.csb`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.cu`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.cv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.cy`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.da`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.de`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.din`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.diq`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.dsb`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.dty`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.dv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.dz`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ee`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.el`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.eml`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.en`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.eo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.es`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.et`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.eu`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ext`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.fa`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ff`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.fi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.fiu-vro`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.fj`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.fo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.fr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.frp`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.frr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.fur`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.fy`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ga`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gag`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gan`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gd`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.glk`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gom`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gor`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.got`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gu`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.gv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ha`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.hak`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.haw`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.he`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.hi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.hif`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ho`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.hr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.hsb`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ht`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.hu`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.hy`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.hz`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ia`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.id`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ie`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ig`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ii`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ik`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ilo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.inh`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.io`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.is`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.it`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.iu`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ja`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.jam`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.jbo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.jv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ka`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kaa`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kab`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kbd`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kbp`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kg`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ki`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kj`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kk`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.km`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ko`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.koi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.krc`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ks`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ksh`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ku`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.kw`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ky`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.la`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lad`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lb`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lbe`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lez`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lfn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lg`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.li`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lij`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lmo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ln`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lrc`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lt`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ltg`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.lv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mai`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.map-bms`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mdf`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mg`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mh`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mhr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.min`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mk`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ml`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mrj`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ms`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mt`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mus`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mwl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.my`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.myv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.mzn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.na`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nah`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nap`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nds`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nds-nl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ne`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.new`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ng`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.no`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nov`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nrm`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nso`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.nv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ny`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.oc`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.olo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.om`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.or`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.os`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pa`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pag`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pam`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pap`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pcd`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pdc`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pfl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pih`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pms`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pnb`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pnt`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ps`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.pt`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.qu`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.rm`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.rmy`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.rn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ro`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.roa-rup`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.roa-tara`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ru`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.rue`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.rw`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sa`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sah`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sat`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sc`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.scn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sco`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sd`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.se`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sg`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sh`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.si`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.simple`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sk`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sm`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.so`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sq`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.srn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ss`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.st`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.stq`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.su`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.sw`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.szl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ta`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tcy`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.te`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tet`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tg`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.th`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ti`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tk`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tl`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tn`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.to`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tpi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tr`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ts`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tt`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tum`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tw`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ty`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.tyv`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.udm`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ug`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.uk`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ur`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.uz`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.ve`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.vec`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.vep`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.vi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.vls`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.vo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.wa`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.war`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.wo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.wuu`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.xal`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.xh`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.xmf`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.yi`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.yo`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.za`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.zea`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.zh`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.zh-classical`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.zh-min-nan`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.zh-yue`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## `wikipedia/20190301.zu`

```python
FeaturesDict({
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## Statistics

None computed

## Urls

*   [https://dumps.wikimedia.org](https://dumps.wikimedia.org)

## Supervised keys (for `as_supervised=True`)

`None`

## Citation

```
@ONLINE {wikidump,
    author = "Wikimedia Foundation",
    title  = "Wikimedia Downloads",
    url    = "https://dumps.wikimedia.org"
}
```

--------------------------------------------------------------------------------

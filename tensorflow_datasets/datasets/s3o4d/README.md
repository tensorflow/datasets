The dataset first described in the "Stanford 3D Objects" section of the paper
[Disentangling by Subspace Diffusion](https://arxiv.org/abs/2006.12982). The
data consists of 100,000 renderings each of the Bunny and Dragon objects from
the
[Stanford 3D Scanning Repository](http://graphics.stanford.edu/data/3Dscanrep/).
More objects may be added in the future, but only the Bunny and Dragon are used
in the paper. Each object is rendered with a uniformly sampled illumination from
a point on the 2-sphere, and a uniformly sampled 3D rotation. The true latent
states are provided as NumPy arrays along with the images. The lighting is given
as a 3-vector with unit norm, while the rotation is provided both as a
quaternion and a 3x3 orthogonal matrix.

There are many similarities between S3O4D and existing ML benchmark datasets
like [NORB](https://cs.nyu.edu/~ylclab/data/norb-v1.0/),
[3D Chairs](https://github.com/mathieuaubry/seeing3Dchairs),
[3D Shapes](https://github.com/deepmind/3d-shapes) and many others, which also
include renderings of a set of objects under different pose and illumination
conditions. However, none of these existing datasets include the *full manifold*
of rotations in 3D - most include only a subset of changes to elevation and
azimuth. S3O4D images are sampled uniformly and independently from the full
space of rotations and illuminations, meaning the dataset contains objects that
are upside down and illuminated from behind or underneath. We believe that this
makes S3O4D uniquely suited for research on generative models where the latent
space has non-trivial topology, as well as for general manifold learning methods
where the curvature of the manifold is important.

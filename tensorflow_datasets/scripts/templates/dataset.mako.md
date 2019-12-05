<%!
import tensorflow_datasets as tfds
from tensorflow_datasets.core.utils.py_utils import get_class_path
from tensorflow_datasets.core.utils.py_utils import get_class_url
%>

## Print URLs
<%def name="display_homepage(builder, level)">\
${'#' * level} Homepage
 * [${builder.info.homepage}](${builder.info.homepage})
</%def>

## Print features
<%def name="display_features(builder, level)">\
${'#' * level} Features
```python
${builder.info.features}
```
</%def>

## Print Supervised keys
<%def name="display_supervised_keys(builder, level)">\
%if builder.info.supervised_keys:
${'#' * level} Supervised keys (for `as_supervised=True`)
`${str(builder.info.supervised_keys)}`
%endif
</%def>

## Print list of supported versions minus default.
<%def name="supported_versions(builder, level)">\
<%
versions = (builder.SUPPORTED_VERSIONS if hasattr(builder, 'SUPPORTED_VERSIONS')
            else builder.supported_versions)
%>\
%for version in versions:
${'  '*level|n}* `${str(version)}`: ${version.description}
%endfor
</%def>

## Print the bullet points + features specific to builder with a single version.
<%def name="print_general_info_one_config(builder)">
${display_description(builder)}

* URL: [${builder.info.homepage}](${builder.info.homepage})
* `DatasetBuilder`: [`${get_class_path(builder)}`](${get_class_url(builder)})
* Version: `v${str(builder.info.version)}`
* Versions:
  * **`${builder.info.version}`** (default): ${builder.info.version.description or ''}
${supported_versions(builder, level=1)}
* Size: `${tfds.units.size_str(builder.info.size_in_bytes)}`

%if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
WARNING: This dataset requires you to download the source data manually into manual_dir
(defaults to `~/tensorflow_datasets/manual/${builder.info.name}/`):
${builder.MANUAL_DOWNLOAD_INSTRUCTIONS}
%endif

${display_features(builder, level=2)}
${display_stats(builder, level=2)}
${display_homepage(builder, level=2)}
${display_supervised_keys(builder, level=2)}
${display_citation(builder.info.citation, level=2)}
</%def>

## Print the configs: list with name/version/size/description + doc for each.
<%def name="print_builder_configs(builder, config_builders)">
<%
len_conf_descs = len(set([c.description for c in  builder.BUILDER_CONFIGS] + [
    builder.info.description]))
%>
%if len_conf_descs == 1 or len_conf_descs > len(builder.BUILDER_CONFIGS):
${display_description(builder)}
%endif

* URL: [${builder.info.homepage}](${builder.info.homepage})
* `DatasetBuilder`: [`${get_class_path(builder)}`](${get_class_url(builder)})

`${builder.name}` is configured with `${get_class_path(builder.builder_config)}` and has
the following configurations predefined (defaults to the first one):

%for config, config_builder in zip(builder.BUILDER_CONFIGS, config_builders):
<%
  size = tfds.units.size_str(config_builder.info.size_in_bytes)
%>
* `${config.name}` (`v${str(config.version)}`) (`Size: ${size}`): ${config.description}
%endfor

%for config, config_builder in zip(builder.BUILDER_CONFIGS, config_builders):
${'##'} `${builder.name}/${config.name}`
${config.description}

Versions:

* **`${config.version}`** (default): ${getattr(config.version, 'description', '') or ''}
${supported_versions(config, level=0)}

%if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
WARNING: This dataset requires you to download the source data manually into manual_dir
(defaults to `~/tensorflow_datasets/manual/${builder.info.name}/`):
${builder.MANUAL_DOWNLOAD_INSTRUCTIONS}
%endif

${display_stats(config_builder, level=3)}
${display_features(config_builder, level=3)}
${display_homepage(config_builder, level=3)}
${display_supervised_keys(config_builder, level=3)}
%endfor
${display_citation(config_builder.info.citation, level=2)}
</%def>

## Display the description of a builder.
<%def name="display_description(builder)">\
${builder.info.description}
</%def>

## Display stats for a split.
<%def name="display_stats(builder, level)">\
<%
  splits = builder.info.splits
  size_name = [(split_info.num_examples, split_name)
               for (split_name, split_info) in splits.items()]
%>\
${'#' * level} Statistics
%if builder.info.splits.total_num_examples:
Split  | Examples
:----- | ---:
ALL    | ${"{:,}".format(splits.total_num_examples)}
%for split_size, split_name in sorted(size_name, key=lambda x:(-x[0], x[1])):
${split_name.upper()} | ${"{:,}".format(split_size)}
%endfor
%else:
None computed
%endif
</%def>

## Display a citation.
<%def name="display_citation(citation, level)">\
%if citation:
${'#' * level} Citation
```
${citation}
```
%endif
</%def>

%if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
# `${builder.name}` (Manual download)
%else:
# `${builder.name}`
%endif


%if builder.builder_config:
${print_builder_configs(builder, config_builders)}
%else:
${print_general_info_one_config(builder)}
%endif
---

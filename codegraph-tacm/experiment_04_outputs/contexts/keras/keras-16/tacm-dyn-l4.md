# keras-16 :: tacm-dyn-l4

query: Modify Sequential config to include model name (breaking change). Matches tf.keras behavior as of TF 1.11.0. (#11133)

## selected nodes

- rank=1 layer=FILE tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=2 layer=CLASS tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_hue_test.py::RandomHueTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_hue_test.py
- rank=3 layer=FUNCTION tokens=302 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::model_metadata file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py
- rank=4 layer=FILE tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/text_dataset_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/text_dataset_utils.py
- rank=5 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_basic_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=6 layer=FILE tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/dataset_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/dataset_utils.py
- rank=7 layer=FUNCTION tokens=309 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/dataset_utils.py::labels_to_dataset_tf file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/dataset_utils.py
- rank=8 layer=FILE tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/image_dataset_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/image_dataset_utils.py
- rank=9 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._write_keras_model_summary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=10 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib.py::deserialize_keras_object file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib.py
- rank=11 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::save_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=12 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/dataset_utils.py::is_tf_dataset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/dataset_utils.py
- rank=13 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_custom_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=14 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::_serialize_model_as_json file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=15 layer=FILE tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/sequential_model.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/sequential_model.py
- rank=16 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/model_benchmark/image_classification_benchmark.py::load_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/model_benchmark/image_classification_benchmark.py
- rank=17 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py::DataAdapter.get_tf_dataset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py
- rank=18 layer=CLASS tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_contrast_test.py::RandomContrastTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_contrast_test.py
- rank=19 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=20 layer=FILE tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py
- rank=21 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py::scipy_sparse_to_tf_sparse file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py
- rank=22 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py::jax_sparse_to_tf_sparse file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py
- rank=23 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::constant file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=24 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py
- rank=25 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/__init__.py
- rank=26 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/__init__.py
- rank=27 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py::dense_bincount file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py
- rank=28 layer=CLASS tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/tree_test.py::TreeTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/tree_test.py
- rank=29 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py::Config.__getattr__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py
- rank=30 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=31 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py::associative_scan file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py
- rank=32 layer=CLASS tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_posterization_test.py::RandomPosterizationTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_posterization_test.py
- rank=33 layer=FILE tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py
- rank=34 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py::_clone_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py
- rank=35 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py::clone_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py
- rank=36 layer=FILE tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/backend_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/backend_utils.py
- rank=37 layer=FILE tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/config/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/config/__init__.py

## context

```text
file saving/saving_lib.py
imports: datetime, io, json, math, os, pathlib, shutil, tempfile
defines: DiskIOStore, H5IOStore, ShardedH5IOStore, NpzIOStore, save_model, _serialize_model_as_json, _save_model_to_dir, _save_model_to_fileobj, _upload_model_to_hf, load_model, _load_model_from_dir, _model_from_config, _load_model_from_fileobj, save_weights_only, load_weights_only, _raise_loading_failure, _write_to_zip_recursively, _name_key, _walk_saveable, _save_state, _load_state, _save_container_state, _load_container_state, get_temp_dir, get_attr_skipset, is_memory_sufficient, _split_path_components, _write_nested_dict_to_dir, _save_assets_to_dict, _load_assets_from_dict

class RandomHueTest(testing.TestCase):  [layers/preprocessing/image_preprocessing/random_hue_test.py:10]
methods: test_layer, test_random_hue_inference
         test_random_hue_no_change_with_zero_factor
         test_random_hue_randomness
         test_random_hue_value_range_0_to_1
         test_random_hue_value_range_0_to_255
         test_tf_data_compatibility

def model_metadata(model, include_optimizer=True, require_config=True):
    """Returns a dictionary containing the model metadata."""
    from keras.src import __version__ as keras_version

    model_config = {"class_name": model.__class__.__name__}
    try:
        model_config["config"] = model.get_config()
    except NotImplementedError as e:
        if require_config:
            raise e

    metadata = dict(
        keras_version=str(keras_version),
        backend=backend.backend(),
        model_config=model_config,
    )
    if getattr(model, "optimizer", False) and include_optimizer:
        if model.compiled:
            training_config = model._compile_config.config
            training_config.pop("optimizer", None)  # Handled separately.
            metadata["training_config"] = _serialize_nested_config(
                training_config
            )
            optimizer_config = {
                "class_name": object_registration.get_registered_name(
                    model.optimizer.__class__
                ),
                "config": model.optimizer.get_config(),
            }
            metadata["training_config"]["optimizer_config"] = optimizer_config
    return metadata

file utils/text_dataset_utils.py
imports: numpy, keras
defines: text_dataset_from_directory, paths_and_labels_to_dataset, _paths_and_labels_to_dataset_tf, _path_to_string_content_tf, _paths_and_labels_to_dataset_grain, _path_to_string_content_grain

def _get_basic_sequential_model(compile=True):
    sequential_model = keras.Sequential(
        [
            keras.layers.Dense(1, name="dense_1"),
            keras.layers.Dense(1, name="dense_2"),
        ],
        name="sequential",
    )
    if compile:
        sequential_model.compile(
            optimizer="adam",
            loss=my_mean_squared_error,
            metrics=[keras.metrics.Hinge(), "mse"],
        )
    return sequential_model

file utils/dataset_utils.py
imports: os, random, time, warnings, multiprocessing, numpy, keras
defines: split_dataset, _split_dataset_tf, _split_dataset_torch, _infer_preferred_backend, _convert_dataset_to_list, _get_data_iterator_from_dataset, _get_next_sample, is_tf_dataset, is_grain_dataset, is_torch_dataset, _mro_matches, _rescale_dataset_split_sizes, _restore_dataset_from_list, is_batched, get_batch_size, index_directory, iter_valid_files, index_subdirectory, get_training_or_validation_split, labels_to_dataset_tf, labels_to_dataset_grain, preprocess_labels_in_cpu, check_validation_split_arg

def labels_to_dataset_tf(labels, label_mode, num_classes):
    """Create a `tf.data.Dataset` from the list/tuple of labels.

    Args:
        labels: list/tuple of labels to be converted into a `tf.data.Dataset`.
        label_mode: String describing the encoding of `labels`. Options are:
        - `"binary"` indicates that the labels (there can be only 2) are encoded
            as `float32` scalars with values 0 or 1
            (e.g. for `binary_crossentropy`).
        - `"categorical"` means that the labels are mapped into a categorical
            vector.  (e.g. for `categorical_crossentropy` loss).
        num_classes: number of classes of labels.

    Returns:
        A `tf.data.Dataset` instance.
    """
    from keras.src.utils.module_utils import tensorflow as tf

    label_ds = tf.data.Dataset.from_tensor_slices(labels)
    if label_mode == "binary":
        label_ds = label_ds.map(
            lambda x: tf.expand_dims(tf.cast(x, "float32"), axis=-1),
            num_parallel_calls=tf.data.AUTOTUNE,
        )
    elif label_mode == "categorical":
        label_ds = label_ds.map(
            lambda x: tf.one_hot(x, num_classes),
            num_parallel_calls=tf.data.AUTOTUNE,
        )
    return label_ds

file utils/image_dataset_utils.py
imports: io, pathlib, numpy, keras, PIL
defines: image_dataset_from_directory, paths_and_labels_to_dataset, _paths_and_labels_to_dataset_tf, _load_image_tf, _paths_and_labels_to_dataset_grain, _load_image_grain

    def _write_keras_model_summary(self):
        """Writes Keras graph network summary to TensorBoard."""
        with self._train_writer.as_default():
            if (
                self.model.__class__.__name__ == "Functional"
                or self.model.__class__.__name__ == "Sequential"
            ):
                keras_model_summary("keras", self.model, step=0)

def deserialize_keras_object(
    config, custom_objects=None, safe_mode=True, **kwargs
):
    """Retrieve the object by deserializing the config dict.

    The config dict is a Python dictionary that consists of a set of key-value
    pairs, and represents a Keras object, such as an `Optimizer`, `Layer`,
    `Metrics`, etc. The saving and loading library uses the following keys to
    record information of a Keras object:

    - `class_name`: String. This is the name of the class,
      as exactly defined in the source
    # ... truncated

def save_model(model, filepath, weights_format="h5", zipped=True):
    """Save a zip-archive representing a Keras model to the given file or path.

    The zip-based archive contains the following structure:

    - JSON-based configuration file (config.json): Records of model, layer, and
        other saveables' configuration.
    - H5-based saveable state files, found in respective directories, such as
        model/states.npz, model/dense_layer/states.npz, etc.
    - Metadata file.

    The states of Keras saveables (layers, optimizers, loss, and metrics) are
    # ... truncated

def is_tf_dataset(dataset):
    return _mro_matches(
        dataset,
        class_names=("DatasetV2", "Dataset"),
        module_substrings=(
            "tensorflow.python.data",  # TF classic
            "tensorflow.data",  # newer TF paths
        ),
    )

def _get_custom_sequential_model(compile=True):
    sequential_model = keras.Sequential(
        [MyDense(1), MyDense(1)], name="sequential"
    )
    if compile:
        sequential_model.compile(
            optimizer="adam",
            loss=my_mean_squared_error,
            metrics=[keras.metrics.Hinge(), "mse"],
        )
    return sequential_model

def _serialize_model_as_json(model):
    with ObjectSharingScope():
        serialized_model_dict = serialize_keras_object(model)
    config_json = json.dumps(serialized_model_dict)
    metadata_json = json.dumps(
        {
            "keras_version": keras_version,
            "date_saved": datetime.datetime.now().strftime("%Y-%m-%d@%H:%M:%S"),
        }
    )
    return config_json, metadata_json

file keras/guides/sequential_model.py
imports: keras
defines: —

def load_model():
    model_class = MODEL_MAP[FLAGS.model]
    # Load the EfficientNetV2B0 model and add a classification head.
    model = model_class(include_top=False, weights="imagenet")
    classifier = keras.models.Sequential(
        [
            keras.Input([IMAGE_SIZE[0], IMAGE_SIZE[1], CHANNELS]),
            model,
            keras.layers.GlobalAveragePooling2D(),
            keras.layers.Dense(2),
        ]
    )
    return classifier

    def get_tf_dataset(self):
        """Get a `tf.data.Dataset` instance for the DataAdapter.

        Note that the dataset returned does not repeat for epoch, so caller
        might need to create new iterator for the same dataset at the beginning
        of the epoch. This behavior might change in the future.

        Returns:
            A `tf.data.Dataset`. Caller might use the dataset in different
            context, e.g. iter(dataset) in eager to get the value directly, or
            in graph mode, provide the iterator tensor to Keras model function.
        """
        raise NotImplementedError

class RandomContrastTest(testing.TestCase):  [layers/preprocessing/image_preprocessing/random_contrast_test.py:9]
methods: test_dict_input, test_layer
         test_random_contrast_with_value_range_0_to_1
         test_random_contrast_with_value_range_0_to_255
         test_tf_data_compatibility

    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

file trainers/data_adapters/data_adapter_utils.py
imports: numpy, keras
defines: ConverterIterableDataset, unpack_x_y_sample_weight, pack_x_y_sample_weight, list_to_tuple, check_data_cardinality, class_weight_to_sample_weights, get_jax_iterator, convert_to_jax_compatible, get_numpy_iterator, convert_to_numpy, get_torch_dataloader, is_tensorflow_tensor, is_tensorflow_ragged, is_tensorflow_sparse, is_jax_array, is_jax_sparse, is_torch_tensor, is_scipy_sparse, scipy_sparse_to_tf_sparse, scipy_sparse_to_jax_sparse, tf_sparse_to_jax_sparse, jax_sparse_to_tf_sparse

def scipy_sparse_to_tf_sparse(x):
    from keras.src.utils.module_utils import tensorflow as tf

    coo = x.tocoo()
    indices = np.concatenate(
        (np.expand_dims(coo.row, 1), np.expand_dims(coo.col, 1)), axis=1
    )
    return tf.SparseTensor(indices, coo.data, coo.shape)

def jax_sparse_to_tf_sparse(x):
    from keras.src.utils.module_utils import tensorflow as tf

    return tf.SparseTensor(x.indices, x.data, x.shape)

def constant(value, dtype=None, shape=None, name=None):
    """DEPRECATED."""
    if dtype is None:
        dtype = backend.floatx()

    return tf.constant(value, dtype=dtype, shape=shape, name=name)

file utils/tf_utils.py
imports: keras
defines: ensure_tensor, is_ragged_tensor, sparse_bincount, dense_bincount, expand_dims, tf_encode_categorical_inputs

file _tf_keras/keras/__init__.py
imports: keras
defines: —

file api/_tf_keras/__init__.py
imports: keras
defines: —

def dense_bincount(inputs, depth, binary_output, dtype, count_weights=None):
    """Apply binary or count encoding to an input."""
    result = tf.math.bincount(
        inputs,
        weights=count_weights,
        minlength=depth,
        maxlength=depth,
        dtype=dtype,
        axis=-1,
        binary_output=binary_output,
    )
    if inputs.shape.rank == 1:
        result.set_shape(tf.TensorShape((depth,)))
    else:
        batch_size = inputs.shape.as_list()[0]
        result.set_shape(tf.TensorShape((batch_size, depth)))
    return result

class TreeTest(testing.TestCase):  [tree/tree_test.py:77]
methods: assertEqualStrict, f1, f1, f2, f2, is_dmtree, setUp
         test_assert_same_paths
         test_assert_same_paths_tf_wrappers
         test_assert_same_structure
         test_assert_same_structure_tf_wrappers
         test_flatten, test_flatten_tf_wrappers
         test_flatten_with_path
         test_flatten_with_path_tf_wrappers
         test_is_nested, test_is_nested_tf_wrappers
         test_lists_to_tuples, test_map_shape_structure
         test_map_structure_up_to
         test_map_structure_with_multiple_structures
         test_map_structure_with_multiple_structures_tf_wrappers
         test_map_structure_with_one_structure
         test_map_structure_with_one_structure_tf_wrappers
         test_pack_sequence_as
         test_pack_sequence_as_tf_wrappers
         test_traverse_bottom_up
         test_traverse_bottom_up_tf_wrappers
         test_traverse_top_down
         test_traverse_top_down_tf_wrappers

    def __getattr__(self, name):
        attrs = object.__getattribute__(self, "__attrs__")
        if attrs is None or name in attrs:
            return object.__getattribute__(self, name)

        if name in self._config:
            return self._config[name]

        msg = f"Unknown attribute: '{name}'."
        if difflib is not None:
            closest_matches = difflib.get_close_matches(
                name, self._config.keys(), n=1, cutoff=0.7
            )
            if closest_matches:
                msg += f" Did you mean '{closest_matches[0]}'?"
        raise AttributeError(msg)

    def get_config(self):
        serialize_fn = serialization_lib.serialize_keras_object
        if global_state.get_global_attribute("use_legacy_config", False):
            # Legacy format serialization used for H5 and SavedModel formats
            serialize_fn = legacy_serialization.serialize_keras_object
        layer_configs = []
        for layer in super().layers:
            # `super().layers` include the InputLayer if available (it is
            # filtered out of `self.layers`).
            layer_configs.append(serialize_fn(layer))
        config = Model.get_config(self)
        config["name"] = self.name
        config["layers"] = copy.deepcopy(layer_configs)
        if self._functional is not None:
            config["build_input_shape"] = self._layers[0].batch_shape
        return config

def associative_scan(f, elems, reverse=False, axis=0):
    # Implementation is the same as tfp.math.scan_associative
    # with additional checks to ensure similar behavior with jax
    if not callable(f):
        raise TypeError(f"`f` should be a callable. Received: f={f}")
    elems_flat = tree.flatten(elems)
    elems_flat = [tf.convert_to_tensor(elem) for elem in elems_flat]
    if reverse:
        elems_flat = [tf.reverse(elem, [axis]) for elem in elems_flat]

    def _combine(a_flat, b_flat):
        a = tree.pack_sequence_as(elems, a_flat)
    # ... truncated

file models/sequential.py
imports: copy, inspect, typing, keras
defines: Sequential

def copy(x):
    return x

# --- Layer 04: Variable context ---
# call-chain context
  called by: save_model_to_hdf5 [legacy_h5_format.py]

# call-chain context
  called by: paths_and_labels_to_dataset [audio_dataset_utils.py]
  called by: _paths_and_labels_to_dataset_tf [image_dataset_utils.py]

# call-chain context
  called by: set_model [tensorboard.py]

# call-chain context
  called by: deserialize [__init__.py]
  called by: get [__init__.py]

# call-chain context
  called by: save [feature_space.py]
  called by: save [model.py]

# call-chain context
  called by: _split_dataset_torch [dataset_utils.py]
  called by: _infer_preferred_backend [dataset_utils.py]

# call-chain context
  called by: _save_checkpoint [orbax_checkpoint.py]
  called by: _save_model_to_dir [saving_lib.py]

# call-chain context
  called by: main [image_classification_benchmark.py]
  called by: make_or_restore_model [distributed_training_with_tensorflow.py]

# call-chain context
  called by: __init__ [trainer.py]

# call-chain context
  called by: align_operand_types [core.py]
  called by: get_ov_output [core.py]

# call-chain context
  called by: convert_to_tf_dataset_compatible [array_slicing.py]
  called by: convert_to_tf [generator_data_adapter.py]

# call-chain context
  called by: convert_to_tf_dataset_compatible [array_slicing.py]
  called by: convert_to_tf [generator_data_adapter.py]

# call-chain context
  called by: get_ov_output [core.py]
  called by: __getitem__ [core.py]

# call-chain context
  called by: tf_encode_categorical_inputs [tf_utils.py]

# call-chain context
  called by: model_metadata [saving_utils.py]
  called by: _clone_layer [cloning.py]

```

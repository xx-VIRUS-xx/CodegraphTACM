# keras-16 :: tacm

query: Modify Sequential config to include model name (breaking change). Matches tf.keras behavior as of TF 1.11.0. (#11133)

## selected nodes

- rank=1 layer=FILE tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=2 layer=FILE tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/sequential_model.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/sequential_model.py
- rank=3 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/__init__.py
- rank=4 layer=CLASS tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_hue_test.py::RandomHueTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_hue_test.py
- rank=5 layer=CLASS tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_contrast_test.py::RandomContrastTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_contrast_test.py
- rank=6 layer=CLASS tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/tree_test.py::TreeTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/tree_test.py
- rank=7 layer=CLASS tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_posterization_test.py::RandomPosterizationTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/image_preprocessing/random_posterization_test.py
- rank=8 layer=CLASS tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py
- rank=9 layer=CLASS tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/model_visualization_test.py::ModelVisualizationTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/model_visualization_test.py
- rank=10 layer=CLASS tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/tf_custom_fit_test.py::CustomModel file=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/tf_custom_fit_test.py
- rank=11 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_custom_tf_workflow.py::MyModel file=/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_custom_tf_workflow.py
- rank=12 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py::SavedModelExportArchive.SavedModelTrackableView file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py
- rank=13 layer=FUNCTION tokens=302 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::model_metadata file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py
- rank=14 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark._build_tf_keras_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py
- rank=15 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_basic_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=16 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._write_keras_model_summary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=17 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib.py::deserialize_keras_object file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib.py
- rank=18 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::save_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=19 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_custom_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=20 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::_serialize_model_as_json file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=21 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::_save_model_to_fileobj file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=22 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/model_benchmark/image_classification_benchmark.py::load_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/model_benchmark/image_classification_benchmark.py
- rank=23 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py::DataAdapter.get_tf_dataset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py
- rank=24 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=25 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py
- rank=26 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::constant file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=27 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::_load_model_from_fileobj file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=28 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py::Config.__getattr__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py
- rank=29 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=30 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py::associative_scan file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py
- rank=31 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.layers file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=32 layer=FUNCTION tokens=387 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::load_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=33 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::save_weights_only file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=34 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::_model_from_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=35 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py::_tensorflow_uses file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py
- rank=36 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=37 layer=FUNCTION tokens=6 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::copy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py

## context

```text
file saving/saving_lib.py
imports: datetime, io, json, math, os, pathlib, shutil, tempfile
defines: DiskIOStore, H5IOStore, ShardedH5IOStore, NpzIOStore, save_model, _serialize_model_as_json, _save_model_to_dir, _save_model_to_fileobj, _upload_model_to_hf, load_model, _load_model_from_dir, _model_from_config, _load_model_from_fileobj, save_weights_only, load_weights_only, _raise_loading_failure, _write_to_zip_recursively, _name_key, _walk_saveable, _save_state, _load_state, _save_container_state, _load_container_state, get_temp_dir, get_attr_skipset, is_memory_sufficient, _split_path_components, _write_nested_dict_to_dir, _save_assets_to_dict, _load_assets_from_dict

file keras/guides/sequential_model.py
imports: keras
defines: —

file _tf_keras/keras/__init__.py
imports: keras
defines: —

class RandomHueTest(testing.TestCase):  [layers/preprocessing/image_preprocessing/random_hue_test.py:10]
methods: test_layer, test_random_hue_inference
         test_random_hue_no_change_with_zero_factor
         test_random_hue_randomness
         test_random_hue_value_range_0_to_1
         test_random_hue_value_range_0_to_255
         test_tf_data_compatibility

class RandomContrastTest(testing.TestCase):  [layers/preprocessing/image_preprocessing/random_contrast_test.py:9]
methods: test_dict_input, test_layer
         test_random_contrast_with_value_range_0_to_1
         test_random_contrast_with_value_range_0_to_255
         test_tf_data_compatibility

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

class RandomPosterizationTest(testing.TestCase):  [layers/preprocessing/image_preprocessing/random_posterization_test.py:10]
methods: test_layer, test_random_posterization_basic
         test_random_posterization_inference
         test_random_posterization_randomness
         test_random_posterization_value_range_0_to_1
         test_random_posterization_value_range_0_to_255
         test_tf_data_compatibility

class LayerBenchmark:  [benchmarks/layer_benchmark/base_benchmark.py:103]
methods: _build_keras_model, _build_tf_keras_model
         benchmark_predict, benchmark_train, __init__

class ModelVisualizationTest(testing.TestCase):  [keras/integration_tests/model_visualization_test.py:85]
methods: multi_plot_model, test_plot_complex
         test_plot_functional_in_functional
         test_plot_functional_in_functional_in_functional
         test_plot_functional_in_sequential_in_sequential
         test_plot_functional_model
         test_plot_functional_model_with_splits_and_merges
         test_plot_nested_functional_model
         test_plot_sequential_in_sequential
         test_plot_sequential_in_sequential_in_sequential
         test_plot_sequential_model
         test_plot_subclassed_model

class CustomModel(keras.Model):  [keras/integration_tests/tf_custom_fit_test.py:8]
methods: metrics, train_step, __init__

class MyModel(Model):  [keras/examples/demo_custom_tf_workflow.py:37]
methods: call, __init__

class SavedModelTrackableView(tf.train.TrackableView):  [export/saved_model_export_archive.py:338]
methods: —

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

    def _build_tf_keras_model(self, input_shape, flat_call_inputs=True):
        inputs = []
        if not isinstance(input_shape[0], (tuple, list)):
            input_shape = [input_shape]

        for shape in input_shape:
            inputs.append(tf.keras.Input(shape=shape))

        if flat_call_inputs:
            outputs = self._tf_keras_layer(*inputs)
        else:
            outputs = self._tf_keras_layer(inputs)
        return tf.keras.Model(inputs=inputs, outputs=outputs)

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

def _save_model_to_fileobj(model, fileobj, weights_format):
    config_json, metadata_json = _serialize_model_as_json(model)

    with zipfile.ZipFile(fileobj, "w") as zf:
        with zf.open(_METADATA_FILENAME, "w") as f:
            f.write(metadata_json.encode())
        with zf.open(_CONFIG_FILENAME, "w") as f:
            f.write(config_json.encode())

        weights_file_path = None
        weights_store = None
        asset_store = None
    # ... truncated

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

    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

    def __init__(
        self,
        layer_name,
        init_args,
        input_shape,
        flat_call_inputs=True,
        jit_compile=True,
        keras_layer=None,
        tf_keras_layer=None,
    ):
        self.layer_name = layer_name
        _keras_layer_class = getattr(keras.layers, layer_name)
    # ... truncated

def constant(value, dtype=None, shape=None, name=None):
    """DEPRECATED."""
    if dtype is None:
        dtype = backend.floatx()

    return tf.constant(value, dtype=dtype, shape=shape, name=name)

def _load_model_from_fileobj(fileobj, custom_objects, compile, safe_mode):
    with zipfile.ZipFile(fileobj, "r") as zf:
        with zf.open(_CONFIG_FILENAME, "r") as f:
            config_json = f.read()

        model = _model_from_config(
            config_json, custom_objects, compile, safe_mode
        )

        all_filenames = zf.namelist()
        extract_dir = None
        weights_store = None
    # ... truncated

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

    def layers(self, _):
        raise AttributeError(
            "`Sequential.layers` attribute is reserved and should not be used. "
            "Use `add()` and `pop()` to change the layers in this model."
        )

def load_model(filepath, custom_objects=None, compile=True, safe_mode=True):
    """Load a zip archive representing a Keras model."""
    if isinstance(filepath, io.IOBase):
        return _load_model_from_fileobj(
            filepath, custom_objects, compile, safe_mode
        )
    elif str(filepath).startswith("hf://"):
        if huggingface_hub is None:
            raise ImportError(
                "To load models from the Hugging Face Hub, "
                "you must install the `huggingface_hub` package."
            )

        repo_id = filepath[5:]
        folder_path = huggingface_hub.snapshot_download(
            repo_id=repo_id,
            library_name="keras",
            library_version=keras_version,
        )
        return _load_model_from_dir(
            folder_path, custom_objects, compile, safe_mode
        )
    else:
        filepath = str(filepath)
        if not filepath.endswith(".keras"):
            is_keras_dir = file_utils.isdir(filepath) and file_utils.exists(
                file_utils.join(filepath, "config.json")
            )
            if is_keras_dir:
                return _load_model_from_dir(
                    filepath, custom_objects, compile, safe_mode
                )
            raise ValueError(
                "Invalid filename: expected a `.keras` extension. "
                f"Received: filepath={filepath}"
            )
        with open(filepath, "rb") as f:
            return _load_model_from_fileobj(
                f, custom_objects, compile, safe_mode
            )

def save_weights_only(
    model, filepath, max_shard_size=None, objects_to_skip=None
):
    """Save only the weights of a model to a target filepath.

    Supports both `.weights.h5` and `.keras`.
    """
    # ... truncated

def _model_from_config(config_json, custom_objects, compile, safe_mode):
    # Note: we should NOT use a custom JSON decoder. Anything that
    # needs custom decoding must be handled in deserialize_keras_object.
    config_dict = json.loads(config_json)
    if not compile:
        # Disable compilation
        config_dict["compile_config"] = None
    # Construct the model from the configuration file in the archive.
    with ObjectSharingScope():
        model = deserialize_keras_object(
            config_dict, custom_objects, safe_mode=safe_mode
        )
    return model

def _tensorflow_uses(device_type):
    import tensorflow as tf

    return len(tf.config.list_physical_devices(device_type.upper())) > 0

    def output(self):
        return self._outputs_struct

def copy(x):
    return x
```

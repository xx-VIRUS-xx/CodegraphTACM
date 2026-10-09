# keras-16 :: hybrid-cs

query: Modify Sequential config to include model name (breaking change). Matches tf.keras behavior as of TF 1.11.0. (#11133)

## selected nodes

- rank=1 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_custom_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=2 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=3 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/legacy_h5_format_test.py::LegacyH5BackwardsCompatTest._check_reloading_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/legacy_h5_format_test.py
- rank=4 layer=FUNCTION tokens=159 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_basic_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=5 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/model_benchmark/image_classification_benchmark.py::load_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/model_benchmark/image_classification_benchmark.py
- rank=6 layer=FUNCTION tokens=347 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::model_metadata file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py
- rank=7 layer=FUNCTION tokens=688 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::model_from_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py
- rank=8 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._write_keras_model_summary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=9 layer=FUNCTION tokens=618 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::Model.from_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py
- rank=10 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/legacy_h5_format_test.py::get_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/legacy_h5_format_test.py
- rank=11 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark._build_tf_keras_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py
- rank=12 layer=FUNCTION tokens=337 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard_test.py::TestTensorBoardV2.fitModelAndAssertKerasModelWritten file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard_test.py
- rank=13 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::LossFunctionWrapper.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py
- rank=14 layer=FUNCTION tokens=441 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py
- rank=15 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/reduction_metrics.py::MeanMetricWrapper.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/reduction_metrics.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_custom_sequential_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/legacy_h5_format_test.py::LegacyH5BackwardsCompatTest._check_reloading_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/legacy_h5_format_test.py]
    def _check_reloading_model(self, ref_input, model, tf_keras_model):
        # Whole model file
        ref_output = tf_keras_model(ref_input)
        temp_filepath = os.path.join(self.get_temp_dir(), "model.h5")
        tf_keras_model.save(temp_filepath)
        loaded = legacy_h5_format.load_model_from_hdf5(temp_filepath)
        output = loaded(ref_input)
        self.assertAllClose(output, ref_output, atol=1e-5)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_basic_sequential_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/model_benchmark/image_classification_benchmark.py::load_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/model_benchmark/image_classification_benchmark.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::model_metadata [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::model_from_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py]
def model_from_config(config, custom_objects=None):
    """Instantiates a Keras model from its config.

    Args:
        config: Configuration dictionary.
        custom_objects: Optional dictionary mapping names
            (strings) to custom classes or functions to be
            considered during deserialization.

    Returns:
        A Keras model instance (uncompiled).

    Raises:
        TypeError: if `config` is not a dictionary.
    """
    if isinstance(config, list):
        raise TypeError(
            "`model_from_config` expects a dictionary, not a list. "
            f"Received: config={config}. Did you meant to use "
            "`Sequential.from_config(config)`?"
        )

    global MODULE_OBJECTS

    if not hasattr(MODULE_OBJECTS, "ALL_OBJECTS"):
        from keras.src import layers
        from keras.src import models

        MODULE_OBJECTS.ALL_OBJECTS = layers.__dict__
        MODULE_OBJECTS.ALL_OBJECTS["InputLayer"] = layers.InputLayer
        MODULE_OBJECTS.ALL_OBJECTS["Functional"] = models.Functional
        MODULE_OBJECTS.ALL_OBJECTS["Model"] = models.Model
        MODULE_OBJECTS.ALL_OBJECTS["Sequential"] = models.Sequential

    batch_input_shape = config["config"].pop("batch_input_shape", None)
    if batch_input_shape is not None:
        if config["class_name"] == "InputLayer":
            config["config"]["batch_shape"] = batch_input_shape
        else:
            config["config"]["input_shape"] = batch_input_shape

    axis = config["config"].pop("axis", None)
    if axis is not None:
        if isinstance(axis, list) and len(axis) == 1:
            config["config"]["axis"] = int(axis[0])
        elif isinstance(axis, (int, float)):
            config["config"]["axis"] = int(axis)

    # Handle backwards compatibility for Keras lambdas
    if config["class_name"] == "Lambda":
        for dep_arg in LAMBDA_DEP_ARGS:
            _ = config["config"].pop(dep_arg, None)
        function_config = config["config"]["function"]
        if isinstance(function_config, list):
            function_dict = {"class_name": "__lambda__", "config": {}}
            function_dict["config"]["code"] = function_config[0]
            function_dict["config"]["defaults"] = function_config[1]
            function_dict["config"]["closure"] = function_config[2]
            config["config"]["function"] = function_dict

    return serialization.deserialize_keras_object(
        config,
        module_objects=MODULE_OBJECTS.ALL_OBJECTS,
        custom_objects=custom_objects,
        printable_module_name="layer",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._write_keras_model_summary [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py]
    def _write_keras_model_summary(self):
        """Writes Keras graph network summary to TensorBoard."""
        with self._train_writer.as_default():
            if (
                self.model.__class__.__name__ == "Functional"
                or self.model.__class__.__name__ == "Sequential"
            ):
                keras_model_summary("keras", self.model, step=0)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::Model.from_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py]
    def from_config(cls, config, custom_objects=None):
        from keras.src.models.functional import Functional

        functional_config_keys = [
            "name",
            "layers",
            "input_layers",
            "output_layers",
        ]
        is_functional_config = all(
            key in config for key in functional_config_keys
        )
        argspec = inspect.getfullargspec(cls.__init__)
        functional_init_args = inspect.getfullargspec(Functional.__init__).args[
            1:
        ]
        revivable_as_functional = (
            cls in {Functional, Model}
            or argspec.args[1:] == functional_init_args
            or (argspec.varargs == "args" and argspec.varkw == "kwargs")
        )
        if is_functional_config and revivable_as_functional:
            # Revive Functional model
            # (but not Functional subclasses with a custom __init__)
            from keras.src.models.functional import functional_from_config

            return functional_from_config(
                cls, config, custom_objects=custom_objects
            )

        # Either the model has a custom __init__, or the config
        # does not contain all the information necessary to
        # revive a Functional model. This happens when the user creates
        # subclassed models where `get_config()` is returning
        # insufficient information to be considered a Functional model.
        # In this case, we fall back to provide all config into the
        # constructor of the class.
        try:
            return cls(**config)
        except TypeError as e:
            raise TypeError(
                "Unable to revive model from config. When overriding "
                "the `get_config()` method, make sure that the "
                "returned config contains all items used as arguments "
                f"in the  constructor to {cls}, "
                "which is the default behavior. "
                "You can override this default behavior by defining a "
                "`from_config(cls, config)` class method to specify "
                "how to create an "
                f"instance of {cls.__name__} from its config.\n\n"
                f"Received config={config}\n\n"
                f"Error encountered during deserialization: {e}"
            )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/legacy_h5_format_test.py::get_sequential_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/legacy_h5_format_test.py]
def get_sequential_model(keras):
    return keras.Sequential(
        [
            keras.layers.Input((3,), batch_size=2),
            keras.layers.Dense(4, activation="relu"),
            keras.layers.BatchNormalization(
                moving_mean_initializer="uniform", gamma_initializer="uniform"
            ),
            keras.layers.Dense(5, activation="softmax"),
        ]
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark._build_tf_keras_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard_test.py::TestTensorBoardV2.fitModelAndAssertKerasModelWritten [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard_test.py]
    def fitModelAndAssertKerasModelWritten(self, model):
        x, y = np.ones((10, 10, 10, 1)), np.ones((10, 1))
        logdir, train_dir, validation_dir = self._get_log_dirs()
        tb_cbk = callbacks.TensorBoard(
            logdir, write_graph=True, profile_batch=0
        )
        model.fit(
            x,
            y,
            batch_size=2,
            epochs=3,
            validation_data=(x, y),
            callbacks=[tb_cbk],
        )
        summary_file = list_summaries(logdir)
        self.assertEqual(
            summary_file.tensors,
            {
                _ObservedSummary(logdir=train_dir, tag="keras"),
            },
        )
        if not model.run_eagerly:
            # There should be one train graph
            self.assertLen(summary_file.graph_defs, 1)
            for graph_def in summary_file.graph_defs:
                graph_def_str = str(graph_def)

                # All the model layers should appear in the graphs
                for layer in model.layers:
                    if "input" not in layer.name:
                        self.assertIn(layer.name, graph_def_str)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::LossFunctionWrapper.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py]
    def get_config(self):
        config = super().get_config()
        config.update({"fn": serialization_lib.serialize_keras_object(self.fn)})
        config.update(serialization_lib.serialize_keras_object(self._fn_kwargs))
        return config

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py]
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
        _tf_keras_layer_class = getattr(tf.keras.layers, layer_name)

        if keras_layer is None:
            # Sometimes you want to initialize the keras layer and tf_keras
            # layer in a different way. For example, `Bidirectional` layer,
            # which takes in `keras.layers.Layer` and
            # `tf.keras.layer.Layer` separately.
            self._keras_layer = _keras_layer_class(**init_args)
        else:
            self._keras_layer = keras_layer

        if tf_keras_layer is None:
            self._tf_keras_layer = _tf_keras_layer_class(**init_args)
        else:
            self._tf_keras_layer = tf_keras_layer

        self.input_shape = input_shape
        self._keras_model = self._build_keras_model(
            input_shape, flat_call_inputs
        )
        self._tf_keras_model = self._build_tf_keras_model(
            input_shape, flat_call_inputs
        )

        self._keras_model.compile(
            loss="mse", optimizer="sgd", jit_compile=jit_compile
        )
        self._tf_keras_model.compile(
            loss="mse", optimizer="sgd", jit_compile=jit_compile
        )

        self.flat_call_inputs = flat_call_inputs
        self.jit_compile = jit_compile
        self.input_shape = input_shape

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/reduction_metrics.py::MeanMetricWrapper.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/reduction_metrics.py]
    def get_config(self):
        base_config = super().get_config()
        config = {"fn": serialization_lib.serialize_keras_object(self._fn)}
        config.update(serialization_lib.serialize_keras_object(self._fn_kwargs))
        return {**base_config, **config}
```

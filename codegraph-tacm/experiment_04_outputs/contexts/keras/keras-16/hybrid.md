# keras-16 :: hybrid

query: Modify Sequential config to include model name (breaking change). Matches tf.keras behavior as of TF 1.11.0. (#11133)

## selected nodes

- rank=1 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py::DataAdapter.get_tf_dataset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py
- rank=2 layer=FUNCTION tokens=441 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py
- rank=3 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._write_keras_model_summary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py
- rank=4 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_custom_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=5 layer=FUNCTION tokens=688 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::model_from_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py
- rank=6 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py::LayerBenchmark._build_tf_keras_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/base_benchmark.py
- rank=7 layer=FUNCTION tokens=159 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::_get_basic_sequential_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=8 layer=FUNCTION tokens=1420 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model.py::ExportArchive.add_endpoint file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model.py
- rank=9 layer=FUNCTION tokens=347 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::model_metadata file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py
- rank=10 layer=FUNCTION tokens=232 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_tensorflow.py::run_training file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_tensorflow.py
- rank=11 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py::Node.input_tensors file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py::DataAdapter.get_tf_dataset [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py::TensorBoard._write_keras_model_summary [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/tensorboard.py]
    def _write_keras_model_summary(self):
        """Writes Keras graph network summary to TensorBoard."""
        with self._train_writer.as_default():
            if (
                self.model.__class__.__name__ == "Functional"
                or self.model.__class__.__name__ == "Sequential"
            ):
                keras_model_summary("keras", self.model, step=0)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model.py::ExportArchive.add_endpoint [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model.py]
    def add_endpoint(self, name, fn, input_signature=None, **kwargs):
        """Register a new serving endpoint.

        Args:
            name: `str`. The name of the endpoint.
            fn: A callable. It should only leverage resources
                (e.g. `keras.Variable` objects or `tf.lookup.StaticHashTable`
                objects) that are available on the models/layers tracked by the
                `ExportArchive` (you can call `.track(model)` to track a new
                model).
                The shape and dtype of the inputs to the function must be
                known. For that purpose, you can either 1) make sure that `fn`
                is a `tf.function` that has been called at least once, or 2)
                provide an `input_signature` argument that specifies the shape
                and dtype of the inputs (see below).
            input_signature: Optional. Specifies the shape and dtype of `fn`.
                Can be a structure of `keras.InputSpec`, `tf.TensorSpec`,
                `backend.KerasTensor`, or backend tensor (see below for an
                example showing a `Functional` model with 2 input arguments). If
                not provided, `fn` must be a `tf.function` that has been called
                at least once. Defaults to `None`.
            **kwargs: Additional keyword arguments:
                - Specific to the JAX backend:
                    - `is_static`: Optional `bool`. Indicates whether `fn` is
                        static. Set to `False` if `fn` involves state updates
                        (e.g., RNG seeds).
                    - `jax2tf_kwargs`: Optional `dict`. Arguments for
                        `jax2tf.convert`. See [`jax2tf.convert`](
                            https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md).
                        If `native_serialization` and `polymorphic_shapes` are
                        not provided, they are automatically computed.

        Returns:
            The `tf.function` wrapping `fn` that was added to the archive.

        Example:

        Adding an endpoint using the `input_signature` argument when the
        model has a single input argument:

        ```python
        export_archive = ExportArchive()
        export_archive.track(model)
        export_archive.add_endpoint(
            name="serve",
            fn=model.call,
            input_signature=[keras.InputSpec(shape=(None, 3), dtype="float32")],
        )
        ```

        Adding an endpoint using the `input_signature` argument when the
        model has two positional input arguments:

        ```python
        export_archive = ExportArchive()
        export_archive.track(model)
        export_archive.add_endpoint(
            name="serve",
            fn=model.call,
            input_signature=[
                keras.InputSpec(shape=(None, 3), dtype="float32"),
                keras.InputSpec(shape=(None, 4), dtype="float32"),
            ],
        )
        ```

        Adding an endpoint using the `input_signature` argument when the
        model has one input argument that is a list of 2 tensors (e.g.
        a Functional model with 2 inputs):

        ```python
        model = keras.Model(inputs=[x1, x2], outputs=outputs)

        export_archive = ExportArchive()
        export_archive.track(model)
        export_archive.add_endpoint(
            name="serve",
            fn=model.call,
            input_signature=[
                [
                    keras.InputSpec(shape=(None, 3), dtype="float32"),
                    keras.InputSpec(shape=(None, 4), dtype="float32"),
                ],
            ],
        )
        ```

        This also works with dictionary inputs:

        ```python
        model = keras.Model(inputs={"x1": x1, "x2": x2}, outputs=outputs)

        export_archive = ExportArchive()
        export_archive.track(model)
        export_archive.add_endpoint(
            name="serve",
            fn=model.call,
            input_signature=[
                {
                    "x1": keras.InputSpec(shape=(None, 3), dtype="float32"),
                    "x2": keras.InputSpec(shape=(None, 4), dtype="float32"),
                },
            ],
        )
        ```

        Adding an endpoint that is a `tf.function`:

        ```python
        @tf.function()
        def serving_fn(x):
            return model(x)

        # The function must be traced, i.e. it must be called at least once.
        serving_fn(tf.random.normal(shape=(2, 3)))

        export_archive = ExportArchive()
        export_archive.track(model)
        export_archive.add_endpoint(name="serve", fn=serving_fn)
        ```

        Combining a model with some TensorFlow preprocessing, which can use
        TensorFlow resources:

        ```python
        lookup_table = tf.lookup.StaticHashTable(initializer, default_value=0.0)

        export_archive = ExportArchive()
        model_fn = export_archive.track_and_add_endpoint(
            "model_fn",
            model,
            input_signature=[tf.TensorSpec(shape=(None, 5), dtype=tf.float32)],
        )
        export_archive.track(lookup_table)

        @tf.function()
        def serving_fn(x):
            x = lookup_table.lookup(x)
            return model_fn(x)

        export_archive.add_endpoint(name="serve", fn=serving_fn)
        ```
        """
        raise NotImplementedError(
            "add_endpoint() is not implemented for this backend."
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_tensorflow.py::run_training [/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_tensorflow.py]
def run_training(epochs=1):
    # Create a MirroredStrategy.
    strategy = tf.distribute.MirroredStrategy()

    # Open a strategy scope and create/restore the model
    with strategy.scope():
        model = make_or_restore_model()

        callbacks = [
            # This callback saves a SavedModel every epoch
            # We include the current epoch in the folder name.
            keras.callbacks.ModelCheckpoint(
                filepath=os.path.join(checkpoint_dir, "ckpt-{epoch}.keras"),
                save_freq="epoch",
            )
        ]
        model.fit(
            train_dataset,
            epochs=epochs,
            callbacks=callbacks,
            validation_data=val_dataset,
            verbose=2,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py::Node.input_tensors [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py]
    def input_tensors(self):
        return self.arguments.keras_tensors
```

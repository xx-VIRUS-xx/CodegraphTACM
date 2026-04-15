# keras-44 :: hybrid

query: Fix RNN layers dynamic `trainable` attr

## selected nodes

- rank=1 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=2 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=3 layer=FUNCTION tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=4 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN._create_state_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=5 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=6 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py::JaxExportArchive._backend_track_layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py
- rank=7 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.non_trainable_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=8 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/export.py::TFExportArchive._backend_track_layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/export.py
- rank=9 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_simple_rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py
- rank=10 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._not_implemented_error file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=11 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable.trainable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py
- rank=12 layer=FUNCTION tokens=523 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._initialize_tracker file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=13 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py::SavedModelExportArchive.trainable_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py
- rank=14 layer=FUNCTION tokens=679 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/rnn.py::lstm file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/rnn.py
- rank=15 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py::DenseTest.stateless_loss_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py
- rank=16 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py::EinsumDenseTest.stateless_loss_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py
- rank=17 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.layer_property file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=18 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=19 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_custom_jax_workflow.py::train_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_custom_jax_workflow.py
- rank=20 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=21 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py::NoTrainingSpecified.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py]
    def __init__(self, layers=None, trainable=True, name=None):
        super().__init__(trainable=trainable, name=name)
        self._functional = None
        self._layers = []
        if layers:
            for layer in layers:
                self.add(layer, rebuild=False)
            self._maybe_rebuild()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def trainable(self, value):
        """Sets trainable attribute for the layer and its sublayers.

        When this value is changed during training (e.g. with a
        `Callback`) you need to call the parent
        `Model.make_train_function` with `force=True` in order to
        recompile the training graph.

        Args:
            value: Boolean with the desired state for the layer's trainable
                attribute.
        """
        value = bool(value)
        self._trainable = value
        for v in self._trainable_variables:
            v.trainable = value
        for layer in self._layers:
            layer.trainable = value

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def build(self, sequences_shape, initial_state_shape=None):
        # Build cell (if layer).
        step_input_shape = (sequences_shape[0],) + tuple(sequences_shape[2:])
        if isinstance(self.cell, Layer) and not self.cell.built:
            self.cell.build(step_input_shape)
            self.cell.built = True
        if self.stateful:
            if self.states is not None:
                self.reset_state()
            else:
                if sequences_shape[0] is None:
                    raise ValueError(
                        "When using `stateful=True` in a RNN, the "
                        "batch size must be static. Found dynamic "
                        f"batch size: sequence.shape={sequences_shape}"
                    )
                self._create_state_variables(sequences_shape[0])
                self._expected_batch_size = ops.shape(
                    tree.flatten(self.states)[0]
                )[0]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN._create_state_variables [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def _create_state_variables(self, batch_size):
        with backend.name_scope(self.name, caller=self):
            self.states = tree.map_structure(
                lambda value: backend.Variable(
                    value,
                    trainable=False,
                    dtype=self.variable_dtype,
                    name="rnn_state",
                ),
                self.get_initial_state(batch_size),
            )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable_variables [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def trainable_variables(self):
        """List of all trainable layer state.

        This is equivalent to `layer.trainable_weights`.
        """
        if not self.trainable:
            return []
        return [v for v in self.variables if v.trainable]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py::JaxExportArchive._backend_track_layer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py]
    def _backend_track_layer(self, layer):
        # Variables in the lists below are actually part of the trackables
        # that get saved, because the lists are created in __init__.
        trainable_variables = layer.trainable_variables
        non_trainable_variables = layer.non_trainable_variables

        self._tf_trackable.trainable_variables += tree.map_structure(
            self._convert_to_tf_variable, trainable_variables
        )
        self._tf_trackable.non_trainable_variables += tree.map_structure(
            self._convert_to_tf_variable, non_trainable_variables
        )
        self._tf_trackable.variables = (
            self._tf_trackable.trainable_variables
            + self._tf_trackable.non_trainable_variables
        )

        self._backend_trainable_variables += trainable_variables
        self._backend_non_trainable_variables += non_trainable_variables
        self._backend_variables = (
            self._backend_trainable_variables
            + self._backend_non_trainable_variables
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.non_trainable_variables [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def non_trainable_variables(self):
        """List of all non-trainable layer state.

        This extends `layer.non_trainable_weights` to include all state used by
        the layer including state for metrics and `SeedGenerator`s.
        """
        if not self.trainable:
            return self.variables
        return [v for v in self.variables if not v.trainable]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/export.py::TFExportArchive._backend_track_layer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/export.py]
    def _backend_track_layer(self, layer):
        # Variables in the lists below are actually part of the trackables
        # that get saved, because the lists are created in __init__.
        variables = layer.variables
        trainable_variables = layer.trainable_variables
        non_trainable_variables = layer.non_trainable_variables
        self._tf_trackable.variables += variables
        self._tf_trackable.trainable_variables += trainable_variables
        self._tf_trackable.non_trainable_variables += non_trainable_variables

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_simple_rnn [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py]
def benchmark_simple_rnn(
    num_samples,
    batch_size,
    jit_compile=True,
):
    layer_name = "SimpleRNN"
    init_args = {
        "units": 32,
    }
    benchmark = LayerBenchmark(
        layer_name,
        init_args,
        input_shape=[256, 256],
        jit_compile=jit_compile,
    )

    benchmark.benchmark_predict(
        num_samples=num_samples,
        batch_size=batch_size,
    )

    benchmark.benchmark_train(
        num_samples=num_samples,
        batch_size=batch_size,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._not_implemented_error [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _not_implemented_error(self, attr, msg=None):
        if callable(attr):
            attr_name = attr.__name__
            attr_type = "method"
        else:
            attr_name = str(attr)
            attr_type = "attribute"
        msg = f" {msg}" if msg is not None else ""
        return NotImplementedError(
            f"Layer {self.__class__.__name__} does not have a `{attr_name}` "
            f"{attr_type} implemented.{msg}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable.trainable [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py]
    def trainable(self, value):
        self._trainable = bool(value)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._initialize_tracker [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _initialize_tracker(self):
        if hasattr(self, "_tracker"):
            return

        trainable_variables = []
        non_trainable_variables = []
        layers = []
        metrics = []
        seed_generators = []
        self._tracker = tracking.Tracker(
            {
                "trainable_variables": (
                    lambda x: isinstance(x, backend.Variable) and x.trainable,
                    trainable_variables,
                ),
                "non_trainable_variables": (
                    lambda x: (
                        isinstance(x, backend.Variable) and not x.trainable
                    ),
                    non_trainable_variables,
                ),
                "metrics": (lambda x: isinstance(x, Metric), metrics),
                "layers": (
                    lambda x: (
                        isinstance(x, Layer) and not isinstance(x, Metric)
                    ),
                    layers,
                ),
                "seed_generators": (
                    lambda x: isinstance(x, backend.random.SeedGenerator),
                    seed_generators,
                ),
            },
            exclusions={"non_trainable_variables": ["trainable_variables"]},
        )
        if backend.backend() == "tensorflow":
            # Remove attribute tracking for lists (TF-specific attribute)
            _self_setattr_tracking = getattr(
                self, "_self_setattr_tracking", True
            )
            self._self_setattr_tracking = False

        self._trainable_variables = trainable_variables
        self._non_trainable_variables = non_trainable_variables
        self._layers = layers
        self._metrics = metrics
        self._seed_generators = seed_generators

        if backend.backend() == "tensorflow":
            # Reset attribute tracking (TF-specific)
            self._self_setattr_tracking = _self_setattr_tracking

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py::SavedModelExportArchive.trainable_variables [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py]
    def trainable_variables(self):
        return self._tf_trackable.trainable_variables

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/rnn.py::lstm [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/rnn.py]
def lstm(
    inputs,
    initial_state_h,
    initial_state_c,
    mask,
    kernel,
    recurrent_kernel,
    bias,
    activation,
    recurrent_activation,
    return_sequences=False,
    go_backwards=False,
    unroll=False,
):
    # Masking is not supported by the cuDNN path; fall back to the
    # generic RNN loop which handles masking correctly.
    if mask is not None:
        raise NotImplementedError

    if not cudnn_ok(
        activation,
        recurrent_activation,
        unroll,
        use_bias=bias is not None,
    ):
        raise NotImplementedError

    try:
        from jax.experimental.rnn import lstm as jax_lstm
    except ImportError as e:
        raise NotImplementedError(
            f"jax.experimental.rnn unavailable: {e}"
        ) from e

    input_size = kernel.shape[0]
    hidden_size = recurrent_kernel.shape[0]
    batch_size = inputs.shape[0]

    # Transpose Keras kernels to cuDNN layout and flatten.
    # Gate order [i, f, c, o] matches cuDNN [i, f, g, o].
    W_ih = jnp.asarray(kernel).T
    W_hh = jnp.asarray(recurrent_kernel).T

    if bias is not None:
        b_ih = jnp.asarray(bias)
    else:
        b_ih = jnp.zeros(4 * hidden_size)
    b_hh = jnp.zeros_like(b_ih)

    # cuDNN flat weight order: [W_ih, W_hh, b_ih, b_hh]
    weights = jnp.concatenate(
        [W_ih.ravel(), W_hh.ravel(), b_ih.ravel(), b_hh.ravel()]
    )

    # cuDNN expects (num_layers * num_directions, batch, hidden)
    h_0 = jnp.asarray(initial_state_h)
    c_0 = jnp.asarray(initial_state_c)
    if h_0.ndim == 2:
        h_0 = h_0[jnp.newaxis]
        c_0 = c_0[jnp.newaxis]

    if go_backwards:
        inputs = jnp.flip(inputs, axis=1)

    seq_lengths = jnp.full((batch_size,), inputs.shape[1], dtype=jnp.int32)

    try:
        y, h_n, c_n = jax_lstm(
            inputs,
            h_0,
            c_0,
            weights,
            seq_lengths,
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=1,
            dropout=0.0,
            bidirectional=False,
        )
    except (RuntimeError, TypeError, ValueError) as e:
        raise NotImplementedError(f"cuDNN LSTM failed: {e}") from e

    # y: (batch, seq_len, hidden), h_n/c_n: (1, batch, hidden)
    h_n = h_n.squeeze(0)
    c_n = c_n.squeeze(0)
    last_output = y[:, -1]

    if not return_sequences:
        outputs = last_output[:, jnp.newaxis, :]
    else:
        outputs = y

    if go_backwards and return_sequences:
        outputs = jnp.flip(outputs, axis=1)

    return last_output, outputs, [h_n, c_n]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py::DenseTest.stateless_loss_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py]
            def stateless_loss_fn(trainable_variables, x, dy):
                y = layer.stateless_call(
                    trainable_variables, [], x, training=True
                )[0]
                loss = y * ops.cast(dy, y.dtype)
                return ops.sum(loss)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py::EinsumDenseTest.stateless_loss_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py]
            def stateless_loss_fn(trainable_variables, x, dy):
                y = layer.stateless_call(
                    trainable_variables, [], x, training=True
                )[0]
                loss = y * ops.cast(dy, y.dtype)
                return ops.sum(loss)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.layer_property [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py]
    def layer_property(self):
        # Properties for layers in the functional graph should not affect saving
        return self.layer_attr

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py]
    def reset_dropout_mask(self):
        """Reset the cached dropout mask if any.

        The RNN layer invokes this in the `call()` method
        so that the cached mask is cleared after calling `cell.call()`. The
        mask should be cached across all timestep within the same batch, but
        shouldn't be cached between batches.
        """
        self._dropout_mask = None

# /Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_custom_jax_workflow.py::train_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_custom_jax_workflow.py]
def train_step(state, data):
    trainable_variables, non_trainable_variables, optimizer_variables = state
    x, y = data
    (loss, non_trainable_variables), grads = grad_fn(
        trainable_variables, non_trainable_variables, x, y
    )
    trainable_variables, optimizer_variables = optimizer.stateless_apply(
        optimizer_variables, grads, trainable_variables
    )
    # Return updated state
    return loss, (
        trainable_variables,
        non_trainable_variables,
        optimizer_variables,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py]
    def __init__(self, **kwargs):
        inputs = keras.Input(shape=(4,), batch_size=2)
        dense = keras.layers.Dense(1, name="first_dense")
        x = dense(inputs)
        outputs = keras.layers.Dense(1, name="second_dense")(x)
        super().__init__(inputs=inputs, outputs=outputs, **kwargs)
        # Attrs for layers in the functional graph should not affect saving
        self.layer_attr = dense

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py::NoTrainingSpecified.build [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py]
            def build(self, input_shape):
                self.activation = layers.Activation("linear")
```

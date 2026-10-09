# keras-44 :: minilm

query: Fix RNN layers dynamic `trainable` attr

## selected nodes

- rank=1 layer=FUNCTION tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=2 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_simple_rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py
- rank=3 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=4 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=5 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.non_trainable_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=6 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=7 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py::DenseTest.stateless_loss_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py
- rank=8 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py::EinsumDenseTest.stateless_loss_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py
- rank=9 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable.trainable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py
- rank=10 layer=FUNCTION tokens=850 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=11 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CounterModel.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=12 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/export.py::TFExportArchive._backend_track_layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/export.py
- rank=13 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py::SavedModelExportArchive.trainable_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py
- rank=14 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=15 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py::JaxExportArchive._backend_track_layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py
- rank=16 layer=FUNCTION tokens=679 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/rnn.py::lstm file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/rnn.py
- rank=17 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer._get_call_rng file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=18 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py::NoTrainingSpecified.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable_variables [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def trainable_variables(self):
        """List of all trainable layer state.

        This is equivalent to `layer.trainable_weights`.
        """
        if not self.trainable:
            return []
        return [v for v in self.variables if v.trainable]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.non_trainable_variables [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def non_trainable_variables(self):
        """List of all non-trainable layer state.

        This extends `layer.non_trainable_weights` to include all state used by
        the layer including state for metrics and `SeedGenerator`s.
        """
        if not self.trainable:
            return self.variables
        return [v for v in self.variables if not v.trainable]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py]
    def __init__(self, layers=None, trainable=True, name=None):
        super().__init__(trainable=trainable, name=name)
        self._functional = None
        self._layers = []
        if layers:
            for layer in layers:
                self.add(layer, rebuild=False)
            self._maybe_rebuild()

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable.trainable [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py]
    def trainable(self, value):
        self._trainable = bool(value)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def call(
        self,
        sequences,
        initial_state=None,
        mask=None,
        training=False,
    ):
        timesteps = sequences.shape[1]
        if self.unroll and timesteps is None:
            raise ValueError(
                "Cannot unroll a RNN if the "
                "time dimension is undefined. \n"
                "- If using a Sequential model, "
                "specify the time dimension by passing "
                "an `Input()` as your first layer.\n"
                "- If using the functional API, specify "
                "the time dimension by passing a `shape` "
                "or `batch_shape` argument to your `Input()`."
            )

        if initial_state is None:
            if self.stateful:
                initial_state = self.states
            else:
                initial_state = self.get_initial_state(
                    batch_size=ops.shape(sequences)[0]
                )
        if self.stateful:
            actual_batch_size = sequences.shape[0]
            if (
                self._expected_batch_size is not None
                and actual_batch_size is not None
                and actual_batch_size != self._expected_batch_size
            ):
                raise ValueError(
                    f"If an RNN is stateful, the batch size of the "
                    f"input sequences must be the same as the batch "
                    f"size of the initial state. \n"
                    f"- Expected batch size: {self._expected_batch_size}\n"
                    f"- Received batch size: {actual_batch_size}"
                )

        # RNN expect the states in a list, even if single state.
        if not tree.is_nested(initial_state):
            initial_state = [initial_state]
        initial_state = list(initial_state)

        # Cast states to compute dtype.
        # Note that states may be deeply nested
        # (e.g. in the stacked cells case).
        initial_state = tree.map_structure(
            lambda x: backend.convert_to_tensor(
                x, dtype=self.cell.compute_dtype
            ),
            initial_state,
        )

        # Prepopulate the dropout state so that the inner_loop is stateless
        # this is particularly important for JAX backend.
        self._maybe_config_dropout_masks(
            self.cell, sequences[:, 0, :], initial_state
        )

        last_output, outputs, states = self.inner_loop(
            sequences=sequences,
            initial_state=initial_state,
            mask=mask,
            training=training,
        )
        last_output = ops.cast(last_output, self.compute_dtype)
        outputs = ops.cast(outputs, self.compute_dtype)
        states = tree.map_structure(
            lambda x: ops.cast(x, dtype=self.compute_dtype), states
        )
        self._maybe_reset_dropout_masks(self.cell)

        if self.stateful:
            for self_state, state in zip(
                tree.flatten(self.states), tree.flatten(states)
            ):
                self_state.assign(state)

        if self.return_sequences:
            output = outputs
        else:
            output = last_output

        if self.return_state:
            return output, *states
        return output

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CounterModel.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def __init__(self):
                super().__init__()
                self.train_counter = self.add_weight(
                    shape=(),
                    initializer="zeros",
                )
                self.test_counter = self.add_weight(
                    shape=(),
                    initializer="zeros",
                )
                self.predict_counter = self.add_weight(
                    shape=(),
                    initializer="zeros",
                )
                self.dense = layers.Dense(3)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py::SavedModelExportArchive.trainable_variables [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/saved_model_export_archive.py]
    def trainable_variables(self):
        return self._tf_trackable.trainable_variables

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py]
    def reset_dropout_mask(self):
        """Reset the cached dropout mask if any.

        The RNN layer invokes this in the `call()` method
        so that the cached mask is cleared after calling `cell.call()`. The
        mask should be cached across all timestep within the same batch, but
        shouldn't be cached between batches.
        """
        self._dropout_mask = None

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer._get_call_rng [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
    def _get_call_rng(self, training):
        """
        Returns a seed or seeds to pass as the `rng` argument of `call_fn`.

        By default, this returns a seed when `training` is `True`, and `None`
        when `training` is `False`. Override this to return a different
        structure or to pass seeds in inference mode too. Overrides should use
        `self._get_call_seed()` to obtain seeds.

        Returns:
            RNG key or structure of keys as tensors of shape [2] and the backend
            dtype for seeds.
        """
        if training:
            return self._get_call_seed()
        else:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py::NoTrainingSpecified.build [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py]
            def build(self, input_shape):
                self.activation = layers.Activation("linear")
```

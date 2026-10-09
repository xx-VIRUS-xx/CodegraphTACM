# keras-19 :: hybrid

query: Update the RNN cell API to be explicit about output_size. (#11021)

## selected nodes

- rank=1 layer=FUNCTION tokens=561 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=2 layer=FUNCTION tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=3 layer=FUNCTION tokens=850 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=4 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=5 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=6 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_output_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=7 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=8 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.get_initial_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=9 layer=FUNCTION tokens=218 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.compute_output_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=10 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.kernel_size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=11 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_simple_rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py
- rank=12 layer=FUNCTION tokens=516 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::adaptive_max_pool file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=13 layer=FUNCTION tokens=289 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.get_initial_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=14 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def __init__(
        self,
        cell,
        return_sequences=False,
        return_state=False,
        go_backwards=False,
        stateful=False,
        unroll=False,
        zero_output_for_mask=False,
        **kwargs,
    ):
        if isinstance(cell, (list, tuple)):
            cell = StackedRNNCells(cell)
        if "call" not in dir(cell):
            raise ValueError(
                "Argument `cell` should have a `call` method. "
                f"Received: cell={cell}"
            )
        if "state_size" not in dir(cell):
            raise ValueError(
                "The RNN cell should have a `state_size` attribute "
                "(single integer or list of integers, "
                "one integer per RNN state). "
                f"Received: cell={cell}"
            )
        super().__init__(**kwargs)

        # If True, the output for masked timestep will be zeros, whereas in the
        # False case, output from previous timestep is returned for masked
        # timestep.
        self.zero_output_for_mask = zero_output_for_mask
        self.cell = cell
        self.return_sequences = return_sequences
        self.return_state = return_state
        self.go_backwards = go_backwards
        self.stateful = stateful
        self.unroll = unroll

        self.supports_masking = True
        self.input_spec = None
        self.states = None
        self._expected_batch_size = None

        state_size = getattr(self.cell, "state_size", None)
        if state_size is None:
            raise ValueError(
                "state_size must be specified as property on the RNN cell."
            )
        if not isinstance(state_size, (list, tuple, int)):
            raise ValueError(
                "state_size must be an integer, or a list/tuple of integers "
                "(one for each state tensor)."
            )
        if isinstance(state_size, int):
            self.state_size = [state_size]
            self.single_state = True
        else:
            self.state_size = list(state_size)
            self.single_state = False

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.build [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py]
    def build(self, input_shape):
        for cell in self.cells:
            if isinstance(cell, Layer) and not cell.built:
                cell.build(input_shape)
                cell.built = True
            if getattr(cell, "output_size", None) is not None:
                output_dim = cell.output_size
            elif isinstance(cell.state_size, (list, tuple)):
                output_dim = cell.state_size[0]
            else:
                output_dim = cell.state_size
            batch_size = tree.flatten(input_shape)[0]
            input_shape = (batch_size, output_dim)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py]
    def reset_dropout_mask(self):
        """Reset the cached dropout mask if any.

        The RNN layer invokes this in the `call()` method
        so that the cached mask is cleared after calling `cell.call()`. The
        mask should be cached across all timestep within the same batch, but
        shouldn't be cached between batches.
        """
        self._dropout_mask = None

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_output_shape [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def compute_output_shape(self, sequences_shape, initial_state_shape=None):
        batch_size = sequences_shape[0]
        length = sequences_shape[1]
        states_shape = []
        for state_size in self.state_size:
            if isinstance(state_size, int):
                states_shape.append((batch_size, state_size))
            elif isinstance(state_size, (list, tuple)):
                states_shape.append([(batch_size, s) for s in state_size])

        output_size = getattr(self.cell, "output_size", None)
        if output_size is None:
            output_size = self.state_size[0]
        if not isinstance(output_size, int):
            raise ValueError("output_size must be an integer.")
        if self.return_sequences:
            output_shape = (batch_size, length, output_size)
        else:
            output_shape = (batch_size, output_size)
        if self.return_state:
            return output_shape, *states_shape
        return output_shape

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_mask [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def compute_mask(self, _, mask):
        # Time step masks must be the same for each input.
        # This is because the mask for an RNN is of size [batch, time_steps, 1],
        # and specifies which time steps should be skipped, and a time step
        # must be skipped for all inputs.
        mask = tree.flatten(mask)[0]
        output_mask = mask if self.return_sequences else None
        if self.return_state:
            state_mask = [None for _ in self.state_size]
            return [output_mask] + state_mask
        else:
            return output_mask

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.get_initial_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def get_initial_state(self, batch_size):
        get_initial_state_fn = getattr(self.cell, "get_initial_state", None)
        if get_initial_state_fn:
            init_state = get_initial_state_fn(batch_size=batch_size)
        else:
            return [
                ops.zeros((batch_size, d), dtype=self.cell.compute_dtype)
                for d in self.state_size
            ]

        # RNN expect the states in a list, even if single state.
        if not tree.is_nested(init_state):
            init_state = [init_state]
        # Force the state to be a list in case it is a namedtuple eg
        # LSTMStateTuple.
        return list(init_state)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.compute_output_shape [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py]
    def compute_output_shape(self, sequences_shape, initial_state_shape=None):
        batch_size = sequences_shape[0]
        steps = sequences_shape[1]
        step_shape = (batch_size,) + sequences_shape[2:]
        state_shape = self.cell.compute_output_shape(step_shape)[0][1:]

        if self.return_sequences:
            output_shape = (
                batch_size,
                steps,
            ) + state_shape
        else:
            output_shape = (batch_size,) + state_shape

        if self.return_state:
            batched_state_shape = (batch_size,) + state_shape
            return output_shape, batched_state_shape, batched_state_shape
        return output_shape

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.kernel_size [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py]
    def kernel_size(self):
        return self.cell.kernel_size

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::adaptive_max_pool [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py]
def adaptive_max_pool(
    inputs,
    output_size,
    data_format=None,
):
    """Adaptive max pooling operation.

    Applies an adaptive max pooling operation that automatically computes the
    kernel size and stride to pool the input to the specified `output_size`.
    This operation is useful when you want a fixed output size regardless of
    input size, commonly used in models like ResNet for global feature
    extraction.
    Args:
        inputs: Tensor of rank 4. Input tensor of shape:
            - If `data_format="channels_last"`:
                `(batch_size, height, width, channels)`.
            - If `data_format="channels_first"`:
                `(batch_size, channels, height, width)`.
        output_size: Integer or tuple/list of 2 integers, specifying the target
            output spatial dimensions `(output_height, output_width)`. If a
            single
            integer is provided, the same value is used for both dimensions.
        data_format: string, either `"channels_last"` or `"channels_first"`.
            Defaults to the value found in your Keras config file at
            `~/.keras/keras.json`. If never set, defaults to `"channels_last"`.

    Returns:
        A tensor of rank 4 representing the adaptive max pooled result.

    Example:

    >>> x = np.random.rand(2, 64, 64, 3)
    >>> y = keras.ops.adaptive_max_pool(x, output_size=(32, 32))
    >>> y.shape
    (2, 32, 32, 3)

    >>> # Works with any input size
    >>> x = np.random.rand(2, 100, 80, 3)
    >>> y = keras.ops.adaptive_max_pool(x, output_size=7)
    >>> y.shape
    (2, 7, 7, 3)
    """
    if data_format is None:
        data_format = config.image_data_format()

    if any_symbolic_tensors((inputs,)):
        return AdaptiveMaxPool(output_size, data_format).symbolic_call(inputs)

    return backend.nn.adaptive_max_pool(
        inputs, output_size=output_size, data_format=data_format
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.get_initial_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py]
    def get_initial_state(self, batch_size=None):
        initial_states = []
        for cell in self.cells:
            get_initial_state_fn = getattr(cell, "get_initial_state", None)
            if get_initial_state_fn:
                initial_states.append(
                    get_initial_state_fn(batch_size=batch_size)
                )
            else:
                if isinstance(cell.state_size, int):
                    initial_states.append(
                        ops.zeros(
                            (batch_size, cell.state_size),
                            dtype=self.compute_dtype,
                        )
                    )
                else:
                    initial_states.append(
                        [
                            ops.zeros((batch_size, d), dtype=self.compute_dtype)
                            for d in cell.state_size
                        ]
                    )
        return initial_states

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::size [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py]
def size(x):
    return np.size(x)
```

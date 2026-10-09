# keras-19 :: hybrid-cs

query: Update the RNN cell API to be explicit about output_size. (#11021)

## selected nodes

- rank=1 layer=FUNCTION tokens=561 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=2 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.kernel_size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=3 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling2d.py::AdaptiveMaxPooling2D.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling2d.py
- rank=4 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._ensure_vocab_size_unchanged file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=5 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling2d.py::AdaptiveAveragePooling2D.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling2d.py
- rank=6 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling3d.py::AdaptiveMaxPooling3D.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling3d.py
- rank=7 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling3d.py::AdaptiveAveragePooling3D.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling3d.py
- rank=8 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling1d.py::AdaptiveMaxPooling1D.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling1d.py
- rank=9 layer=FUNCTION tokens=238 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling1d.py::AdaptiveAveragePooling1D.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling1d.py
- rank=10 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=11 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/file_utils.py::DLProgbar.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/file_utils.py
- rank=12 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.output_size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=13 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._ensure_known_vocab_size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=14 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.get_initial_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=15 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=16 layer=FUNCTION tokens=194 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=17 layer=FUNCTION tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=18 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_output_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=19 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::AdaptiveMaxPool.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.kernel_size [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py]
    def kernel_size(self):
        return self.cell.kernel_size

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling2d.py::AdaptiveMaxPooling2D.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling2d.py]
    def __init__(self, output_size, data_format=None, **kwargs):
        if isinstance(output_size, int):
            output_size_tuple = (output_size, output_size)
        elif isinstance(output_size, (tuple, list)) and len(output_size) == 2:
            output_size_tuple = tuple(output_size)
        else:
            raise TypeError(
                f"`output_size` must be an integer or (height, width) tuple. "
                f"Received: {output_size} of type {type(output_size)}"
            )

        super().__init__(output_size_tuple, data_format, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._ensure_vocab_size_unchanged [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py]
    def _ensure_vocab_size_unchanged(self):
        if self.output_mode == "int" or self.pad_to_max_tokens:
            return

        with tf.init_scope():
            new_vocab_size = self.vocabulary_size()

        if (
            self._frozen_vocab_size is not None
            and new_vocab_size != self._frozen_vocab_size
        ):
            raise RuntimeError(
                f"When using `output_mode={self.output_mode}` "
                "and `pad_to_max_tokens=False`, "
                "the vocabulary size cannot be changed after the layer is "
                f"called. Old vocab size is {self._frozen_vocab_size}, "
                f"new vocab size is {new_vocab_size}"
            )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling2d.py::AdaptiveAveragePooling2D.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling2d.py]
    def __init__(self, output_size, data_format=None, **kwargs):
        if isinstance(output_size, int):
            output_size_tuple = (output_size, output_size)
        elif isinstance(output_size, (tuple, list)) and len(output_size) == 2:
            output_size_tuple = tuple(output_size)
        else:
            raise TypeError(
                f"`output_size` must be an integer or (height, width) tuple. "
                f"Received: {output_size} of type {type(output_size)}"
            )

        super().__init__(output_size_tuple, data_format, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling3d.py::AdaptiveMaxPooling3D.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling3d.py]
    def __init__(self, output_size, data_format=None, **kwargs):
        if isinstance(output_size, int):
            output_size_tuple = (output_size, output_size, output_size)
        elif isinstance(output_size, (tuple, list)) and len(output_size) == 3:
            output_size_tuple = tuple(output_size)
        else:
            raise TypeError(
                f"`output_size` must be an integer or "
                f"(depth, height, width) tuple. "
                f"Received: {output_size} of type {type(output_size)}"
            )

        super().__init__(output_size_tuple, data_format, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling3d.py::AdaptiveAveragePooling3D.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling3d.py]
    def __init__(self, output_size, data_format=None, **kwargs):
        if isinstance(output_size, int):
            output_size_tuple = (output_size, output_size, output_size)
        elif isinstance(output_size, (tuple, list)) and len(output_size) == 3:
            output_size_tuple = tuple(output_size)
        else:
            raise TypeError(
                f"`output_size` must be an integer or "
                f"(depth, height, width) tuple. "
                f"Received: {output_size} of type {type(output_size)}"
            )

        super().__init__(output_size_tuple, data_format, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling1d.py::AdaptiveMaxPooling1D.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_max_pooling1d.py]
    def __init__(self, output_size, data_format=None, **kwargs):
        if isinstance(output_size, int):
            output_size = (output_size,)
        elif isinstance(output_size, (tuple, list)):
            if len(output_size) != 1:
                raise ValueError(
                    f"For 1D input, `output_size` tuple must have length 1. "
                    f"Received: {output_size}"
                )
            output_size = tuple(output_size)
        else:
            raise TypeError(
                f"`output_size` must be an integer or tuple of 1 integer. "
                f"Received: {output_size} of type {type(output_size)}"
            )

        super().__init__(output_size, data_format, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling1d.py::AdaptiveAveragePooling1D.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/pooling/adaptive_average_pooling1d.py]
    def __init__(self, output_size, data_format=None, **kwargs):
        if isinstance(output_size, int):
            output_size = (output_size,)
        elif isinstance(output_size, (tuple, list)):
            if len(output_size) != 1:
                raise ValueError(
                    f"For 1D input, `output_size` tuple must have length 1. "
                    f"Received: {output_size}"
                )
            output_size = tuple(output_size)
        else:
            raise TypeError(
                f"`output_size` must be an integer or tuple of 1 integer. "
                f"Received: {output_size} of type {type(output_size)}"
            )

        super().__init__(output_size, data_format, **kwargs)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/file_utils.py::DLProgbar.__call__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/file_utils.py]
            def __call__(self, block_num, block_size, total_size):
                if total_size == -1:
                    total_size = None
                if not self.progbar:
                    self.progbar = Progbar(total_size)
                current = block_num * block_size

                if total_size is None:
                    self.progbar.update(current)
                else:
                    if current < total_size:
                        self.progbar.update(current)
                    elif not self.finished:
                        self.progbar.update(self.progbar.target)
                        self.finished = True

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.output_size [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py]
    def output_size(self):
        if getattr(self.cells[-1], "output_size", None) is not None:
            return self.cells[-1].output_size
        elif isinstance(self.cells[-1].state_size, (list, tuple)):
            return self.cells[-1].state_size[0]
        else:
            return self.cells[-1].state_size

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._ensure_known_vocab_size [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py]
    def _ensure_known_vocab_size(self):
        if self.output_mode == "int" or self.pad_to_max_tokens:
            return
        if self._frozen_vocab_size is None:
            raise RuntimeError(
                f"When using `output_mode={self.output_mode}` "
                "and `pad_to_max_tokens=False`, "
                "you must set the layer's vocabulary before calling it. Either "
                "pass a `vocabulary` argument to the layer, or call `adapt` "
                "with some sample data."
            )

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::size [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py]
def size(x):
    x = get_ov_output(x)
    shape_tensor = ov_opset.shape_of(x, output_type=Type.i64)
    final_size = ov_opset.reduce_prod(
        shape_tensor,
        ov_opset.constant([0], Type.i64),
        keep_dims=False,
    )
    return OpenVINOKerasTensor(final_size.output(0))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py]
    def __init__(self, cells, **kwargs):
        super().__init__(**kwargs)
        for cell in cells:
            if "call" not in dir(cell):
                raise ValueError(
                    "All cells must have a `call` method. "
                    f"Received cell without a `call` method: {cell}"
                )
            if "state_size" not in dir(cell):
                raise ValueError(
                    "All cells must have a `state_size` attribute. "
                    f"Received cell without a `state_size`: {cell}"
                )
        self.cells = cells

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::AdaptiveMaxPool.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py]
    def call(self, inputs):
        return backend.nn.adaptive_max_pool(
            inputs, output_size=self.output_size, data_format=self.data_format
        )
```

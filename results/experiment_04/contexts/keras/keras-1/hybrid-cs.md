# keras-1 :: hybrid-cs

query: Fix initializers and update ops.

## selected nodes

- rank=1 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py::Config.update file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py
- rank=2 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_core.py::hook file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_core.py
- rank=3 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py::CategoricalTruePositives.update_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py
- rank=4 layer=FUNCTION tokens=258 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::scatter_update file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py
- rank=5 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py
- rank=6 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adagrad.py::Adagrad.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adagrad.py
- rank=7 layer=FUNCTION tokens=424 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lamb.py::Lamb.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lamb.py
- rank=8 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py::compute_float8_amax_history file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py
- rank=9 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SavingTest.setUp file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=10 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTMCell.bias_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=11 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py::Function._setup_nnx_op_mapping file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py
- rank=12 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lion.py::Lion.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lion.py
- rank=13 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTMCell.bias_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=14 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py::KerasTensor.__mod__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py
- rank=15 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.reset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py
- rank=16 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py::TrainingLayer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py
- rank=17 layer=FUNCTION tokens=280 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adamax.py::Adamax.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adamax.py
- rank=18 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py::SliceUpdate.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py
- rank=19 layer=FUNCTION tokens=316 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/sgd.py::SGD.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/sgd.py
- rank=20 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/f_score_metrics.py::FBetaScore.reset_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/f_score_metrics.py
- rank=21 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/muon.py::Muon._adamw_update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/muon.py
- rank=22 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/regression_metrics.py::R2Score.reset_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/regression_metrics.py
- rank=23 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::_adjust_kernel file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py::Config.update [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py]
    def update(self, *args, **kwargs):
        self._raise_if_frozen()
        return self._config.update(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_core.py::hook [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_core.py]
        def hook(*args, **kwargs):
            inp = args[0] if args else kwargs["inputs"]
            num_features = awq_objects[name].rows
            input_2d = ops.reshape(inp, (-1, num_features))
            awq_objects[name].update_activation_magnitudes(input_2d)
            return original_call_func(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py::CategoricalTruePositives.update_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py]
    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = ops.reshape(ops.argmax(y_pred, axis=1), (-1, 1))
        values = ops.cast(y_true, "int32") == ops.cast(y_pred, "int32")
        values = ops.cast(values, "float32")
        if sample_weight is not None:
            sample_weight = ops.cast(sample_weight, "float32")
            values = ops.multiply(values, sample_weight)
        self.true_positives.assign_add(ops.sum(values))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::scatter_update [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py]
def scatter_update(inputs, indices, updates, reduction=None):
    inputs = get_ov_output(inputs)
    indices = get_ov_output(indices)
    updates = get_ov_output(updates)

    inputs, updates = align_operand_types(inputs, updates, "scatter_update")

    # Map Keras reduction to OpenVINO ScatterNDUpdate reduction.
    # OpenVINO Opset 15 supports: "none", "sum", "sub", "prod", "min", "max".
    if reduction is None:
        ov_reduction = "none"
    elif reduction == "add":
        ov_reduction = "sum"
    elif reduction == "mul":
        ov_reduction = "prod"
    elif reduction in ("max", "min"):
        ov_reduction = reduction
    else:
        raise ValueError(f"Unsupported reduction: {reduction}")

    result = ov_opset.scatter_nd_update(
        inputs, indices, updates, reduction=ov_reduction
    ).output(0)
    return OpenVINOKerasTensor(result)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py]
    def fix_index(index, size_node):
        if fill_mode in ("constant", "nearest"):
            zero = ov_opset.constant(0, dtype=Type.i32).output(0)
            size_m1 = ov_opset.subtract(
                size_node, ov_opset.constant(1, dtype=Type.i32)
            ).output(0)
            return ov_opset.minimum(
                ov_opset.maximum(index, zero), size_m1
            ).output(0)
        elif fill_mode == "wrap":
            return ov_opset.floor_mod(index, size_node).output(0)
        elif fill_mode == "mirror":
            return _mirror_index_fixer(index, size_node)
        else:  # reflect
            return _reflect_index_fixer(index, size_node)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adagrad.py::Adagrad.update_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adagrad.py]
    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""
        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)

        accumulator = self._accumulators[self._get_variable_index(variable)]

        self.assign_add(accumulator, ops.square(gradient))
        self.assign_sub(
            variable,
            ops.divide(
                ops.multiply(lr, gradient),
                ops.sqrt(ops.add(accumulator, self.epsilon)),
            ),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lamb.py::Lamb.update_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lamb.py]
    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""
        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)
        local_step = ops.cast(self.iterations + 1, variable.dtype)

        beta_1_power = ops.power(
            ops.cast(self.beta_1, variable.dtype), local_step
        )
        beta_2_power = ops.power(
            ops.cast(self.beta_2, variable.dtype), local_step
        )

        m = self._momentums[self._get_variable_index(variable)]
        v = self._velocities[self._get_variable_index(variable)]

        self.assign_add(
            m, ops.multiply(ops.subtract(gradient, m), 1 - self.beta_1)
        )

        self.assign_add(
            v,
            ops.multiply(
                ops.subtract(ops.square(gradient), v), 1 - self.beta_2
            ),
        )

        m_t_hat = ops.divide(m, (1.0 - beta_1_power))
        v_sqrt = ops.add(
            ops.sqrt(ops.divide(v, (1.0 - beta_2_power))), self.epsilon
        )

        update = ops.divide(m_t_hat, v_sqrt)
        w_norm = ops.sqrt(ops.sum(ops.power(variable, 2)))
        g_norm = ops.sqrt(ops.sum(ops.power(update, 2)))

        # ratio = w_norm / g_norm if w_norm > 0 and g_norm > 0 else 1
        ratio = ops.where(
            ops.greater(w_norm, 0),
            ops.where(ops.greater(g_norm, 0), (w_norm / g_norm), 1.0),
            1.0,
        )

        self.assign_sub(variable, ratio * lr * update)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py::compute_float8_amax_history [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py]
def compute_float8_amax_history(x, amax_history):
    amax_update = ops.cast(ops.max(ops.abs(x)), amax_history.dtype)
    new_amax_history = ops.scatter_update(
        ops.roll(amax_history, shift=-1),
        [[0]],
        ops.reshape(amax_update, [1]),
    )
    return new_amax_history

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SavingTest.setUp [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py]
    def setUp(self):
        super().setUp()
        # Set `_MEMORY_UPPER_BOUND` to zero for testing purpose.
        self.original_value = saving_lib._MEMORY_UPPER_BOUND
        saving_lib._MEMORY_UPPER_BOUND = 0

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTMCell.bias_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py]
                def bias_initializer(_, *args, **kwargs):
                    return ops.concatenate(
                        [
                            self.bias_initializer(
                                (self.filters,), *args, **kwargs
                            ),
                            initializers.get("ones")(
                                (self.filters,), *args, **kwargs
                            ),
                            self.bias_initializer(
                                (self.filters * 2,), *args, **kwargs
                            ),
                        ]
                    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py::Function._setup_nnx_op_mapping [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/function.py]
    def _setup_nnx_op_mapping(self):
        """Setup operation mapping for NNX"""
        # Create a mapping from operation id to operation instance
        self._nnx_op_mapping = {}

        # Assign the list of operations to a single attribute for NNX traversal
        self.nnx_operations = self._operations[:]
        for operation in self._operations:
            # Map the operation id to this operation instance
            self._nnx_op_mapping[id(operation)] = operation

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lion.py::Lion.update_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lion.py]
    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""
        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)
        beta_1 = ops.cast(self.beta_1, variable.dtype)
        beta_2 = ops.cast(self.beta_2, variable.dtype)
        m = self._momentums[self._get_variable_index(variable)]

        self.assign_sub(
            variable,
            ops.multiply(
                lr,
                ops.sign(
                    ops.add(
                        ops.multiply(m, beta_1),
                        ops.multiply(gradient, (1.0 - beta_1)),
                    )
                ),
            ),
        )
        self.assign(
            m,
            ops.add(
                ops.multiply(m, beta_2), ops.multiply(gradient, (1.0 - beta_2))
            ),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTMCell.bias_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py]
                def bias_initializer(_, *args, **kwargs):
                    return ops.concatenate(
                        [
                            self.bias_initializer(
                                (self.units,), *args, **kwargs
                            ),
                            initializers.get("ones")(
                                (self.units,), *args, **kwargs
                            ),
                            self.bias_initializer(
                                (self.units * 2,), *args, **kwargs
                            ),
                        ]
                    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py::KerasTensor.__mod__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py]
    def __mod__(self, other):
        from keras.src import ops

        return ops.Mod().symbolic_call(self, other)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py::EpochIterator.reset [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/epoch_iterator.py]
    def reset(self):
        self._current_iterator = None
        self._num_batches = self.data_adapter.num_batches
        self._steps_seen = 0
        self._epoch_iterator = None
        self.data_adapter.on_epoch_end()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py::TrainingLayer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer_test.py]
            def __init__(self):
                super().__init__()
                self.post_build_modify_layer = PostBuildModifyLayer()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adamax.py::Adamax.update_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adamax.py]
    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""
        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)
        local_step = ops.cast(self.iterations + 1, variable.dtype)
        beta_1_power = ops.power(
            ops.cast(self.beta_1, variable.dtype), local_step
        )

        m = self._m[self._get_variable_index(variable)]
        u = self._u[self._get_variable_index(variable)]

        self.assign_add(
            m, ops.multiply(ops.subtract(gradient, m), (1 - self.beta_1))
        )
        self.assign(
            u, ops.maximum(ops.multiply(self.beta_2, u), ops.abs(gradient))
        )
        self.assign_sub(
            variable,
            ops.divide(
                ops.multiply(lr, m),
                ops.multiply((1 - beta_1_power), ops.add(u, self.epsilon)),
            ),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py::SliceUpdate.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py]
    def call(self, inputs, start_indices, updates):
        return backend.core.slice_update(inputs, start_indices, updates)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/sgd.py::SGD.update_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/sgd.py]
    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""
        learning_rate = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)
        m = None
        if self.momentum != 0:
            m = self.momentums[self._get_variable_index(variable)]

        if m is not None:
            momentum = ops.cast(self.momentum, variable.dtype)
            self.assign(
                m,
                ops.subtract(
                    ops.multiply(m, momentum),
                    ops.multiply(gradient, learning_rate),
                ),
            )
            if self.nesterov:
                self.assign_add(
                    variable,
                    ops.subtract(
                        ops.multiply(m, momentum),
                        ops.multiply(gradient, learning_rate),
                    ),
                )
            else:
                self.assign_add(variable, m)
        else:
            self.assign_sub(variable, ops.multiply(gradient, learning_rate))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/f_score_metrics.py::FBetaScore.reset_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/f_score_metrics.py]
    def reset_state(self):
        for v in self.variables:
            v.assign(ops.zeros(v.shape, dtype=v.dtype))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/muon.py::Muon._adamw_update_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/muon.py]
    def _adamw_update_step(self, gradient, variable, learning_rate, m, v):
        """Update step given gradient and the associated model variable."""
        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)
        local_step = ops.cast(self.iterations + 1, variable.dtype)
        adam_beta_1_power = ops.power(
            ops.cast(self.adam_beta_1, variable.dtype), local_step
        )
        adam_beta_2_power = ops.power(
            ops.cast(self.adam_beta_2, variable.dtype), local_step
        )

        alpha = lr * ops.sqrt(1 - adam_beta_2_power) / (1 - adam_beta_1_power)

        self.assign_add(
            m, ops.multiply(ops.subtract(gradient, m), 1 - self.adam_beta_1)
        )
        self.assign_add(
            v,
            ops.multiply(
                ops.subtract(ops.square(gradient), v), 1 - self.adam_beta_2
            ),
        )
        self.assign_sub(
            variable,
            ops.divide(
                ops.multiply(m, alpha), ops.add(ops.sqrt(v), self.epsilon)
            ),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/regression_metrics.py::R2Score.reset_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/regression_metrics.py]
    def reset_state(self):
        for v in self.variables:
            v.assign(ops.zeros(v.shape, dtype=v.dtype))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::_adjust_kernel [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py]
def _adjust_kernel(kernel, num_spatial_dims):
    if num_spatial_dims == 1:
        permutation = [2, 1, 0]
    elif num_spatial_dims == 2:
        permutation = [3, 2, 0, 1]
    else:
        permutation = [4, 3, 0, 1, 2]
    permutation = ov_opset.constant(permutation, Type.i32)
    return ov_opset.transpose(kernel, permutation).output(0)
```

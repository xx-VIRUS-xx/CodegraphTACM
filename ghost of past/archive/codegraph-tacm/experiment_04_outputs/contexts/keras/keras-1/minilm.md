# keras-1 :: minilm

query: Fix initializers and update ops.

## selected nodes

- rank=1 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::JaxVariable._initialize_with_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py
- rank=2 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py::Variable._initialize_with_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py
- rank=3 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable._initialize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py
- rank=4 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention.py::GroupedQueryAttention._get_common_kwargs_for_sublayer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention.py
- rank=5 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py::Variable._deferred_initialize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py
- rank=6 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/multi_head_attention.py::MultiHeadAttention._get_common_kwargs_for_sublayer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/multi_head_attention.py
- rank=7 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.kernel_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=8 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRU.kernel_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py
- rank=9 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py::SimpleRNN.kernel_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py
- rank=10 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTM.kernel_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=11 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::EpochAgnosticMeanSquaredError.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=12 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::NullInitializer.initialize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=13 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py::Variable._initialize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py
- rank=14 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTMCell.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=15 layer=FUNCTION tokens=261 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable._deferred_initialize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py
- rank=16 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/callback_test.py::TestModel.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/callback_test.py
- rank=17 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py::MyDense.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py
- rank=18 layer=FUNCTION tokens=404 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRUCell.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py
- rank=19 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/activations/prelu.py::PReLU.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/activations/prelu.py
- rank=20 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::JaxVariable._initialize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py
- rank=21 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTMCell.bias_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=22 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._uninitialized_lookup_table file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=23 layer=FUNCTION tokens=217 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py::_clone_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py
- rank=24 layer=FUNCTION tokens=159 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py::Variable._initialize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py
- rank=25 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py::SimpleRNN.recurrent_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py
- rank=26 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::Relu6.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::JaxVariable._initialize_with_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py]
    def _initialize_with_initializer(self, initializer):
        self._initialize_layout()
        layout = self._layout
        shape = self._shape
        if should_shard_at_init(layout, shape):
            jitted_initializer = jax.jit(
                initializer.__call__,
                out_shardings=layout,
                static_argnames=["shape", "dtype"],
            )
            value = jitted_initializer(shape=self._shape, dtype=self._dtype)
            self._value = value
        else:
            super()._initialize_with_initializer(initializer)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py::Variable._initialize_with_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py]
    def _initialize_with_initializer(self, initializer):
        self._initialize(lambda: initializer(self._shape, dtype=self._dtype))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable._initialize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py]
    def _initialize(self, value):
        raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention.py::GroupedQueryAttention._get_common_kwargs_for_sublayer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/grouped_query_attention.py]
    def _get_common_kwargs_for_sublayer(self):
        common_kwargs = dict(
            kernel_regularizer=self.kernel_regularizer,
            bias_regularizer=self.bias_regularizer,
            activity_regularizer=self.activity_regularizer,
            kernel_constraint=self.kernel_constraint,
            bias_constraint=self.bias_constraint,
            dtype=self.dtype_policy,
        )
        # Create new clone of kernel/bias initializer, so that we don't reuse
        # the initializer instance, which could lead to same init value since
        # initializer is stateless.
        kernel_initializer = self.kernel_initializer.__class__.from_config(
            self.kernel_initializer.get_config()
        )
        bias_initializer = self.bias_initializer.__class__.from_config(
            self.bias_initializer.get_config()
        )
        common_kwargs["kernel_initializer"] = kernel_initializer
        common_kwargs["bias_initializer"] = bias_initializer
        return common_kwargs

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py::Variable._deferred_initialize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py]
    def _deferred_initialize(self):
        if self._value is not None:
            raise ValueError(f"Variable {self.path} is already initialized.")

        if in_stateless_scope():
            raise ValueError(
                "You are attempting to initialize a variable "
                "while in a stateless scope. This is disallowed. "
                "Make sure that all variables are initialized "
                "before you start using your layer/model objects."
            )
        with tf.init_scope():
            self._initialize_with_initializer(self._initializer)
            self._initializer = None

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/multi_head_attention.py::MultiHeadAttention._get_common_kwargs_for_sublayer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/attention/multi_head_attention.py]
    def _get_common_kwargs_for_sublayer(self):
        common_kwargs = dict(
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            activity_regularizer=self._activity_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            dtype=self.dtype_policy,
        )
        # Create new clone of kernel/bias initializer, so that we don't reuse
        # the initializer instance, which could lead to same init value since
        # initializer is stateless.
        kernel_initializer = self._kernel_initializer.__class__.from_config(
            self._kernel_initializer.get_config()
        )
        bias_initializer = self._bias_initializer.__class__.from_config(
            self._bias_initializer.get_config()
        )
        common_kwargs["kernel_initializer"] = kernel_initializer
        common_kwargs["bias_initializer"] = bias_initializer
        return common_kwargs

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTM.kernel_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py]
    def kernel_initializer(self):
        return self.cell.kernel_initializer

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRU.kernel_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py]
    def kernel_initializer(self):
        return self.cell.kernel_initializer

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py::SimpleRNN.kernel_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py]
    def kernel_initializer(self):
        return self.cell.kernel_initializer

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTM.kernel_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py]
    def kernel_initializer(self):
        return self.cell.kernel_initializer

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::EpochAgnosticMeanSquaredError.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
    def __init__(self):
        super().__init__(name="mse")
        super().reset_state()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::NullInitializer.initialize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py]
        def initialize(self, table):
            """Returns the table initialization op."""
            pass

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py::Variable._initialize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py]
    def _initialize(self, value):
        self._value = value

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTMCell.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py]
    def get_config(self):
        config = {
            "units": self.units,
            "activation": activations.serialize(self.activation),
            "recurrent_activation": activations.serialize(
                self.recurrent_activation
            ),
            "use_bias": self.use_bias,
            "unit_forget_bias": self.unit_forget_bias,
            "kernel_initializer": initializers.serialize(
                self.kernel_initializer
            ),
            "recurrent_initializer": initializers.serialize(
                self.recurrent_initializer
            ),
            "bias_initializer": initializers.serialize(self.bias_initializer),
            "kernel_regularizer": regularizers.serialize(
                self.kernel_regularizer
            ),
            "recurrent_regularizer": regularizers.serialize(
                self.recurrent_regularizer
            ),
            "bias_regularizer": regularizers.serialize(self.bias_regularizer),
            "kernel_constraint": constraints.serialize(self.kernel_constraint),
            "recurrent_constraint": constraints.serialize(
                self.recurrent_constraint
            ),
            "bias_constraint": constraints.serialize(self.bias_constraint),
            "dropout": self.dropout,
            "recurrent_dropout": self.recurrent_dropout,
            "seed": self.seed,
        }
        base_config = super().get_config()
        return {**base_config, **config}

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable._deferred_initialize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py]
    def _deferred_initialize(self):
        if self._value is not None:
            # If NNX is enabled, it's possible the variable was already
            # initialized by a concrete call. In this case, _deferred_initialize
            # returns early and does not raise an error.
            if config.is_nnx_enabled():
                return
            raise ValueError(f"Variable {self.path} is already initialized.")

        if in_stateless_scope():
            raise ValueError(
                "You are attempting to initialize a variable "
                "while in a stateless scope. This is disallowed. "
                "Make sure that all variables are initialized "
                "before you start using your layer/model objects."
            )
        self._initialize_with_initializer(self._initializer)
        self._initializer = None

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/callback_test.py::TestModel.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/callback_test.py]
            def __init__(self):
                super().__init__()
                self.iterations = self.add_variable(
                    shape=(), initializer="zeros", trainable=False
                )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py::MyDense.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py]
    def __init__(
        self,
        units,
        *,
        kernel_regularizer=None,
        kernel_initializer=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._units = units
        self._kernel_regularizer = kernel_regularizer
        self._kernel_initializer = kernel_initializer

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRUCell.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py]
    def get_config(self):
        config = {
            "units": self.units,
            "activation": activations.serialize(self.activation),
            "recurrent_activation": activations.serialize(
                self.recurrent_activation
            ),
            "use_bias": self.use_bias,
            "kernel_initializer": initializers.serialize(
                self.kernel_initializer
            ),
            "recurrent_initializer": initializers.serialize(
                self.recurrent_initializer
            ),
            "bias_initializer": initializers.serialize(self.bias_initializer),
            "kernel_regularizer": regularizers.serialize(
                self.kernel_regularizer
            ),
            "recurrent_regularizer": regularizers.serialize(
                self.recurrent_regularizer
            ),
            "bias_regularizer": regularizers.serialize(self.bias_regularizer),
            "kernel_constraint": constraints.serialize(self.kernel_constraint),
            "recurrent_constraint": constraints.serialize(
                self.recurrent_constraint
            ),
            "bias_constraint": constraints.serialize(self.bias_constraint),
            "dropout": self.dropout,
            "recurrent_dropout": self.recurrent_dropout,
            "reset_after": self.reset_after,
            "seed": self.seed,
        }
        base_config = super().get_config()
        return {**base_config, **config}

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/activations/prelu.py::PReLU.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/activations/prelu.py]
    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "alpha_initializer": initializers.serialize(
                    self.alpha_initializer
                ),
                "alpha_regularizer": regularizers.serialize(
                    self.alpha_regularizer
                ),
                "alpha_constraint": constraints.serialize(
                    self.alpha_constraint
                ),
                "shared_axes": self.shared_axes,
            }
        )
        return config

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::JaxVariable._initialize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py]
    def _initialize(self, value):
        # Note that variable.shape is needed by distribution_lib
        self._shape = self._validate_shape(value.shape)
        self._initialize_layout()
        self._direct_assign(value)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._uninitialized_lookup_table [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py]
    def _uninitialized_lookup_table(self):
        with tf.init_scope():
            initializer = get_null_initializer(
                self._key_dtype, self._value_dtype
            )
            return tf.lookup.StaticHashTable(initializer, self._default_value)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py::_clone_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py]
def _clone_initializer(initializer):
    """Clones an initializer to ensure a new seed.

    Args:
        initializer: The initializer to clone.

    Returns:
        A cloned initializer if it is clonable, otherwise the original one.

    As of tensorflow 2.10, we need to clone user passed initializers when
    invoking them twice to avoid creating the same randomized initialization.
    """
    if isinstance(initializer, initializers.Initializer):
        config = initializer.get_config()
        return initializer.__class__.from_config(config)
    # If we get a string or dict, just return as we cannot and should not clone.
    return initializer

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py::Variable._initialize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/core.py]
    def _initialize(self, value):
        if isinstance(value, tf.Variable):
            self._value = value
        else:
            self._value = tf.Variable(
                value,
                dtype=self._dtype,
                trainable=self.trainable,
                name=self.name,
                aggregation=self._map_aggregation(self.aggregation),
                synchronization=self._map_synchronization(self.synchronization),
            )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py::SimpleRNN.recurrent_initializer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py]
    def recurrent_initializer(self):
        return self.cell.recurrent_initializer

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::Relu6.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py]
    def call(self, x):
        return backend.nn.relu6(x)
```

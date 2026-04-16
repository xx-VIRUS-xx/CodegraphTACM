# keras-1 :: hybrid

query: Fix initializers and update ops.

## selected nodes

- rank=1 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/activations/prelu.py::PReLU.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/activations/prelu.py
- rank=2 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTMCell.bias_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=3 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTMCell.bias_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=4 layer=FUNCTION tokens=394 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_conv_transpose.py::BaseConvTranspose.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_conv_transpose.py
- rank=5 layer=FUNCTION tokens=217 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py::_clone_initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py
- rank=6 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTMCell.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=7 layer=FUNCTION tokens=404 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRUCell.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py
- rank=8 layer=FUNCTION tokens=428 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_conv.py::BaseConv.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_conv.py
- rank=9 layer=FUNCTION tokens=511 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_separable_conv.py::BaseSeparableConv.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_separable_conv.py
- rank=10 layer=FUNCTION tokens=363 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py::BatchNormalization.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py
- rank=11 layer=FUNCTION tokens=403 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_depthwise_conv.py::BaseDepthwiseConv.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_depthwise_conv.py
- rank=12 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/group_normalization.py::GroupNormalization.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/group_normalization.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_conv_transpose.py::BaseConvTranspose.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_conv_transpose.py]
    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "filters": self.filters,
                "kernel_size": self.kernel_size,
                "strides": self.strides,
                "padding": self.padding,
                "data_format": self.data_format,
                "dilation_rate": self.dilation_rate,
                "activation": activations.serialize(self.activation),
                "use_bias": self.use_bias,
                "kernel_initializer": initializers.serialize(
                    self.kernel_initializer
                ),
                "bias_initializer": initializers.serialize(
                    self.bias_initializer
                ),
                "kernel_regularizer": regularizers.serialize(
                    self.kernel_regularizer
                ),
                "bias_regularizer": regularizers.serialize(
                    self.bias_regularizer
                ),
                "activity_regularizer": regularizers.serialize(
                    self.activity_regularizer
                ),
                "kernel_constraint": constraints.serialize(
                    self.kernel_constraint
                ),
                "bias_constraint": constraints.serialize(self.bias_constraint),
            }
        )
        return config

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_conv.py::BaseConv.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_conv.py]
    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "filters": self.filters,
                "kernel_size": self.kernel_size,
                "strides": self.strides,
                "padding": self.padding,
                "data_format": self.data_format,
                "dilation_rate": self.dilation_rate,
                "groups": self.groups,
                "activation": activations.serialize(self.activation),
                "use_bias": self.use_bias,
                "kernel_initializer": initializers.serialize(
                    self.kernel_initializer
                ),
                "bias_initializer": initializers.serialize(
                    self.bias_initializer
                ),
                "kernel_regularizer": regularizers.serialize(
                    self.kernel_regularizer
                ),
                "bias_regularizer": regularizers.serialize(
                    self.bias_regularizer
                ),
                "activity_regularizer": regularizers.serialize(
                    self.activity_regularizer
                ),
                "kernel_constraint": constraints.serialize(
                    self.kernel_constraint
                ),
                "bias_constraint": constraints.serialize(self.bias_constraint),
            }
        )
        if self.lora_rank:
            config["lora_rank"] = self.lora_rank
            config["lora_alpha"] = self.lora_alpha
        return config

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_separable_conv.py::BaseSeparableConv.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_separable_conv.py]
    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "depth_multiplier": self.depth_multiplier,
                "filters": self.filters,
                "kernel_size": self.kernel_size,
                "strides": self.strides,
                "padding": self.padding,
                "data_format": self.data_format,
                "dilation_rate": self.dilation_rate,
                "activation": activations.serialize(self.activation),
                "use_bias": self.use_bias,
                "depthwise_initializer": initializers.serialize(
                    self.depthwise_initializer
                ),
                "pointwise_initializer": initializers.serialize(
                    self.pointwise_initializer
                ),
                "bias_initializer": initializers.serialize(
                    self.bias_initializer
                ),
                "depthwise_regularizer": regularizers.serialize(
                    self.depthwise_regularizer
                ),
                "pointwise_regularizer": regularizers.serialize(
                    self.pointwise_regularizer
                ),
                "bias_regularizer": regularizers.serialize(
                    self.bias_regularizer
                ),
                "activity_regularizer": regularizers.serialize(
                    self.activity_regularizer
                ),
                "depthwise_constraint": constraints.serialize(
                    self.depthwise_constraint
                ),
                "pointwise_constraint": constraints.serialize(
                    self.pointwise_constraint
                ),
                "bias_constraint": constraints.serialize(self.bias_constraint),
            }
        )
        return config

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py::BatchNormalization.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py]
    def get_config(self):
        base_config = super().get_config()
        config = {
            "axis": self.axis,
            "momentum": self.momentum,
            "epsilon": self.epsilon,
            "center": self.center,
            "scale": self.scale,
            "beta_initializer": initializers.serialize(self.beta_initializer),
            "gamma_initializer": initializers.serialize(self.gamma_initializer),
            "moving_mean_initializer": initializers.serialize(
                self.moving_mean_initializer
            ),
            "moving_variance_initializer": initializers.serialize(
                self.moving_variance_initializer
            ),
            "beta_regularizer": regularizers.serialize(self.beta_regularizer),
            "gamma_regularizer": regularizers.serialize(self.gamma_regularizer),
            "beta_constraint": constraints.serialize(self.beta_constraint),
            "gamma_constraint": constraints.serialize(self.gamma_constraint),
            "synchronized": self.synchronized,
            "renorm": self.renorm,
            "renorm_clipping": self.renorm_clipping,
            "renorm_momentum": self.renorm_momentum,
        }
        return {**base_config, **config}

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_depthwise_conv.py::BaseDepthwiseConv.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/convolutional/base_depthwise_conv.py]
    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "depth_multiplier": self.depth_multiplier,
                "kernel_size": self.kernel_size,
                "strides": self.strides,
                "padding": self.padding,
                "data_format": self.data_format,
                "dilation_rate": self.dilation_rate,
                "activation": activations.serialize(self.activation),
                "use_bias": self.use_bias,
                "depthwise_initializer": initializers.serialize(
                    self.depthwise_initializer
                ),
                "bias_initializer": initializers.serialize(
                    self.bias_initializer
                ),
                "depthwise_regularizer": regularizers.serialize(
                    self.depthwise_regularizer
                ),
                "bias_regularizer": regularizers.serialize(
                    self.bias_regularizer
                ),
                "activity_regularizer": regularizers.serialize(
                    self.activity_regularizer
                ),
                "depthwise_constraint": constraints.serialize(
                    self.depthwise_constraint
                ),
                "bias_constraint": constraints.serialize(self.bias_constraint),
            }
        )
        return config

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/group_normalization.py::GroupNormalization.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/group_normalization.py]
    def get_config(self):
        config = {
            "groups": self.groups,
            "axis": self.axis,
            "epsilon": self.epsilon,
            "center": self.center,
            "scale": self.scale,
            "beta_initializer": initializers.serialize(self.beta_initializer),
            "gamma_initializer": initializers.serialize(self.gamma_initializer),
            "beta_regularizer": regularizers.serialize(self.beta_regularizer),
            "gamma_regularizer": regularizers.serialize(self.gamma_regularizer),
            "beta_constraint": constraints.serialize(self.beta_constraint),
            "gamma_constraint": constraints.serialize(self.gamma_constraint),
        }
        base_config = super().get_config()
        return {**base_config, **config}
```

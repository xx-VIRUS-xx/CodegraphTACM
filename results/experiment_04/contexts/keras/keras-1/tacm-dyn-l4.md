# keras-1 :: tacm-dyn-l4

query: Fix initializers and update ops.

## selected nodes

- rank=1 layer=FILE tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py
- rank=2 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py::Zeros file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py
- rank=3 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py::Ones file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py
- rank=4 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py::Identity file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py
- rank=5 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adafactor.py::Adafactor.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adafactor.py
- rank=6 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lamb.py::Lamb.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lamb.py
- rank=7 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adagrad.py::Adagrad.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adagrad.py
- rank=8 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/schedule_free_adamw.py::ScheduleFreeAdamW.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/schedule_free_adamw.py
- rank=9 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py::STFT file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py
- rank=10 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/random_initializers.py::GlorotUniform file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/random_initializers.py
- rank=11 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/random_initializers.py::GlorotNormal file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/random_initializers.py
- rank=12 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_rewrite_constant_fold file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=13 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py::compute_float8_amax_history file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py
- rank=14 layer=FUNCTION tokens=227 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lion.py::Lion.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lion.py
- rank=15 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/gptq.py::GPTQ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/gptq.py
- rank=16 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/__init__.py::get file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/__init__.py
- rank=17 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adamax.py::Adamax.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adamax.py
- rank=18 layer=FUNCTION tokens=277 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/sgd.py::SGD.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/sgd.py
- rank=19 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adadelta.py::Adadelta.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adadelta.py
- rank=20 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/rmsprop.py::RMSprop.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/rmsprop.py
- rank=21 layer=FUNCTION tokens=271 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/muon.py::Muon._adamw_update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/muon.py
- rank=22 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/random_initializers.py::LecunNormal file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/random_initializers.py
- rank=23 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/ftrl.py::Ftrl.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/ftrl.py
- rank=24 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py::Constant file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/constant_initializers.py
- rank=25 layer=CLASS tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py::BatchNormalization file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py
- rank=26 layer=FUNCTION tokens=356 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py::BatchNormalization._update_renorm_statistics file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py
- rank=27 layer=FUNCTION tokens=357 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py::BatchNormalization._renorm_correction_and_moments file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/normalization/batch_normalization.py
- rank=28 layer=FUNCTION tokens=335 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adam.py::Adam.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adam.py
- rank=29 layer=FILE tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/initializers/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/initializers/__init__.py
- rank=30 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/initializers/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/initializers/__init__.py
- rank=31 layer=FILE tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/initializer.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/initializer.py
- rank=32 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/initializer.py::Initializer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/initializers/initializer.py
- rank=33 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/reduction_metrics.py::Sum.update_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/reduction_metrics.py

## context

```text
file initializers/constant_initializers.py
imports: keras
defines: Constant, Zeros, Ones, Identity, STFT

class Zeros(Initializer):  [initializers/constant_initializers.py:50]
methods: __call__

class Ones(Initializer):  [initializers/constant_initializers.py:79]
methods: __call__

class Identity(Initializer):  [initializers/constant_initializers.py:116]
methods: __call__, __init__

    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""

        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)
        epsilon_2 = ops.cast(self.epsilon_2, variable.dtype)
        one = ops.cast(1.0, variable.dtype)
        local_step = ops.cast(self.iterations + 1, variable.dtype)
        if not callable(self._learning_rate) and self.relative_step:
            lr = ops.minimum(lr, 1 / ops.sqrt(local_step))

        r = self._r[self._get_variable_index(variable)]
    # ... truncated

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
    # ... truncated

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

    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""
        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)
        local_step = ops.cast(self.iterations + 1, variable.dtype)

        beta_1 = ops.cast(self.beta_1, variable.dtype)
        beta_2 = ops.cast(self.beta_2, variable.dtype)
        epsilon = ops.cast(self.epsilon, variable.dtype)

        # Apply warmup
        if self.warmup_steps > 0:
    # ... truncated

class STFT(Initializer):  [initializers/constant_initializers.py:164]
methods: get_config, __call__, __init__

class GlorotUniform(VarianceScaling):  [initializers/random_initializers.py:326]
methods: get_config, __init__

class GlorotNormal(VarianceScaling):  [initializers/random_initializers.py:375]
methods: get_config, __init__

    def patched_rewrite_constant_fold(g, ops):
        """
        We call tensorflow transform with constant folding but in some cases
        tensorflow does fold all constants. Since there are a bunch of ops in
        onnx that use attributes where tensorflow has dynamic inputs, we badly
        want constant folding to work. For cases where tensorflow missed
        something, make another pass over the graph and fix want we care about.
        """
    # ... truncated

def compute_float8_amax_history(x, amax_history):
    amax_update = ops.cast(ops.max(ops.abs(x)), amax_history.dtype)
    new_amax_history = ops.scatter_update(
        ops.roll(amax_history, shift=-1),
        [[0]],
        ops.reshape(amax_update, [1]),
    )
    return new_amax_history

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

class GPTQ:  [quantizers/gptq.py:272]
methods: free, quantize_and_correct_layer
         update_hessian_with_batch, __init__

def get(identifier):
    """Retrieves a Keras initializer object via an identifier.

    The `identifier` may be the string name of a initializers function or class
    (case-sensitively).

    >>> identifier = 'Ones'
    >>> keras.initializers.get(identifier)
    <...keras.initializers.initializers.Ones...>

    You can also specify `config` of the initializer to this function by passing
    dict containing `class_name` and `config` as an identifier. Also note that
    # ... truncated

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

    def update_step(self, grad, variable, learning_rate):
        """Update step given gradient and the associated model variable."""
        lr = ops.cast(learning_rate, variable.dtype)
        grad = ops.cast(grad, variable.dtype)

        rho = self.rho
        accumulated_grad = self._accumulated_grads[
            self._get_variable_index(variable)
        ]
        accumulated_delta_var = self._accumulated_delta_vars[
            self._get_variable_index(variable)
        ]

        def rms(x):
            return ops.sqrt(ops.add(x, self.epsilon))

        self.assign(
            accumulated_grad,
            ops.add(
                rho * accumulated_grad, ops.multiply(1 - rho, ops.square(grad))
            ),
        )
        delta_var = ops.negative(
            ops.divide(
                ops.multiply(rms(accumulated_delta_var), grad),
                rms(accumulated_grad),
            )
        )
        self.assign(
            accumulated_delta_var,
            ops.add(
                ops.multiply(rho, accumulated_delta_var),
                ops.multiply(1 - rho, ops.square(delta_var)),
            ),
        )
        self.assign_add(variable, ops.multiply(lr, delta_var))

    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""
        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)

        velocity = self._velocities[self._get_variable_index(variable)]
        momentum = None
        if self.momentum > 0:
            momentum = self._momentums[self._get_variable_index(variable)]
        average_grad = None
        if self.centered:
            average_grad = self._average_gradients[
    # ... truncated

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

class LecunNormal(VarianceScaling):  [initializers/random_initializers.py:428]
methods: get_config, __init__

    def update_step(self, gradient, variable, learning_rate):
        """Update step given gradient and the associated model variable."""

        lr = ops.cast(learning_rate, variable.dtype)
        gradient = ops.cast(gradient, variable.dtype)

        accum = self._accumulators[self._get_variable_index(variable)]
        linear = self._linears[self._get_variable_index(variable)]

        lr_power = self.learning_rate_power
        l2_reg = self.l2_regularization_strength
        l2_reg = l2_reg + self.beta / (2.0 * lr)
    # ... truncated

class Constant(Initializer):  [initializers/constant_initializers.py:10]
methods: from_config, get_config, __call__, __init__

class BatchNormalization(Layer):  [layers/normalization/batch_normalization.py:32]
methods: _compose_transforms, _moments
         _renorm_correction_and_moments
         _update_renorm_statistics, build, call
         compute_output_shape, get_config
         moving_stddev_initializer, __init__

    def _update_renorm_statistics(self, mean, variance):
        """Updates the renorm and moving statistics.
        Args:
            mean: The mean of the current batch.
            variance: The variance of the current batch.
        """
        stddev = ops.sqrt(variance + self.epsilon)

        # Update renorm moving mean and stddev.
        renorm_mean = ops.cast(self.renorm_mean, mean.dtype)
        renorm_stddev = ops.cast(self.renorm_stddev, mean.dtype)

        self.renorm_mean.assign(
            renorm_mean * self.renorm_momentum
            + mean * (1.0 - self.renorm_momentum)
        )
        self.renorm_stddev.assign(
            renorm_stddev * self.renorm_momentum
            + stddev * (1.0 - self.renorm_momentum)
        )

        moving_mean = ops.cast(self.moving_mean, mean.dtype)
        moving_stddev = ops.cast(self.moving_stddev, mean.dtype)

        self.moving_mean.assign(
            moving_mean * self.momentum + mean * (1.0 - self.momentum)
        )

        new_moving_stddev = moving_stddev * self.momentum + stddev * (
            1.0 - self.momentum
        )
        self.moving_stddev.assign(new_moving_stddev)

        # Derive `moving_variance` from `moving_stddev`, applying ReLU in case
        # floating point rounding causes it to go negative.
        self.moving_variance.assign(
            ops.relu(new_moving_stddev * new_moving_stddev - self.epsilon)
        )

    def _renorm_correction_and_moments(self, mean, variance):
        """Computes the correction for batch renormalization.

        This method computes the r and d correction factors.

        Args:
            mean: The mean of the current batch.
            variance: The variance of the current batch.

        Returns:
            A tuple (r, s, mean, variance) where r and d are the correction
            factors, and mean/variance are passed through unchanged.
        """
        stddev = ops.sqrt(variance + self.epsilon)

        # Get the renorm moving statistics.
        renorm_mean = ops.cast(self.renorm_mean, mean.dtype)
        # Avoid divide by zero early on in training.
        renorm_stddev = ops.maximum(
            ops.cast(self.renorm_stddev, mean.dtype),
            ops.sqrt(ops.cast(self.epsilon, mean.dtype)),
        )

        # Compute the corrections for batch renorm.
        r = ops.divide(stddev, renorm_stddev)
        d = ops.divide(ops.subtract(mean, renorm_mean), renorm_stddev)

        # Apply clipping.
        rmin = self.renorm_clipping.get("rmin")
        rmax = self.renorm_clipping.get("rmax")
        dmax = self.renorm_clipping.get("dmax")

        if rmin is not None:
            r = ops.maximum(r, rmin)
        if rmax is not None:
            r = ops.minimum(r, rmax)
        if dmax is not None:
            d = ops.clip(d, -dmax, dmax)

        return r, d, mean, variance

file keras/initializers/__init__.py
imports: keras
defines: —

file api/initializers/__init__.py
imports: keras
defines: —

file initializers/initializer.py
imports: keras
defines: Initializer

    def output(self):
        return self._outputs_struct

def copy(x):
    return x

# --- Layer 04: Variable context ---
# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: quantized_dequantize_inputs [dense.py]
  called by: grad [dense.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: on_batch_end [training_with_built_in_methods.py]
  called by: on_epoch_end [writing_your_own_callbacks.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: update_step [muon.py]

# call-chain context
  called by: apply_grad_to_update_var [optimizer.py]

# call-chain context
  called by: call [batch_normalization.py]

# call-chain context
  called by: call [batch_normalization.py]

# call-chain context
  called by: align_operand_types [core.py]
  called by: get_ov_output [core.py]

# call-chain context
  called by: _flatten_nnx_variable [core.py]
  called by: _backend_add_endpoint [export.py]

```

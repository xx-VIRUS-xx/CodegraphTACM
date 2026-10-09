# keras-1 :: tacm-full

query: Fix initializers and update ops.

## selected nodes

- rank=1 layer=FUNCTION tokens=743 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adafactor.py::Adafactor.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adafactor.py
- rank=2 layer=FUNCTION tokens=424 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lamb.py::Lamb.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lamb.py
- rank=3 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adagrad.py::Adagrad.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adagrad.py
- rank=4 layer=FUNCTION tokens=1297 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_rewrite_constant_fold file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=5 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py::compute_float8_amax_history file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py
- rank=6 layer=FUNCTION tokens=683 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/schedule_free_adamw.py::ScheduleFreeAdamW.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/schedule_free_adamw.py
- rank=7 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lion.py::Lion.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/lion.py
- rank=8 layer=FUNCTION tokens=280 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adamax.py::Adamax.update_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adamax.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adafactor.py::Adafactor.update_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/adafactor.py]
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
        c = self._c[self._get_variable_index(variable)]
        v = self._v[self._get_variable_index(variable)]

        rho_t = ops.minimum(lr, 1 / ops.sqrt(local_step))
        alpha_t = ops.maximum(epsilon_2, self._rms(variable)) * rho_t
        regulated_grad_square = ops.add(ops.square(gradient), self.epsilon_1)
        beta_2_t = ops.subtract(1, ops.power(local_step, self.beta_2_decay))

        if len(variable.shape) >= 2:
            # `r` deletes the last dimension of gradient, so it is of shape
            # `gradient.shape[:-1]`.
            self.assign(
                r,
                ops.add(
                    ops.multiply(beta_2_t, r),
                    ops.multiply(
                        ops.subtract(1, beta_2_t),
                        ops.mean(regulated_grad_square, axis=-1),
                    ),
                ),
            )
            # `c` deletes the second last dimension of gradient, so it is of
            # shape `gradient.shape[:-2] + gradient.shape[-1]`.
            self.assign(
                c,
                ops.add(
                    ops.multiply(beta_2_t, c),
                    ops.multiply(
                        ops.subtract(1, beta_2_t),
                        ops.mean(regulated_grad_square, axis=-2),
                    ),
                ),
            )
            self.assign(
                v,
                ops.multiply(
                    ops.expand_dims(
                        ops.divide(r, ops.mean(r, axis=-1, keepdims=True)),
                        axis=-1,
                    ),
                    ops.expand_dims(c, -2),
                ),
            )
        else:
            self.assign(
                v,
                ops.add(
                    ops.multiply(beta_2_t, v),
                    ops.multiply(
                        ops.subtract(1, beta_2_t), regulated_grad_square
                    ),
                ),
            )

        u_t = ops.divide(gradient, ops.sqrt(v))
        u_t_hat = ops.divide(
            u_t,
            ops.maximum(one, ops.divide(self._rms(u_t), self.clip_threshold)),
        )
        self.assign_sub(variable, ops.multiply(alpha_t, u_t_hat))

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_rewrite_constant_fold [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py]
    def patched_rewrite_constant_fold(g, ops):
        """
        We call tensorflow transform with constant folding but in some cases
        tensorflow does fold all constants. Since there are a bunch of ops in
        onnx that use attributes where tensorflow has dynamic inputs, we badly
        want constant folding to work. For cases where tensorflow missed
        something, make another pass over the graph and fix want we care about.
        """
        func_map = {
            "Add": np.add,
            "GreaterEqual": np.greater_equal,
            "Cast": np.asarray,
            "ConcatV2": np.concatenate,
            "Less": np.less,
            "ListDiff": np.setdiff1d,
            "Mul": np.multiply,
            "Pack": np.stack,
            "Range": np.arange,
            "Sqrt": np.sqrt,
            "Sub": np.subtract,
        }
        ops = list(ops)

        keep_looking = True
        while keep_looking:
            keep_looking = False
            for idx, op in enumerate(ops):
                func = func_map.get(op.type)
                if func is None:
                    continue
                if set(op.output) & set(g.outputs):
                    continue
                try:
                    inputs = []
                    for node in op.inputs:
                        if not node.is_const():
                            break
                        inputs.append(node.get_tensor_value(as_list=False))

                    logger.debug(
                        "op name %s, %s, %s",
                        op.name,
                        len(op.input),
                        len(inputs),
                    )
                    if inputs and len(op.input) == len(inputs):
                        logger.info(
                            "folding node type=%s, name=%s" % (op.type, op.name)
                        )
                        if op.type == "Cast":
                            dst = op.get_attr_int("to")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(dst)
                            val = np.asarray(*inputs, dtype=np_type)
                        elif op.type == "ConcatV2":
                            axis = inputs[-1]
                            values = inputs[:-1]
                            val = func(tuple(values), axis)
                        elif op.type == "ListDiff":
                            out_type = op.get_attr_int("out_idx")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(
                                out_type
                            )
                            val = func(*inputs)
                            val = val.astype(np_type)
                        elif op.type in ["Pack"]:
                            # handle ops that need input array and axis
                            axis = op.get_attr_int("axis")
                            val = func(inputs, axis=axis)
                        elif op.type == "Range":
                            dtype = op.get_attr_int("Tidx")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(
                                dtype
                            )
                            val = func(*inputs, dtype=np_type)
                        else:
                            val = func(*inputs)

                        new_node_name = tf2onnx.utils.make_name(op.name)
                        new_output_name = new_node_name
                        old_output_name = op.output[0]
                        old_node_name = op.name
                        logger.debug(
                            "create const node [%s] replacing [%s]",
                            new_node_name,
                            old_node_name,
                        )
                        ops[idx] = g.make_const(new_node_name, val)

                        logger.debug(
                            "replace old output [%s] with new output [%s]",
                            old_output_name,
                            new_output_name,
                        )
                        # need to re-write the consumers input name to use the
                        # const name
                        consumers = g.find_output_consumers(old_output_name)
                        if consumers:
                            for consumer in consumers:
                                g.replace_input(
                                    consumer, old_output_name, new_output_name
                                )

                        # keep looking until there is nothing we can fold.
                        # We keep the graph in topological order so if we
                        # folded, the result might help a following op.
                        keep_looking = True
                except Exception as ex:
                    tb = traceback.format_exc()
                    logger.info("exception: %s, details: %s", ex, tb)
                    # ignore errors

        return ops

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py::compute_float8_amax_history [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/quantizers.py]
def compute_float8_amax_history(x, amax_history):
    amax_update = ops.cast(ops.max(ops.abs(x)), amax_history.dtype)
    new_amax_history = ops.scatter_update(
        ops.roll(amax_history, shift=-1),
        [[0]],
        ops.reshape(amax_update, [1]),
    )
    return new_amax_history

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/schedule_free_adamw.py::ScheduleFreeAdamW.update_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/schedule_free_adamw.py]
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
            warmup_steps = ops.cast(self.warmup_steps, variable.dtype)
            warmup_factor = ops.minimum(local_step / warmup_steps, 1.0)
            lr = lr * warmup_factor

        var_index = self._get_variable_index(variable)
        momentum = self._momentums[var_index]
        velocity = self._velocities[var_index]

        # Store momentum_old before any updates
        momentum_old = momentum.value

        # Bias correction for Adam's second moment
        bias_correction_2 = 1 - ops.power(beta_2, local_step)

        # Update velocity (second moment estimate)
        # velocity = beta_2 * velocity + (1 - beta_2) * gradient^2
        self.assign_add(
            velocity,
            ops.multiply(
                ops.subtract(ops.square(gradient), velocity), 1 - beta_2
            ),
        )

        # Compute the denominator (RMSprop-style with bias correction)
        denom = ops.add(ops.sqrt(velocity / bias_correction_2), epsilon)

        # Update momentum: momentum = momentum - lr * gradient / denom
        grad_scaled = ops.divide(ops.multiply(lr, gradient), denom)
        self.assign_sub(momentum, grad_scaled)

        # Compute weight for averaging: weight = 1 / step
        weight = 1.0 / local_step

        # Recover x_old from y_old and momentum_old
        # x_old = (y_old - (1 - beta_1) * momentum_old) / beta_1
        y_old = variable
        x_old = ops.divide(
            ops.subtract(y_old, ops.multiply(1 - beta_1, momentum_old)),
            beta_1,
        )

        # x_new = lerp(x_old, momentum, weight)
        # x_new = (1 - weight) * x_old + weight * momentum
        x_new = ops.add(
            ops.multiply(1 - weight, x_old), ops.multiply(weight, momentum)
        )

        # y_new = lerp(momentum, x_new, beta_1)
        # y_new = (1 - beta_1) * momentum + beta_1 * x_new
        y_new = ops.add(
            ops.multiply(1 - beta_1, momentum), ops.multiply(beta_1, x_new)
        )

        self.assign(variable, y_new)

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
```

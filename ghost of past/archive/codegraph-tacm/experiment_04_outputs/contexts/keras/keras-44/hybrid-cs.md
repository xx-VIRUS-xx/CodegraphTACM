# keras-44 :: hybrid-cs

query: Fix RNN layers dynamic `trainable` attr

## selected nodes

- rank=1 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=2 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=3 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py::JaxExportArchive._backend_track_layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py
- rank=4 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::set_tensor_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=5 layer=FUNCTION tokens=286 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateful_handle_finite_grads file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py
- rank=6 layer=FUNCTION tokens=1599 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py::TestJaxLayer._test_layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py
- rank=7 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::_clear_tensor_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=8 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py::dynamic_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py
- rank=9 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_jax.py::get_replicated_train_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_jax.py
- rank=10 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable.trainable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py
- rank=11 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_custom_jax_workflow.py::train_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_custom_jax_workflow.py
- rank=12 layer=FUNCTION tokens=520 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateless_handle_finite_grads file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::set_tensor_attr [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py]
def set_tensor_attr(tensor, attr, value):
    try:
        setattr(tensor, attr, value)
    except AttributeError:
        attr_dict = global_state.get_global_attribute(f"{attr}_dict")
        if attr_dict is None:
            if value is None:
                return
            attr_dict = {}
            global_state.set_global_attribute(f"{attr}_dict", attr_dict)
        if value is not None:
            attr_dict[id(tensor)] = value
            weakref.finalize(tensor, _clear_tensor_attr, id(tensor), attr)
        elif id(tensor) in attr_dict:
            del attr_dict[id(tensor)]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateful_handle_finite_grads [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py]
    def _stateful_handle_finite_grads(self, grads, trainable_variables):
        scale = self.dynamic_scale
        # Unscale gradients.
        tvs = trainable_variables or self._trainable_variables
        unscaled_grads = [
            g
            if g is None or self._overwrite_variable_with_gradient(v)
            else ops.divide(g, scale)
            for g, v in zip(grads, tvs)
        ]
        self.inner_optimizer.apply(
            unscaled_grads, trainable_variables=trainable_variables
        )

        def upscale():
            self.step_counter.assign(0)
            self.dynamic_scale.assign(ops.multiply(self.dynamic_scale, 2.0))

        def increment():
            self.step_counter.assign_add(1)

        # Potentially upscale loss and reset counter.
        ops.cond(
            ops.equal(self.step_counter, self.dynamic_growth_steps - 1),
            upscale,
            increment,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py::TestJaxLayer._test_layer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py]
    def _test_layer(
        self,
        model_name,
        layer_class,
        layer_init_kwargs,
        trainable_weights,
        trainable_params,
        non_trainable_weights,
        non_trainable_params,
    ):
        layer_init_kwargs.update(self.init_kwargs)

        # Fake MNIST data
        x_train = random.uniform(shape=(320, 28, 28, 1))
        y_train_indices = ops.cast(
            ops.random.uniform(shape=(320,), minval=0, maxval=num_classes),
            dtype="int32",
        )
        y_train = ops.one_hot(y_train_indices, num_classes, dtype="int32")
        x_test = random.uniform(shape=(32, 28, 28, 1))

        def _count_params(weights):
            count = 0
            for weight in weights:
                count = count + math.prod(ops.shape(weight))
            return count

        def verify_weights_and_params(layer):
            self.assertEqual(trainable_weights, len(layer.trainable_weights))
            self.assertEqual(
                trainable_params,
                _count_params(layer.trainable_weights),
            )
            self.assertEqual(
                non_trainable_weights, len(layer.non_trainable_weights)
            )
            self.assertEqual(
                non_trainable_params,
                _count_params(layer.non_trainable_weights),
            )

        # functional model
        layer1 = layer_class(**layer_init_kwargs)
        inputs1 = layers.Input(shape=input_shape)
        outputs1 = layer1(inputs1)
        model1 = models.Model(
            inputs=inputs1, outputs=outputs1, name=f"{model_name}1"
        )
        model1.summary()

        verify_weights_and_params(layer1)

        model1.compile(
            loss="categorical_crossentropy",
            optimizer="adam",
            metrics=[metrics.CategoricalAccuracy()],
        )

        tw1_before_fit = tree.map_structure(
            backend.convert_to_numpy, layer1.trainable_weights
        )
        ntw1_before_fit = tree.map_structure(
            backend.convert_to_numpy, layer1.non_trainable_weights
        )
        model1.fit(x_train, y_train, epochs=1, steps_per_epoch=10)
        tw1_after_fit = tree.map_structure(
            backend.convert_to_numpy, layer1.trainable_weights
        )
        ntw1_after_fit = tree.map_structure(
            backend.convert_to_numpy, layer1.non_trainable_weights
        )

        # verify both trainable and non-trainable weights did change after fit
        for before, after in zip(tw1_before_fit, tw1_after_fit):
            self.assertNotAllClose(before, after)
        for before, after in zip(ntw1_before_fit, ntw1_after_fit):
            self.assertNotAllClose(before, after)

        expected_output_shape = (ops.shape(x_test)[0], num_classes)
        output1 = model1(x_test)
        self.assertEqual(output1.shape, expected_output_shape)
        predict1 = model1.predict(x_test, steps=1)
        self.assertEqual(predict1.shape, expected_output_shape)

        # verify both trainable and non-trainable weights did not change
        tw1_after_call = tree.map_structure(
            backend.convert_to_numpy, layer1.trainable_weights
        )
        ntw1_after_call = tree.map_structure(
            backend.convert_to_numpy, layer1.non_trainable_weights
        )
        for after_fit, after_call in zip(tw1_after_fit, tw1_after_call):
            self.assertAllClose(after_fit, after_call)
        for after_fit, after_call in zip(ntw1_after_fit, ntw1_after_call):
            self.assertAllClose(after_fit, after_call)

        exported_params = jax.tree_util.tree_map(
            backend.convert_to_numpy, layer1.params
        )
        if layer1.state is not None:
            exported_state = jax.tree_util.tree_map(
                backend.convert_to_numpy, layer1.state
            )
        else:
            exported_state = None

        def verify_identical_model(model):
            output = model(x_test)
            self.assertAllClose(output1, output)

            predict = model.predict(x_test, steps=1)
            self.assertAllClose(predict1, predict)

        # sequential model to compare results
        layer2 = layer_class(
            params=exported_params,
            state=exported_state,
            input_shape=input_shape,
            **layer_init_kwargs,
        )
        model2 = models.Sequential([layer2], name=f"{model_name}2")
        model2.summary()
        verify_weights_and_params(layer2)
        model2.compile(
            loss="categorical_crossentropy",
            optimizer="adam",
            metrics=[metrics.CategoricalAccuracy()],
        )
        verify_identical_model(model2)

        # save, load back and compare results
        path = os.path.join(self.get_temp_dir(), "jax_layer_model.keras")
        model2.save(path)

        model3 = saving.load_model(path)
        layer3 = model3.layers[0]
        model3.summary()
        verify_weights_and_params(layer3)
        verify_identical_model(model3)

        # export, load back and compare results
        path = os.path.join(self.get_temp_dir(), "jax_layer_export")
        export_kwargs = {}
        if testing.jax_uses_gpu():
            export_kwargs = {
                "jax2tf_kwargs": {
                    "native_serialization_platforms": ("cpu", "cuda")
                }
            }
        elif testing.jax_uses_tpu():
            export_kwargs = {
                "jax2tf_kwargs": {
                    "native_serialization_platforms": ("cpu", "tpu")
                }
            }
        model2.export(path, format="tf_saved_model", **export_kwargs)
        model4 = tf.saved_model.load(path)
        output4 = model4.serve(x_test)
        self.assertAllClose(output1, output4, atol=1e-2, rtol=1e-3)

        # test subclass model building without a build method
        class TestModel(models.Model):
            def __init__(self, layer):
                super().__init__()
                self._layer = layer

            def call(self, inputs):
                return self._layer(inputs)

        layer5 = layer_class(**layer_init_kwargs)
        model5 = TestModel(layer5)
        output5 = model5(x_test)
        self.assertNotAllClose(output5, 0.0)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::_clear_tensor_attr [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py]
def _clear_tensor_attr(tensor_id, attr):
    attr_dict = global_state.get_global_attribute(f"{attr}_dict")
    if attr_dict is not None and tensor_id in attr_dict:
        del attr_dict[tensor_id]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py::dynamic_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py]
def dynamic_model(X, y, loss, layers=[10]):
    """Creates a basic MLP classifier dynamically choosing binary/multiclass
    classification loss and output activations.
    """
    n_features_in = X.shape[1]
    inp = Input(shape=(n_features_in,))

    hidden = inp
    for layer_size in layers:
        hidden = Dense(layer_size, activation="relu")(hidden)

    n_outputs = y.shape[1] if len(y.shape) > 1 else 1
    out = [Dense(n_outputs, activation="softmax")(hidden)]
    model = Model(inp, out)
    model.compile(loss=loss, optimizer="rmsprop")

    return model

# /Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_jax.py::get_replicated_train_state [/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_jax.py]
def get_replicated_train_state(devices):
    # All variables will be replicated on all devices
    var_mesh = Mesh(devices, axis_names=("_"))
    # In NamedSharding, axes not mentioned are replicated (all axes here)
    var_replication = NamedSharding(var_mesh, P())

    # Apply the distribution settings to the model variables
    trainable_variables = jax.device_put(
        model.trainable_variables, var_replication
    )
    non_trainable_variables = jax.device_put(
        model.non_trainable_variables, var_replication
    )
    optimizer_variables = jax.device_put(optimizer.variables, var_replication)

    # Combine all state in a tuple
    return (trainable_variables, non_trainable_variables, optimizer_variables)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable.trainable [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py]
    def trainable(self, value):
        self._trainable = bool(value)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateless_handle_finite_grads [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py]
    def _stateless_handle_finite_grads(
        self, optimizer_variables, grads, trainable_variables
    ):
        def upscale():
            mapping = list(zip(self.variables, optimizer_variables))
            with backend.StatelessScope(state_mapping=mapping) as scope:
                self.step_counter.assign(0)
                self.dynamic_scale.assign(ops.multiply(self.dynamic_scale, 2.0))
            return [scope.get_current_value(v) for v in self._variables]

        def increment():
            mapping = list(zip(self.variables, optimizer_variables))
            with backend.StatelessScope(state_mapping=mapping) as scope:
                self.step_counter.assign_add(1)
            return [scope.get_current_value(v) for v in self._variables]

        mapping = list(zip(self.variables, optimizer_variables))
        with backend.StatelessScope(state_mapping=mapping):
            # Potentially upscale loss and reset counter.
            own_variables = ops.cond(
                ops.equal(self.step_counter, self.dynamic_growth_steps - 1),
                upscale,
                increment,
            )

            # Unscale gradients.
            scale = self.dynamic_scale
            unscaled_grads = [
                g
                if g is None or self._overwrite_variable_with_gradient(v)
                else ops.divide(g, scale)
                for g, v in zip(grads, self._trainable_variables)
            ]
            (
                new_trainable_variables,
                new_inner_variables,
            ) = self.inner_optimizer.stateless_apply(
                self.inner_optimizer.variables,
                unscaled_grads,
                trainable_variables,
            )

        new_optimizer_variables = own_variables + new_inner_variables
        return new_trainable_variables, new_optimizer_variables
```

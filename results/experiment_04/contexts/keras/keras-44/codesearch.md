# keras-44 :: codesearch

query: Fix RNN layers dynamic `trainable` attr

## selected nodes

- rank=1 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.trainable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=2 layer=FUNCTION tokens=1599 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py::TestJaxLayer._test_layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py
- rank=3 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_jax.py::get_replicated_train_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/distributed_training_with_jax.py
- rank=4 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py::JaxExportArchive._backend_track_layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/export.py
- rank=5 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::FlaxLayer.apply_without_training file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=6 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::FlaxLayer.apply_with_training file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=7 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable.trainable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py
- rank=8 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=9 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::TrainingTestingLayer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=10 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py::EinsumDenseTest.train_one_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py
- rank=11 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py::DenseTest.train_one_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py
- rank=12 layer=FUNCTION tokens=505 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py::TestCase.run_training_step file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py
- rank=13 layer=FUNCTION tokens=266 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_torch_multi_gpu.py::train file=/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_torch_multi_gpu.py
- rank=14 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::FlaxLayer.init_with_training file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::FlaxLayer.apply_without_training [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
        def apply_without_training(params, state, rng, inputs):
            return self.module.apply(
                self._params_and_state_to_variables(params, state),
                inputs,
                rngs=rng,
                method=self.method,
                mutable=apply_mutable,
            )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::FlaxLayer.apply_with_training [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
        def apply_with_training(params, state, rng, inputs, training):
            return self.module.apply(
                self._params_and_state_to_variables(params, state),
                inputs,
                rngs=rng,
                method=self.method,
                mutable=apply_mutable,
                training=training,
            )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py::Variable.trainable [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/variables.py]
    def trainable(self, value):
        self._trainable = bool(value)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py]
    def __init__(self, layers=None, trainable=True, name=None):
        super().__init__(trainable=trainable, name=name)
        self._functional = None
        self._layers = []
        if layers:
            for layer in layers:
                self.add(layer, rebuild=False)
            self._maybe_rebuild()

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::TrainingTestingLayer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
    def __init__(self, **kwargs):
        layers.Layer.__init__(self, **kwargs)
        Trainer.__init__(self)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py::EinsumDenseTest.train_one_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense_test.py]
            def train_one_step(x, dy):
                layer.zero_grad()
                loss = loss_fn(x, dy)
                loss.backward()
                grads = [v.value.grad for v in layer.trainable_variables]
                optimizer.apply(grads, layer.trainable_variables)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py::DenseTest.train_one_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense_test.py]
            def train_one_step(x, dy):
                layer.zero_grad()
                loss = loss_fn(x, dy)
                loss.backward()
                grads = [v.value.grad for v in layer.trainable_variables]
                optimizer.apply(grads, layer.trainable_variables)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py::TestCase.run_training_step [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py]
        def run_training_step(layer, input_data, output_data):
            class TestModel(Model):
                def __init__(self, layer):
                    super().__init__()
                    self.layer = layer

                def call(self, x, training=False):
                    return self.layer(x, training=training)

            model = TestModel(layer)

            data = (input_data, output_data)
            if backend.backend() == "torch":
                data = tree.map_structure(backend.convert_to_numpy, data)

            def data_generator():
                while True:
                    yield data

            # Single op loss to avoid compilation issues with ragged / sparse.
            class TestLoss(Loss):
                def __call__(self, y_true, y_pred, sample_weight=None):
                    return ops.sum(y_pred)

            # test the "default" path for each backend by setting
            # jit_compile="auto".
            # for tensorflow and jax backends auto is jitted
            # Note that tensorflow cannot be jitted with sparse tensors
            # for torch backend auto is eager
            #
            # NB: for torch, jit_compile=True turns on torchdynamo
            #  which may not always succeed in tracing depending
            #  on the model. Run your program with these env vars
            #  to get debug traces of dynamo:
            #    TORCH_LOGS="+dynamo"
            #    TORCHDYNAMO_VERBOSE=1
            #    TORCHDYNAMO_REPORT_GUARD_FAILURES=1
            jit_compile = "auto"
            if backend.backend() == "tensorflow" and input_sparse:
                jit_compile = False
            model.compile(
                optimizer="sgd", loss=TestLoss(), jit_compile=jit_compile
            )
            model.fit(data_generator(), steps_per_epoch=1, verbose=0)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_torch_multi_gpu.py::train [/Users/xxvirusxx/PY/CodegraphTACM/keras/examples/demo_torch_multi_gpu.py]
def train(model, train_loader, num_epochs, optimizer, loss_fn):
    for epoch in range(num_epochs):
        running_loss = 0.0
        for batch_idx, (inputs, targets) in enumerate(train_loader):
            inputs = inputs.cuda(non_blocking=True)
            targets = targets.cuda(non_blocking=True)

            # Forward pass
            outputs = model(inputs)
            loss = loss_fn(outputs, targets)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            # Print loss statistics
            if (batch_idx + 1) % 10 == 0:
                print(
                    f"Epoch [{epoch + 1}/{num_epochs}], "
                    f"Batch [{batch_idx + 1}/{len(train_loader)}], "
                    f"Loss: {running_loss / 10}"
                )
                running_loss = 0.0

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::FlaxLayer.init_with_training [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
        def init_with_training(rng, inputs, training):
            return self._variables_to_params_and_state(
                self.module.init(
                    rng,
                    inputs,
                    method=self.method,
                    training=training,
                )
            )
```

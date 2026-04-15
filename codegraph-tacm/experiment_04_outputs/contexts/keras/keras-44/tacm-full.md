# keras-44 :: tacm-full

query: Fix RNN layers dynamic `trainable` attr

## selected nodes

- rank=1 layer=FUNCTION tokens=318 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::_walk_saveable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=2 layer=FUNCTION tokens=286 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateful_handle_finite_grads file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py
- rank=3 layer=FUNCTION tokens=379 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::Tracker.track file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=4 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=5 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::set_tensor_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=6 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._not_implemented_error file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=7 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::get_tensor_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=8 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::_clear_tensor_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=9 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.layer_property file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=10 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/global_state.py::get_global_attribute file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/global_state.py
- rank=11 layer=FUNCTION tokens=523 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._initialize_tracker file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=12 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateless_handle_non_finite_grads file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py
- rank=13 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/layer.py::TFLayer._convert_tracked_collections file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/layer.py
- rank=14 layer=FUNCTION tokens=455 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_get_value_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=15 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=16 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN._create_state_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=17 layer=FUNCTION tokens=357 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation._get_node_attribute_at_index file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=18 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::_walk_saveable [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py]
def _walk_saveable(saveable):
    from keras.src.saving.keras_saveable import KerasSaveable

    if not isinstance(saveable, KerasSaveable):
        raise ValueError(
            "Expected object to be an "
            "instance of `KerasSaveable`, but "
            f"got {saveable} of type {type(saveable)}"
        )

    obj_type = saveable._obj_type()
    attr_skipset = get_attr_skipset(obj_type)

    # Save all layers directly tracked by Sequential and Functional first.
    # This helps avoid ordering concerns for subclassed Sequential or Functional
    # models with extra attributes--the internal Keras state take precedence.
    if obj_type in ("Sequential", "Functional"):
        yield "layers", saveable.layers

    for child_attr in sorted(dir(saveable), key=lambda x: _name_key(x)):
        if child_attr.startswith("__") or child_attr in attr_skipset:
            continue
        try:
            child_obj = getattr(saveable, child_attr)
        except Exception:
            # Avoid raising the exception when visiting the attributes.
            continue
        yield child_attr, child_obj

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::Tracker.track [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py]
    def track(self, attr):
        if not is_tracking_enabled():
            return attr

        for store_name, (is_attr_type, _) in self.config.items():
            if is_attr_type(attr):
                if store_name in self.exclusions:
                    for excl in self.exclusions[store_name]:
                        if self.is_in_store(excl, attr):
                            return attr
                if not self.is_in_store(store_name, attr):
                    self.add_to_store(store_name, attr)
                return attr
        if isinstance(attr, tuple) and hasattr(attr, "_fields"):
            # Named tuple case.
            wrapped_attr = {}
            for name, e in attr._asdict().items():
                wrapped_attr[name] = self.track(e)
            return attr.__class__(**wrapped_attr)
        if isinstance(attr, tuple):
            wrapped_attr = []
            for e in attr:
                wrapped_attr.append(self.track(e))
            return attr.__class__(wrapped_attr)
        elif isinstance(attr, list):
            return TrackedList(attr, self)
        elif isinstance(attr, OrderedDict):
            return TrackedOrderedDict(attr, self)
        elif isinstance(attr, dict):
            return TrackedDict(attr, self)
        elif isinstance(attr, set):
            return TrackedSet(attr, self)
        return attr

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py]
    def __init__(self, layers=None, trainable=True, name=None):
        super().__init__(trainable=trainable, name=name)
        self._functional = None
        self._layers = []
        if layers:
            for layer in layers:
                self.add(layer, rebuild=False)
            self._maybe_rebuild()

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._not_implemented_error [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _not_implemented_error(self, attr, msg=None):
        if callable(attr):
            attr_name = attr.__name__
            attr_type = "method"
        else:
            attr_name = str(attr)
            attr_type = "attribute"
        msg = f" {msg}" if msg is not None else ""
        return NotImplementedError(
            f"Layer {self.__class__.__name__} does not have a `{attr_name}` "
            f"{attr_type} implemented.{msg}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::get_tensor_attr [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py]
def get_tensor_attr(tensor, attr):
    if not hasattr(tensor, attr):
        attr_dict = global_state.get_global_attribute(f"{attr}_dict")
        if attr_dict is not None:
            return attr_dict.get(id(tensor), None)
        else:
            return None
    return getattr(tensor, attr, None)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::_clear_tensor_attr [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py]
def _clear_tensor_attr(tensor_id, attr):
    attr_dict = global_state.get_global_attribute(f"{attr}_dict")
    if attr_dict is not None and tensor_id in attr_dict:
        del attr_dict[tensor_id]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.layer_property [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py]
    def layer_property(self):
        # Properties for layers in the functional graph should not affect saving
        return self.layer_attr

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/global_state.py::get_global_attribute [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/global_state.py]
def get_global_attribute(name, default=None, set_to_default=False):
    attr = getattr(GLOBAL_STATE_TRACKER, name, None)
    if attr is None and default is not None:
        attr = default
        if set_to_default:
            set_global_attribute(name, attr)
    return attr

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._initialize_tracker [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _initialize_tracker(self):
        if hasattr(self, "_tracker"):
            return

        trainable_variables = []
        non_trainable_variables = []
        layers = []
        metrics = []
        seed_generators = []
        self._tracker = tracking.Tracker(
            {
                "trainable_variables": (
                    lambda x: isinstance(x, backend.Variable) and x.trainable,
                    trainable_variables,
                ),
                "non_trainable_variables": (
                    lambda x: (
                        isinstance(x, backend.Variable) and not x.trainable
                    ),
                    non_trainable_variables,
                ),
                "metrics": (lambda x: isinstance(x, Metric), metrics),
                "layers": (
                    lambda x: (
                        isinstance(x, Layer) and not isinstance(x, Metric)
                    ),
                    layers,
                ),
                "seed_generators": (
                    lambda x: isinstance(x, backend.random.SeedGenerator),
                    seed_generators,
                ),
            },
            exclusions={"non_trainable_variables": ["trainable_variables"]},
        )
        if backend.backend() == "tensorflow":
            # Remove attribute tracking for lists (TF-specific attribute)
            _self_setattr_tracking = getattr(
                self, "_self_setattr_tracking", True
            )
            self._self_setattr_tracking = False

        self._trainable_variables = trainable_variables
        self._non_trainable_variables = non_trainable_variables
        self._layers = layers
        self._metrics = metrics
        self._seed_generators = seed_generators

        if backend.backend() == "tensorflow":
            # Reset attribute tracking (TF-specific)
            self._self_setattr_tracking = _self_setattr_tracking

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateless_handle_non_finite_grads [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py]
    def _stateless_handle_non_finite_grads(
        self, optimizer_variables, trainable_variables
    ):
        mapping = list(zip(self.variables, optimizer_variables))
        with backend.StatelessScope(state_mapping=mapping) as scope:
            self.step_counter.assign(0)
            self.dynamic_scale.assign(ops.multiply(self.dynamic_scale, 0.5))
        new_optimizer_variables = []
        for v in self.variables:
            new_optimizer_variables.append(scope.get_current_value(v))
        return trainable_variables, new_optimizer_variables

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/layer.py::TFLayer._convert_tracked_collections [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/layer.py]
    def _convert_tracked_collections(self, children):
        """Convert TrackedList/Dict/Set to plain Python structures."""
        for tracked_attr in self._tracked:
            tracked_item = getattr(self, tracked_attr)
            if isinstance(tracked_item, tracking.TrackedList):
                children[tracked_attr] = list(tracked_item)
            elif isinstance(tracked_item, tracking.TrackedOrderedDict):
                children[tracked_attr] = collections.OrderedDict(tracked_item)
            elif isinstance(tracked_item, tracking.TrackedDict):
                children[tracked_attr] = dict(tracked_item)
            elif isinstance(tracked_item, tracking.TrackedSet):
                children[tracked_attr] = list(tracked_item)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_get_value_attr [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py]
    def patched_get_value_attr(self, external_tensor_storage=None):
        """
        Return onnx attr for value property of node.
        Attr is modified to point to external tensor data stored in
        external_tensor_storage, if included.
        """
        a = self._attr["value"]
        if (
            external_tensor_storage is not None
            and self in external_tensor_storage.node_to_modified_value_attr
        ):
            return external_tensor_storage.node_to_modified_value_attr[self]
        if external_tensor_storage is None or a.type != AttributeProto.TENSOR:
            return a

        def prod(x):
            if hasattr(np, "product"):
                return np.product(x)
            else:
                return np.prod(x)

        if (
            prod(a.t.dims)
            > external_tensor_storage.external_tensor_size_threshold
        ):
            a = copy.deepcopy(a)
            tensor_name = (
                f"{self.name.strip()}_{external_tensor_storage.name_counter}"
            )
            for c in '~"#%&*:<>?/\\{|}':
                tensor_name = tensor_name.replace(c, "_")
            external_tensor_storage.name_counter += 1
            external_tensor_storage.name_to_tensor_data[tensor_name] = (
                a.t.raw_data
            )
            external_tensor_storage.node_to_modified_value_attr[self] = a
            a.t.raw_data = b""
            a.t.ClearField("raw_data")
            location = a.t.external_data.add()
            location.key = "location"
            location.value = tensor_name
            a.t.data_location = TensorProto.EXTERNAL
        return a

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py]
    def __init__(self, **kwargs):
        inputs = keras.Input(shape=(4,), batch_size=2)
        dense = keras.layers.Dense(1, name="first_dense")
        x = dense(inputs)
        outputs = keras.layers.Dense(1, name="second_dense")(x)
        super().__init__(inputs=inputs, outputs=outputs, **kwargs)
        # Attrs for layers in the functional graph should not affect saving
        self.layer_attr = dense

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN._create_state_variables [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def _create_state_variables(self, batch_size):
        with backend.name_scope(self.name, caller=self):
            self.states = tree.map_structure(
                lambda value: backend.Variable(
                    value,
                    trainable=False,
                    dtype=self.variable_dtype,
                    name="rnn_state",
                ),
                self.get_initial_state(batch_size),
            )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation._get_node_attribute_at_index [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py]
    def _get_node_attribute_at_index(self, node_index, attr, attr_name):
        """Private utility to retrieves an attribute (e.g. inputs) from a node.

        This is used to implement the properties:
        - output
        - input

        Args:
            node_index: Integer index of the node from which
                to retrieve the attribute.
            attr: Exact node attribute name.
            attr_name: Human-readable attribute name, for error messages.

        Returns:
            The operation's attribute `attr` at the node of index `node_index`.
        """
        if not self._inbound_nodes:
            raise AttributeError(
                f"The layer {self.name} has never been called "
                f"and thus has no defined {attr_name}."
            )
        if not len(self._inbound_nodes) > node_index:
            raise ValueError(
                f"Asked to get {attr_name} at node "
                f"{node_index}, but the operation has only "
                f"{len(self._inbound_nodes)} inbound nodes."
            )
        values = getattr(self._inbound_nodes[node_index], attr)
        if isinstance(values, list) and len(values) == 1:
            return values[0]
        else:
            return values

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py]
    def output(self):
        return self._outputs_struct
```

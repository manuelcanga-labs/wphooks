import unittest
from wphooks.wp_filters import wp_filters, filter, add_filter, apply_filters


class FiltersTests(unittest.TestCase):
    """Test filter hooks"""

    def tearDown(self):
        global wp_filters
        wp_filters = {}

    def test_add_filter(self):
        """Test adding a filter with add_filter"""

        add_filter("test.filter1", lambda x: True)
        self.assertNotEqual(wp_filters, {})
        self.assertNotEqual(wp_filters["test.filter1"], {})
        self.assertNotEqual(wp_filters["test.filter1"][10], {})
        self.assertEqual(wp_filters["test.filter1"][10][0]["hook_name"], "test.filter1")
        self.assertEqual(wp_filters["test.filter1"][10][0]["accepted_args"], 1)
        self.assertTrue(wp_filters["test.filter1"][10][0]["callback"](10), True)

    def test_apply_filters_with_add_filter(self):
        """Test applying a filter with add_filter"""

        add_filter("test.filter2", lambda x: x + 1)

        self.assertEqual(apply_filters("test.filter2", 6), 7)
        self.assertEqual(apply_filters("test.filter2", 10), 11)

    def test_apply_filters_default_value(self):
        """Test applying a filter with a default value and without filters"""

        self.assertEqual(apply_filters("test.filter3", 6), 6)
        self.assertEqual(apply_filters("test.filter3", True), True)
        self.assertEqual(apply_filters("test.filter3", {"foo": "bar"}), {"foo": "bar"})

    def test_add_filter_with_accepted_args(self):
        """Test adding a filter with accepted args"""

        add_filter("test.filter_args", lambda x, y: x + y, accepted_args=2)
        self.assertEqual(apply_filters("test.filter_args", 1, 2, "extra1", "extra2"), 3)

    def test_filter_decorator(self):
        """Test the filter decorator"""

        @filter("test.decorator_filter")
        def my_filter(x):
            return x * 2

        self.assertEqual(apply_filters("test.decorator_filter", 5), 10)

    def test_different_priority(self):
        """
        Test filter priority.
        Priority is used to specify the order in which the functions associated with a particular filter are executed.
        Lower numbers correspond with earlier execution, and functions with the same priority are executed in the order in which they were added to the filter.
        """

        # Add priority 10 first, then 5. 5 should run first.
        add_filter("test.priority", lambda x: x + "a", priority=10)
        add_filter("test.priority", lambda x: x + "b", priority=5)

        # If 5 runs first: "start" + "b" = "startb"
        # Then 10 runs: "startb" + "a" = "startba"
        self.assertEqual(apply_filters("test.priority", "start"), "startba")

    def test_multiple_filters(self):
        """Test multiple filters on the same hook"""

        add_filter("test.multiple", lambda x: x + 1)
        add_filter("test.multiple", lambda x: x * 2)

        # Default priority 10 for both. Execution order is insertion order.
        # (1 + 1) * 2 = 4
        self.assertEqual(apply_filters("test.multiple", 1), 4)

    def test_args_passing(self):
        """Test passing arguments to filters"""

        add_filter("test.args", lambda x, y, z: x + y + z, accepted_args=3)
        # default_value=1, args=(2, 3) -> callback(1, 2, 3)
        self.assertEqual(apply_filters("test.args", 1, 2, 3), 6)

    def test_same_priority(self):
        """Test that filters with the same priority run in insertion order"""

        add_filter("test.same_priority", lambda x: x + "a", priority=10)
        add_filter("test.same_priority", lambda x: x + "b", priority=10)

        self.assertEqual(apply_filters("test.same_priority", "start"), "startab")

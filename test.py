import unittest
from abtest import abtest_builder

class MyTestCase(unittest.TestCase):
    def test_ab(self):
        abtest_builder.init_client(16, {})

        ret = abtest_builder.get_experiment("1", "copy_test_v3")
        print(ret)

        key = abtest_builder.get_key("1", "copy_test_v3", "enable", False)
        print("key type", type(key), key)

        key2 = abtest_builder.get_key("1", "copy_test_v3", "weight", 20)
        print("key2 type", type(key2), key2)

        key3 = abtest_builder.get_key("1", "copy_test_v3", "h_str", "fake")
        print("key3 type", type(key3), key3)
        # key_name值对应实验参数配置的实验槽,实现分流
        return



if __name__ == "__main__":
    unittest.main()
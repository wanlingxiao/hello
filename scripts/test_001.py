import pytest,allure

class Test_ABC:

    def setup_class(self):
        print(">>>>>>>setup_class")
    def teardown_class(self):
        print(">>>>>>>teardown_class")

    @allure.step(title="我是测试的步骤")
    def test_a(self):
        allure.attach("题目1","这是错误的断言")
        print(">>>>>>test_a")
        assert False

    def test_b(self):
        allure.attach("题目2","这是一个正确的断言")
        print(">>>>>>>test_b")
        assert True

if __name__ == '__main__':
    pytest.main("-s test_001.py")
from shared_code.class_b import ClassB


class TestClass:

  def test_method2(self):
    classB = ClassB()
    assert classB.method2() == 'world'

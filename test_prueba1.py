from prueba1 import cansplit
import pytest

# #Run test|Debug test: Codigo de prueba inicial
# def test_cansplit():
# 	assert cansplit((1,2,3,4,2)) == 1

@pytest.mark.parametrize(
	"vectors, expected",
	[
		((1,5,3,4),0),
		((2,2,4,1),0),
		((2,1,3,0,1,5),1),
		((2,7,1,5,1),0),
		((2,9,4,1,6),1),
		((1,1),1),
		((13,1,7,2,3,2),1)
	]
)
#Run test(Multiple): Ejecutar varias pruebas a la vez
def test_multi(vectors, expected):
	assert cansplit(vectors) == expected

